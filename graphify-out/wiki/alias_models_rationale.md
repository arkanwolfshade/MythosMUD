# alias models rationale

> 73 nodes

## Key Concepts

- **Alias** (71 connections) — `server/models/alias.py`
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
- *... and 48 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (31 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`

## Audit Trail

- EXTRACTED: 231 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*