# AnyIO vs Asyncio Guide

> 21 nodes

## Key Concepts

- **Path** (12 connections)
- **._get_current_log_file()** (6 connections) — `server/services/chat_logger.py`
- **.__init__()** (5 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_stats()** (5 connections) — `server/services/chat_logger.py`
- **.get_log_file_paths()** (4 connections) — `server/services/chat_logger.py`
- **._get_global_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_whisper_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **._get_system_channel_log_file()** (4 connections) — `server/services/chat_logger.py`
- **.get_global_channel_log_files()** (4 connections) — `server/services/chat_logger.py`
- **.cleanup_old_global_channel_logs()** (4 connections) — `server/services/chat_logger.py`
- **._start_writer_thread()** (3 connections) — `server/services/chat_logger.py`
- **Initialize chat logger.          Args:             log_dir: Directory for log fi** (1 connections) — `server/services/chat_logger.py`
- **Start the background writer thread for thread-safe file writing.** (1 connections) — `server/services/chat_logger.py`
- **Get the current log file path for the specified type.          Args:** (1 connections) — `server/services/chat_logger.py`
- **Get paths to current log files.          Returns:             Dictionary mapping** (1 connections) — `server/services/chat_logger.py`
- **Get the global channel log file path.          Returns:             Path to the** (1 connections) — `server/services/chat_logger.py`
- **Get the whisper channel log file path.          Returns:             Path to the** (1 connections) — `server/services/chat_logger.py`
- **Get the system channel log file path.          Returns:             Path to the** (1 connections) — `server/services/chat_logger.py`
- **Get all global channel log files.          Returns:             List of string p** (1 connections) — `server/services/chat_logger.py`
- **Get statistics for global channel log files.          Returns:             Dicti** (1 connections) — `server/services/chat_logger.py`
- **Clean up old global channel log files.          Args:             days_to_keep:** (1 connections) — `server/services/chat_logger.py`

## Relationships

- [Chat Channel Logger](Chat_Channel_Logger.md) (18 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (1 shared connections)
- [Plan Archive Character](Plan_Archive_Character.md) (1 shared connections)
- [Procedures Readme Semgrep](Procedures_Readme_Semgrep.md) (1 shared connections)

## Source Files

- `server/services/chat_logger.py`

## Audit Trail

- EXTRACTED: 65 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*