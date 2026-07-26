# .load_container_from_room_json

> 13 nodes · cohesion 0.21

## Key Concepts

- **.load_container_from_room_json()** (8 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (7 connections) — `server/services/environmental_container_loader.py`
- **EnvironmentalContainerLoader** (6 connections) — `server/services/environmental_container_loader.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **Any** (3 connections)
- **ContainerComponent** (2 connections)
- **UUID** (2 connections)
- **Migrate a container from room JSON to PostgreSQL.          Checks if container a** (1 connections) — `server/services/environmental_container_loader.py`
- **Load all environmental containers for a room from PostgreSQL.          Args:** (1 connections) — `server/services/environmental_container_loader.py`
- **Service for loading environmental containers from JSON and PostgreSQL.      Hand** (1 connections) — `server/services/environmental_container_loader.py`
- **Initialize the environmental container loader.          Args:             persis** (1 connections) — `server/services/environmental_container_loader.py`
- **Load a container definition from room JSON.          Args:             room_json** (1 connections) — `server/services/environmental_container_loader.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)

## Source Files

- `server/services/environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 37 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*