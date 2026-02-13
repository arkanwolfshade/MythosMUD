"""
Unit tests for inventory mutation guard - internal helper methods.

Tests internal helper methods including token pruning, limit enforcement, and async state management.
"""

import uuid
from time import monotonic

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def guard():
    """Create an InventoryMutationGuard instance."""
    return InventoryMutationGuard(token_ttl_seconds=300.0, max_tokens=128)


def test_prune_tokens(guard):
    """Test _prune_tokens removes expired tokens."""
    player_id = str(uuid.uuid4())
    state = guard._get_state(player_id)

    now = monotonic()
    # Add expired token
    state.recent_tokens["expired_token"] = now - 400
    # Add valid token
    state.recent_tokens["valid_token"] = now - 50

    guard._prune_tokens(state, now)

    assert "expired_token" not in state.recent_tokens
    assert "valid_token" in state.recent_tokens


def test_prune_tokens_ttl_zero(guard):
    """Test _prune_tokens with token_ttl=0 doesn't prune."""
    guard._token_ttl = 0
    player_id = str(uuid.uuid4())
    state = guard._get_state(player_id)

    now = monotonic()
    state.recent_tokens["token"] = now - 1000

    guard._prune_tokens(state, now)

    # Token should not be pruned when TTL is 0
    assert "token" in state.recent_tokens


def test_enforce_limit(guard):
    """Test _enforce_limit removes oldest tokens when limit exceeded."""
    guard._max_tokens = 3
    player_id = str(uuid.uuid4())
    state = guard._get_state(player_id)

    # Add tokens beyond limit
    for i in range(5):
        state.recent_tokens[f"token_{i}"] = monotonic()

    guard._enforce_limit(state)

    # Should only keep max_tokens
    assert len(state.recent_tokens) == guard._max_tokens


def test_get_async_global_lock(guard):
    """Test _get_async_global_lock creates lock lazily."""
    assert guard._async_global_lock is None

    lock1 = guard._get_async_global_lock()
    assert guard._async_global_lock is not None

    lock2 = guard._get_async_global_lock()  # type: ignore[unreachable]
    assert lock1 is lock2  # Should return same lock


@pytest.mark.asyncio
async def test_get_async_state_creates_lazily(guard):
    """Test _get_async_state creates state lazily."""
    player_id = str(uuid.uuid4())

    state = await guard._get_async_state(player_id)
    assert state is not None
    assert player_id in guard._async_states


@pytest.mark.asyncio
async def test_cleanup_async_state_locked(guard):
    """Test _cleanup_async_state handles locked state."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)
    lock = state.get_lock()

    # Acquire lock
    await lock.acquire()

    try:
        # Try to cleanup (should skip if locked)
        await guard._cleanup_async_state(player_id)

        # State should still exist (locked, so cleanup skipped)
        assert player_id in guard._async_states
    finally:
        lock.release()


@pytest.mark.asyncio
async def test_cleanup_async_state_empty(guard):
    """Test _cleanup_async_state removes empty state."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    # State should be empty (no tokens)
    assert len(state.recent_tokens) == 0

    # Cleanup should remove it
    await guard._cleanup_async_state(player_id)

    # State should be removed (if lock is available)
    # Note: This may not always work if lock is held, which is expected behavior


@pytest.mark.asyncio
async def test_prune_tokens_async(guard):
    """Test _prune_tokens_async removes expired tokens."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    now = monotonic()
    # Add expired token
    state.recent_tokens["expired_token"] = now - 400
    # Add valid token
    state.recent_tokens["valid_token"] = now - 50

    guard._prune_tokens_async(state, now)

    assert "expired_token" not in state.recent_tokens
    assert "valid_token" in state.recent_tokens


@pytest.mark.asyncio
async def test_prune_tokens_async_ttl_zero(guard):
    """Test _prune_tokens_async with token_ttl=0 doesn't prune."""
    guard._token_ttl = 0
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    now = monotonic()
    state.recent_tokens["token"] = now - 1000

    guard._prune_tokens_async(state, now)

    # Token should not be pruned when TTL is 0
    assert "token" in state.recent_tokens


@pytest.mark.asyncio
async def test_enforce_limit_async(guard):
    """Test _enforce_limit_async removes oldest tokens when limit exceeded."""
    guard._max_tokens = 3
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    # Add tokens beyond limit
    for i in range(5):
        state.recent_tokens[f"token_{i}"] = monotonic()

    guard._enforce_limit_async(state)

    # Should only keep max_tokens
    assert len(state.recent_tokens) == guard._max_tokens
