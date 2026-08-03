# services admin auth

> 15 nodes

## Key Concepts

- **._get_alias_file_path()** (8 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **Path** (4 connections)
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **Any** (3 connections)
- **.delete_player_aliases()** (3 connections) — `server/alias_storage.py`
- **.__init__()** (2 connections) — `server/alias_storage.py`
- **Get the file path for a player's aliases.          Human: reject path separators** (1 connections) — `server/alias_storage.py`
- **Load alias data from JSON file.** (1 connections) — `server/alias_storage.py`
- **Save alias data to JSON file.** (1 connections) — `server/alias_storage.py`
- **Delete a player's alias file.** (1 connections) — `server/alias_storage.py`
- **Create a backup of a player's aliases.** (1 connections) — `server/alias_storage.py`
- **Validate alias payload against the shared schema when available.          Args:** (1 connections) — `server/alias_storage.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (8 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (2 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*