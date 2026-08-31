# ContainerFactoryOptions

> 32 nodes

## Key Concepts

- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **Any** (5 connections)
- **field_validator** (5 connections)
- **UUID** (5 connections)
- **.create_environment()** (4 connections) — `server/models/container.py`
- **.create_equipment()** (4 connections) — `server/models/container.py`
- **.validate_metadata_no_personal_data()** (4 connections) — `server/models/container.py`
- **.validate_room_id()** (4 connections) — `server/models/container.py`
- **.would_exceed_capacity()** (4 connections) — `server/models/container.py`
- **.has_room_for()** (3 connections) — `server/models/container.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **.to_dict()** (3 connections) — `server/models/container.py`
- **datetime** (3 connections)
- **ValidationInfo** (2 connections)
- **TypedDict** (1 connections)
- **Validate that metadata does not contain personal information (COPPA…** (1 connections) — `server/models/container.py`
- **Validate and convert source_type to enum.** (1 connections) — `server/models/container.py`
- **Validate and convert lock_state to enum.** (1 connections) — `server/models/container.py`
- **Validate that room_id is provided for environment and corpse containers.** (1 connections) — `server/models/container.py`
- **Validate that entity_id is provided for equipment containers.** (1 connections) — `server/models/container.py`
- **Check if container has room for additional items.** (1 connections) — `server/models/container.py`
- *... and 7 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (13 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (3 shared connections)
- [ContainerLockState](ContainerLockState.md) (1 shared connections)

## Source Files

- `server/models/container.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*