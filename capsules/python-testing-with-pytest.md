---
title: Python Testing with pytest
subtitle: A Practical Guide to Writing Reliable Tests
author: Ahmed Adawy
category: Python / Testing
difficulty: Intermediate
language: English
version: 1.0
tags:
  - Python
  - pytest
  - Testing
  - Test Automation
  - Software Quality
---

# Python Testing with pytest

## A Practical Guide to Writing Reliable Tests

**Ahmed Adawy Tech Capsules**

Professional technical micro-books designed for developers who prefer practical knowledge over lengthy theory.

Each capsule focuses on one topic, providing concise explanations, real-world examples, and immediately applicable best practices.

---

# Introduction

Software becomes harder to maintain as it grows.

A small Python project may begin with a few functions and a handful of files. At that stage, manually checking whether everything still works may seem reasonable.

But as the project grows, manual verification becomes expensive.

A change in one function can unexpectedly break another part of the application.

A refactoring can introduce a regression.

A new feature can work correctly while silently breaking an older feature.

This is where automated testing becomes valuable.

Automated tests provide a repeatable way to verify that software behaves as expected.

In the Python ecosystem, **pytest** is one of the most practical tools for writing and running these tests.

This capsule focuses on using pytest to build reliable tests for Python projects.

The goal is not to cover every feature of pytest.

Instead, we will build a practical understanding of the features that developers use most often:

- Writing tests
- Assertions
- Fixtures
- Parametrization
- Exception testing
- Test organization
- Code coverage
- Continuous integration
- Testing a small real-world project

By the end of this capsule, you should be able to create a small but useful automated testing system for a Python project.

---

# 1. Why Automated Testing Matters

Testing is not simply about finding bugs.

A good test suite also provides confidence when software changes.

When developers modify existing code, tests can quickly reveal whether previously working behavior has been affected.

Consider a simple function:

```python
def add(a, b):
    return a + b

A basic test could verify its expected behavior:

def test_add():
    assert add(2, 3) == 5

This test is small, but it establishes an important contract:

When add() receives 2 and 3, the expected result is 5.

As the project grows, more tests can protect more behavior.

2. What pytest Provides

pytest is a Python testing framework designed to make writing and running tests simple.

A typical pytest workflow looks like this:

Write code
    ↓
Write tests
    ↓
Run pytest
    ↓
Inspect failures
    ↓
Fix code
    ↓
Run pytest again

This cycle can be repeated whenever the project changes.

## 2. What pytest Provides

pytest is a Python testing framework designed to make automated testing simple, readable, and practical.

Instead of building a large testing infrastructure, developers can create small Python functions that describe expected behavior and then execute them with pytest.

A typical workflow looks like this:

1. Write application code.
2. Write tests for the expected behavior.
3. Run pytest.
4. Inspect failures.
5. Fix the implementation.
6. Run the tests again.

This cycle can be repeated whenever the project changes.

### Simple Test Discovery

pytest automatically discovers test files and test functions when they follow common naming conventions.

A typical project might contain:

```text
project/
├── calculator.py
├── test_calculator.py
└── requirements.txt

The test file can contain:

from calculator import add


def test_add():
    assert add(2, 3) == 5

Running:

pytest

allows pytest to discover and execute the test automatically.

Why This Matters

The biggest advantage is not simply that pytest runs tests.

The important advantage is that developers can create a predictable feedback loop.

When code changes, the same tests can be executed again.

This makes regression detection much easier.

A developer does not need to remember every behavior that was previously verified manually.

The test suite becomes an executable description of expected behavior.

3. Writing Your First Tests

A pytest test is usually just a Python function whose name begins with test_.

Consider this function:

def multiply(a, b):
    return a * b

A simple test could be:

def test_multiply():
    assert multiply(4, 5) == 20

The test contains an important idea:
Given these inputs, the function should produce this result.

The assert statement verifies that expectation.

If the expression is true, the test passes.

If the expression is false, pytest reports a failure.

Testing More Than One Case

A single test can verify one behavior, but real functions usually need more than one case.

For example:
def divide(a, b):
    return a / b

Tests could include:

def test_divide_positive_numbers():
    assert divide(10, 2) == 5


def test_divide_fraction():
    assert divide(5, 2) == 2.5

Each test has a focused responsibility.

This makes failures easier to understand.

A Useful Testing Principle

A good test should make its expectation obvious.

Compare:

def test_calculation():
    assert calculate(10, 2) == 5

with:

def test_divide_ten_by_two_returns_five():
    assert divide(10, 2) == 5

The second name communicates the intended behavior more clearly.
Test names are part of the documentation of a project.

4. Assertions

Assertions are the foundation of pytest tests.

An assertion expresses something that must be true.

For example:

assert add(2, 3) == 5

The expression can use normal Python comparison operators.

Equality
assert result == expected
This is one of the most common forms.

Example:

assert add(2, 3) == 5
Inequality
assert result != unexpecte
assert calculate_discount(100) != 100
Boolean Conditions

Assertions can also verify boolean expressions:

assert is_valid("admin")

or:

assert not is_valid("")
Membership

Python membership operations can also be tested:

assert "Python" in ["Python", "Java", "Go"]
Comparing Collections

Lists and dictionaries can be compared directly:

def get_languages():
    return ["Python", "JavaScript", "Go"]

A test can verify:
def test_get_languages():
    assert get_languages() == [
        "Python",
        "JavaScript",
        "Go",
    ]

This is one reason pytest tests can remain concise.

There is usually no need to manually construct complex comparison logic for ordinary Python objects.

5. Fixtures

As test suites become larger, tests often need common setup data.

For example, several tests may need the same temporary configuration or object.

Instead of repeating the setup code in every test, pytest provides fixtures.

A simple fixture looks like this:
import pytest


@pytest.fixture
def sample_user():
    return {
        "name": "Ahmed",
        "role": "developer",
    }
A test can request the fixture by using its name as an argument:

def test_user_name(sample_user):
    assert sample_user["name"] == "Ahmed"

Another test can use the same fixture:

def test_user_role(sample_user):
    assert sample_user["role"] == "developer"

The fixture keeps the setup logic in one place.
Why Fixtures Matter

Fixtures become especially useful when tests require:

temporary files
database connections
configuration objects
reusable test data
API clients
application objects
cleanup operations

Instead of every test knowing how to construct these resources, the fixture can provide them.

This creates a cleaner separation between:
Test behavior

and:

Test setup
Fixtures With Cleanup

Fixtures can also be used when a resource needs cleanup.

For example:
import pytest


@pytest.fixture
def resource():
    connection = create_connection()

    yield connection

    connection.close()

The code before yield prepares the resource.

The value after yield is provided to the test.

The code after yield performs cleanup.

This pattern is useful when tests work with resources that should not remain open after execution.

6. Parametrization

Sometimes the same test logic needs to run against several inputs.

Without parametrization, a developer might write:

def test_add_one():
    assert add(1, 1) == 2


def test_add_two():
    assert add(2, 2) == 4


def test_add_three():
    assert add(3, 3) == 6
The tests work, but the structure contains repeated logic.

pytest provides parametrization for this situation.

import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6),
        (10, 5, 15),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
Now the same test logic runs against multiple input combinations.

Why Parametrization Is Useful

Parametrization is especially valuable for functions with many input combinations.

For example:

Input                  Expected Result
--------------------------------------
1 + 1                  2
2 + 2                  4
3 + 3                  6
10 + 5                 15
Instead of creating four separate test functions, one test describes the general behavior.

This reduces duplication while increasing coverage.

Testing Boundary Values

Parametrization is also useful for boundary conditions.

Consider:

def is_adult(age):
    return age >= 18
attention.

@pytest.mark.parametrize(
    "age,expected",
    [
        (17, False),
        (18, True),
        (19, True),
    ],
)
def test_is_adult(age, expected):
    assert is_adult(age) == expected

This makes the boundary explicit.

7. Exception Testing

Not every correct behavior produces a normal return value.

Some functions are expected to raise exceptions when invalid input is provided.

Consider:

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
The test should verify that the exception is actually raised.

pytest provides raises for this:

import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

This test is important because it verifies the error-handling contract of the function.

Testing the Exception Message
Sometimes the message itself is part of the expected behavior.

def test_divide_by_zero_message():
    with pytest.raises(
        ValueError,
        match="Cannot divide by zero",
    ):
        divide(10, 0)

Now the test verifies both:

The correct exception type.
The expected message.
Why Exception Tests Matter

Error paths are often less frequently exercised manually than successful paths.

A function may work correctly for normal input while failing to handle invalid input safely.

Testing exceptions makes those behaviors explicit.

8. Test Organization

A growing project needs a predictable testing structure.

A simple project might look like this:

project/
├── src/
│   ├── calculator.py
│   ├── users.py
│   └── payments.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_users.py
│   └── test_payments.py
│
├── requirements.txt
└── pyproject.toml
Separating application code from test code makes the repository easier to navigate.

One Test File Per Logical Area

For example:

calculator.py
test_calculator.py

and:

users.py
test_users.py

This is not a strict requirement, but it creates an intuitive relationship between implementation and tests.
Keep Tests Focused

A test should ideally verify one behavior or a closely related group of behaviors.

Avoid creating enormous tests that verify many unrelated things.

For example, instead of:

def test_everything():
    ...

prefer focused tests such as:
def test_user_creation():
    ...


def test_user_email_validation():
    ...


def test_user_permissions():
    ...

Focused tests are easier to debug.

Arrange, Act, Assert

A useful structure for many tests is:

Arrange
   ↓
Act
   ↓
Assert
For example:

def test_add():
    # Arrange
    a = 2
    b = 3

    # Act
    result = add(a, b)

    # Assert
    assert result == 5

This structure makes the intention of the test easy to follow.

9. Code Coverage

A test suite can contain many tests without necessarily covering important parts of the application.

Code coverage provides a way to measure which parts of the code are executed by the tests.

A common tool is pytest-cov.

It can be installed with:

pip install pytest-cov

A test suite can then be executed with:
pytest --cov

A more specific example is:

pytest --cov=src

The output can show which files were executed and which lines were missed.

Coverage Is a Measurement, Not a Goal

A high coverage percentage does not automatically mean that a project has high-quality tests.
Consider:

def add(a, b):
    return a + b

A test that executes the function increases coverage.

But the quality of the test depends on whether it verifies meaningful behavior.

Coverage answers a question such as:

Which code was executed?

It does not completely answer:

Was the behavior tested correctly?

Use Coverage to Find Gaps
Coverage becomes useful when it identifies code that has never been exercised.

For example:

calculator.py       95%
users.py            91%
payments.py         63%

The lower coverage in payments.py may indicate that important branches deserve additional tests.

Coverage should therefore be used as a diagnostic tool rather than treated as the only measure of testing quality.

10. Continuous Integration

Automated tests become significantly more useful when they run automatically.

Continuous Integration, commonly called CI, allows tests to run whenever changes are pushed to a repository or submitted through a pull request.

A basic GitHub Actions workflow might look like:
name: Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest

      - name: Run tests
        run: pytest
The workflow creates an automated verification step.

A developer pushes code.

GitHub Actions starts the workflow.

The project dependencies are installed.

pytest runs.

If a test fails, the workflow reports a failure.

Why CI Matters

Without CI, a developer may forget to run the full test suite before pushing changes.

With CI, the repository can automatically verify the changes.

This creates a useful relationship:

Code Change
     ↓
Push
     ↓
Automated Tests
     ↓
Pass or Fail

The feedback becomes part of the development workflow rather than a separate manual task.

11. Testing a Small Real-World Project

The ideas in this capsule become more useful when combined.

Consider a small utility module:

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def is_positive(value):
    return value > 0
A corresponding test file could be:
import pytest

from calculator import add
from calculator import divide
from calculator import is_positive


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (0, False),
        (-1, False),
    ],
)
def test_is_positive(value, expected):
    assert is_positive(value) == expected
This small example already demonstrates several important pytest features:

normal assertions
exception testing
parametrization
focused test functions
readable test names

The project can now be executed with:

pytest

A successful run provides evidence that the tested behaviors currently match the expected results.

12. Best Practices

A useful pytest test suite is not simply a large collection of test functions.

It should be understandable, maintainable, and trustworthy.

Keep Tests Readable

Tests are read by developers when something breaks.

Prefer:

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
over unnecessarily complicated test code.

Test Behavior, Not Implementation Details

Tests should generally focus on what a function or component does.

For example:

assert calculate_total(items) == 150

is often more useful than testing every internal variable used to produce 150.

This makes tests more resistant to refactoring.

Use Descriptive Names
A test name should help explain the expected behavior.

Good:

def test_empty_username_is_rejected():
    ...

Less useful:

def test_case_7():
    ...
Avoid Excessive Duplication

If many tests repeat the same setup, consider a fixture.

If the same test logic is repeated with different values, consider parametrization.

Test Important Boundaries

Typical boundary values deserve special attention.

For example:

Below the boundary
At the boundary
Above the boundary
If a function accepts ages from 18 onward, test:

17
18
19
Keep the Test Suite Fast

A test suite that takes a few seconds is easier to run frequently than one that takes several minutes.

Fast tests encourage developers to run them after every meaningful change.

Run Tests Locally and in CI
Local testing provides immediate feedback.

CI provides an independent automated verification step.

Both are valuable.

13. Final Checklist

Before considering a small Python testing setup complete, verify the following:

 pytest is installed.
 Tests are stored in a dedicated test directory when appropriate.
 Test files follow predictable naming conventions.
 Test functions have descriptive names.
 Assertions verify expected behavior.
 Important error conditions are tested.
 Fixtures are used when setup is shared.
 Parametrization is used when test logic is repeated.
 Boundary values are considered.
 Coverage is used to identify testing gaps.
 Tests run successfully from the command line.
 CI runs the test suite automatically.
 The test suite remains understandable as the project grows.

Conclusion

Automated testing is most valuable when it becomes part of the normal development process.

pytest makes this practical by providing a simple way to write tests using ordinary Python code.

The basic workflow is straightforward:
Write Code
    ↓
Write Tests
    ↓
Run pytest
    ↓
Inspect Failures
    ↓
Improve Code
    ↓
Run Tests Again
As projects grow, fixtures, parametrization, exception testing, coverage, and continuous integration provide additional structure.

The goal is not to create the largest possible test suite.

The goal is to create a test suite that developers can trust.

A reliable test suite gives a project something extremely valuable:

confidence when the code changes.

---

# Thank You for Reading

Thank you for reading **Python Testing with pytest**.

The goal of this capsule was simple: to turn automated testing from a concept into a practical development habit.

You do not need hundreds of tests to start building confidence in your code.

Start small.

Write a test.

Run it.

Improve your code.

Run the tests again.

Over time, this simple workflow becomes one of the strongest safeguards in a growing Python project.

---

## Keep Building. Keep Testing.

Good software is not only code that works.

It is code that can be changed with confidence.

**Write better code.  
Test it.  
Understand it.  
Keep improving it.**

---

### Ahmed Adawy Tech Capsules

Professional technical micro-books designed for developers who prefer practical knowledge over lengthy theory.

**Author:** Ahmed Adawy  
**Series:** Ahmed Adawy Tech Capsules  
**Category:** Python / Testing  
**Version:** 1.0  
**Release:** 2026

---

## More from Ahmed Adawy

Explore more technical capsules covering:

- Python
- Software Architecture
- AI & Generative AI
- High-Performance Computing
- Developer Tools
- Testing & Software Quality

---

**© 2026 Ahmed Adawy**

*Thank you for reading.*
