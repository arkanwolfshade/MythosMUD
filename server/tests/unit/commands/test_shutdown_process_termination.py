"""Unit tests for shutdown process termination."""

import signal
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import cast
from unittest.mock import patch

import psutil
import pytest

from server.commands import shutdown_process_termination as spt

MODULE = "server.commands.shutdown_process_termination"


@dataclass
class FakeProcess:
    """Stands in for a psutil.Process: an ancestor with a command line, or ourselves with ancestors."""

    command: list[str] = field(default_factory=lambda: cast(list[str], []))
    pid: int = 10
    ancestors: list["FakeProcess"] = field(default_factory=lambda: cast(list["FakeProcess"], []))
    parents_error: Exception | None = None
    terminated: bool = False

    def cmdline(self) -> list[str]:
        return self.command

    def parents(self) -> list["FakeProcess"]:
        if self.parents_error is not None:
            raise self.parents_error
        return self.ancestors

    def terminate(self) -> None:
        self.terminated = True


@dataclass
class Outcome:
    signals: list[int] = field(default_factory=lambda: cast(list[int], []))
    exits: list[int] = field(default_factory=lambda: cast(list[int], []))
    iterated_all_processes: bool = False


def test_schedule_process_termination_disabled_by_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """schedule_process_termination returns early when exit is disabled."""
    monkeypatch.setenv("MYTHOSMUD_DISABLE_PROCESS_EXIT", "1")
    with patch(f"{MODULE}.threading.Thread") as mock_thread:
        spt.schedule_process_termination()
    assert not mock_thread.called


def test_schedule_process_termination_starts_thread(monkeypatch: pytest.MonkeyPatch) -> None:
    """schedule_process_termination starts daemon thread when enabled."""
    monkeypatch.delenv("MYTHOSMUD_DISABLE_PROCESS_EXIT", raising=False)
    with patch(f"{MODULE}.threading.Thread") as mock_thread:
        spt.schedule_process_termination(0.1)
    assert mock_thread.call_count == 1
    kwargs = cast(dict[str, object], mock_thread.call_args.kwargs)
    assert kwargs["daemon"] is True
    assert kwargs["name"] == "MythosMUD-ProcessTerminator"


def _run_terminator(monkeypatch: pytest.MonkeyPatch, me: FakeProcess) -> Outcome:
    """Capture the terminator thread body and run it once with sleeping, signals and exit stubbed."""
    monkeypatch.delenv("MYTHOSMUD_DISABLE_PROCESS_EXIT", raising=False)
    captured: list[Callable[[], None]] = []
    outcome = Outcome()

    class ThreadStub:
        def __init__(self, target: Callable[[], None], name: str, daemon: bool) -> None:
            _ = name, daemon
            captured.append(target)

        def start(self) -> None:
            return None

    def process_iter(*_args: object, **_kwargs: object) -> list[object]:
        outcome.iterated_all_processes = True
        return []

    def no_sleep(_seconds: float) -> None:
        return None

    monkeypatch.setattr(f"{MODULE}.threading.Thread", ThreadStub)
    monkeypatch.setattr(f"{MODULE}.time.sleep", no_sleep)
    monkeypatch.setattr(f"{MODULE}.psutil.Process", lambda: me)
    monkeypatch.setattr(f"{MODULE}.psutil.process_iter", process_iter)
    monkeypatch.setattr(f"{MODULE}.signal.raise_signal", outcome.signals.append)
    monkeypatch.setattr(f"{MODULE}.os._exit", outcome.exits.append)

    spt.schedule_process_termination(0.0)
    captured[0]()
    return outcome


def test_terminator_stops_the_reloader_then_asks_uvicorn_to_exit(monkeypatch: pytest.MonkeyPatch) -> None:
    shim = FakeProcess(["python", "-c", "spawn_main"])
    reloader = FakeProcess(["python", "uvicorn", "server.main:app", "--reload"])

    outcome = _run_terminator(monkeypatch, FakeProcess(ancestors=[shim, reloader]))

    assert reloader.terminated
    assert not shim.terminated
    assert outcome.signals == [signal.SIGINT]
    assert outcome.exits == [0]  # the backstop, reached because the stubbed SIGINT ended nothing


def test_terminator_leaves_unrelated_ancestors_alone(monkeypatch: pytest.MonkeyPatch) -> None:
    """A uvicorn without --reload, or any other parent, is not this server's supervisor to kill."""
    plain_uvicorn = FakeProcess(["python", "uvicorn", "server.main:app"])
    shell = FakeProcess(["pwsh", "-File", "start_local.ps1"])

    outcome = _run_terminator(monkeypatch, FakeProcess(ancestors=[plain_uvicorn, shell]))

    assert not plain_uvicorn.terminated
    assert not shell.terminated
    assert outcome.signals == [signal.SIGINT]


@pytest.mark.parametrize("error", [psutil.NoSuchProcess(1), psutil.AccessDenied(1)])
def test_terminator_still_exits_when_the_reloader_cannot_be_inspected(
    monkeypatch: pytest.MonkeyPatch, error: Exception
) -> None:
    outcome = _run_terminator(monkeypatch, FakeProcess(parents_error=error))

    assert outcome.signals == [signal.SIGINT]


def test_terminator_never_enumerates_other_processes(monkeypatch: pytest.MonkeyPatch) -> None:
    """The old behavior terminated every process on the machine named uvicorn; only ancestors are considered now."""
    outcome = _run_terminator(monkeypatch, FakeProcess())

    assert not outcome.iterated_all_processes
