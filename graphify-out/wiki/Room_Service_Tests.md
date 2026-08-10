# Room Service Tests

> 325 nodes

## Key Concepts

- **ValidationError** (540 connections) — `server/exceptions.py`
- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **CommunicationCommandFactory** (15 connections) — `server/utils/command_factories_communication.py`
- **player_requests.py** (14 connections) — `server/schemas/players/player_requests.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **apply_lucidity_loss()** (12 connections) — `server/api/player_effects.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **MeCommand** (12 connections) — `server/models/command_communication.py`
- **EffectResponse** (12 connections) — `server/schemas/players/player_effects.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **apply_fear()** (11 connections) — `server/api/player_effects.py`
- **apply_corruption()** (11 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (11 connections) — `server/api/player_effects.py`
- **heal_player()** (11 connections) — `server/api/player_effects.py`
- **damage_player()** (11 connections) — `server/api/player_effects.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **BaseModel** (11 connections)
- *... and 300 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (71 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (61 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (44 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (34 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (31 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (30 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (21 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (18 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (15 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (14 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (14 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (13 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/api/player_respawn.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/game/profession_service.py`
- `server/models/command_channel.py`
- `server/models/command_communication.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_utility.py`

## Audit Trail

- EXTRACTED: 1250 (72%)
- INFERRED: 497 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*