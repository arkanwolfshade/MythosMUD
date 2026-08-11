# Inventory Command Models

> 190 nodes

## Key Concepts

- **NATSError** (98 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (30 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **event_handlers.py** (23 connections) — `server/realtime/event_handlers.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **format_message_content()** (17 connections) — `server/realtime/message_formatters.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSUnsubscribeError** (12 connections) — `server/services/nats_exceptions.py`
- **message_filtering.py** (11 connections) — `server/realtime/message_filtering.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **_send_combat_participant_updates()** (8 connections) — `server/realtime/event_handlers.py`
- *... and 165 more nodes in this community*

## Relationships

- [Combat Service Bundle](Combat_Service_Bundle.md) (17 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (15 shared connections)
- [SQLAlchemy Model Base](SQLAlchemy_Model_Base.md) (15 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (13 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (13 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (13 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (11 shared connections)
- [Health Check Models](Health_Check_Models.md) (10 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (8 shared connections)
- [Connection State Hooks](Connection_State_Hooks.md) (8 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (7 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (7 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 723 (84%)
- INFERRED: 137 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*