"""Text report for category totals."""

from decimal import Decimal


def format_report(totals: dict[str, Decimal]) -> str:
    lines = [f"{category:<12}{amount:>10.2f}" for category, amount in sorted(totals.items())]
    lines.append(f"{'total':<12}{sum(totals.values()):>10.2f}")
    return "\n".join(lines)
