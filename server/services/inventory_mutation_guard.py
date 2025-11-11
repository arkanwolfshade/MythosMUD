"""Concurrency and duplication guards for inventory mutations."""

from __future__ import annotations

import threading
from collections import OrderedDict
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from time import monotonic

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class MutationDecision:
    """Result of attempting to acquire a guarded mutation context."""

    should_apply: bool
    duplicate: bool = False


@dataclass
class _PlayerGuardState:
    """Internal state tracking per-player mutation metadata."""

    lock: threading.Lock = field(default_factory=threading.Lock)
    recent_tokens: OrderedDict[str, float] = field(default_factory=OrderedDict)


class InventoryMutationGuard:
    """
    Provide per-player locking and idempotency guarantees for inventory mutations.

    The guard enforces three invariants:
        1. Inventory mutations for a given player execute serially.
        2. Duplicate mutation tokens are suppressed in an idempotent fashion.
        3. Duplicate attempts are logged with moderation-friendly metadata.
    """

    def __init__(self, *, token_ttl_seconds: float = 300.0, max_tokens: int = 128):
        self._token_ttl = token_ttl_seconds
        self._max_tokens = max_tokens
        self._global_lock = threading.Lock()
        self._states: dict[str, _PlayerGuardState] = {}

    @contextmanager
    def acquire(self, player_id: str, token: str | None) -> Iterator[MutationDecision]:
        """
        Acquire a mutation context for the given player and token.

        Args:
            player_id: Identifier for the player whose inventory will mutate.
            token: Optional idempotency token unique to the attempted mutation.

        Yields:
            MutationDecision describing whether the caller should perform the mutation.
        """

        state = self._get_state(player_id)
        state.lock.acquire()
        duplicate_detected = False

        try:
            now = monotonic()
            self._prune_tokens(state, now)

            if token:
                if token in state.recent_tokens:
                    duplicate_detected = True
                    logger.warning(
                        "Duplicate inventory mutation suppressed",
                        player_id=player_id,
                        token=token,
                    )
                    decision = MutationDecision(should_apply=False, duplicate=True)
                    yield decision
                    return

                state.recent_tokens[token] = now
                self._enforce_limit(state)

            yield MutationDecision(should_apply=not duplicate_detected)
        finally:
            state.lock.release()
            if not state.recent_tokens:
                self._cleanup_state(player_id)

    def _get_state(self, player_id: str) -> _PlayerGuardState:
        with self._global_lock:
            return self._states.setdefault(player_id, _PlayerGuardState())

    def _cleanup_state(self, player_id: str) -> None:
        with self._global_lock:
            state = self._states.get(player_id)
            if state and not state.recent_tokens:
                # Ensure the lock is not currently held by another thread.
                if state.lock.acquire(blocking=False):
                    try:
                        if not state.recent_tokens:
                            self._states.pop(player_id, None)
                    finally:
                        state.lock.release()

    def _prune_tokens(self, state: _PlayerGuardState, now: float) -> None:
        if self._token_ttl <= 0:
            return

        expiry = now - self._token_ttl
        tokens_to_delete = [token for token, timestamp in state.recent_tokens.items() if timestamp < expiry]
        for token in tokens_to_delete:
            state.recent_tokens.pop(token, None)

    def _enforce_limit(self, state: _PlayerGuardState) -> None:
        while len(state.recent_tokens) > self._max_tokens:
            state.recent_tokens.popitem(last=False)


__all__ = ["InventoryMutationGuard", "MutationDecision"]
