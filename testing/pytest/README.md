# PYTHON In-Class Exercise / Tutorial

## Prerequisites:

* Python 3 installed on laptop
* `pip` available in the terminal/command prompt.

## Setup the code

* Bring up `vscode`
* Create a new project folder (e.g., `pytest_exercise`).
* Open a terminal or command prompt, navigate into this folder
* Install pytest: Run `pip install pytest`
* Create a Python file named `operations.py` in the project folder.
* Paste the following code into `operations.py`:

```python
# operations.py

def simple_greet(name):
    """Returns a simple greeting string."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"

def power(base, exponent):
    """Calculates base raised to the power of exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Base and exponent must be numeric")
    if base == 0 and exponent < 0:
         raise ValueError("Cannot raise 0 to a negative power")
    return base ** exponent
```

* Create a second Python file in the same folder named test_operations.py. This
  is where the tests will live.
* Paste the basic test structure into `test_operations.py`

```python
# test_operations.py
import pytest
from operations import simple_greet, power  # Import the functions to test

# Tests will go here
```

## Task 1: Testing `simple_greet` - "the happy path"

NOTE: The "happy path" tests __working__ code / functions.

In `test_operations.py`, add the following test function:

```python
# test_operations.py
# ... (imports) ...

def test_simple_greet_with_valid_name():
    """Tests simple_greet with a typical name."""
    # 1. Define the input and expected output
    input_name = "Alice"
    expected_output = "Hello, Alice!"

    # 2. Call the function with the input
    actual_output = simple_greet(input_name)

    # 3. Assert that the actual output matches the expected output
    assert actual_output == expected_output
```

* Go back to the terminal (ensure you are in the `pytest_exercise`)
* Run pytest: Simply type `pytest` and press Enter
* Verify that `pytest` finds and runs the test, and that it passes (it should
  show 1 passed). If it fails, debug the test or the function code.

## Task 2: Testing Edge Cases and Expected Errors

Add the following test functions to test_operations.py:

```python
# test_operations.py
# ... (imports and previous test) ...

def test_simple_greet_raises_typeerror_for_non_string():
    """Tests that simple_greet raises TypeError for non-string input."""
    with pytest.raises(TypeError):
        simple_greet(123) # Pass a number instead of a string

def test_simple_greet_raises_valueerror_for_empty_string():
     """Tests that simple_greet raises ValueError for an empty string."""
     with pytest.raises(ValueError):
         simple_greet("")

def test_power_basic():
    """Tests the power function with typical integers."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, -1) == 1/3

def test_power_raises_typeerror_for_non_numeric():
    """Tests that power raises TypeError if inputs are not numeric."""
    with pytest.raises(TypeError):
        power("a", 2)
    with pytest.raises(TypeError):
        power(2, "b")

def test_power_raises_valueerror_for_zero_negative_exponent():
    """Tests raising 0 to a negative power raises ValueError."""
    with pytest.raises(ValueError):
        power(0, -2)
```

* Run `pytest` in the terminal again.
* Verify that all tests now pass (e.g., 6 passed). Debug if necessary. Pay
attention to how `pytest.raises` works – the code inside the `with` block must
trigger the specified error for the test to pass.

