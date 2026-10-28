"""
Process termination for graceful server shutdown.

Only this server's own process tree is touched: the worker asks uvicorn to exit through its normal
lifespan shutdown and, under ``--reload``, stops the reloader that supervises it.
"""

import os
import signal
import threading
import time

import psutil

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# If uvicorn has not ended the process this long after being asked to, force it.
_FORCE_EXIT_AFTER_SECONDS = 10.0


def _is_uvicorn_reloader(cmdline: list[str]) -> bool:
    return "--reload" in cmdline and any("uvicorn" in arg for arg in cmdline)


def _stop_reloader_ancestor() -> None:
    """Terminate the ``uvicorn --reload`` supervisor above this worker, if there is one.

    The reloader never notices that its worker exited, so without this it (and the launcher above it) outlive the
    shutdown. Only ancestors are considered, never processes that merely share a name with uvicorn.
    """
    try:
        for ancestor in psutil.Process().parents():
            if _is_uvicorn_reloader(ancestor.cmdline()):
                logger.info("Terminating uvicorn reloader", pid=ancestor.pid)
                ancestor.terminate()
                return
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        logger.warning("Could not stop uvicorn reloader", error=str(e))


def schedule_process_termination(delay_seconds: float = 0.3) -> None:
    """Schedule a graceful process exit after a short delay.

    Guarded by the environment variable `MYTHOSMUD_DISABLE_PROCESS_EXIT` (set to "1" to disable), which is
    useful during tests.
    """
    if os.environ.get("MYTHOSMUD_DISABLE_PROCESS_EXIT") == "1":
        logger.info("Process termination scheduling disabled by environment variable")
        return

    def _terminator() -> None:
        logger.info("ProcessTerminator thread started", delay_seconds=delay_seconds)
        # Shutdown/termination is sync-only; not used from async request path.
        time.sleep(delay_seconds)
        _stop_reloader_ancestor()
        logger.info("ProcessTerminator asking uvicorn to exit", pid=os.getpid())
        signal.raise_signal(signal.SIGINT)

        # Backstop: uvicorn's lifespan shutdown should end the process before this wakes.
        time.sleep(_FORCE_EXIT_AFTER_SECONDS)
        logger.warning("ProcessTerminator forcing exit with os._exit(0)")
        os._exit(0)

    logger.info("Starting ProcessTerminator thread")
    threading.Thread(target=_terminator, name="MythosMUD-ProcessTerminator", daemon=True).start()
