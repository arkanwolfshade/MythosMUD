# Server Services (46)

> 37 nodes

## Key Concepts

- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
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
- **Corpse lifecycle service for unified container system.  As documented in the res** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Safely get enum value, handling both enum instances and string values.      When** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Filter out database-specific fields that are not part of the ContainerComponent** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Service for managing corpse container lifecycle.      Handles creation on death,** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Initialize the corpse lifecycle service.          Args:             persistence:** (1 connections) — `server/services/corpse_lifecycle_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [Server Services (19)](Server_Services_%2819%29.md) (12 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (6 shared connections)
- [Server App (3)](Server_App_%283%29.md) (4 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (3 shared connections)
- [Server Api](Server_Api.md) (3 shared connections)
- [Server Admin](Server_Admin.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)
- [Server Models (9)](Server_Models_%289%29.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 137 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*