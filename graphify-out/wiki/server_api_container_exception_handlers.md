# server api container exception handlers

> 127 nodes

## Key Concepts

- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (28 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **TestHandleTransferItemsExceptions** (12 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleOpenContainerExceptions** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_raise_container_http()** (9 connections) — `server/api/container_exception_handlers.py`
- **TestExceptionChaining** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerContext** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerLoggerCalls** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleCloseContainerExceptions** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleTransferItemsExceptionsEdgeCases** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_raise_unexpected_container_error()** (7 connections) — `server/api/container_exception_handlers.py`
- **Exception** (6 connections)
- **TestHandleCloseContainerExceptionsEdgeCases** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleOpenContainerExceptionsEdgeCases** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **UUID** (5 connections)
- **Test handle_transfer_items_exceptions detects mutation token error.** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestTransferItemsExceptionsMutationKeyword** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_loot_all_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_open_container_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 102 more nodes in this community*

## Relationships

- [server services container service](server_services_container_service.md) (38 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (15 shared connections)
- [server api players](server_api_players.md) (14 shared connections)
- [dependsparam](dependsparam.md) (7 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (5 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/tests/unit/api/test_container_exception_handlers.py`

## Audit Trail

- EXTRACTED: 243 (83%)
- INFERRED: 49 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*