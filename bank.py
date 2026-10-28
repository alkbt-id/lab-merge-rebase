"""Import a bank statement export."""

import csv
from decimal import Decimal

from budget import Expense

CATEGORY_MAP = {"Groceries": "food", "Transit": "transport"}


def load_statement(path: str) -> list[Expense]:
    with open(path, newline="") as f:
        return [
            Expense(row["Date"], CATEGORY_MAP.get(row["Category"], "other"), -Decimal(row["Amount"]))
            for row in csv.DictReader(f, delimiter=";")
            if Decimal(row["Amount"]) < 0
        ]
