# AsyncPersistenceLayer

> 215 nodes

## Key Concepts

- **AsyncPersistenceLayer** (197 connections) — `server/async_persistence.py`
- **test_async_persistence_delegates.py** (36 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **asyncio** (24 connections)
- **Player** (19 connections)
- **UUID** (18 connections)
- **movement_helpers.py** (17 connections) — `server/game/movement_helpers.py`
- **test_wearable_container_persistence.py** (12 connections) — `server/tests/integration/test_wearable_container_persistence.py`
- **validate_exit()** (11 connections) — `server/game/movement_helpers.py`
- **validate_player_room_membership()** (11 connections) — `server/game/movement_helpers.py`
- **check_combat_state()** (10 connections) — `server/game/movement_helpers.py`
- **check_player_posture()** (8 connections) — `server/game/movement_helpers.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **.__init__()** (8 connections) — `server/services/schedule_service.py`
- **_create_player()** (8 connections) — `server/tests/integration/test_wearable_container_persistence.py`
- **test_equip_creates_one_row_reuses_it_and_unequip_reads_it_back()** (8 connections) — `server/tests/integration/test_wearable_container_persistence.py`
- **InstanceRoomLookup** (7 connections) — `server/async_persistence_types.py`
- **._validate_movement_rooms()** (7 connections) — `server/game/movement_service.py`
- **async_persistence_access.py** (7 connections) — `server/container/async_persistence_access.py`
- **extract_player_id()** (6 connections) — `server/game/movement_helpers.py`
- **_ContainerWithPersistence** (5 connections) — `server/container/async_persistence_access.py`
- **.create_container()** (5 connections) — `server/async_persistence.py`
- **._load_from_database()** (5 connections) — `server/services/schedule_service.py`
- **test_apply_corruption_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_fear_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_apply_lucidity_loss_delegates()** (5 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- *... and 190 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (54 shared connections)
- [Player](Player.md) (18 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [test_movement_service.py](test_movement_service.py.md) (11 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (8 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (8 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (7 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (7 shared connections)
- [real_time.py](real_time.py.md) (5 shared connections)
- [MovementService](MovementService.md) (5 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_types.py`
- `server/container/async_persistence_access.py`
- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/schedule_service.py`
- `server/tests/integration/test_wearable_container_persistence.py`
- `server/tests/unit/infrastructure/conftest.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`

## Audit Trail

- EXTRACTED: 453 (86%)
- INFERRED: 71 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*