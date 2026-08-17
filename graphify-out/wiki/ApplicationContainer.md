# ApplicationContainer

> 119 nodes

## Key Concepts

- **ApplicationContainer** (157 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **_flatten_bundle()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **PlayerLifecycleServices** (5 connections) — `server/services/combat_service_types.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **._initialize_secondary_bundles()** (5 connections) — `server/container/main.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 94 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (49 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (10 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (8 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [NPCStartupService](NPCStartupService.md) (4 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 297 (91%)
- INFERRED: 29 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*