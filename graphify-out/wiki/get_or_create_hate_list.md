# get_or_create_hate_list

> 10 nodes · cohesion 0.20

## Key Concepts

- **get_or_create_hate_list()** (19 connections) — `server/services/aggro_threat.py`
- **test_apply_stealth_wipe_removes_entity()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_apply_taunt_different_room_no_op()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_apply_taunt_same_room_sets_threat_above_top()** (5 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_get_or_create_hate_list_creates_empty()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **Get or create the hate list for an NPC. Mutates combat.npc_hate_lists.** (1 connections) — `server/services/aggro_threat.py`
- **get_or_create_hate_list creates empty list for NPC and returns same dict.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt in same room sets taunter threat to current_top + margin.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_taunt from different room does nothing and returns False.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **apply_stealth_wipe removes entity from NPC hate list.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`

## Relationships

- [test_aggro_threat.py](test_aggro_threat.py.md) (13 shared connections)
- [update_aggro](update_aggro.md) (6 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [add_damage_threat](add_damage_threat.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*