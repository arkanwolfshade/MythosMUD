# Decisions required

> 16 nodes

## Key Concepts

- **test_instance_manager.py** (16 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_create_instance_raises_when_no_templates()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_destroy_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_exit_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_first_room_id()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_none_for_non_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_get_room_by_id_returns_room_when_in_instance()** (2 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Unit tests for InstanceManager. Tests instance creation, destruction, room…** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_exit_room_id returns fixed exit room.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_room_by_id returns None for non-instance room IDs.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_room_by_id returns room when room is in an instance.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test create_instance creates instance with cloned rooms.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test create_instance raises when no template rooms found.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test destroy_instance removes instance from store.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`
- **Test get_first_room_id returns first room of instance.** (1 connections) — `server/tests/unit/game/test_instance_manager.py`

## Relationships

- [applies_to](applies_to.md) (3 shared connections)
- [🎯 Async Remediation - Final Report](🎯_Async_Remediation_-_Final_Report.md) (1 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_instance_manager.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*