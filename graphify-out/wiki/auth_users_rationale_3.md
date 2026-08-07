# auth users rationale

> 30 nodes

## Key Concepts

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
- **Create mock combat service.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **Create mock connection manager.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **Create mock async persistence layer.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **Unit tests for NPC combat integration service - NPC-initiated aggro combat paths** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player starts combat and processes attack on happy pat** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player blocks attack when player is in login grace per** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC instance cannot be found** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC is dead.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when combat location is invalid.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when combat service is missing.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- *... and 5 more nodes in this community*

## Relationships

- [grace period login](grace_period_login.md) (6 shared connections)
- [room sync service](room_sync_service.md) (3 shared connections)
- [models player rationale](models_player_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*