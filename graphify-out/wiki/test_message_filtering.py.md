# test_message_filtering.py

> 146 nodes

## Key Concepts

- **test_message_filtering.py** (41 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **MessageFilteringHelper** (32 connections) — `server/realtime/message_filtering.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (18 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **message_filtering.py** (16 connections) — `server/realtime/message_filtering.py`
- **asyncio** (15 connections)
- **dead_letter_queue.py** (12 connections) — `server/realtime/dead_letter_queue.py`
- **BroadcastFilterContext** (11 connections) — `server/realtime/message_filtering.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **nats_retry_handler.py** (10 connections) — `server/realtime/nats_retry_handler.py`
- **test_message_filtering_helpers.py** (10 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **._should_include_target()** (6 connections) — `server/realtime/message_filtering.py`
- **._debug_dump_receiver_mute_cache()** (5 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (5 connections) — `server/realtime/message_filtering.py`
- **test_filter_target_players_includes_allowed_player()** (5 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_filter_target_players_skips_mute_check_for_non_sensitive_channel()** (5 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **.get_player_room_from_online_players()** (4 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (4 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (4 connections) — `server/realtime/message_filtering.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- *... and 121 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [NATSError](NATSError.md) (11 shared connections)
- [nats_message_handler_processing.py](nats_message_handler_processing.py.md) (8 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (7 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (6 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (6 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (5 shared connections)
- [UserManager](UserManager.md) (4 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (3 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (3 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (3 shared connections)
- [EventHandler](EventHandler.md) (3 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 282 (94%)
- INFERRED: 18 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*