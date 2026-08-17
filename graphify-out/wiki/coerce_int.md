# coerce_int

> 95 nodes

## Key Concepts

- **coerce_int()** (51 connections) — `server/utils/int_coercion.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **_stats_int()** (14 connections) — `server/models/player.py`
- **.get_stats()** (13 connections) — `server/models/player.py`
- **test_inventory_command_coercion.py** (13 connections) — `server/tests/unit/commands/test_inventory_command_coercion.py`
- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.set_stats()** (6 connections) — `server/models/player.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **inventory_command_coercion.py** (6 connections) — `server/commands/inventory_command_coercion.py`
- **UUID** (6 connections)
- **.apply_dp_change()** (5 connections) — `server/models/player.py`
- **.apply_dp_decay()** (5 connections) — `server/models/player.py`
- **.restore_to_full_health()** (5 connections) — `server/models/player.py`
- *... and 70 more nodes in this community*

## Relationships

- [websocket_initial_state.py](websocket_initial_state.py.md) (17 shared connections)
- [pytest.md](pytest.md.md) (15 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (10 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (7 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (5 shared connections)
- [test_look_container_helpers.py](test_look_container_helpers.py.md) (5 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (3 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/models/player.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 232 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*