# Server Config Loading

> 65 nodes · cohesion 0.03

## Key Concepts

- **SchemaValidator** (29 connections) — `schemas/validator.py`
- **emote_service.py** (19 connections) — `server/game/emote_service.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **._get_alias_file_path()** (8 connections) — `server/alias_storage.py`
- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **_get_alias_validator()** (8 connections) — `server/alias_storage.py`
- **schema_validator.py** (8 connections) — `tools/room_toolkit/room_validator/core/schema_validator.py`
- **validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **Path** (5 connections)
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- *... and 40 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (22 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (6 shared connections)
- [UI Panel Manager](UI_Panel_Manager.md) (5 shared connections)
- [Edge Creation Modal](Edge_Creation_Modal.md) (4 shared connections)
- [Room Schema Validator](Room_Schema_Validator.md) (4 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Room Fixer Toolkit](Room_Fixer_Toolkit.md) (2 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (1 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/game/emote_service.py`
- `server/tests/unit/test_alias_storage.py`
- `tools/room_toolkit/room_validator/core/schema_validator.py`

## Audit Trail

- EXTRACTED: 261 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*