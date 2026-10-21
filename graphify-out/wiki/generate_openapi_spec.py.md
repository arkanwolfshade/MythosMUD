# generate_openapi_spec.py

> 23 nodes · cohesion 0.13

## Key Concepts

- **validate_combat_target()** (18 connections) — `server/validators/security_validator.py`
- **field_validator** (7 connections)
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **.validate_target()** (4 connections) — `server/models/command_combat.py`
- **test_validate_combat_target_allows_npc_instance_id()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_combat_target_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_combat_target_rejects_dangerous_chars()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_combat_target_rejects_too_long()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_combat_target_valid_npc()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_combat_target_valid_player()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validate combat target name format using centralized validation.** (1 connections) — `server/models/command_combat.py`
- **Test validating empty combat target.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid player combat target.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test validating valid NPC combat target with title.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_combat_target rejects dangerous characters.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Test that validate_combat_target rejects names that are too long.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Regression: spawned NPC instance IDs exceed the old 50-char display-name limit.** (1 connections) — `server/tests/unit/validators/test_security_validator.py`
- **Validation for combat target fields that can be either players or NPCs. This…** (1 connections) — `server/validators/security_validator.py`

## Relationships

- [test_look_item_helpers.py](test_look_item_helpers.py.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [useMythosAppState.ts](useMythosAppState.ts.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 49 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*