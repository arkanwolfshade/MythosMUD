# UUID

> 30 nodes

## Key Concepts

- **send_game_event()** (29 connections) — `server/realtime/connection_manager_api.py`
- **MagicServiceHealingMixin** (15 connections) — `server/game/magic/magic_healing_events.py`
- **magic_healing_events.py** (14 connections) — `server/game/magic/magic_healing_events.py`
- **__getattr__()** (8 connections) — `server/realtime/connection_manager.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **send_system_notification()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (6 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (6 connections) — `server/realtime/connection_manager_api.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **.send_personal_message()** (3 connections) — `server/realtime/connection_manager_api.py`
- **Healing event notification for spellcasting.  Mixin that sends player_dp_updated** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Mixin for MagicService: send DP update events when spells apply healing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True when healing was applied to another player (heal-other, not steal-life or s** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True if effect result indicates healing was applied (success, effect_applied, he** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Send player_dp_updated event for the healed player (target for heal other, caste** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Load player stats and delegate DP event publishing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Publish DP update via event bus, or send fallback game event.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **If instant cast applied healing, send DP update event to the healed player.** (1 connections) — `server/game/magic/magic_healing_events.py`
- *... and 5 more nodes in this community*

## Relationships

- [connection manager api](connection_manager_api.md) (9 shared connections)
- [Any](Any.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [Connection Manager](Connection_Manager.md) (4 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (4 shared connections)
- [Spell Targeting](Spell_Targeting.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [MagicServiceCore](MagicServiceCore.md) (2 shared connections)
- [message handlers](message_handlers.md) (2 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (2 shared connections)
- [.shutdown()](shutdown%28%29.md) (1 shared connections)
- [spell registry](spell_registry.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`

## Audit Trail

- EXTRACTED: 135 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*