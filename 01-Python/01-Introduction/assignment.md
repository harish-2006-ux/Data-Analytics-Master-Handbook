# Assignment: Weekly Sales Reporter

Build a command-line report for one week of sales.

## Requirements

1. Store seven daily sales values in a list.
2. Calculate total sales, average daily sales, highest sales, and lowest sales.
3. Count how many days met a target chosen by you.
4. Print a readable report with currency values formatted to two decimal places.
5. Print a message stating whether the weekly average met the target.
6. Include at least one comment and use descriptive variable names.

## Example Input

```python
daily_sales = [1200, 980, 1450, 1100, 1675, 1525, 890]
target = 1200
```

## Expected Output Shape

```text
Weekly Sales Report
-------------------
Total: $8820.00
Average: $1260.00
Highest day: $1675.00
Lowest day: $890.00
Days meeting target: 4
Weekly average target: Met
```

## Submission Checklist

- The file runs without errors.
- The report works if the sales values are changed.
- No values are hard-coded into the output messages.
- The code uses `sum`, `len`, `min`, and `max` appropriately.
- The output is clear to a non-programmer.