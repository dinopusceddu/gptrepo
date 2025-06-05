"""Simple data validator with min and max rules."""

from typing import Dict, Tuple, Any

Numeric = float | int


class ValidationError(Exception):
    """Raised when validation fails."""

    pass


def validate_inputs(values: Dict[str, Any], rules: Dict[str, Tuple[Numeric, Numeric]]) -> tuple[bool, Dict[str, str]]:
    """Validate numeric inputs against min/max rules.

    Args:
        values: mapping of field name to value.
        rules: mapping of field name to a tuple ``(min, max)``.

    Returns:
        A tuple ``(is_valid, errors)`` where ``errors`` is a mapping from field
        name to an error message. ``is_valid`` is ``True`` when ``errors`` is
        empty.
    """
    errors: Dict[str, str] = {}
    for field, (minimum, maximum) in rules.items():
        if field not in values:
            errors[field] = f"'{field}' è mancante."
            continue
        value = values[field]
        if not isinstance(value, (int, float)):
            errors[field] = f"'{field}' deve essere un numero."
            continue
        if value < minimum or value > maximum:
            errors[field] = (
                f"'{field}' deve essere compreso tra {minimum} e {maximum}."
            )
    return not errors, errors


def calculate(values: Dict[str, Any], rules: Dict[str, Tuple[Numeric, Numeric]]):
    """Example calculation that only runs with valid inputs."""
    valid, errors = validate_inputs(values, rules)
    if not valid:
        message = "\n".join(f"{field}: {msg}" for field, msg in errors.items())
        raise ValidationError(message)
    return sum(values[field] for field in rules)

