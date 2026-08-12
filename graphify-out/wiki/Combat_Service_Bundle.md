# Combat Service Bundle

> 400 nodes

## Key Concepts

- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **NATSService** (72 connections) — `server/services/nats_service.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **CombatEventPublisher** (30 connections) — `server/services/combat_event_publisher.py`
- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **Any** (17 connections)
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **NPCAttackedEvent** (10 connections) — `server/events/combat_events.py`
- **connection_state_machine.py** (10 connections) — `server/realtime/connection_state_machine.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- *... and 375 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (56 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (43 shared connections)
- [Client Event Store](Client_Event_Store.md) (16 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (12 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Services Rescue Service](Services_Rescue_Service.md) (6 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Realtime Event Delegation](Realtime_Event_Delegation.md) (3 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (3 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (3 shared connections)
- [Command Parser](Command_Parser.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/events/combat_events.py`
- `server/infrastructure/nats_broker.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/connection_state_machine.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 1255 (95%)
- INFERRED: 64 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*