# _MagicServiceCore

> 62 nodes

## Key Concepts

- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **UUID** (21 connections)
- **JsonMap** (12 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (7 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (7 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (7 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (7 connections) — `server/game/magic/magic_service.py`
- **_stat_int()** (7 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (6 connections) — `server/game/magic/magic_service.py`
- **._perform_luck_check()** (6 connections) — `server/game/magic/magic_service.py`
- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **_StatsPlayer** (5 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_lucidity_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_materials_available()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_mp_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_player_knows_spell()** (5 connections) — `server/game/magic/magic_service.py`
- **.interrupt_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._player_persistence()** (5 connections) — `server/game/magic/magic_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (20 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [SpellEffects](SpellEffects.md) (4 shared connections)
- [CastingStateManager](CastingStateManager.md) (3 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (1 shared connections)
- [MagicServiceCompletionMixin](MagicServiceCompletionMixin.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (1 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 154 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*