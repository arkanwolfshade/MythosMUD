# test_command_factories.py

> 123 nodes · cohesion 0.03

## Key Concepts

- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **container_service.py** (38 connections) — `server/services/container_service.py`
- **container_service_session.py** (30 connections) — `server/services/container_service_session.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **container_service_helpers.py** (24 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferFromMixin** (22 connections) — `server/services/container_service_transfer_from.py`
- **ContainerSessionMixin** (21 connections) — `server/services/container_service_session.py`
- **ContainerAccessMixin** (20 connections) — `server/services/container_service_access.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **ContainerCapacityError** (16 connections) — `server/services/container_service_helpers.py`
- **ContainerAccessDeniedError** (15 connections) — `server/services/container_service_helpers.py`
- **filter_container_data()** (14 connections) — `server/services/container_service_helpers.py`
- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **ContainerInteractionEvent** (14 connections) — `server/utils/audit_logger.py`
- **as_object_dict()** (12 connections) — `server/services/container_service_helpers.py`
- **ContainerLockedError** (12 connections) — `server/services/container_service_helpers.py`
- **UUID** (12 connections)
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **get_enum_value()** (11 connections) — `server/services/container_service_helpers.py`
- **._finalize_loot_all()** (11 connections) — `server/services/container_service_transfer_from.py`
- **.open_container()** (10 connections) — `server/services/container_service_session.py`
- **._persist_and_audit_transfer_from_container()** (10 connections) — `server/services/container_service_transfer_from.py`
- **._require_container_for_lock_ops()** (9 connections) — `server/services/container_service_lock.py`
- **InventoryStack** (9 connections)
- *... and 98 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (39 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (30 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (29 shared connections)
- [test_look_player.py](test_look_player.py.md) (19 shared connections)
- [Room](Room.md) (15 shared connections)
- [endpoints.py](endpoints.py.md) (15 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (9 shared connections)
- [AttributeError](AttributeError.md) (9 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Call_of_Cthulhu_Starter_Set__2026-08-12.md) (9 shared connections)
- [CombatParticipant](CombatParticipant.md) (8 shared connections)
- [test_party_service.py](test_party_service.py.md) (3 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (3 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 385 (82%)
- INFERRED: 82 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*