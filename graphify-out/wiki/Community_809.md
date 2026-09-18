# Community 809

> 20 nodes

## Key Concepts

- **SpellTargetingService** (26 connections) — `server/game/magic/spell_targeting.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **UUID** (8 connections)
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **Player** (1 connections)
- **Resolve the target for a spell cast. Args: player_id: ID of the player casting…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get player from persistence.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Build a TargetMatch for a combat opponent, or None if unresolved.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get the combat target for a player if they are in combat. Args: player_id:…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Service for resolving spell targets. Handles target resolution based on spell…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Initialize the spell targeting service. Args: target_resolution_service:…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve self-target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve area/all target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve entity/location target spell with explicit target. Returns…** (1 connections) — `server/game/magic/spell_targeting.py`

## Relationships

- [Community 54](Community_54.md) (9 shared connections)
- [Community 63](Community_63.md) (6 shared connections)
- [Community 180](Community_180.md) (4 shared connections)
- [Community 110](Community_110.md) (2 shared connections)
- [Community 44](Community_44.md) (2 shared connections)
- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (2 shared connections)
- [Community 65](Community_65.md) (2 shared connections)
- [Community 240](Community_240.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 54 (86%)
- INFERRED: 9 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*