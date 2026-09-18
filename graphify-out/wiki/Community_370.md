# Community 370

> 46 nodes

## Key Concepts

- **game_tick_death.py** (33 connections) — `server/app/game_tick_death.py`
- **game_tick_protocols.py** (29 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (24 connections) — `server/app/game_tick_protocols.py`
- **_app_container()** (14 connections) — `server/app/game_tick_protocols.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **Protocol** (10 connections)
- **_online_player_ids()** (9 connections) — `server/app/game_tick_protocols.py`
- **AsyncSession** (8 connections)
- **_handle_player_death_threshold()** (7 connections) — `server/app/game_tick_death.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_TickCorruptionFlux** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickRespawnService** (3 connections) — `server/app/game_tick_protocols.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 21 more nodes in this community*

## Relationships

- [Community 542](Community_542.md) (22 shared connections)
- [Community 883](Community_883.md) (15 shared connections)
- [Community 831](Community_831.md) (11 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (10 shared connections)
- [Community 884](Community_884.md) (9 shared connections)
- [Community 385](Community_385.md) (6 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Community 386](Community_386.md) (3 shared connections)
- [Community 275](Community_275.md) (3 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (2 shared connections)
- [Community 87](Community_87.md) (1 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`
- `server/realtime/event_handler.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 163 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*