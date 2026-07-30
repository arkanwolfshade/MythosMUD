# .set player combat service()

> 131 nodes

## Key Concepts

- **test_player_event_handlers_respawn.py** (34 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 106 more nodes in this community*

## Relationships

- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (13 shared connections)
- [. init ()](_init_%28%29.md) (11 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (5 shared connections)
- [main()](main%28%29.md) (4 shared connections)
- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [test websocket handler helpers extended](test_websocket_handler_helpers_extended.md) (2 shared connections)
- [close db()](close_db%28%29.md) (2 shared connections)
- [combat initialization](combat_initialization.md) (1 shared connections)
- [spawn defaults](spawn_defaults.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 423 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*