# magic_service.py

> 72 nodes

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **send_game_event()** (33 connections) — `server/realtime/connection_manager_api.py`
- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **SpellCostsService** (19 connections) — `server/game/magic/spell_costs.py`
- **spell_costs.py** (16 connections) — `server/game/magic/spell_costs.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **MagicServiceHealingMixin** (14 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (12 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **.apply_costs()** (7 connections) — `server/game/magic/spell_costs.py`
- **._notify_mp_update()** (7 connections) — `server/game/magic/spell_costs.py`
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **._apply_corruption_if_mythos()** (6 connections) — `server/game/magic/spell_costs.py`
- **._spend_lucidity_if_required()** (6 connections) — `server/game/magic/spell_costs.py`
- **UUID** (6 connections)
- **UUID** (6 connections)
- **asyncio** (6 connections)
- **_StatsPlayer** (5 connections) — `server/game/magic/magic_service.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **test_send_instant_heal_event_if_applied()** (5 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **Any** (5 connections)
- *... and 47 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (23 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [SpellEffectType](SpellEffectType.md) (15 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (8 shared connections)
- [SpellEffects](SpellEffects.md) (6 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (6 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (4 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (3 shared connections)
- [CorruptionService](CorruptionService.md) (3 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`

## Audit Trail

- EXTRACTED: 230 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*