# _MagicServiceCore

> 54 nodes

## Key Concepts

- **_MagicServiceCore** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (20 connections)
- **Any** (18 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (8 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (7 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (6 connections) — `server/game/magic/magic_service.py`
- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (6 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_lucidity_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_materials_available()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_mp_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_player_knows_spell()** (5 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (5 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (5 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (5 connections) — `server/game/magic/magic_service.py`
- **.interrupt_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **.send_spell_execution_notifications()** (5 connections) — `server/game/magic/magic_service.py`
- **._calculate_initiative_tick()** (4 connections) — `server/game/magic/magic_service.py`
- **._get_spell_from_registry()** (4 connections) — `server/game/magic/magic_service.py`
- **._perform_luck_check()** (4 connections) — `server/game/magic/magic_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [Spell](Spell.md) (7 shared connections)
- [magic_service.py](magic_service.py.md) (6 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (4 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (1 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 121 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*