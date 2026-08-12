# Look Display Helpers

> 85 nodes

## Key Concepts

- **test_room_renderer.py** (25 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **format_room_drop_lines()** (25 connections) — `server/utils/room_renderer.py`
- **clone_room_drops()** (18 connections) — `server/utils/room_renderer.py`
- **test_room_renderer_functions.py** (14 connections) — `server/tests/unit/utils/test_room_renderer_functions.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_drop_summary()** (13 connections) — `server/utils/room_renderer.py`
- **room_renderer.py** (10 connections) — `server/utils/room_renderer.py`
- **test_websocket_room_updates_build_event.py** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **_coerce_stack()** (4 connections) — `server/utils/room_renderer.py`
- **Any** (4 connections)
- **test_build_room_update_event()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_format_room_drop_lines_empty_none()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_empty_list()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_single_drop()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_multiple_drops()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_uses_item_id_when_no_item_name()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_uses_default_when_no_name_or_id()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_handles_missing_slot_type()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_handles_missing_quantity()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_handles_invalid_quantity_string()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_handles_invalid_quantity_type()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_format_room_drop_lines_handles_large_quantity()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_build_room_drop_summary_empty()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- **test_build_room_drop_summary_single_drop()** (3 connections) — `server/tests/unit/utils/test_room_renderer.py`
- *... and 60 more nodes in this community*

## Relationships

- [Container Persistence Queries](Container_Persistence_Queries.md) (8 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (3 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (2 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)
- [Party Service Management](Party_Service_Management.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/utils/test_room_renderer.py`
- `server/tests/unit/utils/test_room_renderer_functions.py`
- `server/utils/room_renderer.py`

## Audit Trail

- EXTRACTED: 272 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*