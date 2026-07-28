# Combat Aggro Threat

> 20 nodes · cohesion 0.15

## Key Concepts

- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **add_heal_threat()** (14 connections) — `server/services/aggro_threat.py`
- **UUID** (11 connections)
- **get_npc_current_target()** (8 connections) — `server/services/aggro_threat.py`
- **apply_stealth_wipe()** (7 connections) — `server/services/aggro_threat.py`
- **_get_aggro_config()** (7 connections) — `server/services/aggro_threat.py`
- **on_player_entered_stealth()** (7 connections) — `server/services/aggro_threat.py`
- **_select_top_alive_candidate()** (5 connections) — `server/services/aggro_threat.py`
- **_should_switch_to_candidate()** (5 connections) — `server/services/aggro_threat.py`
- **_aggression_scale()** (4 connections) — `server/services/aggro_threat.py`
- **Any** (1 connections)
- **Aggro and threat management for combat (ADR-016).  Per-NPC hate lists, threat fr** (1 connections) — `server/services/aggro_threat.py`
- **Remove entity from NPC's hate list (or set threat to 0). Stealth = full wipe.** (1 connections) — `server/services/aggro_threat.py`
- **Call when a player enters stealth (ADR-016 Option A: wipe).      Removes the pla** (1 connections) — `server/services/aggro_threat.py`
- **Return (candidate_id, candidate_threat) for alive entity with max threat.** (1 connections) — `server/services/aggro_threat.py`
- **Return True if we should switch from current target to candidate.** (1 connections) — `server/services/aggro_threat.py`
- **Return game config for aggro constants.** (1 connections) — `server/services/aggro_threat.py`
- **Return current target participant_id for this NPC, or None.** (1 connections) — `server/services/aggro_threat.py`
- **Scale factor from aggression_level 0-10. None => 1.0 (full threat).** (1 connections) — `server/services/aggro_threat.py`
- **Add threat to an NPC's hate list from healing (e.g. 0.5x heal amount).      thre** (1 connections) — `server/services/aggro_threat.py`

## Relationships

- [App Lifespan Management](App_Lifespan_Management.md) (14 shared connections)
- [Phantom Hostile Requirements](Phantom_Hostile_Requirements.md) (11 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (6 shared connections)
- [Persistence Item Instance](Persistence_Item_Instance.md) (4 shared connections)
- [Cursor Plans Combat](Cursor_Plans_Combat.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*