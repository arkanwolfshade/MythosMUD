# Client Event Store

> 841 nodes

## Key Concepts

- **get_logger()** (510 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (484 connections) — `server/structured_logging/enhanced_logging_config.py`
- **EventBus** (129 connections) — `server/events/event_bus.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **async_persistence.py** (74 connections) — `server/async_persistence.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- **npc_base.py** (41 connections) — `server/npc/npc_base.py`
- **npc.py** (37 connections) — `server/models/npc.py`
- **npc_instance_service.py** (32 connections) — `server/services/npc_instance_service.py`
- **event_bus.py** (29 connections) — `server/events/event_bus.py`
- **PlayerDeathService** (29 connections) — `server/services/player_death_service.py`
- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **NPCDied** (25 connections) — `server/events/event_types.py`
- **NPCThreadManager** (25 connections) — `server/npc/threading.py`
- *... and 816 more nodes in this community*

## Relationships

- [Commands Look Item](Commands_Look_Item.md) (116 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (92 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (63 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (54 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (53 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (46 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (44 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (39 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (38 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (34 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (34 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (32 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `scripts/run_test_ci.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/async_persistence.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/combat_handler.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`

## Audit Trail

- EXTRACTED: 4983 (96%)
- INFERRED: 234 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*