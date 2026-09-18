# Community 31

> 163 nodes

## Key Concepts

- **container_endpoints_basic.py** (62 connections) — `server/api/container_endpoints_basic.py`
- **api/container_helpers.py** (42 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (42 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TransferContainerRequest** (41 connections) — `server/api/container_models.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **get_async_persistence()** (12 connections) — `server/dependencies.py`
- **get_current_user()** (11 connections) — `docs/examples/logging/fastapi_integration.py`
- **execute_transfer()** (11 connections) — `server/api/container_helpers.py`
- **Request** (11 connections)
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **_build_container_data_from_dict()** (10 connections) — `server/api/container_endpoints_basic.py`
- **apply_rate_limiting_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- **ContainerOpenResponse** (9 connections) — `server/schemas/containers/container.py`
- **ContainerData** (9 connections) — `server/schemas/containers/container_data.py`
- *... and 138 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (74 shared connections)
- [Community 144](Community_144.md) (28 shared connections)
- [Community 64](Community_64.md) (24 shared connections)
- [Community 43](Community_43.md) (14 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (12 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (10 shared connections)
- [Community 691](Community_691.md) (8 shared connections)
- [Community 67](Community_67.md) (8 shared connections)
- [FastAPI Dependency Providers](FastAPI_Dependency_Providers.md) (7 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (5 shared connections)
- [Community 111](Community_111.md) (5 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (4 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/dependencies.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_models.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 481 (94%)
- INFERRED: 28 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*