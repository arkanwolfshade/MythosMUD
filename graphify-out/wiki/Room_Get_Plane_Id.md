# Room Get Plane Id

> 8 nodes · cohesion 0.25

## Key Concepts

- **get_plane_from_room_id()** (6 connections) — `server/utils/room_utils.py`
- **test_get_plane_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id_dream()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_plane_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Extract zone from room ID.      Room ID format: {plane}_{zone}_{sub_zone}_{room_** (2 connections) — `server/utils/room_utils.py`
- **Test get_plane_from_room_id() extracts plane.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_plane_from_room_id() extracts different plane.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_plane_from_room_id() returns None for invalid format.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`

## Relationships

- [[Room Get Zone Id]] (5 shared connections)
- [[Room Services Validator]] (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
