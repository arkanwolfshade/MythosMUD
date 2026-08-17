# server persistence repositories experience repository

> 23 nodes

## Key Concepts

- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_player_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_negative_amount()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_publishes_event()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_delta_type()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_name()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_negative_delta()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **Any** (1 connections)
- **Player** (1 connections)
- **fixture** (1 connections)
- **Repository for player experience and stats persistence operations. Handles XP…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Initialize the experience repository. Args: event_bus: Optional EventBus for…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Award experience points to a player atomically. Args: player: Player to award…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Unit tests for ExperienceRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (4 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (3 shared connections)
- [server game mechanics gamemechanicsservice](server_game_mechanics_gamemechanicsservice.md) (2 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (2 shared connections)
- [server persistence container data](server_persistence_container_data.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 47 (73%)
- INFERRED: 17 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*