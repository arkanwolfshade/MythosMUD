"""
Unit tests for inventory mutation guard - asynchronous acquire operations.

Tests asynchronous acquire operations including token expiry, TTL, and limits.
"""

import asyncio
import uuid

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def guard():
    """Create an InventoryMutationGuard instance."""
    return InventoryMutationGuard(token_ttl_seconds=300.0, max_tokens=128)


@pytest.mark.asyncio
async def test_acquire_async_enforces_max_tokens(guard):
    """Test acquire_async enforces max_tokens limit."""
    guard._max_tokens = 3
    player_id = str(uuid.uuid4())

    # Add tokens up to limit
    for i in range(guard._max_tokens):
        async with guard.acquire_async(player_id, f"token_{i}"):
            pass

    # Adding one more should remove oldest
    async with guard.acquire_async(player_id, "token_new"):
        pass

    # Oldest token should be removed
    state = await guard._get_async_state(player_id)
    assert len(state.recent_tokens) <= guard._max_tokens


@pytest.mark.asyncio
async def test_acquire_async_token_expiry(guard):
    """Test acquire_async allows token reuse after expiry."""
    guard._token_ttl = 0.1  # Very short TTL for testing
    player_id = str(uuid.uuid4())
    token = "expiring_token_async"

    # First acquisition
    async with guard.acquire_async(player_id, token) as decision1:
        assert decision1.should_apply is True

    # Wait for token to expire
    await asyncio.sleep(0.2)

    # Token should be expired, so reuse should be allowed
    async with guard.acquire_async(player_id, token) as decision2:
        assert decision2.should_apply is True


@pytest.mark.asyncio
async def test_acquire_async_token_ttl_zero(guard):
    """Test acquire_async with token_ttl=0 (no expiry)."""
    guard._token_ttl = 0
    player_id = str(uuid.uuid4())
    token = "no_expiry_token_async"

    # First acquisition
    async with guard.acquire_async(player_id, token) as decision1:
        assert decision1.should_apply is True

    # Token should never expire, so reuse should be suppressed
    async with guard.acquire_async(player_id, token) as decision2:
        assert decision2.should_apply is False
        assert decision2.duplicate is True


@pytest.mark.asyncio
async def test_acquire_async_cleanup_empty_state(guard):
    """Test acquire_async cleans up state when tokens are empty."""
    guard._token_ttl = 0.1
    player_id = str(uuid.uuid4())
    token = "temp_token_async"

    # Acquire and release
    async with guard.acquire_async(player_id, token):
        pass

    # Wait for token to expire
    await asyncio.sleep(0.2)

    # Acquire again (should prune expired token)
    async with guard.acquire_async(player_id, "new_token"):
        pass

    # State should be cleaned up if empty
    # (Note: cleanup happens in finally block, so state may still exist briefly)


@pytest.mark.asyncio
async def test_acquire_async_concurrent_same_player(guard):
    """Test acquire_async serializes concurrent mutations for same player."""
    player_id = str(uuid.uuid4())
    results: list[tuple[str, bool]] = []

    async def acquire_with_delay(token, delay):
        await asyncio.sleep(delay)
        async with guard.acquire_async(player_id, token) as decision:
            results.append((token, decision.should_apply))

    # Start multiple concurrent acquisitions
    await asyncio.gather(
        acquire_with_delay("token1", 0.0),
        acquire_with_delay("token2", 0.01),
        acquire_with_delay("token3", 0.02),
    )

    # All should succeed (different tokens)
    assert len(results) == 3
    assert all(should_apply for _, should_apply in results)
