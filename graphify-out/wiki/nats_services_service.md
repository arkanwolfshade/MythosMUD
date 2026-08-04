# nats services service

> 280 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **.get_instance()** (35 connections) — `server/container/main.py`
- **main.py** (34 connections) — `server/container/main.py`
- **CombatBundle** (28 connections) — `server/container/bundles/combat.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **RealtimeBundle** (25 connections) — `server/container/bundles/realtime.py`
- **MagicBundle** (22 connections) — `server/container/bundles/magic.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **NPCBundle** (16 connections) — `server/container/bundles/npc.py`
- **SpellRepository** (16 connections) — `server/persistence/repositories/spell_repository.py`
- **_create_registry_and_targeting()** (15 connections) — `server/container/bundles/magic.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **combat.py** (14 connections) — `server/container/bundles/combat.py`
- **FastAPI** (13 connections)
- **realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- *... and 255 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (44 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (38 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (32 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (26 shared connections)
- [models npc rationale](models_npc_rationale.md) (24 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (22 shared connections)
- [combat models rationale](combat_models_rationale.md) (12 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (8 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (7 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/persistence/repositories/spell_repository.py`
- `server/services/player_death_service.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/fixtures/unit/mock_helpers.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 1327 (94%)
- INFERRED: 81 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*