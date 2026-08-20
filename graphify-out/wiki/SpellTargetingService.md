# SpellTargetingService

> 22 nodes

## Key Concepts

- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **UUID** (8 connections)
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **spell_targeting_service()** (5 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
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
- **Create SpellTargetingService with mocks.** (1 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`

## Relationships

- [TargetMatch](TargetMatch.md) (9 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 58 (85%)
- INFERRED: 10 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*