from decimal import Decimal

from budget import Expense
from monthly import by_month


def test_by_month():
    expenses = [
        Expense("2026-09-30", "food", Decimal("5.00")),
        Expense("2026-10-01", "food", Decimal("12.50")),
        Expense("2026-10-02", "fun", Decimal("1.50")),
    ]
    assert by_month(expenses) == {"2026-09": Decimal("5.00"), "2026-10": Decimal("14.00")}
