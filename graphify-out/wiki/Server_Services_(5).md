# Server Services (5)

> 152 nodes

## Key Concepts

- **NATSError** (89 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (32 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (30 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (24 connections) — `server/services/nats_exceptions.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **message_filtering.py** (11 connections) — `server/realtime/message_filtering.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (9 connections) — `server/services/combat_death_handler.py`
- **._create_corpse_on_death()** (9 connections) — `server/services/combat_death_handler.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- *... and 127 more nodes in this community*

## Relationships

- [Server Realtime](Server_Realtime.md) (22 shared connections)
- [Server Services (2)](Server_Services_%282%29.md) (18 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (17 shared connections)
- [Server Services (17)](Server_Services_%2817%29.md) (12 shared connections)
- [Server Commands](Server_Commands.md) (12 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (11 shared connections)
- [Server Services (18)](Server_Services_%2818%29.md) (10 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (9 shared connections)
- [Server Realtime (23)](Server_Realtime_%2823%29.md) (8 shared connections)
- [Server Models (2)](Server_Models_%282%29.md) (7 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (6 shared connections)
- [Server Services (46)](Server_Services_%2846%29.md) (6 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 589 (77%)
- INFERRED: 172 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*