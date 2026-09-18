# Async Persistence Layer

> 190 nodes

## Key Concepts

- **AsyncPersistenceLayer** (155 connections) — `server/async_persistence.py`
- **test_async_persistence_delegates.py** (34 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **asyncio** (22 connections)
- **Player** (20 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **UUID** (15 connections)
- **InstanceRoomLookup** (7 connections) — `server/async_persistence_types.py`
- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **ContainerCreateKwargs** (6 connections) — `server/async_persistence_types.py`
- **PlayerEffectOptions** (6 connections) — `server/async_persistence_types.py`
- **validate_player_room_membership()** (6 connections) — `server/game/movement_helpers.py`
- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **.create_container()** (5 connections) — `server/async_persistence.py`
- **check_combat_state()** (5 connections) — `server/game/movement_helpers.py`
- **validate_exit()** (5 connections) — `server/game/movement_helpers.py`
- **test_apply_corruption_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_fear_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_lucidity_loss_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_damage_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_async_heal_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_with_kwargs()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_with_params()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_damage_player_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_gain_occult_knowledge_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_get_player_by_user_id_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- *... and 165 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (36 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (15 shared connections)
- [Community 181](Community_181.md) (5 shared connections)
- [Community 76](Community_76.md) (4 shared connections)
- [Community 31](Community_31.md) (4 shared connections)
- [Community 64](Community_64.md) (4 shared connections)
- [Community 35](Community_35.md) (4 shared connections)
- [Community 333](Community_333.md) (4 shared connections)
- [Community 378](Community_378.md) (4 shared connections)
- [Community 72](Community_72.md) (3 shared connections)
- [Community 82](Community_82.md) (3 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_types.py`
- `server/container/async_persistence_access.py`
- `server/game/movement_helpers.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 360 (88%)
- INFERRED: 51 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*