# Player Effect Repository

> 69 nodes

## Key Concepts

- **player_effect_repository.py** (20 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_player_effect_repository.py** (18 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **PlayerEffectRepository** (16 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffect** (14 connections) — `server/models/player_effect.py`
- **.get_active_effects_for_player()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **asyncio** (8 connections)
- **UUID** (7 connections)
- **AddEffectInput** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.__init__()** (6 connections) — `server/async_persistence.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.add_effect()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Any** (6 connections)
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.delete_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.expire_effects_for_tick()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effects_expiring_this_tick()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 44 more nodes in this community*

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (7 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (6 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (3 shared connections)
- [Async Persistence](Async_Persistence.md) (2 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (2 shared connections)
- [Admin Setstat Support](Admin_Setstat_Support.md) (2 shared connections)
- [Async Persistence Room Loader](Async_Persistence_Room_Loader.md) (1 shared connections)
- [Experience Repository](Experience_Repository.md) (1 shared connections)
- [Database](Database.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/models/player_effect.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 135 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*