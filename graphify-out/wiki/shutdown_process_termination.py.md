# shutdown_process_termination.py

> 11 nodes

## Key Concepts

- **shutdown_process_termination.py** (11 connections) — `server/commands/shutdown_process_termination.py`
- **_find_uvicorn_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_uvicorn_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_child_processes()** (2 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_with_signals()** (2 connections) — `server/commands/shutdown_process_termination.py`
- **Any** (2 connections)
- **Process termination utilities for graceful server shutdown. This module handles…** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Find all uvicorn processes using psutil.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all uvicorn processes.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all child processes of the current process.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Fallback signal-based termination when psutil is not available.** (1 connections) — `server/commands/shutdown_process_termination.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [shutdown_sequence.py](shutdown_sequence.py.md) (2 shared connections)
- [threading.py](threading.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*