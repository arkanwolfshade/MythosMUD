# npc_combat_grace.py

> 21 nodes

## Key Concepts

- **npc_combat_grace.py** (15 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (10 connections) — `server/services/npc_combat_grace.py`
- **test_npc_combat_grace.py** (9 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_attack_blocked_when_target_in_grace_period()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_npc_attack_fail_open_without_app()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_player_attack_blocked_when_in_grace_period()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_player_attack_fail_open_on_invalid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **test_player_attack_fail_open_without_connection_manager()** (2 connections) — `server/tests/unit/services/test_npc_combat_grace.py`
- **UUID** (2 connections)
- **ConnectionManager** (1 connections)
- **Login grace-period checks for NPC combat integration (extracted to keep service…** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor. Uses getattr on…** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on…** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace…** (1 connections) — `server/services/npc_combat_grace.py`
- **Player attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle a player attacking an NPC using auto-progression combat system. Args:…** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Unit tests for npc_combat_grace login grace checks.** (1 connections) — `server/tests/unit/services/test_npc_combat_grace.py`

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*