import sqlalchemy as salc
from sqlalchemy.orm import Session
from sqlalchemy import String, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

from db import get_engine



Base = declarative_base()


class User(Base):
  __tablename__ = "user_account"

  # auto-generates a UUID for the user. Default is a function that's
  # invoked on __init__.
  uid: Mapped[str] = mapped_column(
      String(), primary_key=True, default=lambda _: str(uuid.uuid4())
  )
  email: Mapped[str] = mapped_column(String())
  firstname: Mapped[str] = mapped_column(String())
  lastname: Mapped[str] = mapped_column(String())
  pw_hash: Mapped[str] = mapped_column(String())

  def __repr__(self) -> str:
    return f"User(email={self.email!r}, firstname={self.firstname!r}, lastname={self.lastname!r})"


def create_all():
  Base.metadata.create_all(bind=get_engine(Base))


create_all()
