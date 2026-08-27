# TaskRegistry

> 29 nodes

## Key Concepts

- **server/persistence/__init__.py** (32 connections) — `server/persistence/__init__.py`
- **item_instance_persistence.py** (18 connections) — `server/persistence/item_instance_persistence.py`
- **test_item_instance_persistence.py** (17 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **ensure_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **create_item_instance()** (11 connections) — `server/persistence/item_instance_persistence.py`
- **get_item_instance()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (7 connections)
- **_execute_item_instance_upsert()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **_handle_item_instance_db_error()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **_item_instance_row_values()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **test_create_item_instance_db_error()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_create_item_instance_missing_id()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_create_item_instance_success()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_ensure_item_instance_calls_create()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_get_item_instance_found()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_get_item_instance_not_found()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_item_instance_exists_false()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_item_instance_exists_true()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **Exception** (1 connections)
- **Persistence package for MythosMUD. This package contains persistence utilities…** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: PersistenceLayer and get_persistence removed - all code now uses…** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from…** (1 connections) — `server/persistence/__init__.py`
- **Item instance persistence operations. As documented in the restricted archives,…** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Create a new item instance in the database.** (1 connections) — `server/persistence/item_instance_persistence.py`
- *... and 4 more nodes in this community*

## Relationships

- [map_minimap.py](map_minimap.py.md) (8 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (7 shared connections)
- [Game Subsystem Design Documents Overview](Game_Subsystem_Design_Documents_Overview.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (6 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (6 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (1 shared connections)
- [test_quality_fragmentation_guard.py](test_quality_fragmentation_guard.py.md) (1 shared connections)
- [test_realtime_bundle_nats.py](test_realtime_bundle_nats.py.md) (1 shared connections)
- [NPCCacheService](NPCCacheService.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_item_instance_persistence.py`

## Audit Trail

- EXTRACTED: 97 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*