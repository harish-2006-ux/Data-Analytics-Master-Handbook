# Python Introduction Cheatsheet

## Running Code

```bash
python --version
python examples.py
```

## Comments and Output

```python
# This is a comment
print("Hello")
print(f"Total: {total:.2f}")
```

## Assignment and Types

```python
name = "Amina"       # str
count = 4             # int
rate = 0.25           # float
active = True         # bool
missing = None        # NoneType
```

## Operators

| Operator | Meaning | Example |
| --- | --- | --- |
| `+`, `-` | Add, subtract | `a + b` |
| `*`, `/` | Multiply, divide | `a * b` |
| `//`, `%` | Floor division, remainder | `7 % 3` |
| `**` | Exponent | `2 ** 3` |
| `==`, `!=` | Equal, not equal | `a == b` |
| `>`, `<` | Greater, less | `sales > target` |

## Built-ins

```python
len(items)
sum(numbers)
min(numbers)
max(numbers)
type(value)
round(number, 2)
```

## Conditions and Comprehensions

```python
if score >= 50:
    result = "Pass"
else:
    result = "Review"

positive = [value for value in values if value > 0]
```

## Naming

Use `snake_case`, begin with a letter or underscore, and avoid Python keywords. Prefer `average_revenue` over `ar`.