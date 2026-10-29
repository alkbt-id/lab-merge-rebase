"""HTML report for category totals."""

from decimal import Decimal
from html import escape


def format_html(totals: dict[str, Decimal]) -> str:
    rows = "".join(
        f"<tr><td>{escape(category)}</td><td>{amount}</td></tr>"
        for category, amount in sorted(totals.items())
    )
    return f"<table>{rows}</table>"
