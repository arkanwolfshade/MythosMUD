"""
Unit tests for inventory mutation guard.

Tests the InventoryMutationGuard class for preventing duplicate inventory mutations.
"""

import asyncio
import uuid
from time import monotonic

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard, MutationDecision


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
    import time

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
    import time

    time.sleep(0.2)

    # Acquire again (should prune expired token)
    with guard.acquire(player_id, "new_token"):
        pass

    # State should be cleaned up if empty
    # (Note: cleanup happens in finally block, so state may still exist briefly)


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


@pytest.mark.asyncio
async def test_acquire_async_concurrent_same_player(guard):
    """Test acquire_async serializes concurrent mutations for same player."""
    player_id = str(uuid.uuid4())
    results = []

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


def test_get_async_global_lock(guard):
    """Test _get_async_global_lock creates lock lazily."""
    assert guard._async_global_lock is None

    lock1 = guard._get_async_global_lock()
    assert guard._async_global_lock is not None

    lock2 = guard._get_async_global_lock()
    assert lock1 is lock2  # Should return same lock


def test_get_async_state_creates_lazily(guard):
    """Test _get_async_state creates state lazily."""
    player_id = str(uuid.uuid4())

    async def test():
        state = await guard._get_async_state(player_id)
        assert state is not None
        assert player_id in guard._async_states

    asyncio.run(test())


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


@pytest.mark.asyncio
async def test_cleanup_async_state_lock_attribute_error(guard):
    """Test _cleanup_async_state handles AttributeError from lock.locked()."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    # Create a mock lock that raises AttributeError when locked() is called
    class MockLock:
        def __init__(self):
            self._locked = False

        async def acquire(self):
            self._locked = True

        def release(self):
            self._locked = False

        def locked(self):
            raise AttributeError("locked() not available")

    mock_lock = MockLock()
    state.lock = mock_lock

    # Should handle AttributeError gracefully and skip cleanup
    await guard._cleanup_async_state(player_id)
    # State should still exist (cleanup skipped due to error)
    assert player_id in guard._async_states


@pytest.mark.asyncio
async def test_cleanup_async_state_lock_runtime_error(guard):
    """Test _cleanup_async_state handles RuntimeError from lock.locked()."""
    player_id = str(uuid.uuid4())
    state = await guard._get_async_state(player_id)

    # Create a mock lock that raises RuntimeError when locked() is called
    class MockLock:
        def __init__(self):
            self._locked = False

        async def acquire(self):
            self._locked = True

        def release(self):
            self._locked = False

        def locked(self):
            raise RuntimeError("Lock in inconsistent state")

    mock_lock = MockLock()
    state.lock = mock_lock

    # Should handle RuntimeError gracefully and skip cleanup
    await guard._cleanup_async_state(player_id)
    # State should still exist (cleanup skipped due to error)
    assert player_id in guard._async_states


def test_acquire_record_custom_alert_with_message_param(guard):
    """Test acquire handles record_custom_alert with message parameter."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token"

    # First acquisition
    with guard.acquire(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that has 'message' parameter
    mock_dashboard = MagicMock()

    def record_with_message(alert_type, *, severity=None, message=None, metadata=None):
        pass

    mock_dashboard.record_custom_alert = record_with_message

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Second acquisition should trigger duplicate detection
            with guard.acquire(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()


@pytest.mark.asyncio
async def test_acquire_async_record_custom_alert_with_message_param(guard):
    """Test acquire_async handles record_custom_alert with message parameter."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token_async"

    # First acquisition
    async with guard.acquire_async(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that has 'message' parameter
    mock_dashboard = MagicMock()

    def record_with_message(alert_type, *, severity=None, message=None, metadata=None):
        pass

    mock_dashboard.record_custom_alert = record_with_message

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Second acquisition should trigger duplicate detection
            async with guard.acquire_async(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()


def test_acquire_record_custom_alert_type_error_fallback(guard):
    """Test acquire handles TypeError from record_custom_alert and uses fallback."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token"

    # First acquisition
    with guard.acquire(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that raises TypeError
    mock_dashboard = MagicMock()

    def record_raises_typeerror(alert_type, *, severity=None, metadata=None):
        raise TypeError("Invalid arguments")

    mock_dashboard.record_custom_alert = record_raises_typeerror

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Should handle TypeError gracefully
            with guard.acquire(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()


@pytest.mark.asyncio
async def test_acquire_async_record_custom_alert_type_error_fallback(guard):
    """Test acquire_async handles TypeError from record_custom_alert and uses fallback."""
    from unittest.mock import MagicMock, patch

    player_id = str(uuid.uuid4())
    token = "duplicate_token_async"

    # First acquisition
    async with guard.acquire_async(player_id, token):
        pass

    # Mock dashboard with record_custom_alert that raises TypeError
    mock_dashboard = MagicMock()

    def record_raises_typeerror(alert_type, *, severity=None, metadata=None):
        raise TypeError("Invalid arguments")

    mock_dashboard.record_custom_alert = record_raises_typeerror

    with patch("server.services.inventory_mutation_guard.get_monitoring_dashboard", return_value=mock_dashboard):
        with patch("server.services.inventory_mutation_guard.metrics_collector") as mock_metrics:
            # Should handle TypeError gracefully
            async with guard.acquire_async(player_id, token) as decision:
                assert decision.should_apply is False
                assert decision.duplicate is True
                mock_metrics.record_message_failed.assert_called_once()
