# Community 785

> 21 nodes

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

## Relationships

- [Community 231](Community_231.md) (10 shared connections)
- [Community 1043](Community_1043.md) (2 shared connections)
- [Community 1297](Community_1297.md) (1 shared connections)
- [Combat Events](Combat_Events.md) (1 shared connections)
- [Community 1419](Community_1419.md) (1 shared connections)
- [Community 149](Community_149.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Community 218](Community_218.md) (1 shared connections)
- [Community 219](Community_219.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 42 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*