# NPC Combat Player Attack

> 30 nodes · cohesion 0.07

## Key Concepts

- **test_npc_combat_integration_service_player_attacks.py** (21 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_grace_period_check_fails()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Unit tests for NPC combat integration service - NPC-initiated aggro combat paths** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_player_attack_on_npc_error_handling()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_login_grace_period_blocked()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_with_existing_combat()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_process_combat_attack_queue_failure()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_process_combat_attack_start_new_combat()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_valid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_first_engagement()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_no_definition()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_no_xp_value()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_non_dict_base_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_validate_and_get_npc_instance_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc returns False when NPC not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _setup_combat_uuids_and_mappings handles ValueError.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _setup_combat_uuids_and_mappings with valid UUID.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin when NPC definition is not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin when base_stats is not a dict.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin applies lucidity effect on first engagement.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin defaults to 0 when xp_value not in base_stat** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _process_combat_attack falls back to immediate execution when queuing fails** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- *... and 5 more nodes in this community*

## Relationships

- [[Npc Services Combat]] (3 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[NPC Combat Integration]] (1 shared connections)
- [[Api Conftest Services]] (1 shared connections)
- [[Services Npc Combat]] (1 shared connections)
- [[Services Service Room]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
