# Monitoring API Endpoints

> 44 nodes

## Key Concepts

- **test_room_utils.py** (22 connections) — `server/tests/unit/utils/test_room_utils.py`
- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **room_utils.py** (10 connections) — `server/utils/room_utils.py`
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

- [Realtime Service Bundle](Realtime_Service_Bundle.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (1 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 140 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*