# _MagicServiceCore

> 50 nodes

## Key Concepts

- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **UUID** (21 connections)
- **JsonMap** (12 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (7 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (7 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (7 connections) — `server/game/magic/magic_service.py`
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
- **.send_spell_execution_notifications()** (5 connections) — `server/game/magic/magic_service.py`
- **_PlayerPersistence** (4 connections) — `server/game/magic/magic_service.py`
- **._calculate_initiative_tick()** (4 connections) — `server/game/magic/magic_service.py`
- **.restore_mp()** (4 connections) — `server/game/magic/magic_service.py`
- **_CombatTickState** (3 connections) — `server/game/magic/magic_service.py`
- *... and 25 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (29 shared connections)
- [magic_service.py](magic_service.py.md) (9 shared connections)
- [SpellCostsService](SpellCostsService.md) (3 shared connections)
- [MagicServiceHealingMixin](MagicServiceHealingMixin.md) (1 shared connections)
- [TargetType](TargetType.md) (1 shared connections)
- [SpellRegistry](SpellRegistry.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 131 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*