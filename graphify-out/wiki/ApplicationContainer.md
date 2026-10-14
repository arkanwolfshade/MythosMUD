# ApplicationContainer

> 111 nodes

## Key Concepts

- **ApplicationContainer** (162 connections) — `server/container/main.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (22 connections) — `server/container/main.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **._sanitarium_failover_callback()** (5 connections) — `server/container/bundles/combat.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 86 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (45 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (17 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (4 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 325 (94%)
- INFERRED: 21 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*