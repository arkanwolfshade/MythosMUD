# security sessionManager SessionManager

> 14 nodes

## Key Concepts

- **validate_admin_permission()** (20 connections) — `server/commands/admin_permission_utils.py`
- **test_admin_permission_utils.py** (11 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **_BrokenAdminPlayer** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_attribute_error()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_logs_secondary_failure()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_no_player()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_missing_is_admin_attr()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_is_admin_false()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_granted()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **.is_admin()** (2 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **Any** (1 connections)
- **Validate that a player has admin permissions.      Args:         player: Player** (1 connections) — `server/commands/admin_permission_utils.py`
- **mock_admin_logger()** (1 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **Unit tests for admin permission validation.** (1 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`

## Relationships

- [admin structured logging](admin_structured_logging.md) (3 shared connections)
- [npc service services](npc_service_services.md) (3 shared connections)
- [npc rewards combat](npc_rewards_combat.md) (3 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*