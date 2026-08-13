# npc_combat_grace.py

> 11 nodes

## Key Concepts

- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_player_attack_blocked_by_login_grace_period()** (6 connections) — `server/services/npc_combat_grace.py`
- **get_app_instance()** (5 connections) — `server/config/__init__.py`
- **UUID** (2 connections)
- **Return the runtime app instance attached during lifespan startup. This provides…** (1 connections) — `server/config/__init__.py`
- **Login grace-period checks for NPC combat integration (extracted to keep service…** (1 connections) — `server/services/npc_combat_grace.py`
- **Resolve connection_manager from the public config app accessor. Uses getattr on…** (1 connections) — `server/services/npc_combat_grace.py`
- **True if the player should not attack (in login grace period). Fail-open on…** (1 connections) — `server/services/npc_combat_grace.py`
- **True if NPC attack on this player should be blocked (player in login grace…** (1 connections) — `server/services/npc_combat_grace.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/services/npc_combat_grace.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*