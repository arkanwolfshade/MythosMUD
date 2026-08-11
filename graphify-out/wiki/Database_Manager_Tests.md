# Database Manager Tests

> 18 nodes

## Key Concepts

- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **UUID** (5 connections)
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (4 connections) — `server/models/container.py`
- **.create_environment()** (4 connections) — `server/models/container.py`
- **.create_equipment()** (4 connections) — `server/models/container.py`
- **.validate_room_id()** (3 connections) — `server/models/container.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **datetime** (3 connections)
- **ValidationInfo** (2 connections)
- **TypedDict** (1 connections)
- **Shared optional fields for container factory methods.** (1 connections) — `server/models/container.py`
- **Validate that room_id is provided for environment and corpse containers.** (1 connections) — `server/models/container.py`
- **Validate that entity_id is provided for equipment containers.** (1 connections) — `server/models/container.py`
- **Check if container has decayed (for corpse containers).** (1 connections) — `server/models/container.py`
- **Factory method to create an environmental container.** (1 connections) — `server/models/container.py`
- **Factory method to create a wearable equipment container.** (1 connections) — `server/models/container.py`
- **Factory method to create a corpse container.** (1 connections) — `server/models/container.py`

## Relationships

- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (6 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (3 shared connections)

## Source Files

- `server/models/container.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*