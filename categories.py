"""Category aliases: several names for one category."""

ALIASES = {"groceries": "food", "taxi": "transport", "metro": "transport"}


def canonical(category: str) -> str:
    name = category.strip().lower()
    return ALIASES.get(name, name)
