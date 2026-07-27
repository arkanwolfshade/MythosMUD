# NPC Combat Integration

> 59 nodes · cohesion 0.05

## Key Concepts

- **test_npc_combat_integration_service.py** (43 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatIntegrationService** (34 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcast_failure_non_fatal()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **_StubGameConfig** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_clear_npc_combat_memory()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_ends_combat()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_no_combat()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_skips_when_player_id_unparseable()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_integration_config()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_npc_combat_memory()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_original_string_id()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_delegates_to_handle_npc_attack_on_player()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_when_npc_dead()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_without_combat_service()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcasts_room_update()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_blocked_during_login_grace()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_room_mismatch_ends_combat()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_integration_service_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_is_auto_progression_enabled()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_process_combat_attack_queues_when_already_in_combat()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_process_combat_attack_starts_new_combat_when_none()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_setup_combat_uuids_npc_attacker_value_error_falls_back_to_random_uuids()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_lookup()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_provided()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Services Npc Combat]] (15 shared connections)
- [[Combat Command Handler]] (3 shared connections)
- [[Npc Services Combat]] (3 shared connections)
- [[Api Conftest Services]] (1 shared connections)
- [[NPC Combat Player Attack]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 187 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
