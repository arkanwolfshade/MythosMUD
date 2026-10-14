# _WearablePersistence

> 13 nodes

## Key Concepts

- **_WearablePersistence** (9 connections) — `server/services/wearable_container_service.py`
- **Player** (4 connections)
- **.create_container()** (3 connections) — `server/services/wearable_container_service.py`
- **.get_containers_by_entity_id()** (3 connections) — `server/services/wearable_container_service.py`
- **.get_player_by_id()** (3 connections) — `server/services/wearable_container_service.py`
- **.update_container()** (3 connections) — `server/services/wearable_container_service.py`
- **.get_container()** (2 connections) — `server/services/wearable_container_service.py`
- **.save_player()** (2 connections) — `server/services/wearable_container_service.py`
- **Protocol** (1 connections)
- **The async persistence calls this service makes (AsyncPersistenceLayer satisfies…** (1 connections) — `server/services/wearable_container_service.py`
- **Containers owned by an entity.** (1 connections) — `server/services/wearable_container_service.py`
- **Create a container row.** (1 connections) — `server/services/wearable_container_service.py`
- **Replace a container's items; None if the container is gone.** (1 connections) — `server/services/wearable_container_service.py`

## Relationships

- [WearableContainerService](WearableContainerService.md) (6 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*