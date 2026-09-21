# ApplicationContainer

> 127 nodes

## Key Concepts

- **ApplicationContainer** (162 connections) — `server/container/main.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (23 connections) — `server/container/main.py`
- **get_container()** (21 connections) — `server/container/main.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **fixtures/unit/__init__.py** (8 connections) — `server/tests/fixtures/unit/__init__.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **.initialize()** (5 connections) — `server/container/main.py`
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
- **dummy_request()** (4 connections) — `server/tests/fixtures/unit/__init__.py`
- **fakerandom()** (4 connections) — `server/tests/fixtures/unit/__init__.py`
- *... and 102 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (51 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (17 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (11 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (9 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (4 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (4 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 348 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*