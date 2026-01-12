"""
Process termination utilities for graceful server shutdown.

This module handles the termination of uvicorn processes and child processes
during server shutdown, ensuring clean process cleanup.
"""

import os
import signal
import threading
import time
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _find_uvicorn_processes() -> list[Any]:
    """Find all uvicorn processes using psutil."""
    import psutil

    uvicorn_processes = []
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if proc.info["name"] and "uvicorn" in proc.info["name"].lower():
                uvicorn_processes.append(proc)
                logger.info("Found uvicorn process", pid=proc.info["pid"], name=proc.info["name"])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return uvicorn_processes


def _terminate_uvicorn_processes(uvicorn_processes: list[Any]) -> None:
    """Terminate all uvicorn processes."""
    import psutil

    for proc in uvicorn_processes:
        try:
            logger.info("Terminating uvicorn process", pid=proc.info["pid"])
            proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            logger.warning("Could not terminate uvicorn process", pid=proc.info["pid"], error=str(e))

    time.sleep(1)

    for proc in uvicorn_processes:
        try:
            if proc.is_running():
                logger.warning("Killing stubborn uvicorn process", pid=proc.info["pid"])
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def _terminate_child_processes(pid: int) -> None:
    """Terminate all child processes of the current process."""
    import psutil

    current_process = psutil.Process(pid)
    children = current_process.children(recursive=True)
    for child in children:
        logger.info("Terminating child process", pid=child.pid, name=child.name())
        try:
            child.terminate()
        except psutil.NoSuchProcess:
            logger.warning("Child process already terminated", pid=child.pid)

    _gone, alive = psutil.wait_procs(children, timeout=2)
    for p in alive:
        logger.warning("Child process did not terminate, killing", pid=p.pid, name=p.name())
        try:
            p.kill()
        except psutil.NoSuchProcess:
            logger.warning("Child process already terminated", pid=p.pid)


def _terminate_with_signals(pid: int, ppid: int) -> None:
    """Fallback signal-based termination when psutil is not available."""
    try:
        logger.info("ProcessTerminator sending SIGINT to child")
        os.kill(pid, signal.SIGINT)
    except OSError as e:
        logger.warning("ProcessTerminator SIGINT(child) failed", error=str(e))

    try:
        if ppid and ppid != 1:
            logger.info("ProcessTerminator sending SIGINT to parent")
            os.kill(ppid, signal.SIGINT)
    except OSError as e:
        logger.warning("ProcessTerminator SIGINT(parent) failed", error=str(e))

    time.sleep(0.1)
    try:
        logger.info("ProcessTerminator sending SIGTERM to child")
        os.kill(pid, signal.SIGTERM)
    except OSError as e:
        logger.warning("ProcessTerminator SIGTERM(child) failed", error=str(e))

    try:
        if ppid and ppid != 1:
            logger.info("ProcessTerminator sending SIGTERM to parent")
            os.kill(ppid, signal.SIGTERM)
    except OSError as e:
        logger.warning("ProcessTerminator SIGTERM(parent) failed", error=str(e))


def schedule_process_termination(delay_seconds: float = 0.3) -> None:
    """Schedule a best-effort graceful process termination after a short delay.

    This signals the parent uvicorn process to exit after all shutdown phases
    complete. Guarded by the environment variable
    `MYTHOSMUD_DISABLE_PROCESS_EXIT` (set to "1" to disable), which is useful
    during tests.
    """
    if os.environ.get("MYTHOSMUD_DISABLE_PROCESS_EXIT") == "1":
        logger.info("Process termination scheduling disabled by environment variable")
        return

    def _terminator() -> None:
        try:
            logger.info("ProcessTerminator thread started", delay_seconds=delay_seconds)
            time.sleep(delay_seconds)
            pid = os.getpid()
            ppid = os.getppid()
            logger.info("ProcessTerminator attempting to terminate process", pid=pid, ppid=ppid)

            # Try to find and kill uvicorn processes specifically
            try:
                uvicorn_processes = _find_uvicorn_processes()
                _terminate_uvicorn_processes(uvicorn_processes)
                _terminate_child_processes(pid)
            except ImportError:
                logger.warning("psutil not available, falling back to signal-based termination")
                _terminate_with_signals(pid, ppid)

            # As a last resort, force exit to avoid hanging processes
            time.sleep(0.2)
            logger.info("ProcessTerminator forcing exit with os._exit(0)")
            os._exit(0)
        except OSError as e:
            logger.error("ProcessTerminator error", error=str(e))
            # Final fallback - force exit
            logger.info("ProcessTerminator final fallback - os._exit(0)")
            os._exit(0)

    logger.info("Starting ProcessTerminator thread")
    threading.Thread(target=_terminator, name="MythosMUD-ProcessTerminator", daemon=True).start()
