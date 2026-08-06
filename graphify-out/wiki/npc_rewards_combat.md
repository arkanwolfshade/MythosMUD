# npc rewards combat

> 41 nodes

## Key Concepts

- **test_goto_helpers.py** (32 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **validate_goto_context()** (13 connections) — `server/commands/goto_helpers.py`
- **execute_goto_teleport()** (13 connections) — `server/commands/goto_helpers.py`
- **validate_confirm_goto_context()** (11 connections) — `server/commands/goto_helpers.py`
- **execute_confirm_goto()** (11 connections) — `server/commands/goto_helpers.py`
- **resolve_goto_target()** (10 connections) — `server/commands/goto_helpers.py`
- **log_goto_failure()** (10 connections) — `server/commands/goto_helpers.py`
- **resolve_target_player_for_goto()** (10 connections) — `server/commands/goto_helpers.py`
- **Any** (7 connections)
- **test_validate_goto_context_no_app()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_goto_context_no_player_service()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_goto_context_not_admin()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_goto_context_player_not_found()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_goto_context_no_connection_manager()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_goto_context_success()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_goto_target_offline()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_goto_target_success()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_execute_goto_teleport_success()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_execute_goto_teleport_db_failure()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_log_goto_failure()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_confirm_goto_context_success()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_target_player_for_goto()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_execute_confirm_goto()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_goto_target_not_in_database()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_confirm_goto_context_no_app()** (2 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- *... and 16 more nodes in this community*

## Relationships

- [npc service services](npc_service_services.md) (22 shared connections)
- [realtime game state](realtime_game_state.md) (7 shared connections)
- [admin structured logging](admin_structured_logging.md) (3 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (2 shared connections)

## Source Files

- `server/commands/goto_helpers.py`
- `server/tests/unit/commands/test_goto_helpers.py`

## Audit Trail

- EXTRACTED: 172 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*