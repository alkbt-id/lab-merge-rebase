from decimal import Decimal

from export import to_json


def test_to_json():
    assert to_json({"food": Decimal("20.50")}) == '{"food": "20.50"}'
