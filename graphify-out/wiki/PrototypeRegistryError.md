# PrototypeRegistryError

> 141 nodes

## Key Concepts

- **NATSService** (144 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (60 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (32 connections) — `server/config/models/nats.py`
- **asyncio** (26 connections)
- **.disconnect()** (8 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (7 connections) — `server/services/nats_service.py`
- **_mock_create_tracked_task()** (7 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **.connect()** (6 connections) — `server/services/nats_service.py`
- **.__init__()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **_assert_tracked_coro_closed()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_start_health_monitoring_creates_task()** (6 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_subject_manager()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_tls_files()** (4 connections) — `server/config/models/nats.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **nats_config()** (4 connections) — `server/tests/unit/services/test_nats_service_health.py`
- **test_create_tracked_task_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **test_initialize_connection_pool_passes_auth_token()** (4 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- *... and 116 more nodes in this community*

## Relationships

- [test_aggro_threat.py](test_aggro_threat.py.md) (42 shared connections)
- [InstanceManager](InstanceManager.md) (19 shared connections)
- [ChatModeration](ChatModeration.md) (12 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (3 shared connections)
- [gen_arena_migration_sql.py](gen_arena_migration_sql.py.md) (2 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [description](description.md) (1 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (1 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (1 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_health.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 263 (74%)
- INFERRED: 91 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*