# server container bundles chat

> 177 nodes

## Key Concepts

- **ApplicationContainer** (154 connections) — `server/container/main.py`
- **test_container_bundles.py** (65 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (54 connections) — `server/container/bundles/game.py`
- **container/main.py** (35 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (23 connections)
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **NPCBundle** (19 connections) — `server/container/bundles/npc.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **bundles/npc.py** (15 connections) — `server/container/bundles/npc.py`
- **bundles/realtime.py** (15 connections) — `server/container/bundles/realtime.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **bundles/monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **test_realtime_bundle_nats.py** (11 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- *... and 152 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (28 shared connections)
- [server container main applicationcontainer reset](server_container_main_applicationcontainer_reset.md) (25 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (19 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (18 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (13 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (11 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (9 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (6 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (6 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (5 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (5 shared connections)
- [server container bundles realtime py](server_container_bundles_realtime_py.md) (5 shared connections)

## Source Files

- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/container/test_time_bundle.py`

## Audit Trail

- EXTRACTED: 560 (81%)
- INFERRED: 130 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*