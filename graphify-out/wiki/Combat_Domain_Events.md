# Combat Domain Events

> 271 nodes

## Key Concepts

- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **NATSError** (98 connections) — `server/services/nats_exceptions.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- *... and 246 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (37 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (25 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (24 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (22 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (21 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (19 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (18 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (16 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (15 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (15 shared connections)
- [Health Check Models](Health_Check_Models.md) (13 shared connections)
- [Error Handling Guide](Error_Handling_Guide.md) (13 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 1157 (85%)
- INFERRED: 211 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*