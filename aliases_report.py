"""Text listing of category aliases."""

from categories import ALIASES


def format_aliases() -> str:
    return "\n".join(f"{alias} -> {category}" for alias, category in sorted(ALIASES.items()))
