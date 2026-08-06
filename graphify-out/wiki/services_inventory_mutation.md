# services inventory mutation

> 196 nodes

## Key Concepts

- **LoggedHTTPException** (474 connections) — `server/exceptions.py`
- **ContainerServiceError** (69 connections) — `server/services/container_service_helpers.py`
- **loot_all_items()** (38 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (32 connections) — `server/api/container_exception_handlers.py`
- **ContainerNotFoundError** (31 connections) — `server/services/container_service_helpers.py`
- **handle_open_container_exceptions()** (26 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (26 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_loot_all_exceptions()** (25 connections) — `server/api/container_exception_handlers.py`
- **ContainerCapacityError** (23 connections) — `server/services/container_service_helpers.py`
- **handle_close_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (19 connections) — `server/api/container_exception_handlers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **ContainerLockedError** (18 connections) — `server/services/container_service_helpers.py`
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **TestHandleTransferItemsExceptions** (13 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleContainerServiceErrorEdgeCases** (13 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceError** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestHandleOpenContainerExceptions** (11 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleLootAllExceptions** (11 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **validate_user_for_loot_all()** (10 connections) — `server/api/container_helpers.py`
- **TestValidateUserForLootAll** (10 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestHandleCloseContainerExceptions** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleTransferItemsExceptionsEdgeCases** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerLoggerCalls** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerContext** (9 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 171 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (89 shared connections)
- [player requests schemas](player_requests_schemas.md) (54 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (53 shared connections)
- [player event handlers](player_event_handlers.md) (45 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (43 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (36 shared connections)
- [Player Stats](Player_Stats.md) (30 shared connections)
- [alias storage commands](alias_storage_commands.md) (26 shared connections)
- [NPC Combat](NPC_Combat.md) (22 shared connections)
- [models player related](models_player_related.md) (20 shared connections)
- [Loot Generation](Loot_Generation.md) (19 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (16 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/exceptions.py`
- `server/services/container_service_helpers.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 863 (61%)
- INFERRED: 552 (39%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*