# PlayerNameExtractor

> 139 nodes

## Key Concepts

- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (28 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
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
- **TestCreateErrorContext** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **UUID** (5 connections)
- **Test handle_transfer_items_exceptions detects mutation token error.** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestTransferItemsExceptionsMutationKeyword** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_close_container_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 114 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (39 shared connections)
- [ChatService](ChatService.md) (15 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (14 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (9 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (8 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [maps.py](maps.py.md) (2 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [✅ Verified Already Implemented](✅_Verified_Already_Implemented.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`

## Audit Trail

- EXTRACTED: 264 (84%)
- INFERRED: 50 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*