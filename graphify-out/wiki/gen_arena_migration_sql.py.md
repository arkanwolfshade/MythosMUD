# gen_arena_migration_sql.py

> 56 nodes

## Key Concepts

- **NATSMessageBroker** (33 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker.py** (21 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (11 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (7 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_message()** (5 connections) — `server/infrastructure/nats_broker.py`
- **Any** (5 connections)
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_subject()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- *... and 31 more nodes in this community*

## Relationships

- [LucidityFluxService](LucidityFluxService.md) (20 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [Scenario Group Execution](Scenario_Group_Execution.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (2 shared connections)
- [Protocol](Protocol.md) (2 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (2 shared connections)
- [description](description.md) (1 shared connections)
- [player_combat_service_support.py](player_combat_service_support.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 121 (87%)
- INFERRED: 18 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*