# server events event types playerdeliriumrespawnedevent

> 332 nodes

## Key Concepts

- **player_event_handlers.py** (42 connections) — `server/realtime/player_event_handlers.py`
- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerEventHandlerUtils** (41 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDPUpdated** (38 connections) — `server/events/event_types.py`
- **RealTimeEventHandler** (36 connections) — `server/realtime/event_handler.py`
- **event_handler.py** (36 connections) — `server/realtime/event_handler.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerEventHandler** (32 connections) — `server/realtime/player_event_handlers.py`
- **PlayerXPAwardEvent** (30 connections) — `server/services/player_combat_service.py`
- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **PlayerDiedEvent** (20 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (17 connections) — `server/events/event_types.py`
- **PlayerDeliriumRespawnedEvent** (16 connections) — `server/events/event_types.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **asyncio** (15 connections)
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerRoomEventHandlerDeps** (12 connections) — `server/realtime/player_event_handlers_room.py`
- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_dispatch_player_dp_updated_payload()** (11 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **message_builders.py** (10 connections) — `server/realtime/message_builders.py`
- *... and 307 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (66 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (47 shared connections)
- [occupantsnap](occupantsnap.md) (28 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (14 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (13 shared connections)
- [moduletype](moduletype.md) (12 shared connections)
- [server container main get container](server_container_main_get_container.md) (11 shared connections)
- [server services combat service types](server_services_combat_service_types.md) (10 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (10 shared connections)
- [server constants spawn defaults](server_constants_spawn_defaults.md) (9 shared connections)
- [server realtime event handler rationale](server_realtime_event_handler_rationale.md) (7 shared connections)
- [server async persistence](server_async_persistence.md) (7 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/services/player_combat_service.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 759 (90%)
- INFERRED: 87 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*