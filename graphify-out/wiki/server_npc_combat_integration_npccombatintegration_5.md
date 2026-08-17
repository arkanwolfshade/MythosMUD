# server npc combat integration npccombatintegration

> 23 nodes

## Key Concepts

- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **UUID** (5 connections)
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **Resolve the player and UUID needed for DP update events.** (1 connections) — `server/npc/combat_integration.py`
- **Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated.** (1 connections) — `server/npc/combat_integration.py`
- **Publish the PlayerDPUpdated event to the event bus.** (1 connections) — `server/npc/combat_integration.py`
- **Publish NPC-on-player attack as player_attacked to NATS so the client receives…** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the combat event publisher used to send PlayerAttacked events to NATS.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve target UUID, player object, and stats needed for NATS attack event.** (1 connections) — `server/npc/combat_integration.py`
- **Construct the PlayerAttackedEvent payload for NATS publication.** (1 connections) — `server/npc/combat_integration.py`
- **Return an integer stat from stats[key], handling common primitive types.** (1 connections) — `server/npc/combat_integration.py`
- **Calculate max_dp from stats with fallbacks.** (1 connections) — `server/npc/combat_integration.py`
- **Publish PlayerDPUpdated so the client's health/DP bar updates after NPC damage.** (1 connections) — `server/npc/combat_integration.py`
- **Get current NPC stats.** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (12 shared connections)
- [server events combat events](server_events_combat_events.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (1 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 44 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*