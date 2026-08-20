# .handle_npc_attack_on_player

> 6 nodes

## Key Concepts

- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **NPC attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Aggressive-mob entrypoint; matches NPCCombatIntegration.handle_npc_attack for…** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle an NPC attacking a player (aggro) using the same combat codepath as…** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*