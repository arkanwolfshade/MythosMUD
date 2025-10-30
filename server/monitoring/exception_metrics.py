from __future__ import annotations

import threading
from collections import Counter
from typing import Any

_lock = threading.Lock()
_exceptions: Counter[str] = Counter()


def increment_exception(exc_type: str) -> None:
    with _lock:
        _exceptions[exc_type] += 1


def get_summary() -> dict[str, Any]:
    with _lock:
        total = sum(_exceptions.values())
        by_type = dict(_exceptions)
    return {"total": total, "by_type": by_type}
