# Loot Generation

> 250 nodes

## Key Concepts

- **ValidationError** (582 connections) — `server/exceptions.py`
- **exceptions.py** (238 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **command_parser.py** (46 connections) — `server/utils/command_parser.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **processing.py** (26 connections) — `server/command_handler/processing.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **PlayerStateCommandFactory** (18 connections) — `server/utils/command_factories_player_state.py`
- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **player_respawn_wrapper.py** (15 connections) — `server/game/player_respawn_wrapper.py`
- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **test_player_respawn_wrapper.py** (13 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **command_processor.py** (13 connections) — `server/utils/command_processor.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_exploration.py** (11 connections) — `server/utils/command_factories_exploration.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- *... and 225 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (59 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (50 shared connections)
- [command inventory models](command_inventory_models.md) (47 shared connections)
- [Exception Containers](Exception_Containers.md) (35 shared connections)
- [Spell Validation](Spell_Validation.md) (32 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (32 shared connections)
- [command factories create](command_factories_create.md) (31 shared connections)
- [Inventory Equip](Inventory_Equip.md) (27 shared connections)
- [services chat logger](services_chat_logger.md) (26 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (24 shared connections)
- [npc commands admin](npc_commands_admin.md) (24 shared connections)
- [npc combat service](npc_combat_service.md) (23 shared connections)

## Source Files

- `server/command_handler/processing.py`
- `server/exceptions.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 1375 (73%)
- INFERRED: 498 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*