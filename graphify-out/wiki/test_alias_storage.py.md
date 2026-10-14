# test_alias_storage.py

> 22 nodes

## Key Concepts

- **test_alias_storage.py** (19 connections) — `server/tests/unit/test_alias_storage.py`
- **_Session** (13 connections) — `server/tests/unit/test_alias_storage.py`
- **_use_session()** (8 connections) — `server/tests/unit/test_alias_storage.py`
- **MonkeyPatch** (8 connections)
- **test_create_alias_refused_at_limit()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_upserts_and_commits()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_calls_procedure_and_maps_row()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_returns_procedure_result()** (7 connections) — `server/tests/unit/test_alias_storage.py`
- **asyncio** (7 connections)
- **test_delete_player_aliases_by_id_binds_player_id()** (6 connections) — `server/tests/unit/test_alias_storage.py`
- **_alias_row()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_create_alias_rejects_invalid_input_without_touching_db()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **test_database_errors_degrade_to_no_alias()** (5 connections) — `server/tests/unit/test_alias_storage.py`
- **_broken_session_maker()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_command()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_validate_alias_name()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **parametrize** (3 connections)
- **.__aenter__()** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **.__aexit__()** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **.commit()** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Unit tests for AliasStorage (#680): validation, row mapping, and DB-failure…** (1 connections) — `server/tests/unit/test_alias_storage.py`
- **Just enough AsyncSession for AliasStorage: execute, commit, async context…** (1 connections) — `server/tests/unit/test_alias_storage.py`

## Relationships

- [AliasStorage](AliasStorage.md) (10 shared connections)
- [_Result](_Result.md) (3 shared connections)
- [._fetch](_fetch.md) (3 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 58 (84%)
- INFERRED: 11 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*