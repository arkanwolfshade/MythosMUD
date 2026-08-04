# room realtime rationale

> 40 nodes

## Key Concepts

- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **MagicServiceHealingMixin** (17 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (17 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **SpellRangeType** (12 connections) — `server/models/spell.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **_spell()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_is_heal_other_target()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_send_instant_heal_event_if_applied()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_effect_result_has_healing()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_send_healing_update_event_skips_without_healing()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_or_send_dp_update_no_player()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_or_send_dp_update_publishes_event()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_dp_event_uses_event_bus()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_dp_event_fallback_send_game_event()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **Mixin for MagicService: send DP update events when spells apply healing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True when healing was applied to another player (heal-other, not steal-life or s** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True if effect result indicates healing was applied (success, effect_applied, he** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Send player_dp_updated event for the healed player (target for heal other, caste** (1 connections) — `server/game/magic/magic_healing_events.py`
- *... and 15 more nodes in this community*

## Relationships

- [coercion int inventory](coercion_int_inventory.md) (18 shared connections)
- [spell game magic](spell_game_magic.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [player respawn event](player_respawn_event.md) (2 shared connections)
- [game models player](game_models_player.md) (2 shared connections)
- [subject nats manager](subject_nats_manager.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (1 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`

## Audit Trail

- EXTRACTED: 146 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*