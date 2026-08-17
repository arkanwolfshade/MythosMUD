# server realtime event handlers

> 167 nodes

## Key Concepts

- **nats_message_handler.py** (35 connections) — `server/realtime/nats_message_handler.py`
- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **NATSMessageHandler** (21 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **asyncio** (11 connections)
- **test_message_filtering_helpers.py** (11 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **_publish_npc_died_to_event_bus()** (6 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (6 connections) — `server/realtime/event_handlers.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- *... and 142 more nodes in this community*

## Relationships

- [server realtime message formatters](server_realtime_message_formatters.md) (22 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (16 shared connections)
- [server realtime dead letter queue](server_realtime_dead_letter_queue.md) (9 shared connections)
- [server realtime circuit breaker](server_realtime_circuit_breaker.md) (8 shared connections)
- [playercombatservice](playercombatservice.md) (7 shared connections)
- [server realtime nats retry handler](server_realtime_nats_retry_handler.md) (7 shared connections)
- [server realtime nats message handler](server_realtime_nats_message_handler.md) (7 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (3 shared connections)
- [queuelistener](queuelistener.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server events event bus](server_events_event_bus.md) (3 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 320 (89%)
- INFERRED: 40 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*