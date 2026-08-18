# test_combat_event_publisher.py

> 153 nodes

## Key Concepts

- **test_combat_event_publisher.py** (49 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (31 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **asyncio** (18 connections)
- **test_combat_event_handler.py** (17 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (11 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **test_publish_paths_no_nats_service()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **.handle_attack_events_and_xp()** (7 connections) — `server/services/combat_event_handler.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **asyncio** (6 connections)
- *... and 128 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (27 shared connections)
- [CombatParticipant](CombatParticipant.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [CombatEventPublisherProtocol](CombatEventPublisherProtocol.md) (3 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 347 (90%)
- INFERRED: 40 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*