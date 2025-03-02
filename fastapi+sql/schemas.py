"""
Pydantic makes sure that the body of the
JSON requests received complies with the data
schemas we describe here, and tells the user
where there are incompatibilities.
"""
from pydantic import BaseModel


class Signup(BaseModel):
  firstname: str
  lastname: str
  email: str
  password: str


class Login(BaseModel):
  email: str
  password: str
