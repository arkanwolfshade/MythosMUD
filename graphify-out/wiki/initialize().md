# .initialize()

> 178 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **main.py** (33 connections) — `server/container/main.py`
- **npc_database.py** (27 connections) — `server/npc_database.py`
- **PerformanceMonitor** (24 connections) — `server/monitoring/performance_monitor.py`
- **npc_instance_service.py** (23 connections) — `server/services/npc_instance_service.py`
- **get_npc_session()** (22 connections) — `server/npc_database.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **npc_startup_service.py** (16 connections) — `server/services/npc_startup_service.py`
- **migrate_combat_data.py** (15 connections) — `server/scripts/migrate_combat_data.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **npc.py** (14 connections) — `server/container/bundles/npc.py`
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **_initialize_npc_database()** (12 connections) — `server/npc_database.py`
- **monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **NPCBundle** (11 connections) — `server/container/bundles/npc.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **get_npc_database_path()** (11 connections) — `server/npc_database.py`
- *... and 153 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (66 shared connections)
- [Any](Any.md) (44 shared connections)
- [. init ()](_init_%28%29.md) (40 shared connections)
- [.shutdown()](shutdown%28%29.md) (25 shared connections)
- [.initialize()](initialize%28%29.md) (17 shared connections)
- [. repr ()](_repr_%28%29.md) (16 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (11 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (10 shared connections)
- [lifespan](lifespan.md) (6 shared connections)
- [.get instance()](get_instance%28%29.md) (6 shared connections)
- [get item prototype count()](get_item_prototype_count%28%29.md) (5 shared connections)
- [Request](Request.md) (5 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/database.py`
- `server/monitoring/performance_monitor.py`
- `server/npc_database.py`
- `server/scripts/migrate_combat_data.py`
- `server/services/npc_instance_service.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_service/queries.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/infrastructure/test_npc_database.py`

## Audit Trail

- EXTRACTED: 795 (93%)
- INFERRED: 60 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*