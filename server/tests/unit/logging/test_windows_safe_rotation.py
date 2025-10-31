import logging
import tempfile
from pathlib import Path

from server.logging.windows_safe_rotation import WindowsSafeRotatingFileHandler


def test_windows_safe_rotating_file_handler_rollover_creates_backup_and_truncates_original():
    with tempfile.TemporaryDirectory() as tmpdir:
        log_path = Path(tmpdir) / "test.log"

        # Create initial file with content
        log_path.write_text("x" * 1024, encoding="utf-8")

        logger = logging.getLogger("test_windows_safe_rotation")
        logger.setLevel(logging.DEBUG)

        handler = WindowsSafeRotatingFileHandler(str(log_path), maxBytes=100, backupCount=3, encoding="utf-8")
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        try:
            # Emit enough data to trigger rollover
            for _ in range(10):
                logger.debug("y" * 50)

            # Verify backup file exists
            backup = Path(f"{log_path}.1")
            assert backup.exists(), "Expected rotated backup file to exist"

            # Original file should exist and be writable (truncated at some point)
            assert log_path.exists(), "Expected original log file to exist"

            # Should be smaller than initial seeded size after rotation
            assert log_path.stat().st_size <= 1024
        finally:
            logger.removeHandler(handler)
            handler.close()
