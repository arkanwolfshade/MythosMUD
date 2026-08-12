# NATSMessageHandler

> 124 nodes

## Key Concepts

- **NATSMessageHandler** (77 connections) — `server/realtime/nats_message_handler.py`
- **Any** (28 connections)
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler.py`
- **._process_single_message()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler.py`
- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._broadcast_by_channel_type()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.unsubscribe_from_subzone()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.cleanup_empty_subzone_subscriptions()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._echo_message_to_sender()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._extract_chat_message_fields()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._filter_target_players()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._process_message_with_retry()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.subscribe_to_event_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- *... and 99 more nodes in this community*

## Relationships

- [build_event](build_event.md) (10 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [database.py](database.py.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 386 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*