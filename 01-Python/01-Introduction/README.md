# Chapter 1: Introduction to Python

Python is a general-purpose programming language widely used for automation, data analysis, visualization, machine learning, and web development. Its readable syntax and extensive library ecosystem make it a strong first language for data professionals.

## Learning Objectives

By the end of this chapter, you should be able to:

- Explain what Python is and why it is useful for data analytics.
- Run Python code in a terminal, script, or notebook.
- Recognize Python's basic syntax and indentation rules.
- Use comments, variables, expressions, and built-in functions.
- Read simple Python code and predict its output.
- Choose an appropriate next step in a data analytics learning path.

## What Is Python?

Python is an interpreted, high-level language. Python code is executed by the Python interpreter rather than compiled directly into a native executable before it runs. Python is dynamically typed, which means a variable name can refer to values of different types during a program's lifetime.

```python
message = "Hello, Python"
print(message)
```

## Why Python for Data Analytics?

Python supports the complete analytics workflow:

| Workflow stage | Common tools |
| --- | --- |
| Data collection | `requests`, APIs, database connectors |
| Data cleaning | `pandas`, built-in string and file tools |
| Numerical computing | `NumPy`, `SciPy` |
| Visualization | `Matplotlib`, `Seaborn`, `Plotly` |
| Machine learning | `scikit-learn`, `XGBoost` |
| Reporting and applications | Jupyter, Streamlit, Dash |

## How Python Code Runs

### Interactive interpreter

The interpreter executes one statement at a time. It is useful for quick experiments.

```text
>>> 2 + 3
5
```

### Script file

A `.py` file stores reusable Python code. Run one from a terminal with:

```bash
python examples.py
```

### Notebook

Jupyter notebooks combine code, output, notes, and charts. They are useful for exploratory analysis because code can be run in small, visible cells.

## Core Syntax Rules

- Python is case-sensitive: `total` and `Total` are different names.
- Indentation defines code blocks. Use four spaces consistently.
- A colon begins an indented block after statements such as `if`, `for`, and `def`.
- Comments begin with `#` and are ignored by the interpreter.
- Names should describe their values, such as `monthly_revenue`.

```python
sales = 1250

if sales > 1000:
	print("Target reached")
```

## Built-in Functions

Python includes functions for common operations:

```python
numbers = [12, 7, 19, 4]
print(len(numbers))
print(sum(numbers))
print(max(numbers))
```

## A Small Analytics Example

```python
daily_sales = [120, 150, 90, 200, 175]
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)

print(f"Total sales: ${total_sales}")
print(f"Average daily sales: ${average_sales:.2f}")
```

## Suggested Study Order

1. Practice the examples in `examples.py`.
2. Complete the exercises in `practice.md` without looking at solutions first.
3. Attempt `assignment.md` as a small independent project.
4. Use `cheatsheet.md` and `glossary.md` for revision.
5. Check your understanding with `quiz.md` and `interview.md`.
6. Continue to Chapter 2, Installation, when you can explain the examples aloud.

## Files in This Chapter

| File | Purpose |
| --- | --- |
| `examples.py` | Runnable demonstrations |
| `practice.md` | Guided exercises |
| `assignment.md` | Independent homework |
| `interview.md` | Interview preparation |
| `cheatsheet.md` | One-page revision |
| `quiz.md` | Multiple-choice questions |
| `glossary.md` | Important terms |
| `resources.md` | Official references |
