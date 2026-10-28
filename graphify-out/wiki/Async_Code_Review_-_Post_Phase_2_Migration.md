# Async Code Review - Post Phase 2 Migration

> 49 nodes · cohesion 0.10

## Key Concepts

- **test_goto_helpers.py** (32 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **goto_helpers.py** (26 connections) — `server/commands/goto_helpers.py`
- **asyncio** (21 connections)
- **patch** (16 connections)
- **validate_goto_context()** (14 connections) — `server/commands/goto_helpers.py`
- **execute_confirm_goto()** (12 connections) — `server/commands/goto_helpers.py`
- **execute_goto_teleport()** (12 connections) — `server/commands/goto_helpers.py`
- **validate_confirm_goto_context()** (12 connections) — `server/commands/goto_helpers.py`
- **resolve_goto_target()** (11 connections) — `server/commands/goto_helpers.py`
- **resolve_target_player_for_goto()** (11 connections) — `server/commands/goto_helpers.py`
- **log_goto_failure()** (10 connections) — `server/commands/goto_helpers.py`
- **Any** (9 connections)
- **_announce_goto_teleport()** (7 connections) — `server/commands/goto_helpers.py`
- **_relocate_admin_player_for_goto()** (5 connections) — `server/commands/goto_helpers.py`
- **test_execute_confirm_goto()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_execute_goto_teleport_success()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_execute_goto_teleport_without_online_admin()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_log_goto_failure_swallows_logger_error()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_goto_target_not_in_database()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_goto_target_offline()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_goto_target_success()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_target_player_for_goto()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_target_player_for_goto_not_in_db()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_resolve_target_player_for_goto_offline()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- **test_validate_confirm_goto_context_not_admin()** (4 connections) — `server/tests/unit/commands/test_goto_helpers.py`
- *... and 24 more nodes in this community*

## Relationships

- [ErrorContext](ErrorContext.md) (18 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (11 shared connections)
- [command_parser.py](command_parser.py.md) (8 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (8 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/commands/goto_helpers.py`
- `server/tests/unit/commands/test_goto_helpers.py`

## Audit Trail

- EXTRACTED: 170 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*