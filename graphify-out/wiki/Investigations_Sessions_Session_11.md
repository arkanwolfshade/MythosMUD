# Investigations Sessions Session

> 5 nodes

## Key Concepts

- **_find_uvicorn_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **_terminate_uvicorn_processes()** (3 connections) — `server/commands/shutdown_process_termination.py`
- **Any** (2 connections)
- **Find all uvicorn processes using psutil.** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Terminate all uvicorn processes.** (1 connections) — `server/commands/shutdown_process_termination.py`

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*