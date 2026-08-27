# WebSocketRequestContext

> 58 nodes

## Key Concepts

- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **test_command_alias.py** (20 connections) — `server/tests/unit/models/test_command_alias.py`
- **AliasCommand** (17 connections) — `server/models/command_alias.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **validate_command_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (9 connections) — `server/validators/security_validator.py`
- **server/validators/__init__.py** (9 connections) — `server/validators/__init__.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **.process_validated_command()** (4 connections) — `server/commands/command_service.py`
- **.validate_command()** (4 connections) — `server/models/command_alias.py`
- **.validate_action()** (4 connections) — `server/models/command_communication.py`
- **.validate_action()** (4 connections) — `server/models/command_communication.py`
- **.validate_pose()** (4 connections) — `server/models/command_communication.py`
- **test_alias_command_alias_name_max_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_alias_name_min_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_command_max_length()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_alias_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_validate_command_none()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_alias_command_with_command()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_aliases_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_alias.py`
- *... and 33 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (31 shared connections)
- [test_rate_limiter_utils.py](test_rate_limiter_utils.py.md) (31 shared connections)
- [subject_controller.py](subject_controller.py.md) (11 shared connections)
- [test_command_factories_inventory_helpers.py](test_command_factories_inventory_helpers.py.md) (4 shared connections)
- [_utc_now](_utc_now.md) (2 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)
- [holidays.schema.json](holidays.schema.json.md) (1 shared connections)
- [PeriodicOrphanAuditor](PeriodicOrphanAuditor.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`
- `server/models/command_alias.py`
- `server/models/command_communication.py`
- `server/tests/unit/models/test_command_alias.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 151 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*