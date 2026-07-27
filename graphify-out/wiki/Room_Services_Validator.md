# Room Services Validator

> 13 nodes · cohesion 0.17

## Key Concepts

- **room_utils.py** (8 connections) — `server/utils/room_utils.py`
- **get_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **is_valid_room_id_format()** (5 connections) — `server/utils/room_utils.py`
- **test_get_local_channel_subject()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_local_channel_subject_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_is_valid_room_id_format()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_is_valid_room_id()** (2 connections) — `server/tests/unit/services/test_room_data_validator.py`
- **Test is_valid_room_id_format() validates room ID format.** (2 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Room utility functions for MythosMUD.  This module provides utility functions fo** (1 connections) — `server/utils/room_utils.py`
- **Check if a room ID follows the expected format.      Args:         room_id: The** (1 connections) — `server/utils/room_utils.py`
- **DEPRECATED: Generate NATS subject for local channel messages.      .. deprecated** (1 connections) — `server/utils/room_utils.py`
- **Test get_local_channel_subject() generates subject (deprecated).** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_local_channel_subject() returns None for invalid room ID.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`

## Relationships

- [[Room Get Zone Id]] (6 shared connections)
- [[Services Room Validator]] (1 shared connections)
- [[Distributed Event Bus]] (1 shared connections)
- [[Chat NATS Publisher]] (1 shared connections)
- [[Room Get Plane Id]] (1 shared connections)
- [[Room Get Subzone Local]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_room_data_validator.py`
- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
