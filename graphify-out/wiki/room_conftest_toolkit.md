# room conftest toolkit

> 20 nodes

## Key Concepts

- **temp_dir()** (11 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **conftest.py** (9 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **temp_rooms_dir()** (3 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **sample_room_data()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **sample_room_database()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **invalid_room_data()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **room_with_new_exit_format()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **room_with_self_reference()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **dead_end_room()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **unreachable_room()** (2 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Create a temporary directory for testing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_utilities.py`
- **Pytest configuration and fixtures for room validator tests.  Provides test data** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Create a temporary directory with test room files.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Sample room data for testing.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Sample room database for testing.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Invalid room data for testing error conditions.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Room data using the new object format for exits.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Room data with self-reference exit.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Room data with no exits (dead end).** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`
- **Room data that would be unreachable from the starting room.** (1 connections) — `tools/room_toolkit/room_validator/tests/conftest.py`

## Relationships

- [room validator toolkit](room_validator_toolkit.md) (4 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (3 shared connections)
- [logging structured utilities](logging_structured_utilities.md) (2 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_logging_utilities.py`
- `tools/room_toolkit/room_validator/tests/conftest.py`

## Audit Trail

- EXTRACTED: 38 (81%)
- INFERRED: 9 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*