# Room

> 85 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerLockState** (14 connections) — `server/models/container.py`
- **CorpseServiceError** (13 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (10 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.load_container_from_room_json()** (8 connections) — `server/services/environmental_container_loader.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.migrate_room_container_to_postgresql()** (7 connections) — `server/services/environmental_container_loader.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **EnvironmentalContainerLoader** (6 connections) — `server/services/environmental_container_loader.py`
- **UUID** (4 connections)
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **Any** (3 connections)
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_persistence_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_corpse()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 60 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (30 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (13 shared connections)
- [real time](real_time.md) (10 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Lock](Lock.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 262 (93%)
- INFERRED: 20 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*