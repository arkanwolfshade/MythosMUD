"""Concurrency and duplication guards for inventory mutations."""

from __future__ import annotations

import inspect
import threading
from collections import OrderedDict
from collections.abc import AsyncIterator, Callable, Iterator, Mapping
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass, field
from time import monotonic
from typing import cast

from anyio import Lock

from server.middleware.metrics_collector import metrics_collector
from server.monitoring.monitoring_dashboard import get_monitoring_dashboard
from server.structured_logging.enhanced_logging_config import get_logger

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


@dataclass
class _AsyncPlayerGuardState:
    """Internal state tracking per-player mutation metadata for async contexts."""

    lock: Lock | None = None
    recent_tokens: OrderedDict[str, float] = field(default_factory=OrderedDict)

    def get_lock(self) -> Lock:
        """Get or create the async lock (lazy initialization)."""
        if self.lock is None:
            self.lock = Lock()
        return self.lock


class InventoryMutationGuard:
    """
    Provide per-player locking and idempotency guarantees for inventory mutations.

    The guard enforces three invariants:
        1. Inventory mutations for a given player execute serially.
        2. Duplicate mutation tokens are suppressed in an idempotent fashion.
        3. Duplicate attempts are logged with moderation-friendly metadata.

    Supports both sync and async contexts:
    - Use `acquire()` for sync contexts (with statement)
    - Use `acquire_async()` for async contexts (async with statement)
    """

    def __init__(self, *, token_ttl_seconds: float = 300.0, max_tokens: int = 128) -> None:
        self._token_ttl = token_ttl_seconds
        self._max_tokens = max_tokens
        self._global_lock = threading.Lock()
        self._async_global_lock: Lock | None = None
        self._states: dict[str, _PlayerGuardState] = {}
        self._async_states: dict[str, _AsyncPlayerGuardState] = {}

    def _get_async_global_lock(self) -> Lock:
        """Get or create the async global lock (lazy initialization)."""
        if self._async_global_lock is None:
            self._async_global_lock = Lock()
        return self._async_global_lock

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

        try:  # pylint: disable=too-many-nested-blocks  # Reason: Mutation guard requires complex nested logic for token validation, duplicate detection, and state management
            now = monotonic()
            self._prune_tokens(state, now)

            if token:
                if token in state.recent_tokens:
                    duplicate_detected = True
                    logger.warning(
                        "Duplicate inventory mutation suppressed",
                        player_id=player_id,
                        token=token,
                        alert="inventory_duplicate",
                        duplicate_token=True,
                        cached_tokens=len(state.recent_tokens),
                    )
                    metrics_collector.record_message_failed("inventory_mutation", "duplicate_token")
                    dashboard = get_monitoring_dashboard()
                    alert_metadata = {
                        "player_id": player_id,
                        "token": token,
                        "cached_tokens": len(state.recent_tokens),
                    }
                    record_custom_alert = getattr(dashboard, "record_custom_alert", None)
                    if callable(record_custom_alert):
                        # Type assertion: after callable() check, we know it's callable
                        record_custom_alert = cast(Callable[..., None], record_custom_alert)
                        try:
                            parameters: Mapping[str, inspect.Parameter]
                            parameters = inspect.signature(record_custom_alert).parameters
                        except (TypeError, ValueError):
                            parameters = cast(Mapping[str, inspect.Parameter], {})
                        # After callable() check and cast, we know record_custom_alert is callable
                        # pylint: disable=not-callable  # Reason: Dynamic callable check with cast ensures function is callable, but pylint cannot infer this from runtime checks
                        try:
                            if "message" in parameters:
                                record_custom_alert(  # pylint: disable=not-callable  # Reason: Verified callable via callable() check and cast above, but pylint cannot infer from runtime checks
                                    "inventory_duplicate",
                                    severity="warning",
                                    message=f"Duplicate inventory mutation suppressed for player {player_id}",
                                    metadata=alert_metadata,
                                )
                            else:
                                # Legacy signature compatibility: (alert_type, *, severity=..., metadata=...)
                                record_custom_alert(  # pylint: disable=not-callable  # Reason: Verified callable via callable() check and cast above, but pylint cannot infer from runtime checks
                                    "inventory_duplicate",
                                    severity="warning",
                                    metadata=alert_metadata,
                                )
                        except TypeError:
                            # Fallback to safest keyword invocation if signature introspection was misleading
                            try:
                                record_custom_alert(  # pylint: disable=not-callable  # Reason: Verified callable via callable() check and cast above, but pylint cannot infer from runtime checks
                                    "inventory_duplicate",
                                    severity="warning",
                                    metadata=alert_metadata,
                                )
                            except TypeError:
                                # If fallback also fails, silently ignore - alert recording is non-critical
                                pass
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

    @asynccontextmanager
    async def acquire_async(self, player_id: str, token: str | None) -> AsyncIterator[MutationDecision]:
        """
        Acquire a mutation context for the given player and token (async version).

        Args:
            player_id: Identifier for the player whose inventory will mutate.
            token: Optional idempotency token unique to the attempted mutation.

        Yields:
            MutationDecision describing whether the caller should perform the mutation.
        """
        state = await self._get_async_state(player_id)
        lock = state.get_lock()
        await lock.acquire()
        duplicate_detected = False

        try:  # pylint: disable=too-many-nested-blocks  # Reason: Async mutation guard requires complex nested logic for token validation, duplicate detection, and async state management
            now = monotonic()
            self._prune_tokens_async(state, now)

            if token:
                if token in state.recent_tokens:
                    duplicate_detected = True
                    logger.warning(
                        "Duplicate inventory mutation suppressed",
                        player_id=player_id,
                        token=token,
                        alert="inventory_duplicate",
                        duplicate_token=True,
                        cached_tokens=len(state.recent_tokens),
                    )
                    metrics_collector.record_message_failed("inventory_mutation", "duplicate_token")
                    dashboard = get_monitoring_dashboard()
                    alert_metadata = {
                        "player_id": player_id,
                        "token": token,
                        "cached_tokens": len(state.recent_tokens),
                    }
                    record_custom_alert = getattr(dashboard, "record_custom_alert", None)
                    if callable(record_custom_alert):
                        # Type assertion: after callable() check, we know it's callable
                        record_custom_alert = cast(Callable[..., None], record_custom_alert)
                        try:
                            parameters: Mapping[str, inspect.Parameter]
                            parameters = inspect.signature(record_custom_alert).parameters
                        except (TypeError, ValueError):
                            parameters = cast(Mapping[str, inspect.Parameter], {})
                        # After callable() check and cast, we know record_custom_alert is callable
                        # pylint: disable=not-callable  # Reason: Dynamic callable check with cast ensures function is callable, but pylint cannot infer this from runtime checks
                        try:
                            if "message" in parameters:
                                record_custom_alert(  # pylint: disable=not-callable  # Reason: Verified callable via callable() check and cast above, but pylint cannot infer from runtime checks
                                    "inventory_duplicate",
                                    severity="warning",
                                    message=f"Duplicate inventory mutation suppressed for player {player_id}",
                                    metadata=alert_metadata,
                                )
                            else:
                                # Legacy signature compatibility: (alert_type, *, severity=..., metadata=...)
                                record_custom_alert(  # pylint: disable=not-callable  # Reason: Verified callable via callable() check and cast above, but pylint cannot infer from runtime checks
                                    "inventory_duplicate",
                                    severity="warning",
                                    metadata=alert_metadata,
                                )
                        except TypeError:
                            # Fallback to safest keyword invocation if signature introspection was misleading
                            try:
                                record_custom_alert(  # pylint: disable=not-callable  # Reason: Verified callable via callable() check and cast above, but pylint cannot infer from runtime checks
                                    "inventory_duplicate",
                                    severity="warning",
                                    metadata=alert_metadata,
                                )
                            except TypeError:
                                # If fallback also fails, silently ignore - alert recording is non-critical
                                pass
                    decision = MutationDecision(should_apply=False, duplicate=True)
                    yield decision
                    return

                state.recent_tokens[token] = now
                self._enforce_limit_async(state)

            yield MutationDecision(should_apply=not duplicate_detected)
        finally:
            lock.release()
            if not state.recent_tokens:
                await self._cleanup_async_state(player_id)

    def _get_state(self, player_id: str) -> _PlayerGuardState:
        """
        Get or create per-player guard state for sync contexts.

        Uses thread-safe dictionary access with the global lock to ensure state creation
        is atomic. The setdefault pattern ensures only one state object exists per player_id.

        Args:
            player_id: Identifier for the player

        Returns:
            Guard state for the player, creating it if it doesn't exist
        """
        with self._global_lock:
            return self._states.setdefault(player_id, _PlayerGuardState())

    async def _get_async_state(self, player_id: str) -> _AsyncPlayerGuardState:
        """
        Get or create per-player guard state for async contexts.

        Uses async lock to ensure thread-safe state creation. The async global lock
        prevents race conditions when multiple async contexts access the states dict
        concurrently. The per-player lock (stored in the state) is used for serializing
        mutations for that specific player.

        Args:
            player_id: Identifier for the player

        Returns:
            Guard state for the player, creating it if it doesn't exist
        """
        async_lock = self._get_async_global_lock()
        async with async_lock:
            if player_id not in self._async_states:
                self._async_states[player_id] = _AsyncPlayerGuardState()
            return self._async_states[player_id]

    def _cleanup_state(self, player_id: str) -> None:
        """
        Clean up per-player guard state when no longer needed (sync context).

        Removes the player's state from the states dictionary if:
        1. The state exists
        2. No recent tokens are cached (state is idle)
        3. The per-player lock is available (not currently held)

        The non-blocking lock acquisition prevents cleanup from blocking if a mutation
        is in progress. If the lock is held, cleanup is skipped and will be retried
        on the next idle period.

        Args:
            player_id: Identifier for the player whose state should be cleaned up
        """
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

    async def _cleanup_async_state(self, player_id: str) -> None:
        """
        Clean up per-player guard state when no longer needed (async context).

        Removes the player's state from the async_states dictionary if:
        1. The state exists
        2. No recent tokens are cached (state is idle)
        3. The per-player async lock is available (not currently held)

        Uses lock.locked() check instead of non-blocking acquire because asyncio.Lock
        doesn't support non-blocking acquisition. If the lock is held, cleanup is
        skipped and will be retried on the next idle period.

        The defensive exception handling for lock.locked() ensures cleanup doesn't fail
        if the lock implementation changes or is in an unexpected state.

        Args:
            player_id: Identifier for the player whose state should be cleaned up
        """
        async_lock = self._get_async_global_lock()
        async with async_lock:
            state = self._async_states.get(player_id)
            if state and not state.recent_tokens:
                # Try to acquire lock non-blocking to check if it's free
                lock = state.get_lock()
                # Use try/except for lock.locked() to handle cases where
                # the method might not be available or the lock is in an inconsistent state
                try:
                    if lock.locked():
                        # Lock is held, can't cleanup yet
                        return
                except (AttributeError, RuntimeError):
                    # If locked() method is not available or raises an error,
                    # assume lock might be held and skip cleanup to be safe
                    return
                # Lock is free, safe to cleanup
                if not state.recent_tokens:
                    self._async_states.pop(player_id, None)

    def _prune_tokens(self, state: _PlayerGuardState, now: float) -> None:
        """
        Remove expired idempotency tokens from the guard state (sync context).

        Tokens older than token_ttl_seconds are removed to prevent unbounded memory growth.
        This is called before checking for duplicates to ensure the token cache doesn't
        retain stale entries indefinitely.

        Args:
            state: Guard state for the player
            now: Current monotonic time for expiration comparison
        """
        if self._token_ttl <= 0:
            return

        expiry = now - self._token_ttl
        tokens_to_delete = [token for token, timestamp in state.recent_tokens.items() if timestamp < expiry]
        for token in tokens_to_delete:
            state.recent_tokens.pop(token, None)

    def _prune_tokens_async(self, state: _AsyncPlayerGuardState, now: float) -> None:
        """
        Remove expired idempotency tokens from the guard state (async context).

        Tokens older than token_ttl_seconds are removed to prevent unbounded memory growth.
        This is called before checking for duplicates to ensure the token cache doesn't
        retain stale entries indefinitely.

        Args:
            state: Guard state for the player
            now: Current monotonic time for expiration comparison
        """
        if self._token_ttl <= 0:
            return

        expiry = now - self._token_ttl
        tokens_to_delete = [token for token, timestamp in state.recent_tokens.items() if timestamp < expiry]
        for token in tokens_to_delete:
            state.recent_tokens.pop(token, None)

    def _enforce_limit(self, state: _PlayerGuardState) -> None:
        """
        Enforce maximum token cache size by removing oldest entries (sync context).

        Uses OrderedDict's FIFO ordering (popitem(last=False)) to remove the oldest
        token when the cache exceeds max_tokens. This prevents unbounded memory growth
        while preserving recent duplicate detection capability.

        Args:
            state: Guard state for the player
        """
        while len(state.recent_tokens) > self._max_tokens:
            state.recent_tokens.popitem(last=False)

    def _enforce_limit_async(self, state: _AsyncPlayerGuardState) -> None:
        """
        Enforce maximum token cache size by removing oldest entries (async context).

        Uses OrderedDict's FIFO ordering (popitem(last=False)) to remove the oldest
        token when the cache exceeds max_tokens. This prevents unbounded memory growth
        while preserving recent duplicate detection capability.

        Args:
            state: Guard state for the player
        """
        while len(state.recent_tokens) > self._max_tokens:
            state.recent_tokens.popitem(last=False)


__all__ = ["InventoryMutationGuard", "MutationDecision"]
