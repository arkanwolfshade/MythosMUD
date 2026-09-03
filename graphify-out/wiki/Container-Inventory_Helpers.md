# Container/Inventory Helpers

> 378 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **LootAllRequest** (59 connections) — `server/api/container_models.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **test_container_helpers.py** (44 connections) — `server/tests/unit/api/test_container_helpers.py`
- **api/container_helpers.py** (43 connections) — `server/api/container_helpers.py`
- **TransferContainerRequest** (41 connections) — `server/api/container_models.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **test_containers.py** (29 connections) — `server/tests/unit/api/test_containers.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **test_container_helpers_loot.py** (24 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **get_container_and_player_for_loot_all()** (17 connections) — `server/api/container_helpers.py`
- **container_models.py** (17 connections) — `server/api/container_models.py`
- **asyncio** (17 connections)
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestTransferAllItemsFromContainer** (16 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **OpenContainerRequest** (14 connections) — `server/api/container_models.py`
- **TestRegisterLootEndpoints** (14 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **asyncio** (14 connections)
- *... and 353 more nodes in this community*

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (62 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (42 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (33 shared connections)
- [Container Service Helpers](Container_Service_Helpers.md) (25 shared connections)
- [Test Container Events](Test_Container_Events.md) (24 shared connections)
- [Test Container Service](Test_Container_Service.md) (24 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (20 shared connections)
- [Character Creation API](Character_Creation_API.md) (10 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (9 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (6 shared connections)
- [Command Aliases](Command_Aliases.md) (6 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_container_models.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 969 (91%)
- INFERRED: 99 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*