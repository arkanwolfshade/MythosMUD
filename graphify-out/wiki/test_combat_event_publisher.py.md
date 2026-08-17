# test_combat_event_publisher.py

> 104 nodes

## Key Concepts

- **test_combat_event_publisher.py** (49 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (31 connections) — `server/services/combat_event_publisher.py`
- **asyncio** (18 connections)
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (11 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_no_nats_service()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **_npc_attacked_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_died_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_took_damage_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_nats_error()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_no_nats_service()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 79 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (39 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 191 (83%)
- INFERRED: 39 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*