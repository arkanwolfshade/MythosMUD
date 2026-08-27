# DatabaseManager

> 100 nodes

## Key Concepts

- **NATSSubjectManager** (52 connections) — `server/services/nats_subject_manager/manager.py`
- **test_manager.py** (49 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **.validate_subject()** (4 connections) — `server/services/nats_subject_manager/manager.py`
- **subject_manager()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_cache()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **subject_manager_no_metrics()** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **Test NATSSubjectManager initialization without metrics.** (4 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **get_subject_manager_dependency()** (3 connections) — `server/api/admin/subject_controller.py`
- **._cache_result()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_subscription_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **._record_validation_metrics()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **.register_pattern()** (3 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_subject_too_long()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_custom_max_length()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_cache()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_no_metrics()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_nats_subject_manager_init_strict_validation()** (3 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **fixture** (3 connections)
- **.clear_cache()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_chat_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **.get_event_subscription_patterns()** (2 connections) — `server/services/nats_subject_manager/manager.py`
- **test_build_subject_invalid_parameter_value()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_missing_parameter()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- **test_build_subject_multiple_params()** (2 connections) — `server/tests/unit/services/nats_subject_manager/test_manager.py`
- *... and 75 more nodes in this community*

## Relationships

- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (15 shared connections)
- [test_websocket_handler_rate_limit.py](test_websocket_handler_rate_limit.py.md) (8 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (7 shared connections)
- [gen_arena_migration_sql.py](gen_arena_migration_sql.py.md) (2 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (2 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [ChatModeration](ChatModeration.md) (1 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (1 shared connections)
- [Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch](Uvicorn-ASGI_Code_Review_-_feature-sqlite-to-postgresql_Branch.md) (1 shared connections)
- [compare_linting_results.py](compare_linting_results.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/services/nats_subject_manager/manager.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 147 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*