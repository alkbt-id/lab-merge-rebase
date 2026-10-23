from decimal import Decimal

from budget import Expense, totals


def test_totals_by_category():
    expenses = [
        Expense("2026-10-01", "food", Decimal("12.50")),
        Expense("2026-10-01", "transport", Decimal("2.10")),
        Expense("2026-10-02", "food", Decimal("8.00")),
    ]
    assert totals(expenses) == {"food": Decimal("20.50"), "transport": Decimal("2.10")}
