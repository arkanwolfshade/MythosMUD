# CombatEventPublisher

> 38 nodes

## Key Concepts

- **CombatEventPublisher** (30 connections) — `server/services/combat_event_publisher.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **._create_event_message()** (4 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **._nats_ready()** (3 connections) — `server/services/combat_event_publisher.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_initialization_with_nats_service()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_initialization_with_subject_manager()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **fixture** (3 connections)
- **._build_combat_subject()** (2 connections) — `server/services/combat_event_publisher.py`
- **Any** (2 connections)
- **Shared NATS publish path for combat events.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish combat started event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish combat ended event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish player attacked event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- *... and 13 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (21 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 81 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*