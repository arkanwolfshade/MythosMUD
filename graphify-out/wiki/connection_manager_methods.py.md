# connection_manager_methods.py

> 178 nodes · cohesion 0.02

## Key Concepts

- **ContainerComponent** (169 connections) — `server/models/container.py`
- **ContainerSourceType** (95 connections) — `server/models/container.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (41 connections) — `server/tests/unit/models/test_container.py`
- **models/container.py** (33 connections) — `server/models/container.py`
- **corpse_lifecycle_service.py** (30 connections) — `server/services/corpse_lifecycle_service.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **test_container_endpoints_loot.py** (12 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **test_container_endpoints_loot_register.py** (10 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **._validate_container_access()** (8 connections) — `server/services/container_service_access.py`
- **_real_container_with_datetime()** (7 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **.validate_entity_id()** (6 connections) — `server/models/container.py`
- **.validate_lock_state()** (6 connections) — `server/models/container.py`
- **.validate_source_type()** (6 connections) — `server/models/container.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **._validate_ownership()** (6 connections) — `server/services/container_service_access.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_metadata_no_personal_data()** (5 connections) — `server/models/container.py`
- **.validate_room_id()** (5 connections) — `server/models/container.py`
- **Any** (5 connections)
- **field_validator** (5 connections)
- **UUID** (5 connections)
- **._raise_corpse_grace_denied()** (5 connections) — `server/services/container_service_access.py`
- **._validate_bank_ownership()** (5 connections) — `server/services/container_service_access.py`
- **._validate_corpse_grace_period()** (5 connections) — `server/services/container_service_access.py`
- *... and 153 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (59 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (30 shared connections)
- [CombatParticipant](CombatParticipant.md) (29 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (27 shared connections)
- [RoomNodeData](RoomNodeData.md) (24 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (20 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (10 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (7 shared connections)
- [endpoints.py](endpoints.py.md) (6 shared connections)
- [AttributeError](AttributeError.md) (6 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Call_of_Cthulhu_Starter_Set__2026-08-12.md) (5 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service_access.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 429 (74%)
- INFERRED: 148 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*