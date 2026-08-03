# Error Conversion

> 215 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (50 connections) — `server/container/bundles/game.py`
- **.get_instance()** (35 connections) — `server/container/main.py`
- **main.py** (34 connections) — `server/container/main.py`
- **CombatBundle** (28 connections) — `server/container/bundles/combat.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **RealtimeBundle** (25 connections) — `server/container/bundles/realtime.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **NPCBundle** (16 connections) — `server/container/bundles/npc.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **utils.py** (8 connections) — `server/container/utils.py`
- **__init__.py** (8 connections) — `server/tests/fixtures/unit/__init__.py`
- **__init__.py** (7 connections) — `server/container/__init__.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- *... and 190 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (34 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (27 shared connections)
- [holiday service services](holiday_service_services.md) (19 shared connections)
- [NPC Combat](NPC_Combat.md) (16 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (16 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (15 shared connections)
- [time service rationale](time_service_rationale.md) (9 shared connections)
- [event publisher realtime](event_publisher_realtime.md) (7 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (5 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/services/combat_cleanup_handler.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 951 (92%)
- INFERRED: 81 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*