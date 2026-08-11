# Combat Disconnect Bug

> 18 nodes

## Key Concepts

- **test_npc_combat_integration_service_player_attacks.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_error_handling()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_valid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_no_definition()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_non_dict_base_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_process_combat_attack_start_new_combat()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_validate_and_get_npc_instance_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Unit tests for NPC combat integration service - player-initiated combat paths.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc returns False when NPC not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test handle_player_attack_on_npc handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _setup_combat_uuids_and_mappings handles ValueError.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _setup_combat_uuids_and_mappings with valid UUID.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin when NPC definition is not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test store_npc_xp_mapping_for_mixin when base_stats is not a dict.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _process_combat_attack starts new combat when none exists.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **Test _validate_and_get_npc_instance returns None when NPC not found.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [test_ensure_room_cache_loaded_concurrent_load](test_ensure_room_cache_loaded_concurrent_load.md) (1 shared connections)
- [test_ensure_room_cache_loaded_database_error](test_ensure_room_cache_loaded_database_error.md) (1 shared connections)
- [NATS Docs Review](NATS_Docs_Review.md) (1 shared connections)
- [test_get_valid_exits_empty_room](test_get_valid_exits_empty_room.md) (1 shared connections)
- [test_should_idle_move_true_when_not_in_combat_and_probability_succeeds](test_should_idle_move_true_when_not_in_combat_and_probability_succeeds.md) (1 shared connections)
- [test_should_idle_move_false_when_registered_in_combat](test_should_idle_move_false_when_registered_in_combat.md) (1 shared connections)
- [test_should_idle_move_probability_fails_when_random_above_threshold](test_should_idle_move_probability_fails_when_random_above_threshold.md) (1 shared connections)
- [mock_request](mock_request.md) (1 shared connections)
- [test_should_idle_move_probability_passes_when_random_below_threshold](test_should_idle_move_probability_passes_when_random_below_threshold.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*