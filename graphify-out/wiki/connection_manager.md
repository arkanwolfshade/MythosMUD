# .connection_manager

> 15 nodes

## Key Concepts

- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **.award_xp_to_killer()** (3 connections) — `server/services/npc_combat_rewards.py`
- **._is_valid_uuid()** (3 connections) — `server/services/npc_combat_rewards.py`
- **Any** (3 connections)
- **setter** (1 connections)
- **Check connection state before publishing combat ended event.** (1 connections) — `server/services/combat_cleanup_handler.py`
- **Lazily resolve the connection manager from the application container.** (1 connections) — `server/services/combat_messaging/base.py`
- **Return the connection manager, resolving it from the application container if…** (1 connections) — `server/services/combat_messaging/base.py`
- **Explicitly set the connection manager (primarily used in tests).** (1 connections) — `server/services/combat_messaging/base.py`
- **Check if a string is a valid UUID.** (1 connections) — `server/services/npc_combat_rewards.py`
- **Check and log player connection state before operations. Args: player_id: ID of…** (1 connections) — `server/services/npc_combat_rewards.py`
- **Award XP to the killer with defensive error handling. Args: killer_id: ID of…** (1 connections) — `server/services/npc_combat_rewards.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [NPCStartupService](NPCStartupService.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (2 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (1 shared connections)
- [is_npc_attack_on_player_blocked_by_login_grace_period](is_npc_attack_on_player_blocked_by_login_grace_period.md) (1 shared connections)
- [test_npc_combat_handlers.py](test_npc_combat_handlers.py.md) (1 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 22 (67%)
- INFERRED: 11 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*