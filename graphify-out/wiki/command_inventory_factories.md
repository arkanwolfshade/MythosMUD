# command inventory factories

> 630 nodes

## Key Concepts

- **ValidationError** (541 connections) — `server/exceptions.py`
- **exceptions.py** (198 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **error_logging.py** (56 connections) — `server/utils/error_logging.py`
- **test_command_factories_exploration.py** (48 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_command_factories_inventory.py** (48 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **emote_service.py** (19 connections) — `server/game/emote_service.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **PlayerStateCommandFactory** (18 connections) — `server/utils/command_factories_player_state.py`
- **ExplorationCommandFactory** (17 connections) — `server/utils/command_factories_exploration.py`
- **InventoryCommandFactory** (16 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **CommunicationCommandFactory** (15 connections) — `server/utils/command_factories_communication.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **UUID** (14 connections)
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- *... and 605 more nodes in this community*

## Relationships

- [Database Access Layer](Database_Access_Layer.md) (85 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (80 shared connections)
- [NATS Messaging](NATS_Messaging.md) (45 shared connections)
- [command utility models](command_utility_models.md) (42 shared connections)
- [Exception Containers](Exception_Containers.md) (33 shared connections)
- [command models admin](command_models_admin.md) (33 shared connections)
- [command inventory models](command_inventory_models.md) (30 shared connections)
- [command communication models](command_communication_models.md) (25 shared connections)
- [Player Stats](Player_Stats.md) (21 shared connections)
- [persistence container item](persistence_container_item.md) (19 shared connections)
- [npc populate databases](npc_populate_databases.md) (17 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (17 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_exploration.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 2494 (82%)
- INFERRED: 557 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*