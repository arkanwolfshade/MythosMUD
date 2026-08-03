# nats exceptions services

> 188 nodes

## Key Concepts

- **NATSError** (101 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (33 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **test_combat_persistence_handler_events.py** (25 connections) — `server/tests/unit/services/test_combat_persistence_handler_events.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **combat_persistence_handler.py** (15 connections) — `server/services/combat_persistence_handler.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **NATSUnsubscribeError** (12 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_persistence_handler.py`
- *... and 163 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (32 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (24 shared connections)
- [nats services service](nats_services_service.md) (18 shared connections)
- [nats message handler](nats_message_handler.md) (15 shared connections)
- [Item Instances](Item_Instances.md) (12 shared connections)
- [combat validator validators](combat_validator_validators.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [subzone realtime nats](subzone_realtime_nats.md) (8 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (5 shared connections)
- [item models rationale](item_models_rationale.md) (5 shared connections)
- [message chat nats](message_chat_nats.md) (4 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (3 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/combat_persistence_handler.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_persistence_handler_events.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 672 (83%)
- INFERRED: 138 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*