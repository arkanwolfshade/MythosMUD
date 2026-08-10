# Player Occupant Processor

> 35 nodes

## Key Concepts

- **CombatEventPublisher** (30 connections) — `server/services/combat_event_publisher.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (5 connections) — `server/services/combat_event_publisher.py`
- **._create_event_message()** (4 connections) — `server/services/combat_event_publisher.py`
- **.__init__()** (3 connections) — `server/services/combat_event_publisher.py`
- **._nats_ready()** (3 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_initialization_with_nats_service()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_combat_event_publisher_initialization_with_subject_manager()** (3 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **Any** (2 connections)
- **._build_combat_subject()** (2 connections) — `server/services/combat_event_publisher.py`
- **Bundled NATS publish inputs (keeps helper parameter count under gate).** (1 connections) — `server/services/combat_event_publisher.py`
- **Service for publishing combat events to NATS for real-time distribution.** (1 connections) — `server/services/combat_event_publisher.py`
- **Initialize combat event publisher.          Args:             nats_service: N** (1 connections) — `server/services/combat_event_publisher.py`
- **Create a standardized event message structure matching EventMessageSchema.** (1 connections) — `server/services/combat_event_publisher.py`
- **Shared NATS publish path for combat events.** (1 connections) — `server/services/combat_event_publisher.py`
- **Publish combat started event to NATS.** (1 connections) — `server/services/combat_event_publisher.py`
- *... and 10 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (21 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (3 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)

## Source Files

- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 130 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*