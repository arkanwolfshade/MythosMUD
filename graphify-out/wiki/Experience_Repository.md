# Experience Repository

> 35 nodes

## Key Concepts

- **ExperienceRepository** (24 connections) — `server/persistence/repositories/experience_repository.py`
- **experience_repository.py** (17 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **_ExperienceEventBus** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **._persist_stat_field_delta()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_xp()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_player_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/persistence/repositories/experience_repository.py`
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
- *... and 10 more nodes in this community*

## Relationships

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (5 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (4 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (3 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (3 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (3 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (2 shared connections)
- [Test Container Persistence Extended Crud](Test_Container_Persistence_Extended_Crud.md) (1 shared connections)
- [Player Effect Repository](Player_Effect_Repository.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 73 (83%)
- INFERRED: 15 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*