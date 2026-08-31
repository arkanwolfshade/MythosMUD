# shutdown_process_termination.py

> 29 nodes

## Key Concepts

- **shutdown_process_termination.py** (12 connections) — `server/commands/shutdown_process_termination.py`
- **test_shutdown_process_termination.py** (9 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **schedule_process_termination()** (7 connections) — `server/commands/shutdown_process_termination.py`
- **_find_uvicorn_processes()** (4 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_uvicorn_processes()** (4 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_child_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_with_signals()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **test_find_uvicorn_processes_collects_uvicorn_names()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_schedule_process_termination_disabled_by_env()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_schedule_process_termination_starts_thread()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminate_child_processes()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminate_uvicorn_processes_kills_stubborn()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminate_with_signals_sends_to_child_and_parent()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminator_thread_import_error_falls_back_to_signals()** (3 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **Any** (2 connections)
- **Process termination utilities for graceful server shutdown. This module handles…** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Schedule a best-effort graceful process termination after a short delay. This…** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Find all uvicorn processes using psutil.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all uvicorn processes.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all child processes of the current process.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Fallback signal-based termination when psutil is not available.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Unit tests for shutdown process termination helpers.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **schedule_process_termination starts daemon thread when enabled.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **_find_uvicorn_processes returns processes whose name contains uvicorn.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **_terminate_with_signals attempts SIGINT and SIGTERM on child and parent.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- *... and 4 more nodes in this community*

## Relationships

- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [threading.py](threading.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`
- `server/tests/unit/commands/test_shutdown_process_termination.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*