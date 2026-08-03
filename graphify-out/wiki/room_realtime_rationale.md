# room realtime rationale

> 9 nodes

## Key Concepts

- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **._run_npc_attack_on_player_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **.get_original_string_id()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (3 connections)
- **NPC attack path after login grace check passes.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Aggressive-mob entrypoint; matches NPCCombatIntegration.handle_npc_attack for in** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Handle an NPC attacking a player (aggro) using the same combat codepath as playe** (1 connections) — `server/services/npc_combat_integration_service.py`
- **Get the original string ID from a UUID.** (1 connections) — `server/services/npc_combat_integration_service.py`

## Relationships

- [Spell Validation](Spell_Validation.md) (4 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 22 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*