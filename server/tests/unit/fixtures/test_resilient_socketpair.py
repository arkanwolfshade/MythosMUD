"""The test event loop's self-pipe must not hang a whole run when one loopback connection is lost."""

import socket

import pytest

from server.tests import socketpair as socketpair_module
from server.tests.socketpair import ATTEMPTS, SocketPair, resilient_socketpair


def _lost_connection() -> SocketPair:
    """What CPython's fallback does when the client's connect is lost: wait in accept() for nobody."""
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen()
        _ = listener.accept()
    raise AssertionError("accept() returned with no client")


@pytest.fixture(autouse=True)
def _short_accept_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(socketpair_module, "ACCEPT_TIMEOUT_SECONDS", 0.05)


def test_a_lost_connection_is_retried() -> None:
    calls: list[int] = []

    def lost_once() -> SocketPair:
        calls.append(1)
        return _lost_connection() if len(calls) == 1 else socket.socketpair()

    first, second = resilient_socketpair(lost_once)()

    with first, second:
        assert len(calls) == 2


def test_a_connection_that_stays_lost_fails_only_the_caller() -> None:
    calls: list[int] = []

    def always_lost() -> SocketPair:
        calls.append(1)
        return _lost_connection()

    with pytest.raises(TimeoutError):
        _ = resilient_socketpair(always_lost)()

    assert len(calls) == ATTEMPTS
    assert socket.getdefaulttimeout() is None


def test_the_pair_behaves_like_a_plain_socketpair() -> None:
    first, second = resilient_socketpair(socket.socketpair)()

    with first, second:
        assert socket.getdefaulttimeout() is None
        assert first.gettimeout() is None
        assert second.gettimeout() is None
        assert first.getsockopt(socket.SOL_SOCKET, socket.SO_LINGER) != 0
        _ = first.send(b"x")
        assert second.recv(1) == b"x"
