# baseexception

> 190 nodes

## Key Concepts

- **NATSService** (146 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (58 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **asyncio** (26 connections)
- **nats_service.py** (24 connections) — `server/services/nats_service.py`
- **test_nats_service_health.py** (22 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **asyncio** (15 connections)
- **JsonMap** (9 connections)
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **_NatsListenerClient** (5 connections) — `server/services/nats_service.py`
- **NatsMessageCallback** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_perform_health_check_error()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **_NatsSubscription** (4 connections) — `server/services/nats_service.py`
- **._acknowledge_message()** (4 connections) — `server/services/nats_service.py`
- **._call_callback()** (4 connections) — `server/services/nats_service.py`
- **._decode_message_data()** (4 connections) — `server/services/nats_service.py`
- **.get_connection_stats()** (4 connections) — `server/services/nats_service.py`
- *... and 165 more nodes in this community*

## Relationships

- [docs nats subject patterns](docs_nats_subject_patterns.md) (35 shared connections)
- [server config init create config](server_config_init_create_config.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [moduletype](moduletype.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (2 shared connections)
- [server events combat events](server_events_combat_events.md) (2 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server container bundles realtime py](server_container_bundles_realtime_py.md) (1 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 307 (75%)
- INFERRED: 102 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*