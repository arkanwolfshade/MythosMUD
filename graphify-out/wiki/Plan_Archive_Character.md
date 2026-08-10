# Plan Archive Character

> 4 nodes

## Key Concepts

- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **._writer_worker()** (3 connections) — `server/services/chat_logger.py`
- **Background worker thread that handles all file writing operations.** (1 connections) — `server/services/chat_logger.py`
- **Process a log entry from the queue and write it to the appropriate file.** (1 connections) — `server/services/chat_logger.py`

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