# CombatEventPublisher

> 29 nodes

## Key Concepts

- **CombatEventPublisher** (31 connections) — `server/services/combat_event_publisher.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **_CombatPublishJob** (11 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **._create_event_message()** (4 connections) — `server/services/combat_event_publisher.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._nats_ready()** (3 connections) — `server/services/combat_event_publisher.py`
- **._build_combat_subject()** (2 connections) — `server/services/combat_event_publisher.py`
- **Any** (2 connections)
- **Shared NATS publish path for combat events.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish combat started event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish combat ended event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish player attacked event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish NPC attacked event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish NPC took damage event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Bundled NATS publish inputs (keeps helper parameter count under gate).** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish NPC died event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish combat turn advanced event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- *... and 4 more nodes in this community*

## Relationships

- [combat_event_publisher.py](combat_event_publisher.py.md) (5 shared connections)
- [asyncio](asyncio.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [CombatEndedEvent](CombatEndedEvent.md) (2 shared connections)
- [test_combat_event_publisher_initialization_with_nats_service](test_combat_event_publisher_initialization_with_nats_service.md) (1 shared connections)
- [test_combat_event_publisher_initialization_with_subject_manager](test_combat_event_publisher_initialization_with_subject_manager.md) (1 shared connections)
- [NATSPublishError](NATSPublishError.md) (1 shared connections)
- [combat_event_publisher](combat_event_publisher.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 64 (85%)
- INFERRED: 11 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*