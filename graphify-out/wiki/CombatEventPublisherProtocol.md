# CombatEventPublisherProtocol

> 5 nodes

## Key Concepts

- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **Protocol** (2 connections)
- **Publish a PlayerAttackedEvent to the combat event stream.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Combat event publisher (avoids importing CombatEventPublisher).** (1 connections) — `server/npc/combat_integration_protocols.py`

## Relationships

- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*