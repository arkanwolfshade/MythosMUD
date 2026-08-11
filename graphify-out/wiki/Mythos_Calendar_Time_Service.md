# Mythos Calendar Time Service

> 17 nodes

## Key Concepts

- **_JSONDict** (10 connections)
- **_loads_json_dict()** (7 connections) — `server/models/npc.py`
- **.get_spawn_conditions()** (5 connections) — `server/models/npc.py`
- **.get_behavior_config()** (4 connections) — `server/models/npc.py`
- **.get_ai_integration_stub()** (4 connections) — `server/models/npc.py`
- **.set_base_stats()** (3 connections) — `server/models/npc.py`
- **.set_behavior_config()** (3 connections) — `server/models/npc.py`
- **.set_ai_integration_stub()** (3 connections) — `server/models/npc.py`
- **.set_spawn_conditions()** (3 connections) — `server/models/npc.py`
- **Parse JSON object from string; empty dict on failure or non-object root.** (1 connections) — `server/models/npc.py`
- **Set base stats from dictionary.** (1 connections) — `server/models/npc.py`
- **Get behavior configuration as dictionary.** (1 connections) — `server/models/npc.py`
- **Set behavior configuration from dictionary.** (1 connections) — `server/models/npc.py`
- **Get AI integration stub configuration as dictionary.** (1 connections) — `server/models/npc.py`
- **Set AI integration stub configuration from dictionary.** (1 connections) — `server/models/npc.py`
- **Get spawn conditions as dictionary.** (1 connections) — `server/models/npc.py`
- **Set spawn conditions from dictionary.** (1 connections) — `server/models/npc.py`

## Relationships

- [Command Parser Tests](Command_Parser_Tests.md) (5 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (5 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (2 shared connections)

## Source Files

- `server/models/npc.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*