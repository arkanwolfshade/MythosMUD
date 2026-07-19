# Container Exception Handlers

> 182 nodes · cohesion 0.03

## Key Concepts

- **LoggedHTTPException** (261 connections) — `server/exceptions.py`
- **ContainerServiceError** (80 connections) — `server/services/container_service.py`
- **ContainerCapacityError** (41 connections) — `server/services/container_service.py`
- **ContainerNotFoundError** (39 connections) — `server/services/container_service.py`
- **ContainerLockedError** (35 connections) — `server/services/container_service.py`
- **ContainerAccessDeniedError** (31 connections) — `server/services/container_service.py`
- **test_containers.py** (29 connections) — `server/tests/unit/api/test_containers.py`
- **test_container_exception_handlers.py** (28 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **handle_transfer_items_exceptions()** (27 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (23 connections) — `server/api/container_exception_handlers.py`
- **handle_open_container_exceptions()** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **TestHelperFunctions** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestOpenContainer** (20 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleTransferItemsExceptions** (18 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **TestCloseContainer** (17 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleLootAllExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestHandleOpenContainerExceptions** (16 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestRequestModels** (16 connections) — `server/tests/unit/api/test_containers.py`
- **TestHandleContainerServiceErrorEdgeCases** (15 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestExceptionChaining** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerContext** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **TestExceptionHandlerLoggerCalls** (14 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 157 more nodes in this community*

## Relationships

- [[Container API Endpoints]] (116 shared connections)
- [[Standardized Error Responses]] (45 shared connections)
- [[Inventory Service Helpers]] (33 shared connections)
- [[NPC Admin API]] (32 shared connections)
- [[API Test Fixtures]] (28 shared connections)
- [[Loot All Endpoint]] (24 shared connections)
- [[NPC Definition Admin API]] (20 shared connections)
- [[Container Loot Helpers]] (18 shared connections)
- [[Monitoring API Endpoints]] (18 shared connections)
- [[Players API Endpoints]] (16 shared connections)
- [[Character Creation API]] (13 shared connections)
- [[NATS Metrics API]] (11 shared connections)

## Source Files

- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/exceptions.py`
- `server/services/container_service.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 969 (74%)
- INFERRED: 340 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
