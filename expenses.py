def add_expense(expenses, amount, category):
    if amount <= 0:
        raise ValueError("Amount must be more than 0")
    expenses.append({"amount": amount, "category": category})


def total_for(expenses, category):
    return sum(e["amount"] for e in expenses if e["category"] == category)
