# Server Realtime

> 187 nodes

## Key Concepts

- **CircuitBreaker** (41 connections) — `server/realtime/circuit_breaker.py`
- **nats_message_handler.py** (33 connections) — `server/realtime/nats_message_handler.py`
- **test_circuit_breaker.py** (31 connections) — `server/tests/unit/realtime/test_circuit_breaker.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **MessageFilteringHelper** (23 connections) — `server/realtime/message_filtering.py`
- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (17 connections) — `server/realtime/nats_message_handler_processing.py`
- **NATSMessageProcessingMixin** (14 connections) — `server/realtime/nats_message_handler_processing.py`
- **circuit_breaker.py** (11 connections) — `server/realtime/circuit_breaker.py`
- **CircuitBreakerOpen** (9 connections) — `server/realtime/circuit_breaker.py`
- **.call()** (9 connections) — `server/realtime/circuit_breaker.py`
- **._process_single_message()** (9 connections) — `server/realtime/nats_message_handler_processing.py`
- **.is_player_in_room()** (7 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **Any** (7 connections)
- **CircuitState** (6 connections) — `server/realtime/circuit_breaker.py`
- **._transition_to()** (6 connections) — `server/realtime/circuit_breaker.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 162 more nodes in this community*

## Relationships

- [Server Services (5)](Server_Services_%285%29.md) (22 shared connections)
- [Server Commands](Server_Commands.md) (10 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (10 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (4 shared connections)
- [Server Realtime (26)](Server_Realtime_%2826%29.md) (4 shared connections)
- [Server Realtime (80)](Server_Realtime_%2880%29.md) (4 shared connections)
- [Server Realtime (89)](Server_Realtime_%2889%29.md) (3 shared connections)
- [Server Realtime (49)](Server_Realtime_%2849%29.md) (3 shared connections)
- [Server Realtime (58)](Server_Realtime_%2858%29.md) (3 shared connections)
- [Server Realtime (16)](Server_Realtime_%2816%29.md) (3 shared connections)
- [Server Realtime (41)](Server_Realtime_%2841%29.md) (2 shared connections)
- [Server Realtime (86)](Server_Realtime_%2886%29.md) (2 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_circuit_breaker.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 600 (95%)
- INFERRED: 32 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*