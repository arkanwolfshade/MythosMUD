# Game Service Bundle

> 950 nodes

## Key Concepts

- **get_logger()** (507 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (481 connections) — `server/structured_logging/enhanced_logging_config.py`
- **exceptions.py** (195 connections) — `server/exceptions.py`
- **command.py** (96 connections) — `server/models/command.py`
- **database.py** (79 connections) — `server/database.py`
- **async_persistence.py** (74 connections) — `server/async_persistence.py`
- **ExplorationService** (73 connections) — `server/services/exploration_service.py`
- **maps.py** (63 connections) — `server/api/maps.py`
- **test_container_persistence.py** (61 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **user.py** (56 connections) — `server/models/user.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **users.py** (46 connections) — `server/auth/users.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **game.py** (42 connections) — `server/container/bundles/game.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **factory.py** (37 connections) — `server/app/factory.py`
- **rooms.py** (35 connections) — `server/api/rooms.py`
- **main.py** (33 connections) — `server/container/main.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **_parse_jsonb_column()** (28 connections) — `server/container_persistence/container_persistence.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **subject_controller.py** (27 connections) — `server/api/admin/subject_controller.py`
- **npc_database.py** (27 connections) — `server/npc_database.py`
- *... and 925 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (207 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (111 shared connections)
- [Client Event Store](Client_Event_Store.md) (89 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (80 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (74 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (68 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (61 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (59 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (54 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (43 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (37 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (30 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/api/__init__.py`
- `server/api/admin/__init__.py`
- `server/api/admin/subject_controller.py`
- `server/api/base.py`
- `server/api/containers.py`
- `server/api/game.py`
- `server/api/maps.py`
- `server/api/player_helpers.py`
- `server/api/professions.py`
- `server/api/rooms.py`
- `server/api/skills.py`
- `server/app/factory.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`

## Audit Trail

- EXTRACTED: 5782 (96%)
- INFERRED: 215 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*