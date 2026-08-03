# command inventory models

> 597 nodes

## Key Concepts

- **ValidationError** (541 connections) — `server/exceptions.py`
- **PlayerService** (140 connections) — `server/game/player_service.py`
- **test_command_inventory.py** (63 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_command_factories_inventory.py** (48 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_player_service_mutations.py** (34 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **player_respawn.py** (24 connections) — `server/api/player_respawn.py`
- **get_npc_session()** (24 connections) — `server/npc_database.py`
- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **test_npc_database.py** (22 connections) — `server/tests/unit/infrastructure/test_npc_database.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **UUID** (14 connections)
- **get_npc_engine()** (14 connections) — `server/npc_database.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **command_inventory.py** (13 connections) — `server/models/command_inventory.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- *... and 572 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (91 shared connections)
- [command factories create](command_factories_create.md) (79 shared connections)
- [Database Config](Database_Config.md) (67 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (54 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (43 shared connections)
- [command communication models](command_communication_models.md) (31 shared connections)
- [Exception Containers](Exception_Containers.md) (30 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (28 shared connections)
- [command models moderation](command_models_moderation.md) (20 shared connections)
- [game models player](game_models_player.md) (20 shared connections)
- [game models stats](game_models_stats.md) (18 shared connections)
- [Inventory Equip](Inventory_Equip.md) (14 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/character_creation_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_service.py`
- `server/models/command_inventory.py`
- `server/npc_database.py`
- `server/schemas/players/player_respawn.py`
- `server/scripts/migrate_combat_data.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/infrastructure/test_npc_database.py`
- `server/tests/unit/models/test_command_inventory.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 1952 (76%)
- INFERRED: 605 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*