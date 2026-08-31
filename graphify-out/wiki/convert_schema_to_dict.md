# convert_schema_to_dict

> 9 nodes

## Key Concepts

- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **.model_dump()** (4 connections) — `server/models/alias.py`
- **test_convert_schema_to_dict_with_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_model_dump()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Any** (1 connections)
- **Convert alias to dictionary for JSON serialization.** (1 connections) — `server/models/alias.py`
- **Convert Pydantic schema to dictionary.** (1 connections) — `server/realtime/websocket_helpers.py`
- **Test convert_schema_to_dict() uses model_dump() when available.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test convert_schema_to_dict() uses dict() when model_dump() not available.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (3 shared connections)
- [Alias](Alias.md) (1 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*