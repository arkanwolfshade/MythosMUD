# logging_file_setup.py

> 86 nodes · cohesion 0.07

## Key Concepts

- **ContainerService** (98 connections) — `server/services/container_service.py`
- **test_container_service.py** (80 connections) — `server/tests/unit/services/test_container_service.py`
- **asyncio** (29 connections)
- **_container_data()** (27 connections) — `server/tests/unit/services/test_container_service.py`
- **_stack()** (21 connections) — `server/tests/unit/services/test_container_service.py`
- **MutationDecision** (17 connections) — `server/services/inventory_mutation_guard.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **_open_from_fixture()** (11 connections) — `server/tests/unit/services/test_container_service.py`
- **_bank_box()** (10 connections) — `server/tests/unit/services/test_container_service.py`
- **_allow_all_mutations()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_capacity_exceeded()** (8 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_item_not_found()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_mutation_guard_suppressed()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_reraises_unexpected_error()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_from_container_success()** (7 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_stops_on_capacity_error()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_player_not_found()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_transfer_to_container_success()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **test_lock_container_updates_state()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_continues_past_other_errors()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_loot_all_success()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_already_open_is_idempotent()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- **test_open_container_player_not_found()** (5 connections) — `server/tests/unit/services/test_container_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (20 shared connections)
- [CombatParticipant](CombatParticipant.md) (13 shared connections)
- [test_look_player.py](test_look_player.py.md) (12 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (9 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (6 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [test_metadata.py](test_metadata.py.md) (3 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_S._Petersen's_Field_Guide_to_Lovecraftian_Horrors__2026-08-12.md) (2 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_container_service.py`

## Audit Trail

- EXTRACTED: 235 (71%)
- INFERRED: 96 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*