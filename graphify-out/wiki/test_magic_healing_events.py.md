# test_magic_healing_events.py

> 41 nodes

## Key Concepts

- **test_magic_healing_events.py** (21 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **MagicServiceHealingMixin** (14 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (12 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
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
- *... and 16 more nodes in this community*

## Relationships

- [SpellEffectType](SpellEffectType.md) (10 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`

## Audit Trail

- EXTRACTED: 96 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*