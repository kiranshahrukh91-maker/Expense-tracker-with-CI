import sqlite3

from expenses import add_expense

DEFAULT_DB = "expenses.db"


def connect(path=DEFAULT_DB):
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS expenses ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "amount REAL NOT NULL, "
        "category TEXT NOT NULL)"
    )
    conn.commit()
    return conn


def save_expense(conn, amount, category):
    # Reuse the existing validation so the DB never holds invalid amounts.
    add_expense([], amount, category)
    conn.execute(
        "INSERT INTO expenses (amount, category) VALUES (?, ?)",
        (amount, category),
    )
    conn.commit()


def load_expenses(conn):
    rows = conn.execute(
        "SELECT amount, category FROM expenses ORDER BY id"
    ).fetchall()
    return [{"amount": amount, "category": category} for amount, category in rows]


def db_total_for(conn, category):
    amounts = [e["amount"] for e in load_expenses(conn) if e["category"] == category]
    return max(amounts, default=0)
