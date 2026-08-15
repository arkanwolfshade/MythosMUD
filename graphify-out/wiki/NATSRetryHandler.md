# NATSRetryHandler

> 111 nodes

## Key Concepts

- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **Any** (7 connections)
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._filter_target_players()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **.retry_async()** (5 connections) — `server/realtime/nats_retry_handler.py`
- **UserManager** (5 connections)
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._preload_receiver_mute_data()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **.calculate_backoff()** (4 connections) — `server/realtime/nats_retry_handler.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 86 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [test_nats_retry_handler.py](test_nats_retry_handler.py.md) (11 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [RetryableMessage](RetryableMessage.md) (6 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (4 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (4 shared connections)
- [RetryConfig](RetryConfig.md) (3 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (2 shared connections)
- [EventHandler](EventHandler.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (2 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (2 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 176 (81%)
- INFERRED: 40 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*