# extract_subzone_from_room_id

> 10 nodes

## Key Concepts

- **extract_subzone_from_room_id()** (15 connections) — `server/utils/room_utils.py`
- **room_utils.py** (10 connections) — `server/utils/room_utils.py`
- **chat_channel_logger.py** (8 connections) — `server/services/chat_channel_logger.py`
- **get_subzone_local_channel_subject()** (6 connections) — `server/utils/room_utils.py`
- **log_time_formats.py** (6 connections) — `server/structured_logging/log_time_formats.py`
- **Channel-specific chat log methods for MythosMUD. Mixin used by ChatLogger:…** (1 connections) — `server/services/chat_channel_logger.py`
- **Stable strftime patterns for log filenames and aggregation keys. These are…** (1 connections) — `server/structured_logging/log_time_formats.py`
- **Room utility functions for MythosMUD. This module provides utility functions…** (1 connections) — `server/utils/room_utils.py`
- **Extract sub-zone from room ID. Room ID format:…** (1 connections) — `server/utils/room_utils.py`
- **Generate NATS subject for sub-zone local channel messages. This creates a…** (1 connections) — `server/utils/room_utils.py`

## Relationships

- [test_room_utils.py](test_room_utils.py.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (2 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (1 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (1 shared connections)

## Source Files

- `server/services/chat_channel_logger.py`
- `server/structured_logging/log_time_formats.py`
- `server/utils/room_utils.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*