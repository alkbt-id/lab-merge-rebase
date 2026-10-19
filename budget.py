"""Expenses: loading from CSV and totals."""

import csv
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Expense:
    day: str
    category: str
    amount: Decimal


def load(path: str) -> list[Expense]:
    with open(path, newline="") as f:
        return [
            Expense(row["day"], row["category"], Decimal(row["amount"]))
            for row in csv.DictReader(f)
        ]
