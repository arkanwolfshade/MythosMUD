# map RoomMapViewer mapUtils

> 31 nodes

## Key Concepts

- **test_game_tick_processing.py** (69 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_loop()** (16 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (11 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (10 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (6 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (6 connections) — `server/app/game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_no_persistence()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_with_session()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_decayed_corpses_on_interval()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_create_corpse_lifecycle_service()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_broadcast_tick_event()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_loop_cancelled_on_sleep()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_passive_lucidity_flux()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_log_cleanup_results_warning_path()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay for mortally wounded players and handle deaths.** (1 connections) — `server/app/game_tick_processing.py`
- **Create and initialize CorpseLifecycleService.      Args:         app: FastAPI ap** (1 connections) — `server/app/game_tick_processing.py`
- *... and 6 more nodes in this community*

## Relationships

- [player persistence repository](player_persistence_repository.md) (25 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (15 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (7 shared connections)
- [tick game processing](tick_game_processing.md) (6 shared connections)
- [realtime message nats](realtime_message_nats.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (3 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (3 shared connections)
- [tracked app task](tracked_app_task.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 176 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*