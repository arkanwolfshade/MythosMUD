# NATSService

> 130 nodes

## Key Concepts

- **NATSService** (72 connections) — `server/services/nats_service.py`
- **CombatEventPublisher** (30 connections) — `server/services/combat_event_publisher.py`
- **Any** (17 connections)
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **.disconnect()** (10 connections) — `server/services/nats_service.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- *... and 105 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (28 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [test_nats_service_init_with_subject_manager](test_nats_service_init_with_subject_manager.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)
- [NATSMetrics](NATSMetrics.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [._connect_nats](_connect_nats.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 261 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*