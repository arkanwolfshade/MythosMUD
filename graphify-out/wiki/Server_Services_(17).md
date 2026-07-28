# Server Services (17)

> 89 nodes

## Key Concepts

- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **NPCAttackedEvent** (10 connections) — `server/events/combat_events.py`
- **CombatTurnAdvancedEvent** (7 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (7 connections) — `server/events/combat_events.py`
- **.publish_combat_started()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_ended()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (4 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (4 connections) — `server/services/combat_event_publisher.py`
- **test_publish_combat_started_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_nats_error()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **.publish_player_attacked()** (3 connections) — `server/npc/combat_integration_protocols.py`
- **.publish_combat_started_event()** (3 connections) — `server/services/combat_service.py`
- *... and 64 more nodes in this community*

## Relationships

- [Server Services (29)](Server_Services_%2829%29.md) (19 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (12 shared connections)
- [Server Events](Server_Events.md) (8 shared connections)
- [Server Npc](Server_Npc.md) (4 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (3 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (3 shared connections)
- [Server Services (2)](Server_Services_%282%29.md) (3 shared connections)
- [Server Npc (8)](Server_Npc_%288%29.md) (2 shared connections)
- [Server Services (3)](Server_Services_%283%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (2 shared connections)
- [Server Services (11)](Server_Services_%2811%29.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 325 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*