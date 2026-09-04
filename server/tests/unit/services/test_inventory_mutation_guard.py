"""
Unit tests for inventory mutation guard - core functionality.

Tests initialization, MutationDecision, and basic acquire operations.
"""

import uuid

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard, MutationDecision

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def guard():
    """Create an InventoryMutationGuard instance."""
    return InventoryMutationGuard(token_ttl_seconds=300.0, max_tokens=128)


def test_mutation_decision_init():
    """Test MutationDecision initialization."""
    decision = MutationDecision(should_apply=True, duplicate=False)
    assert decision.should_apply is True
    assert decision.duplicate is False


def test_mutation_decision_duplicate():
    """Test MutationDecision for duplicate."""
    decision = MutationDecision(should_apply=False, duplicate=True)
    assert decision.should_apply is False
    assert decision.duplicate is True


def test_inventory_mutation_guard_init(guard):
    """Test InventoryMutationGuard initialization."""
    assert guard._token_ttl == 300.0
    assert guard._max_tokens == 128
    assert guard._states == {}
    assert guard._async_states == {}


def test_inventory_mutation_guard_init_custom_params():
    """Test InventoryMutationGuard initialization with custom parameters."""
    guard = InventoryMutationGuard(token_ttl_seconds=600.0, max_tokens=256)
    assert guard._token_ttl == 600.0
    assert guard._max_tokens == 256


def test_acquire_without_token(guard):
    """Test acquire without token allows mutation."""
    player_id = str(uuid.uuid4())

    with guard.acquire(player_id, None) as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


def test_acquire_with_unique_token(guard):
    """Test acquire with unique token allows mutation."""
    player_id = str(uuid.uuid4())
    token = "unique_token_123"

    with guard.acquire(player_id, token) as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


def test_acquire_with_duplicate_token(guard):
    """Test acquire with duplicate token suppresses mutation."""
    player_id = str(uuid.uuid4())
    token = "duplicate_token_123"

    # First acquisition should succeed
    with guard.acquire(player_id, token) as decision1:
        assert decision1.should_apply is True

    # Second acquisition with same token should be suppressed
    with guard.acquire(player_id, token) as decision2:
        assert decision2.should_apply is False
        assert decision2.duplicate is True


def test_acquire_different_players_same_token(guard):
    """Test acquire allows same token for different players."""
    player1_id = str(uuid.uuid4())
    player2_id = str(uuid.uuid4())
    token = "shared_token"

    with guard.acquire(player1_id, token) as decision1:
        assert decision1.should_apply is True

    # Same token for different player should be allowed
    with guard.acquire(player2_id, token) as decision2:
        assert decision2.should_apply is True


@pytest.mark.asyncio
async def test_acquire_async_without_token(guard):
    """Test acquire_async without token allows mutation."""
    player_id = str(uuid.uuid4())

    async with guard.acquire_async(player_id, None) as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


@pytest.mark.asyncio
async def test_acquire_async_with_unique_token(guard):
    """Test acquire_async with unique token allows mutation."""
    player_id = str(uuid.uuid4())
    token = "unique_token_async_123"

    async with guard.acquire_async(player_id, token) as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


@pytest.mark.asyncio
async def test_acquire_async_with_duplicate_token(guard):
    """Test acquire_async with duplicate token suppresses mutation."""
    player_id = str(uuid.uuid4())
    token = "duplicate_token_async_123"

    # First acquisition should succeed
    async with guard.acquire_async(player_id, token) as decision1:
        assert decision1.should_apply is True

    # Second acquisition with same token should be suppressed
    async with guard.acquire_async(player_id, token) as decision2:
        assert decision2.should_apply is False
        assert decision2.duplicate is True


@pytest.mark.asyncio
async def test_acquire_async_different_players_same_token(guard):
    """Test acquire_async allows same token for different players."""
    player1_id = str(uuid.uuid4())
    player2_id = str(uuid.uuid4())
    token = "shared_token_async"

    async with guard.acquire_async(player1_id, token) as decision1:
        assert decision1.should_apply is True

    # Same token for different player should be allowed
    async with guard.acquire_async(player2_id, token) as decision2:
        assert decision2.should_apply is True
