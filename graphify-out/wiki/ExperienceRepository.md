# ExperienceRepository

> 19 nodes

## Key Concepts

- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **.gain_occult_knowledge()** (4 connections) — `server/game/mechanics.py`
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
- **fixture** (1 connections)
- **Gain occult knowledge (with lucidity loss).** (1 connections) — `server/game/mechanics.py`
- **Repository for player experience and stats persistence operations. Handles XP…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Unit tests for ExperienceRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Relationships

- [DatabaseError](DatabaseError.md) (12 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [.gain_experience](gain_experience.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 43 (72%)
- INFERRED: 17 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*