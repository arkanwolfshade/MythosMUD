# test_combat_event_publisher.py

> 151 nodes

## Key Concepts

- **test_combat_event_publisher.py** (48 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (31 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **asyncio** (18 connections)
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **test_combat_event_handler.py** (16 connections) — `server/tests/unit/services/test_combat_event_handler.py`
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
- **asyncio** (6 connections)
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- *... and 126 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (28 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [models/combat.py](models-combat.py.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [NATSError](NATSError.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (1 shared connections)
- [CombatEventPublisherProtocol](CombatEventPublisherProtocol.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 319 (84%)
- INFERRED: 61 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*