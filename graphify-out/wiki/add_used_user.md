# add used user

> 321 nodes

## Key Concepts

- **ValidationError** (582 connections) — `server/exceptions.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **test_player_service_mutations.py** (34 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_mechanics.py** (16 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **player_respawn_wrapper.py** (15 connections) — `server/game/player_respawn_wrapper.py`
- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **mechanics.py** (13 connections) — `server/game/mechanics.py`
- **test_player_respawn_wrapper.py** (13 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (9 connections) — `server/game/player_creation_service.py`
- **.create_player()** (8 connections) — `server/game/player_creation_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.load_container_from_room_json()** (8 connections) — `server/services/environmental_container_loader.py`
- *... and 296 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (86 shared connections)
- [Inventory Equip](Inventory_Equip.md) (52 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (39 shared connections)
- [command communication models](command_communication_models.md) (34 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (28 shared connections)
- [command inventory models](command_inventory_models.md) (28 shared connections)
- [health models rationale](health_models_rationale.md) (26 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (24 shared connections)
- [npc commands admin](npc_commands_admin.md) (24 shared connections)
- [player service game](player_service_game.md) (21 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (21 shared connections)
- [Error Conversion](Error_Conversion.md) (18 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/npc/combat_integration.py`
- `server/persistence/repositories/experience_repository.py`
- `server/services/environmental_container_loader.py`
- `server/tests/unit/game/test_mechanics.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 1159 (68%)
- INFERRED: 538 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*