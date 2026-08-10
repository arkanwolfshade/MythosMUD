# Redis to NATS Migration

> 24 nodes

## Key Concepts

- **ContainerRepository** (16 connections) — `server/persistence/repositories/container_repository.py`
- **_container_data_to_dict()** (10 connections) — `server/persistence/repositories/container_repository.py`
- **Any** (7 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **UUID** (5 connections)
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- **datetime** (2 connections)
- **ContainerData** (1 connections)
- **Convert ContainerData to dict with items_json/metadata_json for compatibility.** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Repository for container persistence operations.      Uses async SQLAlchemy sess** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Initialize the container repository.** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Create a new container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get a container by ID (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get all containers in a room (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get all containers owned by an entity (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Update a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get decayed containers (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Delete a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`

## Relationships

- [JSONB Column Parsing](JSONB_Column_Parsing.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (4 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (3 shared connections)

## Source Files

- `server/persistence/repositories/container_repository.py`

## Audit Trail

- EXTRACTED: 98 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*