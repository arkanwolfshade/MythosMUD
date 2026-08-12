# E2E Suite Overview

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

- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (1 shared connections)
- [Services Combat Initialization](Services_Combat_Initialization.md) (1 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (1 shared connections)
- [Cursor Plans First](Cursor_Plans_First.md) (1 shared connections)
- [Cursor Plans Eliminate](Cursor_Plans_Eliminate.md) (1 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (1 shared connections)
- [Persistence Item Repositories](Persistence_Item_Repositories.md) (1 shared connections)
- [E 2 E Scenarios Lucidity](E_2_E_Scenarios_Lucidity.md) (1 shared connections)
- [Lucidity Utc Now](Lucidity_Utc_Now.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*