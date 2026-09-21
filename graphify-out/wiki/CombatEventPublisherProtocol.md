# CombatEventPublisherProtocol

> 7 nodes

## Key Concepts

- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **._get_combat_event_publisher()** (6 connections) — `server/npc/combat_integration.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **Protocol** (2 connections)
- **Publish a PlayerAttackedEvent to the combat event stream.** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Combat event publisher (avoids importing CombatEventPublisher).** (1 connections) — `server/npc/combat_integration_protocols.py`
- **Resolve the combat event publisher used to send PlayerAttacked events to NATS.** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (1 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (1 shared connections)
- [combat_service.py](combat_service.py.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`

## Audit Trail

- EXTRACTED: 13 (87%)
- INFERRED: 2 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*