# Alias Expansion Logic

> 79 nodes

## Key Concepts

- **Alias** (52 connections) — `server/models/alias.py`
- **test_alias.py** (29 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_alias.py`
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
- **test_alias_is_reserved_command_case_insensitive()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_is_reserved_command_false()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_validate_name_valid()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_validate_name_with_whitespace()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_validate_name_empty()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_validate_name_whitespace_only()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_get_expanded_command_no_args()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_get_expanded_command_with_args()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_model_dump()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_model_dump_timestamps_isoformat()** (3 connections) — `server/tests/unit/models/test_alias.py`
- *... and 54 more nodes in this community*

## Relationships

- [Alias Storage Services](Alias_Storage_Services.md) (7 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (5 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (1 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 221 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*