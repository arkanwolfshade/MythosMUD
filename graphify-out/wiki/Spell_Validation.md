# Spell Validation

> 58 nodes

## Key Concepts

- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **SpellCommand** (13 connections) — `server/models/command_magic.py`
- **LearnCommand** (13 connections) — `server/models/command_magic.py`
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
- **test_learn_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_learn_command_validate_spell_name_valid()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- *... and 33 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (10 shared connections)
- [command factories create](command_factories_create.md) (3 shared connections)
- [event events serialization](event_events_serialization.md) (1 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (1 shared connections)
- [message handler factory](message_handler_factory.md) (1 shared connections)
- [services service hallucination](services_service_hallucination.md) (1 shared connections)

## Source Files

- `server/models/command_magic.py`
- `server/tests/unit/models/test_command_magic.py`

## Audit Trail

- EXTRACTED: 167 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*