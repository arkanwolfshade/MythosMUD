# .get_player_aliases

> 40 nodes

## Key Concepts

- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (9 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **AliasPayload** (5 connections)
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias_count()** (4 connections) — `server/alias_storage.py`
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **_as_alias_payload()** (4 connections) — `server/alias_storage.py`
- **.clear_aliases()** (3 connections) — `server/alias_storage.py`
- **.delete_player_aliases()** (3 connections) — `server/alias_storage.py`
- **._resolved_alias_open_path()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_command()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_name()** (3 connections) — `server/alias_storage.py`
- **_empty_alias_payload()** (3 connections) — `server/alias_storage.py`
- **.__init__()** (2 connections) — `server/alias_storage.py`
- **Get the file path for a player's aliases. Human: reject path separators /…** (1 connections) — `server/alias_storage.py`
- **Absolute str path for open(); re-checks containment at the open site. Human:…** (1 connections) — `server/alias_storage.py`
- **Load alias data from JSON file.** (1 connections) — `server/alias_storage.py`
- *... and 15 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (18 shared connections)
- [Alias](Alias.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 80 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*