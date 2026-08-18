# CombatEventPublisherProtocol

> 9 nodes

## Key Concepts

- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **.handle_npc_attack_on_player()** (2 connections) — `server/npc/combat_integration_protocols.py`
- **Protocol** (2 connections)
- **Publish a PlayerAttackedEvent to the combat event stream.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Typed surface for npc_combat_service.handle_npc_attack_on_player.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Handle an NPC attack against a player via the main combat service.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Combat event publisher (avoids importing CombatEventPublisher).** (1 connections) — `server/npc/combat_integration_protocols.py`

## Relationships

- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 14 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*