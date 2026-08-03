# command communication models

> 189 nodes

## Key Concepts

- **test_command_communication.py** (45 connections) — `server/tests/unit/models/test_command_communication.py`
- **security_validator.py** (34 connections) — `server/validators/security_validator.py`
- **test_command_factories_communication.py** (29 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **command_communication.py** (19 connections) — `server/models/command_communication.py`
- **WhisperCommand** (15 connections) — `server/models/command_communication.py`
- **SayCommand** (13 connections) — `server/models/command_communication.py`
- **PoseCommand** (13 connections) — `server/models/command_communication.py`
- **LocalCommand** (12 connections) — `server/models/command_communication.py`
- **SystemCommand** (12 connections) — `server/models/command_communication.py`
- **EmoteCommand** (12 connections) — `server/models/command_communication.py`
- **MeCommand** (12 connections) — `server/models/command_communication.py`
- **ReplyCommand** (12 connections) — `server/models/command_communication.py`
- **validate_action_content()** (11 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (10 connections) — `server/validators/security_validator.py`
- **__init__.py** (9 connections) — `server/validators/__init__.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **validate_command_content()** (9 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (9 connections) — `server/validators/security_validator.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **normalize_command()** (8 connections) — `server/validators/command_validator.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **.create_local_command()** (7 connections) — `server/utils/command_factories_communication.py`
- *... and 164 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (47 shared connections)
- [command inventory models](command_inventory_models.md) (31 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (25 shared connections)
- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [command validator validators](command_validator_validators.md) (15 shared connections)
- [subject nats manager](subject_nats_manager.md) (8 shared connections)
- [commands admin mute](commands_admin_mute.md) (5 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (5 shared connections)
- [auth users rationale](auth_users_rationale.md) (3 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (2 shared connections)
- [app tick game](app_tick_game.md) (2 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/utils/command_factories_communication.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 646 (92%)
- INFERRED: 57 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*