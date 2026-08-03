# archive 2025 AUDIT

> 4 nodes

## Key Concepts

- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._complete_player_attack_on_npc_after_grace()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **Player attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle a player attacking an NPC using auto-progression combat system.** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [Spell Validation](Spell_Validation.md) (2 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*