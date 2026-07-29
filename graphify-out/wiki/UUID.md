# UUID

> 187 nodes

## Key Concepts

- **build_event()** (112 connections) — `server/realtime/envelope.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (26 connections) — `server/realtime/envelope.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **nats_message_handler_processing.py** (19 connections) — `server/realtime/nats_message_handler_processing.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **dead_letter_queue.py** (9 connections) — `server/realtime/dead_letter_queue.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_send_combat_participant_updates()** (8 connections) — `server/realtime/event_handlers.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- *... and 162 more nodes in this community*

## Relationships

- [Any](Any.md) (43 shared connections)
- [main()](main%28%29.md) (24 shared connections)
- [. init ()](_init_%28%29.md) (19 shared connections)
- [Player](Player.md) (11 shared connections)
- [as event data dict()](as_event_data_dict%28%29.md) (11 shared connections)
- [message formatters](message_formatters.md) (6 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (6 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (5 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (5 shared connections)
- [Room](Room.md) (5 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [test combat messaging service](test_combat_messaging_service.md) (4 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 791 (97%)
- INFERRED: 25 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*