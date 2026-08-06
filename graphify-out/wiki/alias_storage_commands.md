# alias storage commands

> 72 nodes

## Key Concepts

- **ContainerService** (104 connections) — `server/services/container_service.py`
- **test_container_service.py** (60 connections) — `server/tests/unit/services/test_container_service.py`
- **ContainerAccessDeniedError** (31 connections) — `server/services/container_service_helpers.py`
- **_container_data()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_container()** (15 connections) — `server/tests/unit/services/test_container_service.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **_stack()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_corpse_grace_period_blocks_non_owner()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_capacity_exceeded()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **UUID** (4 connections)
- **test_validate_proximity_different_room_raises()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_ownership_equipment_mismatch_raises()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_role_access_denies_player_without_role()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_remove_item_from_container_partial_quantity()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_player_not_found()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_locked_without_key()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_already_open()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_sealed_non_admin()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_validate_corpse_grace_period_expired_allows_other_player()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_non_dict_container_data()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_not_found()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **mock_container_service()** (3 connections) — `server/tests/unit/api/conftest.py`
- *... and 47 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (28 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (26 shared connections)
- [player event handlers](player_event_handlers.md) (23 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (12 shared connections)
- [add used user](add_used_user.md) (11 shared connections)
- [task registry app](task_registry_app.md) (7 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/container_service_helpers.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 342 (80%)
- INFERRED: 83 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*