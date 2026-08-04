# room rationale subzone

> 44 nodes

## Key Concepts

- **test_room_utils.py** (22 connections) — `server/tests/unit/utils/test_room_utils.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **room_utils.py** (9 connections) — `server/utils/room_utils.py`
- **get_zone_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_plane_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **get_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **is_valid_room_id_format()** (5 connections) — `server/utils/room_utils.py`
- **test_extract_subzone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_downtown()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id_innsmouth()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id_dream()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_is_valid_room_id_format()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_local_channel_subject()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_local_channel_subject_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_subzone_local_channel_subject()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_subzone_local_channel_subject_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Unit tests for room_utils.  Tests utility functions for room operations.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() extracts subzone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() extracts different subzone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- *... and 19 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [alias command models](alias_command_models.md) (1 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (1 shared connections)
- [persistence services combat](persistence_services_combat.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 139 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*