# Test Npc Combat Integration Service

> 68 nodes

## Key Concepts

- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **asyncio** (25 connections)
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_no_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_skips_when_player_id_unparseable()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_integration_config()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_delegates_to_handle_npc_attack_on_player()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_when_npc_dead()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_without_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcast_failure_non_fatal()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcasts_room_update()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_blocked_during_login_grace()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_room_mismatch_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_process_combat_attack_queue_fail_falls_back_to_process_attack()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_process_combat_attack_queues_when_already_in_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_process_combat_attack_starts_new_combat_when_none()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_dead()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_lookup()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_and_get_npc_instance_provided()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_combat_location()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_combat_location_combat_room_mismatch()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_validate_combat_location_different_rooms()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [Npc Combat Integration Service](Npc_Combat_Integration_Service.md) (32 shared connections)
- [Test Npc Combat Integration Service](Test_Npc_Combat_Integration_Service.md) (10 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (1 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 105 (77%)
- INFERRED: 31 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*