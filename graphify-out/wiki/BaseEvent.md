# baseevent

> 149 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **PlayerRespawnService** (35 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
- **PlayerRespawnedEvent** (17 connections) — `server/events/event_types.py`
- **UUID** (16 connections)
- **PlayerDeliriumRespawnedEvent** (12 connections) — `server/events/event_types.py`
- **._prepare_sanitarium_respawn()** (10 connections) — `server/services/player_respawn_service.py`
- **._apply_sanitarium_liability_update()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player()** (9 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_delirium()** (8 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (8 connections) — `server/services/player_respawn_service.py`
- **Player** (8 connections)
- **._prepare_delirium_respawn()** (7 connections) — `server/services/player_respawn_service.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections)
- **fixture** (7 connections)
- **._clear_respawn_combat_state()** (6 connections) — `server/services/player_respawn_service.py`
- **._publish_standard_respawn_event()** (6 connections) — `server/services/player_respawn_service.py`
- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **._can_move_to_limbo()** (5 connections) — `server/services/player_respawn_service.py`
- **.get_respawn_room()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_delirium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- **._log_sanitarium_respawn()** (5 connections) — `server/services/player_respawn_service.py`
- *... and 124 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (26 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (9 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (7 shared connections)
- [server realtime player event handlers](server_realtime_player_event_handlers.md) (6 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (4 shared connections)
- [server events event bus](server_events_event_bus.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server realtime event handler py](server_realtime_event_handler_py.md) (2 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [chatlogger](chatlogger.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 278 (90%)
- INFERRED: 31 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*