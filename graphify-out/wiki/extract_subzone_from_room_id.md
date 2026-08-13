# extract_subzone_from_room_id

> 12 nodes

## Key Concepts

- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **test_extract_subzone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_downtown()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Resolve the subzone ID for a destination room (from room attribute or room_id).…** (1 connections) — `server/npc/movement_integration.py`
- **Validate that a destination room is within the NPC's allowed subzone. This…** (1 connections) — `server/npc/movement_integration.py`
- **Test extract_subzone_from_room_id() extracts subzone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() extracts different subzone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() returns None for invalid format.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Extract sub-zone from room ID. Room ID format:…** (1 connections) — `server/utils/room_utils.py`

## Relationships

- [test_room_utils.py](test_room_utils.py.md) (5 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [chat_nats_publisher.py](chat_nats_publisher.py.md) (2 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)
- [get_subzone_local_channel_subject](get_subzone_local_channel_subject.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`
- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*