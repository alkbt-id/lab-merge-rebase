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
            Expense(row["day"], row["category"].strip(), Decimal(row["amount"]))
            for row in csv.DictReader(f)
        ]


def totals(expenses: list[Expense]) -> dict[str, Decimal]:
    result: dict[str, Decimal] = {}
    for expense in expenses:
        result[expense.category] = result.get(expense.category, Decimal(0)) + expense.amount
    return result
