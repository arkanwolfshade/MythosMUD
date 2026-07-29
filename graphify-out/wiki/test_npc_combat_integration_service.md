# test npc combat integration service

> 30 nodes

## Key Concepts

- **test_npc_combat_integration_service_player_attacks.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_grace_period_check_fails()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_with_existing_combat()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_login_grace_period_blocked()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_error_handling()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_valid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_no_definition()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_non_dict_base_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_first_engagement()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_no_xp_value()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_process_combat_attack_queue_failure()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_process_combat_attack_start_new_combat()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_validate_and_get_npc_instance_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Unit tests for NPC combat integration service - player-initiated combat paths.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc queues action when combat exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc blocks attack when player is in login grace per** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc continues when grace period check fails.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc returns False when NPC not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _setup_combat_uuids_and_mappings handles ValueError.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _setup_combat_uuids_and_mappings with valid UUID.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin when NPC definition is not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin when base_stats is not a dict.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- *... and 5 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [mock async persistence()](mock_async_persistence%28%29.md) (3 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*