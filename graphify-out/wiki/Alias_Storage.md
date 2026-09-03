# Alias Storage

> 85 nodes

## Key Concepts

- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **SchemaValidator** (21 connections) — `schemas/validator.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (9 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **alias_graph.py** (8 connections) — `server/utils/alias_graph.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **schemas/validator.py** (7 connections) — `schemas/validator.py`
- **Any** (7 connections)
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **_apply_alias_timestamps()** (5 connections) — `server/alias_storage.py`
- **AliasPayload** (5 connections)
- **_AliasValidatorCache** (4 connections) — `server/alias_storage.py`
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- *... and 60 more nodes in this community*

## Relationships

- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (25 shared connections)
- [Command Aliases Storage](Command_Aliases_Storage.md) (8 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Emote Service](Emote_Service.md) (4 shared connections)
- [Alias Graph](Alias_Graph.md) (4 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (4 shared connections)
- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (4 shared connections)
- [Test Room Loader](Test_Room_Loader.md) (2 shared connections)
- [Test World Loader](Test_World_Loader.md) (2 shared connections)
- [Security Validators](Security_Validators.md) (2 shared connections)
- [Test Admin Commands](Test_Admin_Commands.md) (2 shared connections)
- [Inventory Drop Command](Inventory_Drop_Command.md) (2 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 223 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*