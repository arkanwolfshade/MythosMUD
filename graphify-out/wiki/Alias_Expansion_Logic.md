# Alias Expansion Logic

> 81 nodes

## Key Concepts

- **Alias** (52 connections) — `server/models/alias.py`
- **test_alias.py** (29 connections) — `server/tests/unit/models/test_alias.py`
- **alias.py** (6 connections) — `server/models/alias.py`
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
- *... and 56 more nodes in this community*

## Relationships

- [Alias Storage Services](Alias_Storage_Services.md) (6 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (1 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`
- `server/tests/unit/test_alias_storage.py`

## Audit Trail

- EXTRACTED: 228 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*