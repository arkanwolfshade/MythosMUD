# Alias Storage Services

> 100 nodes

## Key Concepts

- **test_alias_storage.py** (65 connections) — `server/tests/unit/test_alias_storage.py`
- **sample_alias2()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_storage_dir()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_with_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_init_without_env_var()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_alias_storage_creates_directory()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_case_insensitive()** (3 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_file_path()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_nonexistent_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_existing_file()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_invalid_json()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_load_alias_data_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_success()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_alias_data_io_error()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_empty()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_with_aliases()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_with_timestamps()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_player_aliases_invalid_alias_data()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_save_player_aliases()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_add_alias_new()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_existing()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_nonexistent()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_remove_alias_case_insensitive()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_existing()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- **test_get_alias_nonexistent()** (2 connections) — `server/tests/unit/test_alias_storage.py`
- *... and 75 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Commands Container Inventory](Commands_Container_Inventory.md) (5 shared connections)
- [E 2 E Ai Execution](E_2_E_Ai_Execution.md) (4 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [sample_alias](sample_alias.md) (1 shared connections)
- [test_add_alias_updates_existing](test_add_alias_updates_existing.md) (1 shared connections)

## Source Files

- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 219 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*