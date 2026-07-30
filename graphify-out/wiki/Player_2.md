# Player

> 840 nodes

## Key Concepts

- **ConnectionManager** (221 connections) — `server/realtime/connection_manager.py`
- **connection_manager.py** (160 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (79 connections) — `server/realtime/connection_manager_methods.py`
- **NATSRetryHandler** (42 connections) — `server/realtime/nats_retry_handler.py`
- **UUID** (41 connections)
- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **test_connection_helpers_impl.py** (35 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **nats_message_handler.py** (34 connections) — `server/realtime/nats_message_handler.py`
- **test_nats_retry_handler.py** (34 connections) — `server/tests/unit/realtime/test_nats_retry_handler.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **EventHandler** (24 connections) — `server/realtime/event_handlers.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **test_connection_statistics.py** (24 connections) — `server/tests/unit/realtime/test_connection_statistics.py`
- **nats_message_handler_processing.py** (23 connections) — `server/realtime/nats_message_handler_processing.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **UUID** (21 connections)
- **nats_message_handler_base.py** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **connection_cleanup_methods.py** (18 connections) — `server/realtime/connection_cleanup_methods.py`
- **convert_uuids_to_strings()** (18 connections) — `server/realtime/connection_helpers.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- *... and 815 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (80 shared connections)
- [Any](Any.md) (67 shared connections)
- [connection delegates](connection_delegates.md) (32 shared connections)
- [UUID](UUID.md) (24 shared connections)
- [real time](real_time.md) (21 shared connections)
- [connection disconnection](connection_disconnection.md) (19 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (19 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (14 shared connections)
- [. init ()](_init_%28%29.md) (13 shared connections)
- [circuit breaker](circuit_breaker.md) (12 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (11 shared connections)
- [.is required()](is_required%28%29.md) (10 shared connections)

## Source Files

- `server/realtime/connection_cleanup_methods.py`
- `server/realtime/connection_delegates.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/event_handlers.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/realtime/nats_retry_handler.py`
- `server/realtime/payload_optimizer.py`

## Audit Trail

- EXTRACTED: 3232 (97%)
- INFERRED: 108 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*