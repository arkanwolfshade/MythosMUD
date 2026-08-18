# magic_service_completion.py

> 25 nodes

## Key Concepts

- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
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
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **Casting completion flow for spellcasting. Mixin that handles completing a…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Parse target_id from casting state. Returns None if missing or invalid.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply costs and queue spell for next combat round. Returns True if queued,…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs/effects, send completion message and healing event.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **If in combat, try to queue spell for next round. Return True if queued, False…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Complete a casting and apply spell effects. In combat, spells are queued for…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Mixin for MagicService: complete casting (player/room, target, costs/effects,…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Get player and room_id for casting completion. Returns: Tuple of (player,…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Recreate target from stored casting state. Args: casting_state: The casting…** (1 connections) — `server/game/magic/magic_service_completion.py`

## Relationships

- [magic_service.py](magic_service.py.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [TargetType](TargetType.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Spell](Spell.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*