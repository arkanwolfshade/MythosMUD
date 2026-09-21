# TargetType

> 37 nodes

## Key Concepts

- **TargetType** (45 connections) — `server/schemas/shared/target_resolution.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **test_add_disambiguation_suffixes()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_disambiguation_suffix_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_build_target_result_single_match()** (5 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **BaseModel** (1 connections)
- **StrEnum** (1 connections)
- **Casting completion flow for spellcasting. Mixin that handles completing a…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Parse target_id from casting state. Returns None if missing or invalid.** (1 connections) — `server/game/magic/magic_service_completion.py`
- *... and 12 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (6 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (6 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (4 shared connections)
- [follow_service.py](follow_service.py.md) (3 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [spell_effects.py](spell_effects.py.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/services/test_target_resolution_service.py`

## Audit Trail

- EXTRACTED: 138 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*