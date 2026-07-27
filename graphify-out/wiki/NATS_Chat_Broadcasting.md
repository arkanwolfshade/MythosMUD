# NATS Chat Broadcasting

> 128 nodes · cohesion 0.02

## Key Concepts

- **NATSMessageHandler** (79 connections) — `server/realtime/nats_message_handler.py`
- **Any** (36 connections) — `server/realtime/nats_message_handler.py`
- **UUID** (15 connections) — `server/realtime/nats_message_handler.py`
- **CircuitBreakerOpen** (13 connections) — `server/realtime/circuit_breaker.py`
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler.py`
- **._process_single_message()** (9 connections) — `server/realtime/nats_message_handler.py`
- **._send_messages_to_players()** (8 connections) — `server/realtime/nats_message_handler.py`
- **._apply_dampening_and_send_message()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._get_player_lucidity_tier()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (6 connections) — `server/realtime/nats_message_handler.py`
- **.unsubscribe_from_subzone()** (6 connections) — `server/realtime/nats_message_handler.py`
- **._broadcast_by_channel_type()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._echo_message_to_sender()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.subscribe_to_event_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.subscribe_to_subzone()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.cleanup_empty_subzone_subscriptions()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler.py`
- *... and 103 more nodes in this community*

## Relationships

- [[Database Manager Tests]] (9 shared connections)
- [[Dead Letter Queue]] (8 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[Circuit Breaker Core]] (7 shared connections)
- [[Realtime Service Bundle]] (5 shared connections)
- [[NATS Message Handler Tests]] (3 shared connections)
- [[Room Occupant Events]] (3 shared connections)
- [[Realtime Event Handlers]] (3 shared connections)
- [[Chat Message Filtering]] (3 shared connections)
- [[NATS Retry Handler]] (3 shared connections)
- [[Realtime Conftest Mocks]] (2 shared connections)
- [[Realtime Message Formatters]] (2 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 408 (91%)
- INFERRED: 38 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
