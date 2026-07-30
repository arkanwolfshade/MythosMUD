# datetime

> 30 nodes

## Key Concepts

- **ContainerLockState** (14 connections) — `server/models/container.py`
- **Any** (8 connections)
- **.create_corpse()** (7 connections) — `server/models/container.py`
- **.create_environment()** (6 connections) — `server/models/container.py`
- **.create_equipment()** (6 connections) — `server/models/container.py`
- **UUID** (5 connections)
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
- **StrEnum** (2 connections)
- **ValidationInfo** (2 connections)
- **Lock state for container instances.** (1 connections) — `server/models/container.py`
- **Validate that metadata does not contain personal information (COPPA compliance).** (1 connections) — `server/models/container.py`
- **Validate and convert lock_state to enum.** (1 connections) — `server/models/container.py`
- **Validate that room_id is provided for environment and corpse containers.** (1 connections) — `server/models/container.py`
- **Validate that entity_id is provided for equipment containers.** (1 connections) — `server/models/container.py`
- **Check if container has room for additional items.** (1 connections) — `server/models/container.py`
- **Check if adding the given items would exceed container capacity.** (1 connections) — `server/models/container.py`
- *... and 5 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (14 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [datetime](datetime.md) (1 shared connections)

## Source Files

- `server/models/container.py`

## Audit Trail

- EXTRACTED: 95 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*