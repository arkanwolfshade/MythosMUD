# server api container helpers handle

> 49 nodes

## Key Concepts

- **TransferContainerRequest** (39 connections) — `server/api/container_models.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **TestTransferItems** (11 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleContainerServiceErrorEdgeCases** (8 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceError** (8 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_transfer_items_capacity_error()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_rate_limit()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_stale_token()** (6 connections) — `server/tests/unit/api/test_containers.py`
- **TestRequestModels** (5 connections) — `server/tests/unit/api/test_containers.py`
- **.test_handle_container_service_error_with_request_data()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_transfer_items_not_authenticated()** (5 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_to_container()** (5 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_items_to_player()** (5 connections) — `server/tests/unit/api/test_containers.py`
- **.test_handle_container_service_error_mutation_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_no_container_id_or_request_data()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_stack_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_stale_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_token_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_generic()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_invalid_stack()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_stale_token()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.validate_direction()** (3 connections) — `server/api/container_models.py`
- **.test_transfer_container_request_direction_validation()** (3 connections) — `server/tests/unit/api/test_containers.py`
- **.test_transfer_container_request_quantity_validation()** (3 connections) — `server/tests/unit/api/test_containers.py`
- **field_validator** (1 connections)
- *... and 24 more nodes in this community*

## Relationships

- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (30 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (13 shared connections)
- [server api container events emit](server_api_container_events_emit.md) (10 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (4 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (2 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (2 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 104 (81%)
- INFERRED: 25 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*