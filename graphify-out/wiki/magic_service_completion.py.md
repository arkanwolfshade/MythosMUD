# magic_service_completion.py

> 35 nodes

## Key Concepts

- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **UUID** (12 connections)
- **spell_costs.py** (12 connections) — `server/game/magic/spell_costs.py`
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **UUID** (3 connections)
- **Any** (1 connections)
- **Casting completion flow for spellcasting. Mixin that handles completing a…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Parse target_id from casting state. Returns None if missing or invalid.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply costs and queue spell for next combat round. Returns True if queued,…** (1 connections) — `server/game/magic/magic_service_completion.py`
- *... and 10 more nodes in this community*

## Relationships

- [magic_service.py](magic_service.py.md) (15 shared connections)
- [Spell](Spell.md) (5 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (2 shared connections)
- [send_game_event](send_game_event.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [spell_effects.py](spell_effects.py.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 169 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*