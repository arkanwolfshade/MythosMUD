# npc_combat_grace.py

> 19 nodes

## Key Concepts

- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (6 connections) — `server/services/npc_combat_grace.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (2 connections)
- **Return the runtime app instance attached during lifespan startup. This provides…** (1 connections) — `server/config/__init__.py`
- **Check if participant is alive enough to be in combat. For players: alive if DP…** (1 connections) — `server/models/combat.py`
- **Login grace-period checks for NPC combat integration (extracted to keep service…** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor. Uses getattr on…** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on…** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace…** (1 connections) — `server/services/npc_combat_grace.py`
- **NPC attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Aggressive-mob entrypoint; matches NPCCombatIntegration.handle_npc_attack for…** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle an NPC attacking a player (aggro) using the same combat codepath as…** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/models/combat.py`
- `server/services/npc_combat_grace.py`
- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 61 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*