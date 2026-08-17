# setup_enhanced_file_logging

> 28 nodes

## Key Concepts

- **setup_enhanced_file_logging()** (20 connections) — `server/structured_logging/logging_file_setup.py`
- **test_logging_file_setup.py** (15 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_queue_listener_has_aggregator_handlers()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_warning_and_error_reach_aggregator_files()** (7 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **get_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **stop_queue_listener()** (6 connections) — `server/structured_logging/logging_file_setup.py`
- **_restore_root_handlers()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_root_handlers_snapshot()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **test_aggregator_handlers_on_root_when_async()** (6 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **_setup_async_logging_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **test_log_directory_under_env()** (5 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **default_log_config()** (3 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **temp_log_base()** (3 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **QueueListener** (2 connections)
- **fixture** (2 connections)
- **Set up async logging queue listener for non-blocking file I/O. Uses…** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Return the global QueueListener if running (for tests and shutdown). Returns:…** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Stop the global QueueListener and reset state (for tests and shutdown). Allows…** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Set up enhanced file logging with async QueueHandler/QueueListener when…** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Unit tests for logging file setup. Verifies aggregator handlers attached to…** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **H4 (setup): Log files are created under env_log_dir (e.g. .../test/).** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Temporary directory used as log_base for setup.** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Default log config with rotation.** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Return a copy of root logger handlers (for restore).** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- **Replace root logger handlers with the given list.** (1 connections) — `server/tests/unit/structured_logging/test_logging_file_setup.py`
- *... and 3 more nodes in this community*

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (15 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/structured_logging/test_logging_file_setup.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*