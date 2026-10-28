# test_look_item_helpers.py

> 221 nodes · cohesion 0.01

## Key Concepts

- **test_security_validator.py** (101 connections) — `server/tests/unit/validators/test_security_validator.py`
- **security_validator.py** (37 connections) — `server/validators/security_validator.py`
- **validate_player_name()** (29 connections) — `server/validators/security_validator.py`
- **validate_message_content()** (23 connections) — `server/validators/security_validator.py`
- **comprehensive_sanitize_input()** (20 connections) — `server/validators/security_validator.py`
- **strip_ansi_codes()** (13 connections) — `server/validators/security_validator.py`
- **validate_action_content()** (12 connections) — `server/validators/security_validator.py`
- **validate_alias_name()** (11 connections) — `server/validators/security_validator.py`
- **validate_reason_content()** (11 connections) — `server/validators/security_validator.py`
- **field_validator** (10 connections)
- **validate_command_content()** (10 connections) — `server/validators/security_validator.py`
- **validate_pose_content()** (10 connections) — `server/validators/security_validator.py`
- **server/validators/__init__.py** (9 connections) — `server/validators/__init__.py`
- **sanitize_unicode_input()** (9 connections) — `server/validators/security_validator.py`
- **validate_filter_name()** (9 connections) — `server/validators/security_validator.py`
- **validate_help_topic()** (9 connections) — `server/validators/security_validator.py`
- **validate_target_player()** (9 connections) — `server/validators/security_validator.py`
- **field_validator** (8 connections)
- **validate_security_comprehensive()** (8 connections) — `server/validators/security_validator.py`
- **check_dangerous_characters()** (6 connections) — `server/validators/security_validator.py`
- **check_injection_patterns()** (6 connections) — `server/validators/security_validator.py`
- **.validate_name()** (5 connections) — `server/schemas/players/player_requests.py`
- **get_dangerous_characters()** (5 connections) — `server/validators/security_validator.py`
- **get_injection_patterns()** (5 connections) — `server/validators/security_validator.py`
- **.validate_action()** (4 connections) — `server/models/command_communication.py`
- *... and 196 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (34 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (11 shared connections)
- [generate_openapi_spec.py](generate_openapi_spec.py.md) (8 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (5 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [EmoteService](EmoteService.md) (3 shared connections)
- [test_nats_service_pool.py](test_nats_service_pool.py.md) (2 shared connections)
- [ensure_directory_exists](ensure_directory_exists.md) (2 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (2 shared connections)

## Source Files

- `server/models/command_communication.py`
- `server/models/command_moderation.py`
- `server/models/command_utility.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/__init__.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 417 (95%)
- INFERRED: 20 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*