# test_combat_event_publisher.py

> 150 nodes

## Key Concepts

- **test_combat_event_publisher.py** (55 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **PlayerDPDecayEvent** (29 connections) — `server/events/event_types.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- *... and 125 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (20 shared connections)
- [CombatService](CombatService.md) (13 shared connections)
- [PlayerLeftRoom](PlayerLeftRoom.md) (13 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (11 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [NATSError](NATSError.md) (8 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (5 shared connections)
- [models/combat.py](models-combat.py.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 374 (89%)
- INFERRED: 45 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*