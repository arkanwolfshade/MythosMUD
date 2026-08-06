# game weapon player

> 27 nodes

## Key Concepts

- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **UUID** (7 connections)
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **.handle_npc_death()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **Publish PlayerDPUpdated so the client's health/DP bar updates after NPC damage.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the player and UUID needed for DP update events.** (1 connections) — `server/npc/combat_integration.py`
- **Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated.** (1 connections) — `server/npc/combat_integration.py`
- **Publish the PlayerDPUpdated event to the event bus.** (1 connections) — `server/npc/combat_integration.py`
- **Publish NPC-on-player attack as player_attacked to NATS so the client receives i** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the combat event publisher used to send PlayerAttacked events to NATS.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve target UUID, player object, and stats needed for NATS attack event.** (1 connections) — `server/npc/combat_integration.py`
- **Construct the PlayerAttackedEvent payload for NATS publication.** (1 connections) — `server/npc/combat_integration.py`
- **Handle NPC death and related effects.          Args:             npc_id: ID of t** (1 connections) — `server/npc/combat_integration.py`
- **Return an integer stat from stats[key], handling common primitive types.** (1 connections) — `server/npc/combat_integration.py`
- **Calculate max_dp from stats with fallbacks.** (1 connections) — `server/npc/combat_integration.py`
- *... and 2 more nodes in this community*

## Relationships

- [services nats service](services_nats_service.md) (12 shared connections)
- [add used user](add_used_user.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)
- [tools generate invite](tools_generate_invite.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 81 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*