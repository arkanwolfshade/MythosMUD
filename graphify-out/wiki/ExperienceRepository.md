# ExperienceRepository

> 27 nodes

## Key Concepts

- **ExperienceRepository** (23 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (9 connections)
- **.award_player_xp()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **._persist_stat_field_delta()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **_row()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_award_player_xp_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_award_player_xp_publishes_event()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_award_player_xp_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **UUID** (4 connections)
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_award_player_xp_negative_delta()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_award_player_xp_player_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_delta_type()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_invalid_name()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_stat_field_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **fixture** (1 connections)
- **Run update_player_stat_field stored procedure and log success.** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Update a specific numeric field in player stats atomically. Args: player_id:…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Repository for player experience and stats persistence operations. Handles XP…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Initialize the experience repository. Args: event_bus: Optional EventBus for…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- **Award XP and recompute level atomically via the award_player_xp stored…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- *... and 2 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [ValueError](ValueError.md) (3 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [session](session.md) (1 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 57 (79%)
- INFERRED: 15 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*