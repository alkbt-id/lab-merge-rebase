from decimal import Decimal

from limits import over_limit


def test_over_limit():
    totals = {"food": Decimal("120"), "fun": Decimal("30")}
    limits = {"food": Decimal("100"), "fun": Decimal("50")}
    assert over_limit(totals, limits) == {"food": Decimal("20")}
