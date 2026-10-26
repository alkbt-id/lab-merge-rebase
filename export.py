"""Export category totals to JSON."""

import json
from decimal import Decimal


def to_json(totals: dict[str, Decimal]) -> str:
    return json.dumps({category: str(amount) for category, amount in totals.items()})
