# server app lifespan startup legacy

> 108 nodes

## Key Concepts

- **ApplicationContainer** (166 connections) — `server/container/main.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **peek_application_container()** (6 connections) — `server/container/main.py`
- **_container_instance()** (6 connections) — `server/realtime/memory_monitor.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **PlayerLifecycleServices** (5 connections) — `server/services/combat_service_types.py`
- **.initialize()** (5 connections) — `server/container/bundles/time.py`
- **.initialize()** (5 connections) — `server/container/main.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_legacy_service_bindings()** (4 connections) — `server/app/lifespan_startup.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **._start_nats_message_handler()** (4 connections) — `server/container/bundles/combat.py`
- **._validate_nats_combat_prerequisites()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 83 more nodes in this community*

## Relationships

- [server container bundles chat](server_container_bundles_chat.md) (45 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (14 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (12 shared connections)
- [memorymonitor](memorymonitor.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server container main get container](server_container_main_get_container.md) (9 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (6 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (6 shared connections)
- [server app lifespan](server_app_lifespan.md) (5 shared connections)
- [server events combat events](server_events_combat_events.md) (5 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (5 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/realtime/memory_monitor.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 319 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*