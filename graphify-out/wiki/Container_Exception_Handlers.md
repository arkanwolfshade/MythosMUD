# Container Exception Handlers

> 134 nodes · cohesion 0.02

## Key Concepts

- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_npc_combat_integration_service_player_attacks.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **test_npc_combat_integration_service_npc_aggro.py** (19 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **integration_service()** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **_StubConfigRoot** (6 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_async_persistence()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_integration_service_init_creates_combat_service_when_none()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_integration_service_init_with_shared_player_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_player_attack_on_npc_grace_period_check_fails()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
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
- **test_handle_npc_death_broadcast_failure_non_fatal()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_death_broadcasts_room_update()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 109 more nodes in this community*

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (41 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 327 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*