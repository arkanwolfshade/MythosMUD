# shutdown_sequence.py

> 21 nodes

## Key Concepts

- **shutdown_sequence.py** (16 connections) — `server/commands/shutdown_sequence.py`
- **execute_shutdown_sequence()** (13 connections) — `server/commands/shutdown_sequence.py`
- **Any** (8 connections)
- **schedule_process_termination()** (4 connections) — `server/commands/shutdown_process_termination.py`
- **_cancel_background_tasks()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_cleanup_connection_manager()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_despawn_all_npcs()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_all_players()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_disconnect_nats_service()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_persist_all_players()** (4 connections) — `server/commands/shutdown_sequence.py`
- **_stop_nats_message_handler()** (4 connections) — `server/commands/shutdown_sequence.py`
- **Schedule a best-effort graceful process termination after a short delay. This…** (1 connections) — `server/commands/shutdown_process_termination.py`
- **Shutdown sequence execution for graceful server shutdown. This module handles…** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 4: Stop NATS message handler.** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 5: Disconnect NATS service.** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 6: Clean up connection manager.** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 7: Cancel remaining background tasks.** (1 connections) — `server/commands/shutdown_sequence.py`
- **Execute the graceful shutdown sequence. This function performs an orderly…** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 1: Persist all active player data.** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 2: Despawn all NPCs.** (1 connections) — `server/commands/shutdown_sequence.py`
- **Phase 3: Disconnect all players gracefully.** (1 connections) — `server/commands/shutdown_sequence.py`

## Relationships

- [admin_shutdown_command.py](admin_shutdown_command.py.md) (3 shared connections)
- [shutdown_process_termination.py](shutdown_process_termination.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/commands/shutdown_process_termination.py`
- `server/commands/shutdown_sequence.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*