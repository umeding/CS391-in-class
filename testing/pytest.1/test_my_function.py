import pytest
from my_function import add

def test_add():
  """Test the add function"""
  assert add(2, 3) == 5
  assert add(-1, 1) == 0

  assert add("2", 4)

def test_with_exceptuion():

  with pytest.raises(ValueError):
    add("test", 2)
