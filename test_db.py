import pytest

from db import connect, db_total_for, load_expenses, save_expense


def test_saved_expenses_are_loaded_in_order():
    conn = connect(":memory:")
    save_expense(conn, 20, "food")
    save_expense(conn, 30, "food")
    assert load_expenses(conn) == [
        {"amount": 20, "category": "food"},
        {"amount": 30, "category": "food"},
    ]


def test_db_total_for_returns_max_food():
    conn = connect(":memory:")
    save_expense(conn, 20, "food")
    save_expense(conn, 30, "food")
    save_expense(conn, 15, "travel")
    assert db_total_for(conn, "food") == 30


def test_invalid_amount_is_not_saved():
    conn = connect(":memory:")
    with pytest.raises(ValueError):
        save_expense(conn, 0, "food")
    assert load_expenses(conn) == []


def test_values_persist_across_connections(tmp_path):
    path = str(tmp_path / "expenses.db")
    conn = connect(path)
    save_expense(conn, 20, "food")
    conn.close()

    conn = connect(path)
    assert load_expenses(conn) == [{"amount": 20, "category": "food"}]
