# ApplicationContainer

> 116 nodes

## Key Concepts

- **ApplicationContainer** (157 connections) — `server/container/main.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **container/__init__.py** (17 connections) — `server/container/__init__.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 91 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (51 shared connections)
- [lifespan.py](lifespan.py.md) (12 shared connections)
- [CombatInstance](CombatInstance.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [.initialize](initialize.md) (6 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 339 (92%)
- INFERRED: 28 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*