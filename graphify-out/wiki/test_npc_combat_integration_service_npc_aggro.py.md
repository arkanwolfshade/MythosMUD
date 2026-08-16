# test_npc_combat_integration_service_npc_aggro.py

> 25 nodes

## Key Concepts

- **test_npc_combat_integration_service_npc_aggro.py** (20 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **asyncio** (9 connections)
- **test_handle_npc_attack_on_player_existing_combat_with_other_npc()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_existing_combat_with_same_npc()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_grace_period_blocked()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_happy_path()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_invalid_location()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_no_combat_service()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_dead()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_npc_not_found()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_handle_npc_attack_on_player_skips_already_dead_target()** (3 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_valid()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **test_setup_combat_uuids_npc_attacker_value_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Unit tests for NPC combat integration service - NPC-initiated aggro combat…** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC instance cannot be…** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when NPC is dead.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when combat location is invalid.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when combat service is missing.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns True when combat already exists with…** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player returns False when player is in combat with…** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **ValueError from combat path when player is dead must not log as error.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test _setup_combat_uuids_npc_attacker with valid UUID mapping.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test _setup_combat_uuids_npc_attacker falls back to random UUIDs on ValueError.** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player starts combat and processes attack on happy…** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **Test handle_npc_attack_on_player blocks attack when player is in login grace…** (1 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [mock_async_persistence](mock_async_persistence.md) (3 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`

## Audit Trail

- EXTRACTED: 36 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*