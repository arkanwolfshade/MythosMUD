# Community 466

> 38 nodes

## Key Concepts

- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **MagicServiceHealingMixin** (14 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (12 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **asyncio** (6 connections)
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **test_send_instant_heal_event_if_applied()** (5 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **Any** (5 connections)
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **test_is_heal_other_target()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_dp_event_fallback_send_game_event()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_dp_event_uses_event_bus()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_or_send_dp_update_no_player()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_publish_or_send_dp_update_publishes_event()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_send_healing_update_event_skips_without_healing()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_effect_result_has_healing()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **.__init__()** (1 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **Healing event notification for spellcasting. Mixin that sends player_dp_updated…** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Publish DP update via event bus, or send fallback game event.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **If instant cast applied healing, send DP update event to the healed player.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Mixin for MagicService: send DP update events when spells apply healing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- *... and 13 more nodes in this community*

## Relationships

- [Community 54](Community_54.md) (17 shared connections)
- [Community 219](Community_219.md) (3 shared connections)
- [Community 110](Community_110.md) (2 shared connections)
- [Community 93](Community_93.md) (2 shared connections)
- [Community 499](Community_499.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (2 shared connections)
- [Community 240](Community_240.md) (1 shared connections)
- [Community 44](Community_44.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`

## Audit Trail

- EXTRACTED: 85 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*