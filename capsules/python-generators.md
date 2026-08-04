---
title: Python Generators
subtitle: Memory Efficient Iteration
category: Python
difficulty: Intermediate
language: en
version: 1.0
author: Ahmed Adawy
---

# Python Generators

Generators allow lazy evaluation in Python.

## Why use generators?

- Lower memory usage
- Faster iteration
- Infinite sequences

## Example

```python
def squares():
    n = 0
    while True:
        yield n * n
        n += 1
```

## Best Practices

- Use generators for large datasets.
- Prefer `yield` over building huge lists.
- Combine with itertools when appropriate.
