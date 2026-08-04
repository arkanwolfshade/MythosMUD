# Loot Generation

> 699 nodes

## Key Concepts

- **get_logger()** (516 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (489 connections) — `server/structured_logging/enhanced_logging_config.py`
- **exceptions.py** (238 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **alias_storage.py** (67 connections) — `server/alias_storage.py`
- **error_logging.py** (56 connections) — `server/utils/error_logging.py`
- **command_parser.py** (46 connections) — `server/utils/command_parser.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **player_respawn.py** (25 connections) — `server/api/player_respawn.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (22 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **combat_integration_base.py** (21 connections) — `server/npc/combat_integration_base.py`
- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- *... and 674 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (141 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (112 shared connections)
- [models npc rationale](models_npc_rationale.md) (89 shared connections)
- [command factories create](command_factories_create.md) (55 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (47 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (41 shared connections)
- [command inventory models](command_inventory_models.md) (39 shared connections)
- [persistence container item](persistence_container_item.md) (37 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (32 shared connections)
- [task registry app](task_registry_app.md) (30 shared connections)
- [Inventory Equip](Inventory_Equip.md) (28 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (26 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/api/base.py`
- `server/api/player_helpers.py`
- `server/api/player_respawn.py`
- `server/api/professions.py`
- `server/async_persistence.py`
- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/command_handler/processing.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/system_commands.py`
- `server/commands/time_commands.py`
- `server/container/utils.py`
- `server/exceptions.py`
- `server/game/character_creation_service.py`
- `server/game/items/component_hooks.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 4457 (98%)
- INFERRED: 98 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*