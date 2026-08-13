# test_room_utils.py

> 22 nodes

## Key Concepts

- **test_room_utils.py** (22 connections) — `server/tests/unit/utils/test_room_utils.py`
- **room_utils.py** (10 connections) — `server/utils/room_utils.py`
- **get_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **get_zone_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **is_valid_room_id_format()** (5 connections) — `server/utils/room_utils.py`
- **test_get_local_channel_subject()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_local_channel_subject_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id_innsmouth()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_zone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_is_valid_room_id_format()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Unit tests for room_utils. Tests utility functions for room operations.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_zone_from_room_id() extracts zone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_zone_from_room_id() extracts different zone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_zone_from_room_id() returns None for invalid format.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test is_valid_room_id_format() validates room ID format.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_local_channel_subject() generates subject (deprecated).** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_local_channel_subject() returns None for invalid room ID.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Room utility functions for MythosMUD. This module provides utility functions…** (1 connections) — `server/utils/room_utils.py`
- **Check if a room ID follows the expected format. Args: room_id: The room ID to…** (1 connections) — `server/utils/room_utils.py`
- **DEPRECATED: Generate NATS subject for local channel messages. .. deprecated::…** (1 connections) — `server/utils/room_utils.py`
- **Extract zone from room ID. Room ID format:…** (1 connections) — `server/utils/room_utils.py`

## Relationships

- [extract_subzone_from_room_id](extract_subzone_from_room_id.md) (5 shared connections)
- [get_plane_from_room_id](get_plane_from_room_id.md) (5 shared connections)
- [get_subzone_local_channel_subject](get_subzone_local_channel_subject.md) (4 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*