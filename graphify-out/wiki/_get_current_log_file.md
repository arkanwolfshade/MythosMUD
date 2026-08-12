# ._get_current_log_file

> 15 nodes

## Key Concepts

- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **._process_log_entry()** (5 connections) — `server/services/chat_logger.py`
- **Path** (5 connections)
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **._queue_log_entry()** (4 connections) — `server/services/chat_logger.py`
- **._start_writer_thread()** (3 connections) — `server/services/chat_logger.py`
- **._writer_worker()** (3 connections) — `server/services/chat_logger.py`
- **Queue a log entry for writing by the background thread. Args: log_type: Type of…** (1 connections) — `server/services/chat_logger.py`
- **Get the current log file path for the specified type. Args: log_type: Type of…** (1 connections) — `server/services/chat_logger.py`
- **Initialize chat logger. Args: log_dir: Directory for log files (if None, uses…** (1 connections) — `server/services/chat_logger.py`
- **Get paths to current log files. Returns: Dictionary mapping log types to file…** (1 connections) — `server/services/chat_logger.py`
- **Start the background writer thread for thread-safe file writing.** (1 connections) — `server/services/chat_logger.py`
- **Background worker thread that handles all file writing operations.** (1 connections) — `server/services/chat_logger.py`
- **Process a log entry from the queue and write it to the appropriate file. Args:…** (1 connections) — `server/services/chat_logger.py`

## Relationships

- [ChatLogger](ChatLogger.md) (11 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*