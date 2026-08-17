# combat_integration.py

> 13 nodes

## Key Concepts

- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **Protocol** (2 connections)
- **Protocols for NPC combat integration (shared by base and facade modules).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Publish a PlayerAttackedEvent to the combat event stream.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Typed surface for npc_combat_service.handle_npc_attack_on_player.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Handle an NPC attack against a player via the main combat service.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Combat event publisher (avoids importing CombatEventPublisher).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **NPC Combat Integration for MythosMUD. This module provides integration between…** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [CombatService](CombatService.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (3 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [NPCAttacked](NPCAttacked.md) (1 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [combat_attack.py](combat_attack.py.md) (1 shared connections)
- [test_combat_integration_base.py](test_combat_integration_base.py.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 44 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*