"""Totals by month."""

from decimal import Decimal

from budget import Expense


def by_month(expenses: list[Expense]) -> dict[str, Decimal]:
    result: dict[str, Decimal] = {}
    for expense in expenses:
        month = expense.day[:7]
        result[month] = result.get(month, Decimal(0)) + expense.amount
    return result
