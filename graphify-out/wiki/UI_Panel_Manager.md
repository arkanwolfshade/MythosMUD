# UI Panel Manager

> 77 nodes · cohesion 0.03

## Key Concepts

- **Alias** (52 connections) — `server/models/alias.py`
- **test_alias.py** (29 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_default_id()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_default_timestamps()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_default_version()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_different_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_different_ids()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_different_name()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_same_name_and_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_equality_with_non_alias()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_get_expanded_command_no_args()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_get_expanded_command_with_args()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_different_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_different_name()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_same_name_and_command()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_hash_usable_in_set()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_case_insensitive()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_false()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_true()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_model_dump()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_model_dump_timestamps_isoformat()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_repr()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_update_timestamp()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_validate_name_empty()** (3 connections) — `server/tests/unit/models/test_alias.py`
- *... and 52 more nodes in this community*

## Relationships

- [Alias Storage Layer](Alias_Storage_Layer.md) (7 shared connections)
- [Server Config Loading](Server_Config_Loading.md) (5 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (3 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (1 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 219 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*