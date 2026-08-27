# NATSMessageHandler

> 74 nodes

## Key Concepts

- **Alias** (70 connections) — `server/models/alias.py`
- **test_alias.py** (30 connections) — `server/tests/unit/models/test_alias.py`
- **.model_dump()** (3 connections) — `server/models/alias.py`
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
- **test_alias_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_repr()** (3 connections) — `server/tests/unit/models/test_alias.py`
- **test_alias_update_timestamp()** (3 connections) — `server/tests/unit/models/test_alias.py`
- *... and 49 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (28 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [bench_cache.py](bench_cache.py.md) (2 shared connections)

## Source Files

- `server/models/alias.py`
- `server/tests/unit/models/test_alias.py`

## Audit Trail

- EXTRACTED: 115 (86%)
- INFERRED: 19 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*