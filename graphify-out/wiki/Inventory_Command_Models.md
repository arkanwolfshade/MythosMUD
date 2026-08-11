# Inventory Command Models

> 337 nodes

## Key Concepts

- **NATSError** (98 connections) — `server/services/nats_exceptions.py`
- **NATSService** (72 connections) — `server/services/nats_service.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **CombatEventPublisher** (30 connections) — `server/services/combat_event_publisher.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **format_message_content()** (17 connections) — `server/realtime/message_formatters.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **Any** (17 connections)
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **nats_event_bridge.py** (13 connections) — `server/events/nats_event_bridge.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- *... and 312 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (83 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (20 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (19 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (14 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (11 shared connections)
- [Dual Connection API Reference](Dual_Connection_API_Reference.md) (6 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (6 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (5 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (5 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (4 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (4 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (3 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/nats_event_bridge.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/event_handlers.py`
- `server/realtime/message_formatters.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 1259 (88%)
- INFERRED: 167 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*