# combat_integration.py

> 19 nodes

## Key Concepts

- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **NPCAttacked** (14 connections) — `server/events/event_types.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **Protocol** (2 connections)
- **Event fired when an NPC attacks a target. This event is triggered when an NPC…** (1 connections) — `server/events/event_types.py`
- **Protocols for NPC combat integration (shared by base and facade modules).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Publish a PlayerAttackedEvent to the combat event stream.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Typed surface for npc_combat_service.handle_npc_attack_on_player.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Handle an NPC attack against a player via the main combat service.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Combat event publisher (avoids importing CombatEventPublisher).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **NPC Combat Integration for MythosMUD. This module provides integration between…** (1 connections) — `server/npc/combat_integration.py`
- **Publish NPC attack event to event bus.** (1 connections) — `server/npc/combat_integration.py`
- **_publish_attack_event forwards to event bus when configured.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (5 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (3 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (2 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 59 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*