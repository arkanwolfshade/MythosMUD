# ._build_player_attacked_event

> 34 nodes

## Key Concepts

- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
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
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **.get_stats()** (3 connections) — `server/npc/npc_base.py`
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **Protocol** (2 connections)
- **Protocols for NPC combat integration (shared by base and facade modules).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Publish a PlayerAttackedEvent to the combat event stream.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Typed surface for npc_combat_service.handle_npc_attack_on_player.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Handle an NPC attack against a player via the main combat service.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Combat event publisher (avoids importing CombatEventPublisher).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Resolve the player and UUID needed for DP update events.** (1 connections) — `server/npc/combat_integration.py`
- **Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated.** (1 connections) — `server/npc/combat_integration.py`
- *... and 9 more nodes in this community*

## Relationships

- [NPCCombatIntegration](NPCCombatIntegration.md) (13 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 62 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*