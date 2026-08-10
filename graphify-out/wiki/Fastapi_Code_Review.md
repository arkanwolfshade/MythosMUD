# Fastapi Code Review

> 15 nodes

## Key Concepts

- **._get_alias_file_path()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **Path** (5 connections)
- **Any** (4 connections)
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **.delete_player_aliases()** (3 connections) — `server/alias_storage.py`
- **.__init__()** (2 connections) — `server/alias_storage.py`
- **Get the file path for a player's aliases.** (1 connections) — `server/alias_storage.py`
- **Load alias data from JSON file.** (1 connections) — `server/alias_storage.py`
- **Save alias data to JSON file.** (1 connections) — `server/alias_storage.py`
- **Delete a player's alias file.** (1 connections) — `server/alias_storage.py`
- **Create a backup of a player's aliases.** (1 connections) — `server/alias_storage.py`
- **Validate alias payload against the shared schema when available.          Args:** (1 connections) — `server/alias_storage.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (2 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (2 shared connections)
- [E 2 E Ai Execution](E_2_E_Ai_Execution.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*