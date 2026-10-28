"""Monthly limits per category."""

from decimal import Decimal


def over_limit(totals: dict[str, Decimal], limits: dict[str, Decimal]) -> dict[str, Decimal]:
    return {
        category: amount - limits[category]
        for category, amount in totals.items()
        if category in limits and amount > limits[category]
    }
