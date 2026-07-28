# Api Player Respawn

> 222 nodes · cohesion 0.01

## Key Concepts

- **ValidationError** (537 connections) — `server/exceptions.py`
- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **player_respawn.py** (24 connections) — `server/api/player_respawn.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **MythosValidationError** (8 connections)
- **RespawnResponse** (8 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **test_enhanced_error_logging.py** (7 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_handle_delirium_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_lucidity_keyword()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_must_be_delirious()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_delirium_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_generic_500()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_must_be_dead()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **test_handle_respawn_validation_not_found()** (5 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- *... and 197 more nodes in this community*

## Relationships

- [Admin Command Models](Admin_Command_Models.md) (117 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (45 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (31 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (30 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (30 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (29 shared connections)
- [Look Container Command](Look_Container_Command.md) (24 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (20 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (16 shared connections)
- [Player Preferences Service](Player_Preferences_Service.md) (14 shared connections)
- [API Test Fixtures](API_Test_Fixtures.md) (13 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (12 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/exceptions.py`
- `server/models/command_communication.py`
- `server/models/command_magic.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/models/test_command_magic.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 774 (61%)
- INFERRED: 485 (39%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*