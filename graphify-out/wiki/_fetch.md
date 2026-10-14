# ._fetch

> 15 nodes

## Key Concepts

- **._fetch()** (8 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **_row_to_alias()** (6 connections) — `server/alias_storage.py`
- **.get_player_aliases()** (5 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.validate_alias_command()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_name()** (3 connections) — `server/alias_storage.py`
- **test_row_to_alias_stores_naive_utc()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **SimpleNamespace** (2 connections)
- **Validate alias name format.** (1 connections) — `server/alias_storage.py`
- **Validate alias command.** (1 connections) — `server/alias_storage.py`
- **Run a row-returning alias function; None on database error.** (1 connections) — `server/alias_storage.py`
- **Get all aliases for a player (empty on unknown player or DB error).** (1 connections) — `server/alias_storage.py`
- **Get a specific alias for a player (case-insensitive name match).** (1 connections) — `server/alias_storage.py`
- **Create (or replace the command of) an alias; None if invalid, over the limit,…** (1 connections) — `server/alias_storage.py`

## Relationships

- [AliasStorage](AliasStorage.md) (6 shared connections)
- [Alias](Alias.md) (5 shared connections)
- [test_alias_storage.py](test_alias_storage.py.md) (3 shared connections)
- [alias_storage.py](alias_storage.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*