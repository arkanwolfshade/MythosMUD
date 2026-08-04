# health monitor realtime

> 11 nodes

## Key Concepts

- **shutdown_process_termination.py** (12 connections) — `server/commands/shutdown_process_termination.py`
- **_find_uvicorn_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_uvicorn_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **Any** (2 connections)
- **_terminate_child_processes()** (2 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_with_signals()** (2 connections) — `server/commands/shutdown_process_termination.py`
- **Process termination utilities for graceful server shutdown.  This module handles** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Find all uvicorn processes using psutil.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all uvicorn processes.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all child processes of the current process.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Fallback signal-based termination when psutil is not available.** (1 connections) — `server/commands/shutdown_process_termination.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [shutdown commands sequence](shutdown_commands_sequence.md) (2 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [middleware security headers](middleware_security_headers.md) (1 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*