"""
Debug instrumentation helper for writing to debug log file.

This module provides a helper function for debug mode instrumentation that
writes to the specific debug log file. This is separate from the enhanced
logging system which writes to standard log directories.

As noted in the Pnakotic Manuscripts, temporary instrumentation for debugging
must be clearly marked and easily removable.
"""

import json
import time
from pathlib import Path
from typing import Any

# Debug log file path - matches the path used in debug mode instructions
DEBUG_LOG_PATH = Path(r"e:\projects\GitHub\MythosMUD\.cursor\debug.log")


def write_debug_log(
    location: str,
    message: str,
    data: dict[str, Any] | None = None,
    session_id: str = "debug-session",
    run_id: str = "run1",
    hypothesis_id: str = "D",
) -> None:
    """
    Write a debug instrumentation log entry to the debug log file.

    This function writes NDJSON-formatted log entries to the debug log file
    for debug mode instrumentation. This is separate from the enhanced logging
    system which writes to standard log directories.

    Args:
        location: File location (e.g., "room.py:85")
        message: Log message
        data: Optional data dictionary to include in the log entry
        session_id: Debug session ID (default: "debug-session")
        run_id: Debug run ID (default: "run1")
        hypothesis_id: Hypothesis ID for debugging (default: "D")
    """
    try:
        log_entry = {
            "location": location,
            "message": message,
            "data": data or {},
            "timestamp": int(time.time() * 1000),
            "sessionId": session_id,
            "runId": run_id,
            "hypothesisId": hypothesis_id,
        }

        with open(DEBUG_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception:
        # Silently fail - debug instrumentation should not break the application
        pass
