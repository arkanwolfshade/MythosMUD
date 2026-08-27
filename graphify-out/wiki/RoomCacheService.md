# RoomCacheService

> 31 nodes

## Key Concepts

- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **._resolve_heal_cast()** (4 connections) — `server/utils/command_factories_utility.py`
- **field_validator** (4 connections)
- **.validate_spell_name()** (3 connections) — `server/models/command_magic.py`
- **.validate_target()** (3 connections) — `server/models/command_magic.py`
- **.validate_spell_name()** (3 connections) — `server/models/command_magic.py`
- **.validate_spell_name()** (3 connections) — `server/models/command_magic.py`
- **test_cast_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_spell_name_max_length()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_target_max_length()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_empty()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_valid()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_target_empty_string()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_target_strips()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_target_whitespace()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_magic.py`
- **Validate spell name format.** (3 connections) — `server/models/command_magic.py`
- **Command for casting a spell.** (1 connections) — `server/models/command_magic.py`
- **Validate target format.** (1 connections) — `server/models/command_magic.py`
- **Test CastCommand requires spell_name.** (1 connections) — `server/tests/unit/models/test_command_magic.py`
- **Test CastCommand can have optional target.** (1 connections) — `server/tests/unit/models/test_command_magic.py`
- **Test CastCommand validates and strips spell_name.** (1 connections) — `server/tests/unit/models/test_command_magic.py`
- **Test CastCommand rejects empty spell_name.** (1 connections) — `server/tests/unit/models/test_command_magic.py`
- **Test CastCommand rejects whitespace-only spell_name.** (1 connections) — `server/tests/unit/models/test_command_magic.py`
- *... and 6 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (17 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (3 shared connections)

## Source Files

- `server/models/command_magic.py`
- `server/tests/unit/models/test_command_magic.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 52 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*