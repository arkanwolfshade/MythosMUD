# Procedures Readme Semgrep

> 4 nodes

## Key Concepts

- **.get_local_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **.get_local_channel_log_files()** (3 connections) — `server/services/chat_logger.py`
- **Get all local channel log files.          Returns:             List of string pa** (1 connections) — `server/services/chat_logger.py`
- **Get statistics for local channel log files.          Returns:             Dictio** (1 connections) — `server/services/chat_logger.py`

## Relationships

- [Chat Channel Logger](Chat_Channel_Logger.md) (3 shared connections)
- [AnyIO vs Asyncio Guide](AnyIO_vs_Asyncio_Guide.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*