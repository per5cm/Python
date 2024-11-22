# Unit Testing:

    Unit tests are automated tests written to ensure that individual parts (or units) of your code behave as expected.
    Python's built-in unittest module is commonly used for unit testing, but there are also popular third-party tools like pytest that simplify testing.

# assert:

    assert is a statement used to check whether a condition is true.
    If the condition evaluates to True, nothing happens. If it evaluates to False, the program raises an AssertionError.

```python
assert x == 5  # Nothing happens if x is 5, but if not, AssertionError is raised.
```

# AssertionError:

    AssertionError occurs when an assertion fails. It's Python's way of telling you that the assumption (condition) in the assert statement is not true.

```python
x = 3
assert x == 5  # Raises AssertionError because x is not equal to 5.
```

    Assertion errors are a helpful debugging tool when testing code because they help you catch mistakes early.

# pytest:

    pytest is a popular third-party testing framework in Python. It allows you to write simple test cases and automate testing easily.
    
    You can install it via pip:

        pip install pytest

        Once installed, you can create test functions using assert, and pytest will automatically find and run them.
        Documentation: pytest docs.

# Handling Floating Point Numbers:

    Floating-point numbers are tricky due to precision limitations in binary representation. To avoid assertion errors when comparing floats, you can use pytest.approx to compare floating point numbers with tolerance.

```python
assert 0.1 + 0.2 == pytest.approx(0.3)
```

# Packages and __init__.py:

    In Python, an __init__.py file signals to Python that the folder is a package. This file can be empty or contain initialization code for the package.
    If you have tests inside a package folder, pytest will automatically run tests in that folder when you run it from the command line.

Example of Simple Unit Test with pytest:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```
    To run this test with pytest, save the code to a file (e.g., test_example.py), and run:

    bash

    pytest

This will output the results of the tests and any assertion errors if the code doesn't behave as expected.

By using pytest and assert, you can ensure that your code works as intended and catch problems early in development!
