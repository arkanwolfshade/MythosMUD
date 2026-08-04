# message queue realtime

> 15 nodes

## Key Concepts

- **UUID** (7 connections)
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **.handle_npc_death()** (4 connections) — `server/npc/combat_integration.py`
- **Publish PlayerDPUpdated so the client's health/DP bar updates after NPC damage.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the player and UUID needed for DP update events.** (1 connections) — `server/npc/combat_integration.py`
- **Publish the PlayerDPUpdated event to the event bus.** (1 connections) — `server/npc/combat_integration.py`
- **Publish NPC-on-player attack as player_attacked to NATS so the client receives i** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the combat event publisher used to send PlayerAttacked events to NATS.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve target UUID, player object, and stats needed for NATS attack event.** (1 connections) — `server/npc/combat_integration.py`
- **Handle NPC death and related effects.          Args:             npc_id: ID of t** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [room conftest toolkit](room_conftest_toolkit.md) (7 shared connections)
- [memory lifespan app](memory_lifespan_app.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*