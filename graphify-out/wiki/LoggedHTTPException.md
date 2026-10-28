# LoggedHTTPException

> 143 nodes · cohesion 0.02

## Key Concepts

- **handle_transfer_items_exceptions()** (29 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (27 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_open_container_exceptions()** (24 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **TestHandleTransferItemsExceptions** (12 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_raise_container_http()** (10 connections) — `server/api/container_exception_handlers.py`
- **TestHandleOpenContainerExceptions** (10 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **Exception** (7 connections)
- **_raise_unexpected_container_error()** (7 connections) — `server/api/container_exception_handlers.py`
- **TestExceptionChaining** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerContext** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerLoggerCalls** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleCloseContainerExceptions** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleTransferItemsExceptionsEdgeCases** (7 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **_raise_for_transfer_service_error()** (6 connections) — `server/api/container_exception_handlers.py`
- **UUID** (5 connections)
- **TestHandleCloseContainerExceptionsEdgeCases** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **.test_handle_open_container_exceptions_open_by_another_player()** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleOpenContainerExceptionsEdgeCases** (5 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestCreateErrorContext** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_close_container_exceptions_chains_exception()** (4 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 118 more nodes in this community*

## Relationships

- [test_command_factories.py](test_command_factories.py.md) (39 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (14 shared connections)
- [test_look_player.py](test_look_player.py.md) (10 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (8 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [generate_arkham_grid.py](generate_arkham_grid.py.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)
- [Room](Room.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (2 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`

## Audit Trail

- EXTRACTED: 272 (83%)
- INFERRED: 56 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*