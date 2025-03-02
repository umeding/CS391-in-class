from typing import Annotated
from fastapi import FastAPI, HTTPException, Response, Cookie, status, Depends
from sqlalchemy.orm import Session
import sqlalchemy as salc
from db import get_db
import models
import config
import schemas
import jwt

# Marketed as 'acceptable' password hashing in their documentation.
# Argon2id or Scrypt are recommended by BCrypt maintainers.
import bcrypt

app = FastAPI()

"""
TODO: 
    * validate emails as well-formed
    * validate passwords as sufficiently strong
    * try allowing uploading PDFs to local disk - limit size of uploaded document.
        - https://chat.openai.com/share/bc8b8c8b-ce2b-4fc2-8e66-449ab96e8507
        - should be able to share them back to the client if authorized to access them.
    * allow alternate authorization w/ Authorization header rather than JWT for raw API usage.
"""


@app.get("/")
def root():
  return {"message": "hello world!"}


@app.post("/signup")
def signup(body: schemas.Signup, session: Session = Depends(get_db)):
  # does user with requested email already exist?
  # returns exactly one user matching email, if they exist.
  res:  models.User = session.scalar(
      salc.select(models.User).where(models.User.email == body.email)
  )

  # evals to True if user exists.
  if res:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email in use- please use another one or log in with email.",
    )

  # create user account in db
  new_user = models.User(
      email=body.email,
      firstname=body.firstname,
      lastname=body.lastname,
      # hash password; don't store in plain text.
      pw_hash=bcrypt.hashpw(
          body.password.encode("utf-8"), bcrypt.gensalt(12)),
  )
  session.add(new_user)
  session.commit()

  return {"message": "SIGNUP SUCCESSFUL"}


@app.post("/login")
def login(body: schemas.Login, response: Response, session: Session = Depends(get_db)):
  # check db for user w/ requested email
  res = session.scalar(
      salc.select(models.User).where(models.User.email == body.email)
  )

  # if user exists, check password hash match
  if res:
    if bcrypt.checkpw(body.password.encode("utf-8"), res.pw_hash):
      # create token allowing access to protected resources.
      encoded_jwt = jwt.encode(
          payload={"isAdmin": False, "isLoggedIn": True, "email": body.email},
          key=config.JWT_SECRET,
          algorithm="HS256",
      )

      # store token in client cookie storage.
      response.set_cookie(key="session_jwt", value=encoded_jwt, httponly=True)
      return {"message": "LOGIN SUCCESSFUL"}

  return {"message": "INVALID CREDENTIALS"}


async def jwt_required(session_jwt: Annotated[str | None, Cookie()] = None) -> dict:
  """
  Common logic to validate access to protected resources
  based on whether user can provide a valid session with
  appropriate credentials.
  """
  exc = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Unable to authorize access. Please log In.",
  )

  # is there a session_jwt to begin with?
  if not session_jwt:
    raise exc

  # there's a jwt. can it be decoded?
  try:
    decoded_jwt = jwt.decode(
        jwt=session_jwt, key=config.JWT_SECRET, algorithms=["HS256"]
    )

    # jwt was successfully decoded. pass along to route as common argument.
    return decoded_jwt

  except jwt.DecodeError:
    raise exc


@app.get("/me")
def me(decoded_jwt: Annotated[dict, Depends(jwt_required)]):
  return {"message": decoded_jwt}


@app.get("/echo_secrets/{secret}")
def echo_secrets(secret: str, decoded_jwt: Annotated[dict, Depends(jwt_required)]):
  return {"secret_message": secret, "sent_from": decoded_jwt}
