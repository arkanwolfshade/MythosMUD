"""Unit tests for shutdown process termination helpers."""

from unittest.mock import MagicMock, patch

from server.commands import shutdown_process_termination as spt


def test_schedule_process_termination_disabled_by_env(monkeypatch):
    """schedule_process_termination returns early when exit is disabled."""
    monkeypatch.setenv("MYTHOSMUD_DISABLE_PROCESS_EXIT", "1")
    with patch("server.commands.shutdown_process_termination.threading.Thread") as mock_thread:
        spt.schedule_process_termination()
    mock_thread.assert_not_called()


def test_schedule_process_termination_starts_thread(monkeypatch):
    """schedule_process_termination starts daemon thread when enabled."""
    monkeypatch.delenv("MYTHOSMUD_DISABLE_PROCESS_EXIT", raising=False)
    with patch("server.commands.shutdown_process_termination.threading.Thread") as mock_thread:
        spt.schedule_process_termination(0.1)
    mock_thread.assert_called_once()
    kwargs = mock_thread.call_args.kwargs
    assert kwargs["daemon"] is True
    assert kwargs["name"] == "MythosMUD-ProcessTerminator"


def test_find_uvicorn_processes_collects_uvicorn_names():
    """_find_uvicorn_processes returns processes whose name contains uvicorn."""
    good = MagicMock()
    good.info = {"pid": 2, "name": "uvicorn-worker"}
    other = MagicMock()
    other.info = {"pid": 3, "name": "python"}

    with patch("psutil.process_iter", return_value=[good, other]):
        result = spt._find_uvicorn_processes()

    assert result == [good]


def test_terminate_with_signals_sends_to_child_and_parent():
    """_terminate_with_signals attempts SIGINT and SIGTERM on child and parent."""
    with patch("server.commands.shutdown_process_termination.os.kill") as mock_kill:
        with patch("server.commands.shutdown_process_termination.time.sleep"):
            spt._terminate_with_signals(pid=100, ppid=200)
    assert mock_kill.call_count >= 2


def test_terminate_uvicorn_processes_kills_stubborn():
    """_terminate_uvicorn_processes kills processes still running after terminate."""
    proc = MagicMock()
    proc.info = {"pid": 42}
    proc.is_running.side_effect = [True, False]
    proc.kill = MagicMock()

    with patch("server.commands.shutdown_process_termination.time.sleep"):
        with patch("psutil.NoSuchProcess", Exception):
            with patch("psutil.AccessDenied", Exception):
                spt._terminate_uvicorn_processes([proc])

    proc.terminate.assert_called_once()
    proc.kill.assert_called_once()


def test_terminate_child_processes():
    """_terminate_child_processes terminates and kills surviving children."""
    child = MagicMock()
    child.pid = 7
    child.name.return_value = "worker"
    parent = MagicMock()
    parent.children.return_value = [child]

    with patch("psutil.Process", return_value=parent):
        with patch("psutil.wait_procs", return_value=([], [child])):
            with patch("psutil.NoSuchProcess", Exception):
                spt._terminate_child_processes(pid=1)

    child.terminate.assert_called_once()
    child.kill.assert_called_once()


def test_terminator_thread_import_error_falls_back_to_signals(monkeypatch):
    """Terminator thread uses signal fallback when psutil import fails."""
    monkeypatch.delenv("MYTHOSMUD_DISABLE_PROCESS_EXIT", raising=False)

    captured_target = {}

    class _ThreadStub:
        def __init__(self, target=None, name=None, daemon=None):
            captured_target["fn"] = target

        def start(self):
            return None

    with patch("server.commands.shutdown_process_termination.threading.Thread", _ThreadStub):
        with patch("server.commands.shutdown_process_termination.time.sleep"):
            with patch("server.commands.shutdown_process_termination._find_uvicorn_processes", side_effect=ImportError):
                with patch("server.commands.shutdown_process_termination._terminate_with_signals") as mock_signals:
                    with patch("server.commands.shutdown_process_termination.os._exit") as mock_exit:
                        spt.schedule_process_termination(0.0)
                        captured_target["fn"]()

    mock_signals.assert_called_once()
    mock_exit.assert_called_once_with(0)
