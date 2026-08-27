# 🎯 Async Remediation - Final Report

> 30 nodes

## Key Concepts

- **InstanceManager** (16 connections) — `server/game/instance_manager.py`
- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.destroy_instance()** (2 connections) — `server/game/instance_manager.py`
- **.get_exit_room_id()** (2 connections) — `server/game/instance_manager.py`
- **.get_first_room_id()** (2 connections) — `server/game/instance_manager.py`
- **UUID** (2 connections)
- **Return template rooms matching instance_template_id.** (1 connections) — `server/game/instance_manager.py`
- **Clone template rooms into instance-scoped rooms with remapped exits.** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from room - use room.id if it looks like a full path.** (1 connections) — `server/game/instance_manager.py`
- **Remap exit targets: same-instance rooms use instance IDs, outside exits use…** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from a room ID (may be full path or short form).** (1 connections) — `server/game/instance_manager.py`
- **Return the instance if it exists.** (1 connections) — `server/game/instance_manager.py`
- **Remove the instance from the store.** (1 connections) — `server/game/instance_manager.py`
- **Return the first room ID of the instance (for spawn placement). Order is…** (1 connections) — `server/game/instance_manager.py`
- **Return the fixed exit room ID for this instance (e.g. Main Foyer).** (1 connections) — `server/game/instance_manager.py`
- *... and 5 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [Decisions required](Decisions_required.md) (1 shared connections)
- [applies_to](applies_to.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*