# TestRoomDataFixer

> 128 nodes · cohesion 0.03

## Key Concepts

- **NATSPublishError** (41 connections) — `server/services/nats_exceptions.py`
- **NATSConfig** (34 connections) — `server/config/models/nats.py`
- **nats_service.py** (32 connections) — `server/services/nats_service.py`
- **NATSServicePoolMixin** (28 connections) — `server/services/nats_service_pool.py`
- **test_nats_service_pool.py** (23 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- **nats_service_pool.py** (19 connections) — `server/services/nats_service_pool.py`
- **nats_service_subscriptions.py** (18 connections) — `server/services/nats_service_subscriptions.py`
- **nats_service_connect.py** (11 connections) — `server/services/nats_service_connect.py`
- **asyncio** (11 connections)
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- **.publish_with_pool()** (9 connections) — `server/services/nats_service_pool.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- **TestNATSPublishError** (8 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **nats_metrics.py** (6 connections) — `server/services/nats_metrics.py`
- **configure_nats_tls()** (6 connections) — `server/services/nats_service_connect.py`
- **nats_connect()** (6 connections) — `server/services/nats_service_connect.py`
- **._initialize_connection_pool()** (6 connections) — `server/services/nats_service_pool.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service_pool.py`
- **NatsSubscription** (6 connections) — `server/services/nats_service_subscriptions.py`
- **._configure_tls()** (5 connections) — `server/services/nats_service_pool.py`
- **._create_pool_connections()** (5 connections) — `server/services/nats_service_pool.py`
- **._get_connection()** (5 connections) — `server/services/nats_service_pool.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service_pool.py`
- **._validate_pool_publish_subject()** (5 connections) — `server/services/nats_service_pool.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_pool.py`
- *... and 103 more nodes in this community*

## Relationships

- [CombatAttackHandler](CombatAttackHandler.md) (40 shared connections)
- [Room](Room.md) (18 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (11 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (10 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (8 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (6 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (6 shared connections)
- [useRoomEditModal.ts](useRoomEditModal.ts.md) (5 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (4 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (3 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (3 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`
- `server/services/nats_service_subscriptions.py`
- `server/tests/unit/services/test_nats_exceptions.py`
- `server/tests/unit/services/test_nats_service_pool.py`

## Audit Trail

- EXTRACTED: 291 (89%)
- INFERRED: 37 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*