# .shutdown()

> 60 nodes

## Key Concepts

- **ApplicationContainer** (136 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **reset_container()** (8 connections) — `server/container/main.py`
- **__init__.py** (7 connections) — `server/container/__init__.py`
- **.reset_instance()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **Test ApplicationContainer._decode_json_column() decodes JSON.** (6 connections) — `server/tests/unit/test_application_container.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **Test ApplicationContainer._normalize_path_from_url_or_path() normalizes path.** (4 connections) — `server/tests/unit/test_application_container.py`
- **.shutdown()** (3 connections) — `server/container/bundles/monitoring.py`
- **.shutdown()** (3 connections) — `server/container/bundles/realtime.py`
- **.__init__()** (3 connections) — `server/container/main.py`
- **test_get_container()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_is_initialized()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service_invalid()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service_not_initialized_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- *... and 35 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (30 shared connections)
- [. init ()](_init_%28%29.md) (23 shared connections)
- [Any](Any.md) (16 shared connections)
- [lifespan](lifespan.md) (8 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (7 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [.get instance()](get_instance%28%29.md) (6 shared connections)
- [lifespan shutdown](lifespan_shutdown.md) (4 shared connections)
- [Path](Path.md) (4 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (3 shared connections)
- [. handle nats unavailable()](_handle_nats_unavailable%28%29.md) (3 shared connections)
- [message handlers](message_handlers.md) (3 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 316 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*