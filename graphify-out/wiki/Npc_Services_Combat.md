# Npc Services Combat

> 26 nodes · cohesion 0.08

## Key Concepts

- **test_npc_combat_integration_service_npc_aggro.py** (18 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **mock_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **Test handle_npc_attack_on_player returns False when NPC is dead.** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_other_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_same_npc()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_grace_period_blocked()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_happy_path()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_invalid_location()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_no_combat_service()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_dead()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_not_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_skips_already_dead_target()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_valid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC instance cannot be found** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when combat service is missing.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns True when combat already exists with sa** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when player is in combat with dif** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **ValueError from combat path when player is dead must not log as error.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test _setup_combat_uuids_npc_attacker with valid UUID mapping.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test _setup_combat_uuids_npc_attacker falls back to random UUIDs on ValueError.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player starts combat and processes attack on happy pat** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player blocks attack when player is in login grace per** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Create mock combat service.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [[NPC Combat Integration]] (3 shared connections)
- [[NPC Combat Player Attack]] (3 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[Api Conftest Services]] (1 shared connections)
- [[Services Npc Combat]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
