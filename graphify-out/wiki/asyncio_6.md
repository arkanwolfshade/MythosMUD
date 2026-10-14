# asyncio

> 38 nodes

## Key Concepts

- **asyncio** (29 connections)
- **_container_data()** (27 connections) — `server/tests/unit/services/test_container_service.py`
- **_stack()** (21 connections) — `server/tests/unit/services/test_container_service.py`
- **_open_from_fixture()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **_allow_all_mutations()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_capacity_exceeded()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_item_not_found()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_mutation_guard_suppressed()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_reraises_unexpected_error()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_success()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_stops_on_capacity_error()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_continues_past_other_errors()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_success()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_already_open_is_idempotent()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_rejects_second_player_naming_holder()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_release_player_sessions_frees_containers_for_other_players()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_capacity_exceeded()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_non_dict_container_data()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_close_container_logs_audit_when_data_available()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_audit_failure_still_succeeds()** (4 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [ContainerService](ContainerService.md) (63 shared connections)
- [MutationDecision](MutationDecision.md) (7 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 120 (76%)
- INFERRED: 37 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*