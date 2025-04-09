---
title: Tutorial
---

# Pytest Tutorial

This tutorial will guide you through the basics of writing tests for your Python
code using pytest. Pytest is a popular testing framework known for its
simplicity and flexibility.

## Installation

Make sure you have pytest installed. You can install it using `pip`:

```bash
pip install pytest
```

## Your First Test

Let's start by writing a simple function and a test for it. Create a file named
`my_functions.py` and add the following code:

```python
def add(x, y):
  """This function adds two numbers."""
  return x + y
```

Now, create another file named `test_my_functions.py` and write the following
test function:

```python
from my_functions import add

def test_add():
  """Test the add function."""
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
```

## Running the Test

Open your terminal, navigate to the directory containing your test file, and run
the following command:

```bash
pytest
```

Pytest will automatically discover and run the test functions in your
`test_my_functions.py` file. You should see output indicating that the test
passed.

## Key Concepts

Test Discovery: Pytest automatically discovers test files and functions by
searching for files named `test_*.py` or `*_test.py` and functions that start
with `test_`.

- __Assertions__: The assert statement is used to check if a condition is true.
  If the condition is false, the test will fail.
- __Test Functions__: Each test should be encapsulated in a function. This helps
  organize your tests and makes it easier to identify which tests are failing

## Advanced Features

Pytest offers many advanced features to help you write more effective tests, including:

- Fixtures: Fixtures are functions that provide reusable test data or setup and teardown procedures.
- Parametrization: Parametrization allows you to run the same test with different inputs.
- Marks: Marks allow you to categorize and selectively run tests.
- Plugins: Pytest has a rich ecosystem of plugins that extend its functionality.

## Example with Fixtures

Let's modify our example to use a fixture:

```python
import pytest
from my_functions import add

@pytest.fixture
def numbers():
  """Provides a tuple of numbers for testing."""
  return (2, 3)

def test_add(numbers):
  """Test the add function using a fixture."""
  assert add(numbers[0], numbers[1]) == 5
```

In this example, the numbers fixture provides a tuple of numbers that is used in
the test_add function. Fixtures help avoid code duplication and make your tests
more maintainable.

This tutorial provides a basic introduction to pytest. I encourage you to
explore the official pytest documentation and experiment with its features to
write robust tests for your Python code.