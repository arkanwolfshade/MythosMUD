# connection manager realtime

> 6 nodes

## Key Concepts

- **test_initiate_shutdown_countdown_success()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_initiate_shutdown_countdown_supersedes()** (5 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateStateStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **_InitiateAppStub** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test initiate_shutdown_countdown() successfully initiates shutdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test initiate_shutdown_countdown() cancels existing shutdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (4 shared connections)
- [eventLog projectorRoom roomMergeUtils](eventLog_projectorRoom_roomMergeUtils.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*