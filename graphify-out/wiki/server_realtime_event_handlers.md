# server realtime event handlers

> 278 nodes

## Key Concepts

- **nats_message_handler.py** (36 connections) — `server/realtime/nats_message_handler.py`
- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **Any** (12 connections)
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **asyncio** (11 connections)
- **test_message_filtering_helpers.py** (11 connections) — `server/tests/unit/realtime/test_message_filtering_helpers.py`
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- *... and 253 more nodes in this community*

## Relationships

- [server realtime message formatters](server_realtime_message_formatters.md) (19 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server realtime dead letter queue](server_realtime_dead_letter_queue.md) (12 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (9 shared connections)
- [server realtime circuit breaker](server_realtime_circuit_breaker.md) (8 shared connections)
- [server realtime nats retry handler](server_realtime_nats_retry_handler.md) (7 shared connections)
- [server container main get container](server_container_main_get_container.md) (6 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (3 shared connections)
- [logger](logger.md) (3 shared connections)
- [server models lucidity](server_models_lucidity.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [memorymonitor](memorymonitor.md) (3 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`

## Audit Trail

- EXTRACTED: 506 (93%)
- INFERRED: 37 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*