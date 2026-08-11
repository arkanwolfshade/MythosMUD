# React Node Upgrade Summary

> 53 nodes

## Key Concepts

- **SchemaValidator** (29 connections) — `schemas/validator.py`
- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **Any** (7 connections)
- **._get_alias_file_path()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **.validate_data()** (6 connections) — `schemas/validator.py`
- **.validate_room()** (6 connections) — `schemas/validator.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Path** (5 connections)
- **.__init__()** (4 connections) — `schemas/validator.py`
- **.validate_room_file()** (4 connections) — `schemas/validator.py`
- **.validate_room_database()** (4 connections) — `schemas/validator.py`
- **.validate_alias_bundle()** (4 connections) — `schemas/validator.py`
- **.validate_emote_file()** (4 connections) — `schemas/validator.py`
- **Any** (4 connections)
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **._load_schema()** (3 connections) — `schemas/validator.py`
- **Path** (3 connections)
- **.get_exit_target()** (3 connections) — `schemas/validator.py`
- **.get_exit_flags()** (3 connections) — `schemas/validator.py`
- *... and 28 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (16 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Health Endpoint Spec](Health_Endpoint_Spec.md) (4 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (4 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (2 shared connections)
- [Room Schema Validator](Room_Schema_Validator.md) (2 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)
- [Room Fixer Toolkit](Room_Fixer_Toolkit.md) (1 shared connections)
- [Alias Storage Services](Alias_Storage_Services.md) (1 shared connections)

## Source Files

- `schemas/validator.py`
- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 169 (93%)
- INFERRED: 13 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*