# Expense tracker with CI

A simple expense tracker with continuous integration.

## Usage

```python
from expenses import add_expense, total_for

expenses = []
add_expense(expenses, 12.5, "food")
print(total_for(expenses, "food"))  # 12.5
```
