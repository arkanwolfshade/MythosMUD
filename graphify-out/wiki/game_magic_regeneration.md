# game magic regeneration

> 12 nodes

## Key Concepts

- **._is_uuid_string()** (8 connections) — `server/realtime/occupant_formatter.py`
- **._process_string_occupant_for_update()** (4 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_valid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_length()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_dashes()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_is_uuid_string_invalid_chars()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Check if a string looks like a UUID.          Args:             value: The strin** (1 connections) — `server/realtime/occupant_formatter.py`
- **Process a string occupant (legacy format) and add to list if valid.          Arg** (1 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._is_uuid_string() returns True for valid UUID.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_uuid_string() returns False for invalid length.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_uuid_string() returns False for wrong dash count.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._is_uuid_string() returns False for invalid characters.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [occupant formatter realtime](occupant_formatter_realtime.md) (4 shared connections)
- [container sql injection](container_sql_injection.md) (2 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (2 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*