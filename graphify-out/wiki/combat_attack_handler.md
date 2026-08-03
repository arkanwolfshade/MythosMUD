# combat attack handler

> 62 nodes

## Key Concepts

- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **SpellCommand** (13 connections) — `server/models/command_magic.py`
- **LearnCommand** (13 connections) — `server/models/command_magic.py`
- **command_magic.py** (10 connections) — `server/models/command_magic.py`
- **SpellsCommand** (8 connections) — `server/models/command_magic.py`
- **test_cast_command_validate_spell_name_empty()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_spell_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spell_command_validate_spell_name_empty()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spell_command_validate_spell_name_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spell_command_spell_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_learn_command_validate_spell_name_empty()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_learn_command_validate_spell_name_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_learn_command_spell_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_valid()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_target_empty_string()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_target_whitespace()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_target_strips()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spell_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spell_command_validate_spell_name_valid()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spells_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- *... and 37 more nodes in this community*

## Relationships

- [container persistence rationale](container_persistence_rationale.md) (11 shared connections)
- [command inventory models](command_inventory_models.md) (10 shared connections)
- [command factories create](command_factories_create.md) (5 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (5 shared connections)

## Source Files

- `server/models/command_magic.py`
- `server/tests/unit/models/test_command_magic.py`

## Audit Trail

- EXTRACTED: 185 (91%)
- INFERRED: 18 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*