"""Parse numeric fields from object-typed JSON command payloads."""


def _int_from_decimal_string(stripped: str, default: int) -> int:
    try:
        return int(stripped)
    except ValueError:
        return default


def _int_from_float_safe(value: float, default: int) -> int:
    try:
        return int(value)
    except (ValueError, OverflowError):
        return default


def coerce_int(value: object, *, default: int = 1) -> int:
    """
    Parse stack quantity fields from object-typed JSON payloads.

    Non-numeric strings and invalid floats fall back to ``default`` (no uncaught
    ``ValueError``), matching the pattern in ``_coerce_transfer_quantity``.
    """
    if value is None:
        return default
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return default
        return _int_from_decimal_string(stripped, default)
    if isinstance(value, float):
        return _int_from_float_safe(value, default)
    return default
