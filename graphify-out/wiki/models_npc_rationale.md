# models npc rationale

> 599 nodes

## Key Concepts

- **get_logger()** (516 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (489 connections) — `server/structured_logging/enhanced_logging_config.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **time.py** (96 connections) — `server/container/bundles/time.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **threading.py** (48 connections) — `server/npc/threading.py`
- **NPCCombatDataProvider** (39 connections) — `server/services/npc_combat_data_provider.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **time_service.py** (26 connections) — `server/time/time_service.py`
- **game.py** (25 connections) — `server/api/game.py`
- **MemoryThresholdMonitor** (25 connections) — `server/app/memory_cleanup_service.py`
- **test_hallucination_services.py** (23 connections) — `server/tests/unit/services/test_hallucination_services.py`
- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_memory_cleanup_service.py** (20 connections) — `server/tests/unit/app/test_memory_cleanup_service.py`
- **lifecycle_periodic.py** (19 connections) — `server/npc/lifecycle_periodic.py`
- **argon2_utils.py** (18 connections) — `server/auth/argon2_utils.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- *... and 574 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (91 shared connections)
- [NPC Combat](NPC_Combat.md) (66 shared connections)
- [combat commands handler](combat_commands_handler.md) (47 shared connections)
- [combat services messaging](combat_services_messaging.md) (42 shared connections)
- [command inventory factories](command_inventory_factories.md) (35 shared connections)
- [Error Conversion](Error_Conversion.md) (33 shared connections)
- [Database Config](Database_Config.md) (32 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (31 shared connections)
- [player service game](player_service_game.md) (27 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (27 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (25 shared connections)
- [admin auth service](admin_auth_service.md) (24 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/__init__.py`
- `server/api/base.py`
- `server/api/containers.py`
- `server/api/game.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/command_handler/processing.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/shutdown_process_termination.py`
- `server/commands/time_commands.py`
- `server/config/__init__.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/game/chat_pose_manager.py`
- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 3740 (98%)
- INFERRED: 87 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*