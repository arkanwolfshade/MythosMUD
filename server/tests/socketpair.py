"""A socket.socketpair() for Windows test runs: it frees its port on close and survives a lost loopback connection."""

import functools
import socket
import struct
from collections.abc import Callable

type SocketPair = tuple[socket.socket, socket.socket]

# SO_LINGER (on, 0 s): close() sends RST instead of FIN, so the connection skips TIME_WAIT and frees its port at once.
_ABORTIVE_CLOSE = struct.pack("ii", 1, 0)

# A healthy pair takes about a millisecond, so a whole attempt going by means its connection is gone.
ACCEPT_TIMEOUT_SECONDS = 1.0
ATTEMPTS = 5


def resilient_socketpair[**P](original: Callable[P, SocketPair]) -> Callable[P, SocketPair]:
    """Wrap socket.socketpair(): bound its accept(), retry a lost connection, close abortively; same signature."""

    @functools.wraps(original)
    def socketpair(*args: P.args, **kwargs: P.kwargs) -> SocketPair:
        previous_timeout = socket.getdefaulttimeout()
        # shortcut: a socket another thread creates during this call also gets the timeout; no test does that today,
        # copy CPython's fallback here and time out only its listener if one ever does.
        socket.setdefaulttimeout(ACCEPT_TIMEOUT_SECONDS)
        try:
            for _ in range(ATTEMPTS - 1):
                try:
                    pair = original(*args, **kwargs)
                    break
                except TimeoutError:
                    continue
            else:
                pair = original(*args, **kwargs)  # a TimeoutError here fails one test, not the whole run
        finally:
            socket.setdefaulttimeout(previous_timeout)
        for sock in pair:
            sock.setblocking(True)  # accept() handed one end the default timeout
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, _ABORTIVE_CLOSE)
        return pair

    return socketpair
