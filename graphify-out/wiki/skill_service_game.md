# skill service game

> 16 nodes

## Key Concepts

- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **UUID** (8 connections)
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **Player** (1 connections)
- **Resolve self-target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve area/all target spell. Returns (target_match, error_message).** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve entity/location target spell with explicit target. Returns (target_match** (1 connections) — `server/game/magic/spell_targeting.py`
- **Resolve the target for a spell cast.          Args:             player_id: ID of** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get player from persistence.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Build a TargetMatch for a combat opponent, or None if unresolved.** (1 connections) — `server/game/magic/spell_targeting.py`
- **Get the combat target for a player if they are in combat.          Args:** (1 connections) — `server/game/magic/spell_targeting.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [spell game magic](spell_game_magic.md) (8 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*