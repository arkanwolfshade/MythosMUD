# Logging Aggregator Verification Plan

## Overview

Verify that the enhanced file logging setup correctly attaches aggregator handlers
(warnings.log and errors.log) to the root logger and QueueListener, that
WARNING/ERROR records propagate to root, that the log directory is as expected
(logs/local for default environment), and that handlers receive records (level and
filter do not drop all).

## Hypotheses (Remaining Todos)

### H1: Aggregator handlers attached to root / listener

- When async is disabled: root logger has the aggregator file handlers directly.
- When async is enabled: root logger has QueueHandlers that feed the queue; the
  QueueListener holds the actual aggregator file handlers.
- **Success:** Test asserts root has appropriate handlers (QueueHandler when async,
  or file handlers when sync). Optionally assert listener's handlers include
  aggregator handlers when async.

### H2: Records at WARNING/ERROR propagate to root

- Child loggers use default propagate=True, so records reach the root logger where
  aggregator QueueHandlers (or handlers) are attached.
- **Success:** Log WARNING/ERROR from a child logger and verify they appear in
  warnings.log / errors.log (proves propagation to root and handler receipt).

### H3: QueueListener started with aggregator handlers

- `_setup_async_logging_queue(all_file_handlers)` is called with
  `all_file_handlers` that includes `aggregator_handlers`.
- **Success:** Test that after setup with enable_async=True, the QueueListener is
  started and its handlers include the aggregator handlers (warnings and errors).

### H4: Log directory is the expected one (logs/local)

- `resolve_log_base(log_config.get("log_base", "logs"))` with default yields
  project_root / "logs"; `env_log_dir = log_base / environment` with
  environment "local" yields project_root / "logs" / "local".
- **Success:** Test that with default log_base "logs" and environment "local", the
  resolved env log directory is .../logs/local.

### H5: Handlers receive records (level/filter not dropping all)

- Aggregator handlers have level WARNING and ERROR respectively; they do not use
  a name filter (they are on root and receive all records that reach root).
- **Success:** After setup, log one WARNING and one ERROR; assert warnings.log
  contains the warning and errors.log contains the error.

## Implementation

- Add unit tests in `server/tests/unit/structured_logging/` that:
  - (H4) Test `resolve_log_base("logs")` and env_log_dir for "local" yields
    path ending in "logs/local".
  - (H1, H2, H3, H5) Test `setup_enhanced_file_logging()` with a temporary
    log directory: assert root has expected handlers; log WARNING and ERROR;
    flush/stop listener if async; assert warnings.log and errors.log contain
    the expected messages.
- Optionally expose `get_queue_listener()` in `logging_file_setup.py` for
  test teardown (stop listener) and for H3 assertion.

## Success Criteria

- All five hypotheses verified by tests.
- Tests use temporary directories and clean up (remove handlers, stop listener)
  so they do not affect other tests or leave background threads.
