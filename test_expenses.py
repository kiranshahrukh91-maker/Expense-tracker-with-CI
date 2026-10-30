import pytest

from expenses import add_expense, total_for


def test_add_expense_appends_valid_expense():
    expenses = []
    add_expense(expenses, 10, "food")
    assert expenses == [{"amount": 10, "category": "food"}]


def test_add_expense_keeps_order():
    expenses = []
    add_expense(expenses, 10, "food")
    add_expense(expenses, 20, "travel")
    assert [e["category"] for e in expenses] == ["food", "travel"]


def test_add_expense_zero_amount_raises():
    with pytest.raises(ValueError):
        add_expense([], 0, "food")


def test_add_expense_negative_amount_raises():
    with pytest.raises(ValueError):
        add_expense([], -5, "food")


def test_add_expense_rejected_leaves_list_unchanged():
    expenses = [{"amount": 10, "category": "food"}]
    with pytest.raises(ValueError):
        add_expense(expenses, -1, "food")
    assert expenses == [{"amount": 10, "category": "food"}]


def test_total_for_sums_only_matching_category():
    expenses = []
    add_expense(expenses, 10, "food")
    add_expense(expenses, 20, "travel")
    add_expense(expenses, 5, "food")
    assert total_for(expenses, "food") == 15


def test_total_for_unknown_category_is_zero():
    expenses = [{"amount": 10, "category": "food"}]
    assert total_for(expenses, "rent") == 0


def test_total_for_empty_list_is_zero():
    assert total_for([], "food") == 0


def test_total_for_handles_decimals():
    expenses = []
    add_expense(expenses, 0.1, "food")
    add_expense(expenses, 0.2, "food")
    assert total_for(expenses, "food") == pytest.approx(0.3)


def test_total_for_two_food_expenses():
    expenses = []
    add_expense(expenses, 20, "food")
    add_expense(expenses, 30, "food")
    assert total_for(expenses, "food") == 50
