# Security Validator Tests

> 52 nodes

## Key Concepts

- **test_security_validator.py** (96 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_sanitize_unicode_input_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_sanitize_unicode_input_none()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_sanitize_unicode_input_normal_text()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_no_ansi()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_color_codes()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_strip_ansi_codes_cursor_movement()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_normal()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_removes_null_bytes()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_normalizes_newlines()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_comprehensive_sanitize_input_preserves_tabs()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_action_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_action_content_rejects_html_tags()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_action_content_rejects_injection_patterns()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_single_char()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_player_name_long()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_command_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_command_content_rejects_injection()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_reason_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_reason_content_rejects_html()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_pose_content_empty()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_pose_content_valid()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_validate_pose_content_rejects_html()** (3 connections) — `server/tests/unit/validators/test_security_validator.py`
- **test_injection_patterns_defined()** (2 connections) — `server/tests/unit/validators/test_security_validator.py`
- *... and 27 more nodes in this community*

## Relationships

- [command communication models](command_communication_models.md) (25 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (14 shared connections)
- [subject nats manager](subject_nats_manager.md) (11 shared connections)
- [commands who helpers](commands_who_helpers.md) (6 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (5 shared connections)
- [app tick game](app_tick_game.md) (5 shared connections)
- [combat services initialization](combat_services_initialization.md) (5 shared connections)
- [auth dependencies rationale](auth_dependencies_rationale.md) (4 shared connections)
- [eventLog eventStore projector](eventLog_eventStore_projector.md) (4 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (4 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)

## Source Files

- `server/tests/unit/validators/test_security_validator.py`

## Audit Trail

- EXTRACTED: 195 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*