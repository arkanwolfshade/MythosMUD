# middleware security headers

> 16 nodes

## Key Concepts

- **test_shutdown_process_termination.py** (9 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_schedule_process_termination_disabled_by_env()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_schedule_process_termination_starts_thread()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_find_uvicorn_processes_collects_uvicorn_names()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminate_with_signals_sends_to_child_and_parent()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminate_uvicorn_processes_kills_stubborn()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminate_child_processes()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **test_terminator_thread_import_error_falls_back_to_signals()** (2 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **Unit tests for shutdown process termination helpers.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **schedule_process_termination returns early when exit is disabled.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **schedule_process_termination starts daemon thread when enabled.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **_find_uvicorn_processes returns processes whose name contains uvicorn.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **_terminate_with_signals attempts SIGINT and SIGTERM on child and parent.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **_terminate_uvicorn_processes kills processes still running after terminate.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **_terminate_child_processes terminates and kills surviving children.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`
- **Terminator thread uses signal fallback when psutil import fails.** (1 connections) — `server/tests/unit/commands/test_shutdown_process_termination.py`

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_shutdown_process_termination.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*