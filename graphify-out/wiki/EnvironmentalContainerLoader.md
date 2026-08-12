# EnvironmentalContainerLoader

> 16 nodes

## Key Concepts

- **EnvironmentalContainerLoader** (8 connections) — `server/services/environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **._parse_lock_state()** (4 connections) — `server/services/environmental_container_loader.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **._validate_container_capacity()** (3 connections) — `server/services/environmental_container_loader.py`
- **Any** (3 connections)
- **ContainerComponent** (2 connections)
- **UUID** (2 connections)
- **ContainerLockState** (1 connections)
- **migrate_room_container_to_postgresql.** (1 connections) — `server/services/environmental_container_loader.py`
- **Load all environmental containers for a room from PostgreSQL. Args: room_id:…** (1 connections) — `server/services/environmental_container_loader.py`
- **Service for loading environmental containers from JSON and PostgreSQL. Handles…** (1 connections) — `server/services/environmental_container_loader.py`
- **Initialize the environmental container loader. Args: persistence: Persistence…** (1 connections) — `server/services/environmental_container_loader.py`
- **Load environmental container definition from room JSON.** (1 connections) — `server/services/environmental_container_loader.py`

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)

## Source Files

- `server/services/environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*