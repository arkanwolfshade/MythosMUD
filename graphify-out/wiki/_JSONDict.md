# _JSONDict

> 25 nodes

## Key Concepts

- **_JSONDict** (10 connections)
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **.get_ai_integration_stub()** (4 connections) — `server/models/npc.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- **.check_spawn_conditions()** (4 connections) — `server/models/npc.py`
- **.calculate_xp_reward()** (4 connections) — `server/services/player_combat_service.py`
- **.set_ai_integration_stub()** (3 connections) — `server/models/npc.py`
- **.set_base_stats()** (3 connections) — `server/models/npc.py`
- **.set_behavior_config()** (3 connections) — `server/models/npc.py`
- **.set_spawn_conditions()** (3 connections) — `server/models/npc.py`
- **Get base stats as dictionary.** (1 connections) — `server/models/npc.py`
- **Set base stats from dictionary.** (1 connections) — `server/models/npc.py`
- **Get behavior configuration as dictionary.** (1 connections) — `server/models/npc.py`
- **Set behavior configuration from dictionary.** (1 connections) — `server/models/npc.py`
- **Get AI integration stub configuration as dictionary.** (1 connections) — `server/models/npc.py`
- **Set AI integration stub configuration from dictionary.** (1 connections) — `server/models/npc.py`
- **Get spawn conditions as dictionary.** (1 connections) — `server/models/npc.py`
- **Set spawn conditions from dictionary.** (1 connections) — `server/models/npc.py`
- **Check if current game state meets spawn conditions.** (1 connections) — `server/models/npc.py`
- **Parse JSON object from string; empty dict on failure or non-object root.** (1 connections) — `server/models/npc.py`
- **Try to get XP reward from persistence lifecycle manager. Returns XP amount if…** (1 connections) — `server/services/player_combat_service.py`
- **Calculate XP reward for defeating an NPC. Args: npc_id: ID of the NPC (UUID…** (1 connections) — `server/services/player_combat_service.py`

## Relationships

- [NPCDefinition](NPCDefinition.md) (10 shared connections)
- [._check_dict_condition](_check_dict_condition.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [_NPCCombatIntegrationValidationDeps](_NPCCombatIntegrationValidationDeps.md) (1 shared connections)

## Source Files

- `server/models/npc.py`
- `server/services/player_combat_service.py`

## Audit Trail

- EXTRACTED: 43 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*