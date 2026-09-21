# ExperienceRepository

> 25 nodes

## Key Concepts

- **ExperienceRepository** (26 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **._persist_stat_field_delta()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_player_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **UUID** (4 connections)
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_negative_amount()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_publishes_event()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_gain_experience_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_delta_type()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_name()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_negative_delta()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **Player** (1 connections)
- **fixture** (1 connections)
- **Run update_player_stat_field stored procedure and log success.** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Update a specific numeric field in player stats atomically. Args: player_id:…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Repository for player experience and stats persistence operations. Handles XP…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Award experience points to a player atomically. Args: player: Player to award…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Unit tests for ExperienceRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Relationships

- [DatabaseError](DatabaseError.md) (14 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [ContainerData](ContainerData.md) (1 shared connections)
- [_ExperienceEventBus](_ExperienceEventBus.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 53 (79%)
- INFERRED: 14 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*