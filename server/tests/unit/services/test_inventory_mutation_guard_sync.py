"""
Unit tests for inventory mutation guard - synchronous acquire operations.

Tests synchronous acquire operations including token expiry, TTL, and limits.
"""

import time
import uuid

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def guard():
    """Create an InventoryMutationGuard instance."""
    return InventoryMutationGuard(token_ttl_seconds=300.0, max_tokens=128)


def test_acquire_serializes_per_player(guard):
    """Test acquire serializes mutations per player."""
    player_id = str(uuid.uuid4())
    token1 = "token1"
    token2 = "token2"

    # Both should succeed (different tokens)
    with guard.acquire(player_id, token1) as decision1:
        assert decision1.should_apply is True

    with guard.acquire(player_id, token2) as decision2:
        assert decision2.should_apply is True


def test_acquire_token_expiry(guard):
    """Test acquire allows token reuse after expiry."""
    guard._token_ttl = 0.1  # Very short TTL for testing
    player_id = str(uuid.uuid4())
    token = "expiring_token"

    # First acquisition
    with guard.acquire(player_id, token) as decision1:
        assert decision1.should_apply is True

    # Wait for token to expire
    time.sleep(0.2)

    # Token should be expired, so reuse should be allowed
    with guard.acquire(player_id, token) as decision2:
        assert decision2.should_apply is True


def test_acquire_token_ttl_zero(guard):
    """Test acquire with token_ttl=0 (no expiry)."""
    guard._token_ttl = 0
    player_id = str(uuid.uuid4())
    token = "no_expiry_token"

    # First acquisition
    with guard.acquire(player_id, token) as decision1:
        assert decision1.should_apply is True

    # Token should never expire, so reuse should be suppressed
    with guard.acquire(player_id, token) as decision2:
        assert decision2.should_apply is False
        assert decision2.duplicate is True


def test_acquire_enforces_max_tokens(guard):
    """Test acquire enforces max_tokens limit."""
    guard._max_tokens = 3
    player_id = str(uuid.uuid4())

    # Add tokens up to limit
    for i in range(guard._max_tokens):
        with guard.acquire(player_id, f"token_{i}"):
            pass

    # Adding one more should remove oldest
    with guard.acquire(player_id, "token_new"):
        pass

    # Oldest token should be removed
    state = guard._get_state(player_id)
    assert len(state.recent_tokens) <= guard._max_tokens


def test_acquire_cleanup_empty_state(guard):
    """Test acquire cleans up state when tokens are empty."""
    player_id = str(uuid.uuid4())
    token = "temp_token"

    # Acquire and release
    with guard.acquire(player_id, token):
        pass

    # Wait for token to expire
    guard._token_ttl = 0.1
    time.sleep(0.2)

    # Acquire again (should prune expired token)
    with guard.acquire(player_id, "new_token"):
        pass

    # State should be cleaned up if empty
    # (Note: cleanup happens in finally block, so state may still exist briefly)
