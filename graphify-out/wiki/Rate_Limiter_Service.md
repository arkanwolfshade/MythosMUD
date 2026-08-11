# Rate Limiter Service

> 16 nodes

## Key Concepts

- **EnvironmentalContainerLoader** (8 connections) — `server/services/environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (7 connections) — `server/services/environmental_container_loader.py`
- **._parse_lock_state()** (5 connections) — `server/services/environmental_container_loader.py`
- **._validate_container_capacity()** (4 connections) — `server/services/environmental_container_loader.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **Any** (3 connections)
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **ContainerComponent** (2 connections)
- **UUID** (2 connections)
- **ContainerLockState** (1 connections)
- **Service for loading environmental containers from JSON and PostgreSQL.      Ha** (1 connections) — `server/services/environmental_container_loader.py`
- **Initialize the environmental container loader.          Args:             per** (1 connections) — `server/services/environmental_container_loader.py`
- **Load environmental container definition from room JSON.** (1 connections) — `server/services/environmental_container_loader.py`
- **migrate_room_container_to_postgresql.** (1 connections) — `server/services/environmental_container_loader.py`
- **Load all environmental containers for a room from PostgreSQL.          Args:** (1 connections) — `server/services/environmental_container_loader.py`

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (5 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (3 shared connections)

## Source Files

- `server/services/environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 47 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*