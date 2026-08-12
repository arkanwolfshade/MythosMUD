# validate_occupant_name

> 14 nodes

## Key Concepts

- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **_accumulate_valid_occupant_name()** (4 connections) — `server/realtime/websocket_helpers.py`
- **test_validate_occupant_name_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_none()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_not_string()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_uuid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_validate_occupant_name_valid()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Validate that a name is not a UUID string.** (1 connections) — `server/realtime/websocket_helpers.py`
- **Parse one occupant row: append display name or log when it looks like a UUID.** (1 connections) — `server/realtime/websocket_helpers.py`
- **Test validate_occupant_name() returns True for valid name.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test validate_occupant_name() returns False for UUID string.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test validate_occupant_name() returns False for empty string.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test validate_occupant_name() returns False for None.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test validate_occupant_name() returns False for non-string.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (7 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 26 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*