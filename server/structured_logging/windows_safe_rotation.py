"""
Windows-safe log rotation handlers.

These handlers avoid rename-while-open issues on Windows by implementing
copy-then-truncate semantics during rollover. They are drop-in replacements
for the standard RotatingFileHandler/TimedRotatingFileHandler.
"""

import os
import shutil
import sys
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


def _copy_then_truncate(src_path: str, dst_path: str, retries: int = 3, delay: float = 0.1) -> None:
    """
    Copy the source file to destination, then truncate the source file.

    This avoids rename failures on Windows when another process/thread still
    has the file open. Retries are used to be resilient to transient locks.
    """
    last_exc: Exception | None = None
    for _ in range(retries):
        try:
            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            # Copy with metadata
            shutil.copy2(src_path, dst_path)
            # Truncate source file
            with open(src_path, "w", encoding="utf-8"):
                # Opening with write mode truncates the file
                pass
            return
        except Exception as exc:  # noqa: BLE001 - we want resilience here  # pylint: disable=broad-exception-caught  # Reason: File operation errors unpredictable, must retry with backoff
            last_exc = exc
            time.sleep(delay)
            delay = min(delay * 2, 1.0)
    if last_exc:
        raise last_exc


class WindowsSafeRotatingFileHandler(RotatingFileHandler):
    """
    Size-based rotating file handler that uses copy-then-truncate on Windows.
    """

    def doRollover(self) -> None:  # noqa: N802 - match logging API
        if self.stream:
            self.stream.close()

        # Compute destination rotated filename (same scheme as base class)
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = f"{self.baseFilename}.{i}"
                dfn = f"{self.baseFilename}.{i + 1}"
                if os.path.exists(sfn):
                    try:
                        if os.path.exists(dfn):
                            os.remove(dfn)
                        os.rename(sfn, dfn)
                    except OSError:
                        # Best-effort; continue rotating the next one
                        pass

            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                try:
                    os.remove(dfn)
                except OSError:
                    pass

            # Windows-safe rollover for the current log file
            if sys.platform == "win32":
                _copy_then_truncate(self.baseFilename, dfn)
            else:
                try:
                    os.rename(self.baseFilename, dfn)
                except OSError:
                    # Fallback to copy-then-truncate even on non-Windows if needed
                    _copy_then_truncate(self.baseFilename, dfn)

        # Reopen the stream
        self.mode = "a"
        self.stream = self._open()


class WindowsSafeTimedRotatingFileHandler(TimedRotatingFileHandler):
    """
    Timed rotating file handler that uses copy-then-truncate on Windows.
    """

    def rotation_filename(self, default_name: str) -> str:  # noqa: D401
        # Use default naming
        return default_name

    def rotate(self, source: str, dest: str) -> None:
        if sys.platform == "win32":
            _copy_then_truncate(source, dest)
        else:
            try:
                os.rename(source, dest)
            except OSError:
                _copy_then_truncate(source, dest)
