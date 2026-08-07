# nats services service

> 240 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (50 connections) — `server/container/bundles/game.py`
- **.get_instance()** (35 connections) — `server/container/main.py`
- **main.py** (34 connections) — `server/container/main.py`
- **CombatBundle** (28 connections) — `server/container/bundles/combat.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **RealtimeBundle** (25 connections) — `server/container/bundles/realtime.py`
- **MagicBundle** (22 connections) — `server/container/bundles/magic.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **NPCBundle** (16 connections) — `server/container/bundles/npc.py`
- **_create_registry_and_targeting()** (15 connections) — `server/container/bundles/magic.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **npc.py** (15 connections) — `server/container/bundles/npc.py`
- **combat.py** (14 connections) — `server/container/bundles/combat.py`
- **realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- *... and 215 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (34 shared connections)
- [combat models rationale](combat_models_rationale.md) (21 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (21 shared connections)
- [aggro threat services](aggro_threat_services.md) (21 shared connections)
- [Error Conversion](Error_Conversion.md) (12 shared connections)
- [rate limiter services](rate_limiter_services.md) (9 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (8 shared connections)
- [quest chat game](quest_chat_game.md) (7 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (5 shared connections)
- [player service game](player_service_game.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (5 shared connections)

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
- `server/game/chat_npc_system.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 1110 (92%)
- INFERRED: 93 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*