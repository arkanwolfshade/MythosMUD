# .resolve_spell_target

> 14 nodes

## Key Concepts

- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **UUID** (7 connections)
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **Any** (1 connections)
- **Resolve the target for a spell cast. Args: player_id: ID of the player casting…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get player object from persistence.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get the combat target for a player if they are in combat. Args: player_id:…** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve self-target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve area/all target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve entity/location target spell with explicit target. Returns…** (1 connections) — `server/game/magic/spell_targeting.py`

## Relationships

- [magic_service.py](magic_service.py.md) (7 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [Spell](Spell.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*