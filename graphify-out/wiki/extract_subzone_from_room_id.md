# extract_subzone_from_room_id

> 8 nodes

## Key Concepts

- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **test_extract_subzone_from_room_id()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_downtown()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **test_extract_subzone_from_room_id_invalid()** (3 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() extracts subzone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() extracts different subzone.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Test extract_subzone_from_room_id() returns None for invalid format.** (1 connections) — `server/tests/unit/utils/test_room_utils.py`
- **Extract sub-zone from room ID. Room ID format:…** (1 connections) — `server/utils/room_utils.py`

## Relationships

- [test_room_utils.py](test_room_utils.py.md) (5 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)
- [get_subzone_local_channel_subject](get_subzone_local_channel_subject.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_room_utils.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*