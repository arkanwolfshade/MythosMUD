# CastingStateManager

> 61 nodes

## Key Concepts

- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **test_casting_state_manager.py** (12 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **UUID** (8 connections)
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **.start_casting()** (6 connections) — `server/game/magic/casting_state_manager.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.get_casting_state()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **.interrupt_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- *... and 36 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (9 shared connections)
- [TargetMatch](TargetMatch.md) (8 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (7 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service_completion.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`

## Audit Trail

- EXTRACTED: 143 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*