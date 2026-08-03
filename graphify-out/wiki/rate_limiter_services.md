# rate limiter services

> 35 nodes

## Key Concepts

- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpse()** (10 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **_filter_container_data()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (5 connections)
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (4 connections)
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_get_enum_value_enum()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_enum_value_string()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **corpse_service()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Safely get enum value, handling both enum instances and string values.      When** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Filter out database-specific fields that are not part of the ContainerComponent** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Service for managing corpse container lifecycle.      Handles creation on death,** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Initialize the corpse lifecycle service.          Args:             persistence:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Create a corpse container when a player dies.          Args:             player_** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a player can access a corpse container.          During grace period, o** (1 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 10 more nodes in this community*

## Relationships

- [task registry app](task_registry_app.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (4 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [realtime message nats](realtime_message_nats.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [character creation validate](character_creation_validate.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 117 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*