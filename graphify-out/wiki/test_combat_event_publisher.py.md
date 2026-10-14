# test_combat_event_publisher.py

> 224 nodes

## Key Concepts

- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_status_message_categories.py** (47 connections) — `server/tests/unit/services/test_combat_status_message_categories.py`
- **CombatEventPublisher** (45 connections) — `server/services/combat_event_publisher.py`
- **PlayerDPDecayEvent** (33 connections) — `server/events/event_types.py`
- **combat_event_publisher.py** (31 connections) — `server/services/combat_event_publisher.py`
- **test_combat_npc_disposition.py** (30 connections) — `server/tests/unit/services/test_combat_npc_disposition.py`
- **PlayerAttackedEvent** (24 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (23 connections) — `server/events/combat_events.py`
- **CombatMessagingIntegration** (23 connections) — `server/services/combat_messaging/integration.py`
- **combat_events.py** (22 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (21 connections) — `server/services/combat_event_handler.py`
- **NPCDiedEvent** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **combat_service_events.py** (19 connections) — `server/services/combat_service_events.py`
- **NPCAttackedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatEndedEvent** (17 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatTargetSwitchEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **asyncio** (13 connections)
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 199 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (59 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (17 shared connections)
- [MessageCategory](MessageCategory.md) (17 shared connections)
- [test_message_category_invariants.py](test_message_category_invariants.py.md) (14 shared connections)
- [NATSError](NATSError.md) (12 shared connections)
- [BaseEvent](BaseEvent.md) (10 shared connections)
- [NpcDisposition](NpcDisposition.md) (10 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_combat_npc_disposition.py`
- `server/tests/unit/services/test_combat_status_message_categories.py`

## Audit Trail

- EXTRACTED: 603 (87%)
- INFERRED: 92 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*