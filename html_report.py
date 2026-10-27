"""HTML report for category totals."""

from decimal import Decimal


def format_html(totals: dict[str, Decimal]) -> str:
    rows = "".join(
        f"<tr><td>{category}</td><td>{amount}</td></tr>"
        for category, amount in sorted(totals.items())
    )
    return f"<table>{rows}</table>"
