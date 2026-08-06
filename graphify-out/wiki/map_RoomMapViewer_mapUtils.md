# map RoomMapViewer mapUtils

> 75 nodes

## Key Concepts

- **test_game_tick_processing.py** (69 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (16 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (10 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (10 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (9 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_mp_regeneration()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **process_casting_progress()** (6 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (6 connections)
- **_process_passive_lucidity_flux()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_dead_players()** (6 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_processing.py`
- *... and 50 more nodes in this community*

## Relationships

- [command helpers functions](command_helpers_functions.md) (36 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (10 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [game skill service](game_skill_service.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 429 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*