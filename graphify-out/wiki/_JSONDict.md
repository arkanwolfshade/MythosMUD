# _JSONDict

> 17 nodes · cohesion 0.15

## Key Concepts

- **_JSONDict** (10 connections)
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.get_base_stats()** (6 connections) — `server/models/npc.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **.get_ai_integration_stub()** (4 connections) — `server/models/npc.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- **.set_ai_integration_stub()** (3 connections) — `server/models/npc.py`
- **.set_base_stats()** (3 connections) — `server/models/npc.py`
- **.set_behavior_config()** (3 connections) — `server/models/npc.py`
- **Get base stats as dictionary.** (1 connections) — `server/models/npc.py`
- **Set base stats from dictionary.** (1 connections) — `server/models/npc.py`
- **Get behavior configuration as dictionary.** (1 connections) — `server/models/npc.py`
- **Set behavior configuration from dictionary.** (1 connections) — `server/models/npc.py`
- **Get AI integration stub configuration as dictionary.** (1 connections) — `server/models/npc.py`
- **Set AI integration stub configuration from dictionary.** (1 connections) — `server/models/npc.py`
- **Get spawn conditions as dictionary.** (1 connections) — `server/models/npc.py`
- **Parse JSON object from string; empty dict on failure or non-object root.** (1 connections) — `server/models/npc.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (4 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/models/npc.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*