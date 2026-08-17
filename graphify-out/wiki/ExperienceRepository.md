# ExperienceRepository

> 30 nodes

## Key Concepts

- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **.update_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_occult_knowledge()** (4 connections) — `server/game/mechanics.py`
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
- **UUID** (3 connections)
- **Any** (1 connections)
- **Player** (1 connections)
- **fixture** (1 connections)
- **Gain occult knowledge (with lucidity loss).** (1 connections) — `server/game/mechanics.py`
- **Update player experience points atomically. Args: player_id: Player UUID or…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (3 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 59 (78%)
- INFERRED: 17 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*