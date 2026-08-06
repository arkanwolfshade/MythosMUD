# alias models rationale

> 95 nodes

## Key Concepts

- **Alias** (71 connections) — `server/models/alias.py`
- **test_alias.py** (29 connections) — `server/tests/unit/models/test_alias.py`
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **.remove_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias()** (4 connections) — `server/alias_storage.py`
- **.get_alias_count()** (4 connections) — `server/alias_storage.py`
- **test_alias_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_alias.py`
- **.clear_aliases()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_name()** (3 connections) — `server/alias_storage.py`
- **.validate_alias_command()** (3 connections) — `server/alias_storage.py`
- **test_alias_repr()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_same_name_and_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_different_ids()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_different_name()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_different_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_with_non_alias()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_same_name_and_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_different_name()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_different_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_usable_in_set()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_update_timestamp()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_true()** (3 connections) — `server/tests/unit/models/test_alias.py`
- *... and 70 more nodes in this community*

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (33 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (5 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (3 shared connections)
- [rescue service services](rescue_service_services.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)
- [add used user](add_used_user.md) (1 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 293 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*