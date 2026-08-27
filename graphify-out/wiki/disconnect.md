# .disconnect

> 24 nodes

## Key Concepts

- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **TestHandleContainerServiceErrorEdgeCases** (8 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **TestHandleContainerServiceError** (8 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_with_request_data()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_mutation_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_no_container_id_or_request_data()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_stack_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_stale_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_token_keyword()** (4 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.test_handle_container_service_error_generic()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_invalid_stack()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_stale_token()** (4 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Handle ContainerServiceError with appropriate status codes. Args: e:…** (1 connections) — `server/api/container_helpers.py`
- **Additional edge case tests for handle_container_service_error.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test handle_container_service_error detects 'mutation' in error message.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test handle_container_service_error uses 'unknown' when no container_id…** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test handle_container_service_error detects 'token' in error message.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test handle_container_service_error detects 'stale' in error message.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test handle_container_service_error detects 'stack' in error message.** (1 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **Test handle_container_service_error function.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test handle_container_service_error returns 412 for stale token.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test handle_container_service_error returns 400 for invalid stack.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test handle_container_service_error returns 500 for generic error.** (1 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Test handle_container_service_error uses request_data.container_id when…** (1 connections) — `server/tests/unit/api/test_container_helpers.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (10 shared connections)
- [ChatService](ChatService.md) (5 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (3 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`

## Audit Trail

- EXTRACTED: 41 (76%)
- INFERRED: 13 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*