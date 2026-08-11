# Async Persistence Types

> 117 nodes

## Key Concepts

- **SchemaValidator** (29 connections) — `schemas/validator.py`
- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **handle_emote_command()** (15 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (14 connections) — `server/commands/emote_commands.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **._get_alias_file_path()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **_get_emote_services()** (7 connections) — `server/commands/emote_commands.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **test_emote_commands.py** (6 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Path** (5 connections)
- **Any** (5 connections)
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- *... and 92 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (27 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (11 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (5 shared connections)
- [Room Schema Validator](Room_Schema_Validator.md) (4 shared connections)
- [Status Command Handlers](Status_Command_Handlers.md) (4 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (3 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (3 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (3 shared connections)
- [Legacy Cleanup Summary](Legacy_Cleanup_Summary.md) (3 shared connections)
- [Alias Storage Services](Alias_Storage_Services.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (2 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/commands/emote_commands.py`
- `server/commands/utility_commands.py`
- `server/game/emote_service.py`
- `server/tests/unit/commands/test_emote_commands.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 387 (95%)
- INFERRED: 21 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*