# uuid npc combat

> 22 nodes

## Key Concepts

- **test_instance_manager.py** (15 connections) — `server/tests/unit/game/test_instance_manager.py`
- **instance_manager()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **tutorial_room()** (3 connections) — `server/tests/unit/game/test_instance_manager.py`
- **room_cache()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_raises_when_no_templates()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_destroy_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_first_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_exit_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_none_for_non_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_room_when_in_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Unit tests for InstanceManager.  Tests instance creation, destruction, room clon** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Create tutorial bedroom template room.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Room cache with tutorial template.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Create InstanceManager with tutorial template in cache.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test create_instance creates instance with cloned rooms.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test create_instance raises when no template rooms found.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test destroy_instance removes instance from store.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_first_room_id returns first room of instance.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_exit_room_id returns fixed exit room.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_room_by_id returns None for non-instance room IDs.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_room_by_id returns room when room is in an instance.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [player presence tracker](player_presence_tracker.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*