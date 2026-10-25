"""Text report for category totals."""

from decimal import Decimal

BOLD = "\033[1m"
RESET = "\033[0m"


def format_report(totals: dict[str, Decimal]) -> str:
    lines = [f"{category:<12}{amount:>10}" for category, amount in sorted(totals.items())]
    lines.append(f"{BOLD}{'total':<12}{sum(totals.values()):>10}{RESET}")
    return "\n".join(lines)
