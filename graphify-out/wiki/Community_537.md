# Community 537

> 32 nodes

## Key Concepts

- **ExperienceRepository** (21 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (9 connections)
- **.award_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **._persist_stat_field_delta()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **_ExperienceEventBus** (5 connections) — `server/persistence/repositories/experience_repository.py`
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
- **.publish()** (2 connections) — `server/persistence/repositories/experience_repository.py`
- **BaseEvent** (1 connections)
- **Protocol** (1 connections)
- **fixture** (1 connections)
- **Run update_player_stat_field stored procedure and log success.** (1 connections) — `server/persistence/repositories/experience_repository.py`
- *... and 7 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (12 shared connections)
- [Community 226](Community_226.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 51](Community_51.md) (1 shared connections)
- [Community 281](Community_281.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 57 (78%)
- INFERRED: 16 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*