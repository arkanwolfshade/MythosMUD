# NATSMessageHandler

> 129 nodes · cohesion 0.02

## Key Concepts

- **NATSMessageHandler** (77 connections) — `server/realtime/nats_message_handler.py`
- **Any** (28 connections)
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler.py`
- **._process_single_message()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._send_messages_to_players()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._apply_dampening_and_send_message()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_lucidity_tier()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (7 connections) — `server/realtime/nats_message_handler.py`
- **UUID** (7 connections)
- **._broadcast_by_channel_type()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._echo_message_to_sender()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler.py`
- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler.py`
- **apply_communication_dampening()** (6 connections) — `server/services/lucidity_communication_dampening.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.unsubscribe_from_subzone()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.cleanup_empty_subzone_subscriptions()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._extract_chat_message_fields()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._filter_target_players()** (4 connections) — `server/realtime/nats_message_handler.py`
- *... and 104 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (9 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (3 shared connections)
- [EventHandler](EventHandler.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [format_message_content](format_message_content.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 406 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*