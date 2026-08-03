# shutdown commands sequence

> 32 nodes

## Key Concepts

- **shutdown_sequence.py** (16 connections) — `server/commands/shutdown_sequence.py`
- **execute_shutdown_sequence()** (13 connections) — `server/commands/shutdown_sequence.py`
- **shutdown_process_termination.py** (11 connections) — `server/commands/shutdown_process_termination.py`
- **Any** (8 connections)
- **schedule_process_termination()** (4 connections) — `server/commands/shutdown_process_termination.py`
- **_persist_all_players()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_despawn_all_npcs()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_all_players()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_stop_nats_message_handler()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_nats_service()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_cleanup_connection_manager()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_cancel_background_tasks()** (4 connections) — `server/commands/shutdown_sequence.py`
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
- **Schedule a best-effort graceful process termination after a short delay.      Th** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Shutdown sequence execution for graceful server shutdown.  This module handles t** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 1: Persist all active player data.** (1 connections) — `server/commands/shutdown_sequence.py`
- *... and 7 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (3 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`
- `server/commands/shutdown_sequence.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*