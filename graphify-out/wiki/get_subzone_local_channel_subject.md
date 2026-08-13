# get_subzone_local_channel_subject

> 6 nodes

## Key Concepts

- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **test_get_subzone_local_channel_subject()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_get_subzone_local_channel_subject_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_subzone_local_channel_subject() generates subject.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test get_subzone_local_channel_subject() returns None for invalid room ID.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Generate NATS subject for sub-zone local channel messages. This creates a…** (1 connections) — `server/utils/room_utils.py`

## Relationships

- [test_room_utils.py](test_room_utils.py.md) (4 shared connections)
- [extract_subzone_from_room_id](extract_subzone_from_room_id.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*