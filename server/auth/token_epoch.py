"""Auth token epoch for server-restart invalidation.

All JWTs issued before the current server process started must be rejected.
This module holds the current auth epoch (set at startup); tokens must
include this epoch and validation rejects any token with a different or
missing epoch.
"""

from __future__ import annotations

_auth_epoch: str | None = None


def set_auth_epoch(epoch: str) -> None:
    """Set the current auth epoch (call once at server startup)."""
    global _auth_epoch  # noqa: PLW0603  # pylint: disable=global-statement  # Reason: Single process-wide epoch for restart invalidation
    _auth_epoch = epoch


def get_auth_epoch() -> str:
    """Return the current auth epoch. Must be set before any token validation."""
    if _auth_epoch is None:
        raise RuntimeError("Auth epoch not set - server startup may not have completed")
    return _auth_epoch
