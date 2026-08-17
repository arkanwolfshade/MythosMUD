# server game magic magic healing

> 18 nodes

## Key Concepts

- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **MagicServiceHealingMixin** (12 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **._is_heal_other_target()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **._send_instant_heal_event_if_applied()** (5 connections) — `server/game/magic/magic_healing_events.py`
- **Any** (5 connections)
- **._effect_result_has_healing()** (4 connections) — `server/game/magic/magic_healing_events.py`
- **Healing event notification for spellcasting. Mixin that sends player_dp_updated…** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Publish DP update via event bus, or send fallback game event.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **If instant cast applied healing, send DP update event to the healed player.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Mixin for MagicService: send DP update events when spells apply healing.** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True when healing was applied to another player (heal-other, not steal-life or…** (1 connections) — `server/game/magic/magic_healing_events.py`
- **True if effect result indicates healing was applied (success, effect_applied,…** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Send player_dp_updated event for the healed player (target for heal other,…** (1 connections) — `server/game/magic/magic_healing_events.py`
- **Load player stats and delegate DP event publishing.** (1 connections) — `server/game/magic/magic_healing_events.py`

## Relationships

- [server game magic spell registry](server_game_magic_spell_registry.md) (4 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (3 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (3 shared connections)
- [followtargetvalue](followtargetvalue.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (1 shared connections)
- [server api players](server_api_players.md) (1 shared connections)
- [server api character creation](server_api_character_creation.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`

## Audit Trail

- EXTRACTED: 47 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*