# auth users rationale

> 58 nodes

## Key Concepts

- **test_npc_combat_integration_service_player_attacks.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_npc_combat_integration_service_npc_aggro.py** (19 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **mock_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_async_persistence()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_happy_path()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_grace_period_blocked()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_dead()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_invalid_location()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_no_combat_service()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_same_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_other_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_skips_already_dead_target()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_valid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_player_attack_on_npc_with_existing_combat()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_login_grace_period_blocked()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_handle_player_attack_on_npc_error_handling()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_setup_combat_uuids_and_mappings_valid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_no_definition()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_non_dict_base_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_store_npc_xp_mapping_first_engagement()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- *... and 33 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (7 shared connections)
- [player event realtime](player_event_realtime.md) (4 shared connections)
- [room sync service](room_sync_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 130 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*