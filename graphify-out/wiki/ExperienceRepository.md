# ExperienceRepository

> 26 nodes

## Key Concepts

- **ExperienceRepository** (25 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
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
- **.publish()** (2 connections) — `server/persistence/repositories/experience_repository.py`
- **Player** (1 connections)
- **Protocol** (1 connections)
- **fixture** (1 connections)
- **Minimal event bus surface for XP award publishing.** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Repository for player experience and stats persistence operations. Handles XP…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Initialize the experience repository. Args: event_bus: Optional EventBus for…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Award experience points to a player atomically. Args: player: Player to award…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- *... and 1 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [PlayerXPAwardEvent](PlayerXPAwardEvent.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 52 (78%)
- INFERRED: 15 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*