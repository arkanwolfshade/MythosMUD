# rescue service services

> 20 nodes

## Key Concepts

- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- **.get_alias_file_path()** (7 connections) — `server/alias_storage.py`
- **._save_alias_data()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **Path** (6 connections)
- **AliasPayload** (5 connections)
- **._resolved_alias_open_path()** (5 connections) — `server/alias_storage.py`
- **_as_alias_payload()** (4 connections) — `server/alias_storage.py`
- **.backup_aliases()** (4 connections) — `server/alias_storage.py`
- **_empty_alias_payload()** (3 connections) — `server/alias_storage.py`
- **.delete_player_aliases()** (3 connections) — `server/alias_storage.py`
- **.__init__()** (2 connections) — `server/alias_storage.py`
- **Narrow json.load output to a string-keyed object map.** (1 connections) — `server/alias_storage.py`
- **Get the file path for a player's aliases.          Human: reject path separators** (1 connections) — `server/alias_storage.py`
- **Absolute str path for open(); re-checks containment at the open site.          H** (1 connections) — `server/alias_storage.py`
- **Load alias data from JSON file.** (1 connections) — `server/alias_storage.py`
- **Save alias data to JSON file.** (1 connections) — `server/alias_storage.py`
- **Delete a player's alias file.** (1 connections) — `server/alias_storage.py`
- **Create a backup of a player's aliases.** (1 connections) — `server/alias_storage.py`
- **Validate alias payload against the shared schema when available.          Args:** (1 connections) — `server/alias_storage.py`

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (8 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [alias models rationale](alias_models_rationale.md) (2 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`

## Audit Trail

- EXTRACTED: 70 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*