"""Exception metrics tracking for monitoring.

This module provides thread-safe exception counting and metrics tracking
for monitoring system health and error rates.
"""

from __future__ import annotations

import threading
from collections import Counter
from typing import Any

_lock = threading.Lock()
_exceptions: Counter[str] = Counter()


def increment_exception(exc_type: str) -> None:
    """Increment the count for a specific exception type.

    Args:
        exc_type: The exception type name to increment
    """
    with _lock:
        _exceptions[exc_type] += 1


def get_summary() -> dict[str, Any]:
    """Get a summary of exception counts.

    Returns:
        dict[str, Any]: Dictionary containing total count and individual exception counts
    """
    with _lock:
        total = sum(_exceptions.values())
        by_type = dict(_exceptions)
    return {"total": total, "by_type": by_type}
