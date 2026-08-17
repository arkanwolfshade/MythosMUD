# docs examples logging fastapi integration

> 229 nodes

## Key Concepts

- **container_endpoints_basic.py** (64 connections) — `server/api/container_endpoints_basic.py`
- **test_container_helpers.py** (44 connections) — `server/tests/unit/api/test_container_helpers.py`
- **api/container_helpers.py** (43 connections) — `server/api/container_helpers.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **container_endpoints_loot.py** (32 connections) — `server/api/container_endpoints_loot.py`
- **test_containers.py** (29 connections) — `server/tests/unit/api/test_containers.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **asyncio** (17 connections)
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **container_models.py** (14 connections) — `server/api/container_models.py`
- **OpenContainerRequest** (13 connections) — `server/api/container_models.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **TestOpenContainer** (11 connections) — `server/tests/unit/api/test_containers.py`
- **execute_transfer()** (11 connections) — `server/api/container_helpers.py`
- **Request** (11 connections)
- **CloseContainerRequest** (10 connections) — `server/api/container_models.py`
- **ContainerLootAllResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **TestHelperFunctions** (10 connections) — `server/tests/unit/api/test_containers.py`
- **_build_container_data_from_dict()** (10 connections) — `server/api/container_endpoints_basic.py`
- **apply_rate_limiting_for_close_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- *... and 204 more nodes in this community*

## Relationships

- [server api container endpoints loot](server_api_container_endpoints_loot.md) (41 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (34 shared connections)
- [server api container helpers handle](server_api_container_helpers_handle.md) (30 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (26 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (23 shared connections)
- [server api container exception handlers](server_api_container_exception_handlers.md) (19 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (18 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (15 shared connections)
- [server api container events emit](server_api_container_events_emit.md) (6 shared connections)
- [server api players get player](server_api_players_get_player.md) (5 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (4 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (4 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 632 (93%)
- INFERRED: 45 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*