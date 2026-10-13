# Schema Validation & Channels

> 490 nodes

## Key Concepts

- **ValidationError** (327 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (112 connections) — `server/utils/enhanced_error_logging.py`
- **InventoryCommandFactory** (98 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (70 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **PlayerStateCommandFactory** (43 connections) — `server/utils/command_factories_player_state.py`
- **CommunicationCommandFactory** (42 connections) — `server/utils/command_factories_communication.py`
- **enhanced_error_logging.py** (37 connections) — `server/utils/enhanced_error_logging.py`
- **test_command_factories_communication.py** (31 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_player_state.py** (31 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_enhanced_error_logging.py** (27 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **.create_get_command()** (20 connections) — `server/utils/command_factories_inventory.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **PlayerRespawnWrapper** (18 connections) — `server/game/player_respawn_wrapper.py`
- **command_factories.py** (18 connections) — `server/utils/command_factories.py`
- **command_factories_inventory.py** (17 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **world_loader.py** (13 connections) — `server/world_loader.py`
- **create_validator()** (12 connections) — `schemas/validator.py`
- *... and 465 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (50 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (35 shared connections)
- [Admin & Alias Commands](Admin_&_Alias_Commands.md) (34 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (27 shared connections)
- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (26 shared connections)
- [Community 72](Community_72.md) (25 shared connections)
- [Assist Wiring Tests](Assist_Wiring_Tests.md) (24 shared connections)
- [API Response Models](API_Response_Models.md) (21 shared connections)
- [Community 268](Community_268.md) (21 shared connections)
- [Inventory Commands](Inventory_Commands.md) (20 shared connections)
- [Channel Commands](Channel_Commands.md) (19 shared connections)
- [Base Command Models](Base_Command_Models.md) (15 shared connections)

## Source Files

- `schemas/validator.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 1109 (76%)
- INFERRED: 356 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*