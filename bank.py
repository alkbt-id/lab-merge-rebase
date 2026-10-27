"""Import a bank statement export."""

import csv
from decimal import Decimal

from budget import Expense


def load_statement(path: str) -> list[Expense]:
    with open(path, newline="") as f:
        return [
            Expense(row["Date"], row["Category"], -Decimal(row["Amount"]))
            for row in csv.DictReader(f, delimiter=";")
            if Decimal(row["Amount"]) < 0
        ]
