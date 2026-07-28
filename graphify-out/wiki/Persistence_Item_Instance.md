# Persistence Item Instance

> 6 nodes · cohesion 0.33

## Key Concepts

- **add_damage_threat()** (20 connections) — `server/services/aggro_threat.py`
- **test_add_damage_threat_accumulates()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_add_damage_threat_ignores_zero()** (4 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **Add threat to an NPC's hate list from damage dealt.      threat += amount * mult** (1 connections) — `server/services/aggro_threat.py`
- **add_damage_threat adds amount * multiplier to source entity.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **add_damage_threat does nothing for amount <= 0.** (1 connections) — `server/tests/unit/services/test_aggro_threat.py`

## Relationships

- [Test Value Distribution](Test_Value_Distribution.md) (7 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (4 shared connections)
- [Phantom Hostile Requirements](Phantom_Hostile_Requirements.md) (3 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (2 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Cursor Plans Combat](Cursor_Plans_Combat.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/tests/unit/services/test_aggro_threat.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*