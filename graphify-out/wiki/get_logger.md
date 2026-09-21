# get_logger

> 705 nodes

## Key Concepts

- **get_logger()** (544 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (519 connections) — `server/structured_logging/enhanced_logging_config.py`
- **server/exceptions.py** (250 connections) — `server/exceptions.py`
- **get_config()** (113 connections) — `server/config/__init__.py`
- **log_and_raise_enhanced()** (106 connections) — `server/utils/enhanced_error_logging.py`
- **combat_service.py** (105 connections) — `server/services/combat_service.py`
- **alias_storage.py** (79 connections) — `server/alias_storage.py`
- **models/combat.py** (61 connections) — `server/models/combat.py`
- **player_service.py** (50 connections) — `server/game/player_service.py`
- **command_parser.py** (49 connections) — `server/utils/command_parser.py`
- **CombatParticipantType** (47 connections) — `server/models/combat.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **threading.py** (45 connections) — `server/npc/threading.py`
- **event_bus.py** (40 connections) — `server/events/event_bus.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **security_validator.py** (38 connections) — `server/validators/security_validator.py`
- **AppConfig** (35 connections) — `server/config/models/app.py`
- **disconnect_grace_period.py** (35 connections) — `server/realtime/disconnect_grace_period.py`
- **player_combat_service.py** (32 connections) — `server/services/player_combat_service.py`
- **game_tick_protocols.py** (31 connections) — `server/app/game_tick_protocols.py`
- **server/config/__init__.py** (29 connections) — `server/config/__init__.py`
- **api/player_respawn.py** (28 connections) — `server/api/player_respawn.py`
- **target_resolution_service.py** (28 connections) — `server/services/target_resolution_service.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- *... and 680 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (101 shared connections)
- [DatabaseError](DatabaseError.md) (73 shared connections)
- [connection_manager.py](connection_manager.py.md) (70 shared connections)
- [NPCDefinition](NPCDefinition.md) (64 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (51 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (47 shared connections)
- [CombatInstance](CombatInstance.md) (46 shared connections)
- [PlayerService](PlayerService.md) (42 shared connections)
- [ValidationError](ValidationError.md) (40 shared connections)
- [CombatService](CombatService.md) (36 shared connections)
- [CombatParticipant](CombatParticipant.md) (35 shared connections)
- [test_config_models.py](test_config_models.py.md) (32 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `schemas/validator.py`
- `server/alias_storage.py`
- `server/api/player_respawn.py`
- `server/app/game_tick_protocols.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/tracked_task_manager.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler/processing.py`
- `server/commands/admin_permission_utils.py`
- `server/commands/combat_handler.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/shutdown_process_termination.py`

## Audit Trail

- EXTRACTED: 4069 (98%)
- INFERRED: 63 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*