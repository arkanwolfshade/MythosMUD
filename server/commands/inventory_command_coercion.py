"""Parse numeric fields from object-typed JSON command payloads."""


def coerce_int(value: object, *, default: int = 1) -> int:
    """Parse stack quantity fields from object-typed JSON payloads."""
    if value is None:
        return default
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return int(value)
    if isinstance(value, float):
        return int(value)
    return default
