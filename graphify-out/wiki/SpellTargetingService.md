# SpellTargetingService

> 22 nodes

## Key Concepts

- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
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
- **Spell targeting service for resolving spell targets. This module handles target…** (1 connections) — `server/game/magic/spell_targeting.py`
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

- [TargetMatch](TargetMatch.md) (12 shared connections)
- [SpellEffectType](SpellEffectType.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [TargetType](TargetType.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (3 shared connections)
- [SpellEffects](SpellEffects.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [magic_service.py](magic_service.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 78 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*