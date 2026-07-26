# add_damage_threat

> 6 nodes · cohesion 0.33

## Key Concepts

- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **test_add_damage_threat_accumulates()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_ignores_zero()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **Add threat to an NPC's hate list from damage dealt.      threat += amount * mult** (1 connections) — `server/services/aggro_threat.py`
- **add_damage_threat adds amount * multiplier to source entity.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat does nothing for amount <= 0.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`

## Relationships

- [test_aggro_threat.py](test_aggro_threat.py.md) (7 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (4 shared connections)
- [update_aggro](update_aggro.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [get_or_create_hate_list](get_or_create_hate_list.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*