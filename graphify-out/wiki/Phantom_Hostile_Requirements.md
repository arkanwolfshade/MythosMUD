# Phantom Hostile Requirements

> 20 nodes · cohesion 0.20

## Key Concepts

- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- **test_aggro_flow.py** (14 connections) — `server/tests/integration/test_aggro_flow.py`
- **apply_taunt()** (12 connections) — `server/services/aggro_threat.py`
- **_make_participant()** (9 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_combat()** (8 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_healer_overpull_switches_target()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_nightgaunt_like_damage_and_heal_threat()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_passive_mob_no_damage_threat_taunt_switches()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_stealth_wipe_switches_to_next()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_taunt_from_next_room_no_effect()** (7 connections) — `server/tests/integration/test_aggro_flow.py`
- **test_aggro_tank_swap_taunt_sequence()** (6 connections) — `server/tests/integration/test_aggro_flow.py`
- **Set taunter's threat to current top + margin so they become top. Room-local only** (1 connections) — `server/services/aggro_threat.py`
- **Resolve current target for an NPC from hate list and stability rule.      - Cand** (1 connections) — `server/services/aggro_threat.py`
- **Integration tests for aggro/threat flow (ADR-016).  Scenarios: healer overpull,** (1 connections) — `server/tests/integration/test_aggro_flow.py`
- **Player in combat enters stealth; that player removed from NPC hate list; mob swi** (1 connections) — `server/tests/integration/test_aggro_flow.py`
- **passive_mob: attack adds no threat; taunt adds threat and UpdateAggro switches t** (1 connections) — `server/tests/integration/test_aggro_flow.py`
- **Nightgaunt-style aggressive mob: scaled damage/heal threat and UpdateAggro targe** (1 connections) — `server/tests/integration/test_aggro_flow.py`
- **Tank has threat; healer does one big heal; after UpdateAggro mob switches to hea** (1 connections) — `server/tests/integration/test_aggro_flow.py`
- **Tank A taunts (room-local), gets top. Tank B taunts, gets top. Mob switches to B** (1 connections) — `server/tests/integration/test_aggro_flow.py`
- **Taunt from adjacent room has no effect; mob does not switch.** (1 connections) — `server/tests/integration/test_aggro_flow.py`

## Relationships

- [App Lifespan Management](App_Lifespan_Management.md) (11 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (11 shared connections)
- [Cursor Plans Combat](Cursor_Plans_Combat.md) (6 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (5 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (5 shared connections)
- [Persistence Item Instance](Persistence_Item_Instance.md) (3 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/tests/integration/test_aggro_flow.py`

## Audit Trail

- EXTRACTED: 117 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*