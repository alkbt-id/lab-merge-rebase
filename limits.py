"""Monthly limits per category."""

from decimal import Decimal


def over_limit(totals: dict[str, Decimal], limits: dict[str, Decimal]) -> dict[str, Decimal]:
    return {
        category: amount - limits[category]
        for category, amount in totals.items()
        if category in limits and amount > limits[category]
    }


def format_warnings(over: dict[str, Decimal]) -> str:
    return "\n".join(f"{category}: over by {amount}" for category, amount in sorted(over.items()))
