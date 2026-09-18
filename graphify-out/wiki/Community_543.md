# Community 543

> 31 nodes

## Key Concepts

- **ExperienceRepository** (26 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **asyncio** (10 connections)
- **._persist_stat_field_delta()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
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
- **Initialize the async persistence layer. This facade delegates to focused async…** (1 connections) — `server/async_persistence.py`
- **Update player experience points atomically. Args: player_id: Player UUID or…** (1 connections) — `server/persistence/repositories/experience_repository.py`
- *... and 6 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (14 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)
- [Community 219](Community_219.md) (2 shared connections)
- [Event Bus](Event_Bus.md) (2 shared connections)
- [Invite Codes & Session Maker (E2E)](Invite_Codes_&_Session_Maker_E2E.md) (2 shared connections)
- [Community 630](Community_630.md) (1 shared connections)
- [Community 863](Community_863.md) (1 shared connections)
- [Community 302](Community_302.md) (1 shared connections)
- [Community 1136](Community_1136.md) (1 shared connections)
- [Community 378](Community_378.md) (1 shared connections)
- [Community 333](Community_333.md) (1 shared connections)
- [Community 226](Community_226.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 71 (84%)
- INFERRED: 14 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*