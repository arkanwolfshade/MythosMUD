# server app game tick death

> 55 nodes

## Key Concepts

- **game_tick_death.py** (34 connections) — `server/app/game_tick_death.py`
- **game_tick_protocols.py** (28 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_tick_online_players()** (9 connections) — `server/app/game_tick_protocols.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (7 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (5 connections)
- **_TickCombatService** (4 connections) — `server/app/game_tick_protocols.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_protocols.py`
- *... and 30 more nodes in this community*

## Relationships

- [server app game tick protocols](server_app_game_tick_protocols.md) (17 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (16 shared connections)
- [server app game tick corpses](server_app_game_tick_corpses.md) (7 shared connections)
- [server models player player apply](server_models_player_player_apply.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server async persistence](server_async_persistence.md) (5 shared connections)
- [server app game tick status](server_app_game_tick_status.md) (4 shared connections)
- [server models combat](server_models_combat.md) (3 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (2 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server constants spawn defaults](server_constants_spawn_defaults.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 170 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*