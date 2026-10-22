"""Command line: python cli.py <expenses.csv>"""

import sys

from budget import load, totals
from report import format_report


def main() -> None:
    expenses = load(sys.argv[1])
    print(format_report(totals(expenses)))


if __name__ == "__main__":
    main()
