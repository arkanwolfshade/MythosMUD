# Container/Loot Events

> 208 nodes

## Key Concepts

- **ContainerComponent** (147 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **error_logging.py** (61 connections) — `server/utils/error_logging.py`
- **ContainerLockState** (44 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **models/container.py** (34 connections) — `server/models/container.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **ContainerAccessMixin** (19 connections) — `server/services/container_service_access.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **test_container_events_loot.py** (17 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **.test_emit_loot_all_event_emission_error()** (8 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_all_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_success()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_zero_items_removed()** (7 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **asyncio** (7 connections)
- **ConnectionManager** (7 connections)
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **.test_emit_loot_all_event_no_connection_manager()** (6 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.test_emit_loot_all_event_no_room_id()** (6 connections) — `server/tests/unit/api/test_container_events_loot.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- *... and 183 more nodes in this community*

## Relationships

- [Container Service Helpers](Container_Service_Helpers.md) (42 shared connections)
- [Test Corpse Lifecycle Service](Test_Corpse_Lifecycle_Service.md) (41 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (33 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (22 shared connections)
- [Test Container Events](Test_Container_Events.md) (21 shared connections)
- [Test Container Service](Test_Container_Service.md) (17 shared connections)
- [Test Error Logging](Test_Error_Logging.md) (11 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (10 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (10 shared connections)
- [Environmental Container Loader](Environmental_Container_Loader.md) (9 shared connections)
- [Test Inventory Service](Test_Inventory_Service.md) (9 shared connections)
- [Test Container Websocket Events](Test_Container_Websocket_Events.md) (8 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/models/container.py`
- `server/services/container_service_access.py`
- `server/services/container_service_lock.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/test_container_events_loot.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 550 (81%)
- INFERRED: 127 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*