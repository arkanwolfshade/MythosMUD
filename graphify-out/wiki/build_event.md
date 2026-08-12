# build_event

> 363 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **NATSError** (60 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **NATSSubscribeError** (25 connections) — `server/services/nats_exceptions.py`
- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **MessageFilteringHelper** (23 connections) — `server/realtime/message_filtering.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **asyncio** (18 connections)
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **format_message_content()** (17 connections) — `server/realtime/message_formatters.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- *... and 338 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (40 shared connections)
- [NATSService](NATSService.md) (27 shared connections)
- [CombatService](CombatService.md) (16 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (11 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (10 shared connections)
- [send_game_event](send_game_event.md) (8 shared connections)
- [connection_manager.py](connection_manager.py.md) (8 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (7 shared connections)
- [player_combat_service.py](player_combat_service.py.md) (7 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (6 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/player_event_handlers_state.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`
- `server/tests/unit/realtime/test_message_filtering_helpers.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 1367 (95%)
- INFERRED: 76 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*