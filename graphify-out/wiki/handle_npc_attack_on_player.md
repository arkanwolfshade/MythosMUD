# .handle_npc_attack_on_player

> 8 nodes

## Key Concepts

- **.handle_npc_attack_on_player()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **.is_alive()** (4 connections) — `server/models/combat.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **Check if participant is alive enough to be in combat. For players: alive if DP…** (1 connections) — `server/models/combat.py`
- **NPC attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Aggressive-mob entrypoint; matches NPCCombatIntegration.handle_npc_attack for…** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle an NPC attacking a player (aggro) using the same combat codepath as…** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 11 (85%)
- INFERRED: 2 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*