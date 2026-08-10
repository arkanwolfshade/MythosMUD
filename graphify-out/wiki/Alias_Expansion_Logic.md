# Alias Expansion Logic

> 74 nodes

## Key Concepts

- **Alias** (52 connections) — `server/models/alias.py`
- **test_alias.py** (29 connections) — `server/tests/unit/models/test_alias.py`
- **.model_dump()** (4 connections) — `server/models/alias.py`
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
- *... and 49 more nodes in this community*

## Relationships

- [Alias Command Models](Alias_Command_Models.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Alias Storage Services](Alias_Storage_Services.md) (3 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (2 shared connections)
- [sample_alias](sample_alias.md) (1 shared connections)
- [test_add_alias_updates_existing](test_add_alias_updates_existing.md) (1 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (1 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`

## Audit Trail

- EXTRACTED: 210 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*