# ApplicationContainer

> 112 nodes

## Key Concepts

- **ApplicationContainer** (163 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (25 connections) — `server/container/main.py`
- **get_container()** (21 connections) — `server/container/main.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **PlayerLifecycleServices** (5 connections) — `server/services/combat_service_types.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 87 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (47 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (21 shared connections)
- [SpellEffects](SpellEffects.md) (10 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (6 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (3 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 322 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*