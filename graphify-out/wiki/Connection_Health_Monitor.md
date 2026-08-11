# Connection Health Monitor

> 16 nodes

## Key Concepts

- **MagicServiceHealingMixin** (15 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **Mixin for MagicService: send DP update events when spells apply healing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True when healing was applied to another player (heal-other, not steal-life or s** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True if effect result indicates healing was applied (success, effect_applied, he** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Send player_dp_updated event for the healed player (target for heal other, caste** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Load player stats and delegate DP event publishing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Publish DP update via event bus, or send fallback game event.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **If instant cast applied healing, send DP update event to the healed player.** (1 connections) — `server/game/magic/magic_healing_events.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (4 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`

## Audit Trail

- EXTRACTED: 61 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*