# log_and_raise

> 81 nodes

## Key Concepts

- **log_and_raise()** (196 connections) — `server/utils/error_logging.py`
- **MovementService** (45 connections) — `server/game/movement_service.py`
- **UUID** (18 connections)
- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **._require_container_for_lock_ops()** (9 connections) — `server/services/container_service_lock.py`
- **._validate_movement()** (8 connections) — `server/game/movement_service.py`
- **.lock_container()** (8 connections) — `server/services/container_service_lock.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **._persist_lock_state()** (7 connections) — `server/services/container_service_lock.py`
- **._raise_if_cannot_lock()** (7 connections) — `server/services/container_service_lock.py`
- **._require_player_for_lock_ops()** (7 connections) — `server/services/container_service_lock.py`
- **.unlock_container()** (7 connections) — `server/services/container_service_lock.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._validate_movement_rooms()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- *... and 56 more nodes in this community*

## Relationships

- [container_service_transfer_to.py](container_service_transfer_to.py.md) (16 shared connections)
- [get_session_maker](get_session_maker.md) (13 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (13 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (12 shared connections)
- [test_container_persistence_crud.py](test_container_persistence_crud.py.md) (10 shared connections)
- [pytest.md](pytest.md.md) (8 shared connections)
- [row_to_player](row_to_player.md) (8 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (7 shared connections)
- [QuestInstance](QuestInstance.md) (7 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/services/container_service_lock.py`
- `server/tests/unit/game/test_movement_service.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 356 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*