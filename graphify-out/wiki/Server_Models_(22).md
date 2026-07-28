# Server Models (22)

> 29 nodes

## Key Concepts

- **Any** (8 connections)
- **.create_corpse()** (7 connections) — `server/models/container.py`
- **.create_environment()** (6 connections) — `server/models/container.py`
- **.create_equipment()** (6 connections) — `server/models/container.py`
- **UUID** (5 connections)
- **.validate_source_type()** (4 connections) — `server/models/container.py`
- **.validate_lock_state()** (4 connections) — `server/models/container.py`
- **.validate_entity_id()** (4 connections) — `server/models/container.py`
- **.would_exceed_capacity()** (4 connections) — `server/models/container.py`
- **.validate_metadata_no_personal_data()** (3 connections) — `server/models/container.py`
- **.validate_room_id()** (3 connections) — `server/models/container.py`
- **.has_room_for()** (3 connections) — `server/models/container.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **datetime** (3 connections)
- **InventoryStack** (3 connections)
- **.to_dict()** (3 connections) — `server/models/container.py`
- **ValidationInfo** (2 connections)
- **Validate that metadata does not contain personal information (COPPA compliance).** (1 connections) — `server/models/container.py`
- **Validate and convert source_type to enum.** (1 connections) — `server/models/container.py`
- **Validate and convert lock_state to enum.** (1 connections) — `server/models/container.py`
- **Validate that room_id is provided for environment and corpse containers.** (1 connections) — `server/models/container.py`
- **Validate that entity_id is provided for equipment containers.** (1 connections) — `server/models/container.py`
- **Check if container has room for additional items.** (1 connections) — `server/models/container.py`
- **Check if adding the given items would exceed container capacity.** (1 connections) — `server/models/container.py`
- **Check if container has decayed (for corpse containers).** (1 connections) — `server/models/container.py`
- *... and 4 more nodes in this community*

## Relationships

- [Server Models (9)](Server_Models_%289%29.md) (12 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (7 shared connections)

## Source Files

- `server/models/container.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*