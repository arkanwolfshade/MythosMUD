# map RoomMapViewer mapUtils

> 57 nodes

## Key Concepts

- **test_game_tick_processing.py** (69 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (16 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (11 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (10 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (9 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (9 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **process_casting_progress()** (6 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_invalid_id()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_success()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 32 more nodes in this community*

## Relationships

- [tick game processing](tick_game_processing.md) (24 shared connections)
- [realtime message nats](realtime_message_nats.md) (14 shared connections)
- [player persistence repository](player_persistence_repository.md) (14 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (11 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [tracked app task](tracked_app_task.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [combat npc services](combat_npc_services.md) (3 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 349 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*