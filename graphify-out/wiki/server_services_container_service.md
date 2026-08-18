# server services container service

> 128 nodes

## Key Concepts

- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **container_service.py** (33 connections) — `server/services/container_service.py`
- **container_service_transfer_to.py** (33 connections) — `server/services/container_service_transfer_to.py`
- **container_service_session.py** (28 connections) — `server/services/container_service_session.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **container_service_transfer_from.py** (26 connections) — `server/services/container_service_transfer_from.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **ContainerAccessMixin** (19 connections) — `server/services/container_service_access.py`
- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **container_service_access.py** (17 connections) — `server/services/container_service_access.py`
- **audit_logger.py** (16 connections) — `server/utils/audit_logger.py`
- **ContainerCapacityError** (15 connections) — `server/services/container_service_helpers.py`
- **ContainerAccessDeniedError** (14 connections) — `server/services/container_service_helpers.py`
- **filter_container_data()** (14 connections) — `server/services/container_service_helpers.py`
- **ContainerLockedError** (12 connections) — `server/services/container_service_helpers.py`
- **as_object_dict()** (12 connections) — `server/services/container_service_helpers.py`
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **get_enum_value()** (11 connections) — `server/services/container_service_helpers.py`
- **._finalize_loot_all()** (10 connections) — `server/services/container_service_transfer_from.py`
- **._require_container_component()** (10 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (10 connections)
- *... and 103 more nodes in this community*

## Relationships

- [server api container exception handlers](server_api_container_exception_handlers.md) (38 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (29 shared connections)
- [server api container helpers get](server_api_container_helpers_get.md) (22 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (19 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server async persistence](server_async_persistence.md) (12 shared connections)
- [server services container service lock](server_services_container_service_lock.md) (10 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (9 shared connections)
- [server models container containercomponent](server_models_container_containercomponent.md) (7 shared connections)
- [server services inventory mutation guard](server_services_inventory_mutation_guard.md) (5 shared connections)
- [server api container events](server_api_container_events.md) (5 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (4 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 418 (83%)
- INFERRED: 84 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*