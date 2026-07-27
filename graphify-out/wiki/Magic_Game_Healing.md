# Magic Game Healing

> 15 nodes · cohesion 0.20

## Key Concepts

- **UUID** (9 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (8 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **Spell** (4 connections) — `server/game/magic/magic_healing_events.py`
- **Publish DP update via event bus, or send fallback game event.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **If instant cast applied healing, send DP update event to the healed player.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True when healing was applied to another player (heal-other, not steal-life or s** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True if effect result indicates healing was applied (success, effect_applied, he** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Send player_dp_updated event for the healed player (target for heal other, caste** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Load player stats and delegate DP event publishing.** (1 connections) — `server/game/magic/magic_healing_events.py`

## Relationships

- [[Magic Service Bundle]] (6 shared connections)
- [[Player Event Handler Tests]] (4 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Spell Registry Costs]] (3 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`

## Audit Trail

- EXTRACTED: 51 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
