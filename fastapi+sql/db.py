import config
import sqlalchemy as salc
from sqlalchemy.orm import sessionmaker

_Engine = None
_SessionLocal = None


def _initialize_engine():
  """Initialize the DB Engine"""
  global _Engine, _SessionLocal
  if _Engine is None:
    _Engine = salc.create_engine(url=config.DB_URI, echo=True)
    _SessionLocal = sessionmaker(bind=_Engine)


_initialize_engine()

_Base = None


def get_engine(base):
  """Get the current SQL Alchemy DB Engine instance"""
  global _Base
  _Base = base
  return _Engine


def get_db():
  """Get the current attached SQL Alchemy DB"""
  _Base.metadata.create_all(bind=_Engine)
  db = _SessionLocal()
  try:
    yield db
  finally:
    db.close()
