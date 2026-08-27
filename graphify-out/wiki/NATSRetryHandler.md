# NATSRetryHandler

> 330 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **DeadLetterQueue** (40 connections) — `server/realtime/dead_letter_queue.py`
- **test_message_filtering.py** (37 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **test_dead_letter_queue.py** (29 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **asyncio** (13 connections)
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **Any** (12 connections)
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_filtering_helpers.py** (11 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **._setup_nats_dependent_services()** (7 connections) — `server/container/bundles/realtime.py`
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **Any** (7 connections)
- **Any** (7 connections)
- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- *... and 305 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (48 shared connections)
- [test_nats_retry_handler.py](test_nats_retry_handler.py.md) (32 shared connections)
- [NATSError](NATSError.md) (9 shared connections)
- [EventHandler](EventHandler.md) (7 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (7 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (3 shared connections)
- [get_async_session](get_async_session.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [PlayerRoomEventHandler](PlayerRoomEventHandler.md) (3 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 571 (94%)
- INFERRED: 34 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*