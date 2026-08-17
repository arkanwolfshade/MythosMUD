# playerdpupdated

> 41 nodes

## Key Concepts

- **game_tick_death.py** (28 connections) — `server/app/game_tick_death.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **game_tick_protocols.py** (19 connections) — `server/app/game_tick_protocols.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_player()** (11 connections) — `server/app/game_tick_death.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (9 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_handle_player_death_threshold()** (7 connections) — `server/app/game_tick_death.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (7 connections)
- **_TickMpRegen** (6 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (6 connections) — `server/app/game_tick_death.py`
- **_regenerate_mp_for_players()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **.handle_player_dp_updated()** (3 connections) — `server/realtime/player_event_handlers.py`
- **Player** (3 connections)
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_protocols.py`
- **PlayerDPUpdated** (2 connections)
- **FastAPI** (2 connections)
- **UUID** (2 connections)
- **FastAPI** (2 connections)
- *... and 16 more nodes in this community*

## Relationships

- [server app game tick processing](server_app_game_tick_processing.md) (23 shared connections)
- [server app game tick protocols](server_app_game_tick_protocols.md) (10 shared connections)
- [corpselifecycleservice](corpselifecycleservice.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server app game tick status](server_app_game_tick_status.md) (6 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [chatlogger](chatlogger.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)
- [server commands inventory command coercion](server_commands_inventory_command_coercion.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`
- `server/realtime/player_event_handlers.py`

## Audit Trail

- EXTRACTED: 128 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*