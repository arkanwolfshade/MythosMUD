"""
Unit tests for combat persistence handler - persistence operations.

Tests player DP persistence, verification, and background task handling.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.combat_persistence_handler import CombatPersistenceHandler

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    return MagicMock()


@pytest.fixture
def persistence_handler(mock_combat_service):
    """Create CombatPersistenceHandler instance."""
    return CombatPersistenceHandler(mock_combat_service)


@pytest.fixture
def mock_player():
    """Create mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.stats = {"current_dp": 50, "max_dp": 100, "position": "standing"}
    player.get_stats = MagicMock(return_value={"current_dp": 50, "max_dp": 100, "position": "standing"})
    player.set_stats = MagicMock()
    player.apply_dp_change = MagicMock(return_value=(50, False, False))
    return player


@pytest.mark.asyncio
async def test_verify_player_save_success(persistence_handler):
    """Test _verify_player_save verifies player save successfully."""
    player_id = uuid.uuid4()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"current_dp": 30}
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    await persistence_handler._verify_player_save(mock_persistence, player_id, "TestPlayer", 50, 30)


@pytest.mark.asyncio
async def test_verify_player_save_player_not_found(persistence_handler):
    """Test _verify_player_save handles player not found."""
    player_id = uuid.uuid4()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    # Should not raise, just log error
    await persistence_handler._verify_player_save(mock_persistence, player_id, "TestPlayer", 50, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_success(persistence_handler, mock_player):
    """Test _persist_player_dp_sync persists DP successfully."""
    player_id = mock_player.player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_no_persistence(persistence_handler):
    """Test _persist_player_dp_sync handles no persistence layer."""
    player_id = uuid.uuid4()
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=None):
        # Should not raise, just log warning
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_player_not_found(persistence_handler):
    """Test _persist_player_dp_sync handles player not found."""
    player_id = uuid.uuid4()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        # Should not raise, just log warning
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_error(persistence_handler, mock_player):
    """Test _persist_player_dp_sync handles errors gracefully."""
    player_id = mock_player.player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(side_effect=ValueError("Database error"))
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        # Should not raise, just log error
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_verify_player_save_called(persistence_handler, mock_player):
    """Test _persist_player_dp_sync calls _verify_player_save."""
    player_id = mock_player.player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        with patch.object(persistence_handler, "_verify_player_save", new_callable=AsyncMock) as mock_verify:
            await persistence_handler._persist_player_dp_sync(player_id, 30)
            mock_verify.assert_awaited_once()


@pytest.mark.asyncio
async def test_persist_player_dp_sync_save_error(persistence_handler, mock_player):
    """Test _persist_player_dp_sync handles save_player error."""
    player_id = mock_player.player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock(side_effect=ValueError("Save error"))
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        # Should not raise, just log error
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_complete_flow(persistence_handler, mock_player):
    """Test _persist_player_dp_sync completes full flow with verification and logging."""
    player_id = mock_player.player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        with patch.object(persistence_handler, "_verify_player_save", new_callable=AsyncMock) as mock_verify:
            with patch.object(persistence_handler, "_log_death_state_changes") as mock_log:
                await persistence_handler._persist_player_dp_sync(player_id, 30)
                mock_verify.assert_awaited_once()
                mock_log.assert_called_once()


@pytest.mark.asyncio
async def test_persist_player_dp_sync_get_stats_error(persistence_handler):
    """Test _persist_player_dp_sync handles get_stats error."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(side_effect=AttributeError("No stats"))
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        # Should not raise, just log error
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_sync_complete_flow_with_verification_new(persistence_handler, mock_player):
    """Test _persist_player_dp_sync complete flow including verification."""
    player_id = mock_player.player_id
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        with patch.object(persistence_handler, "_verify_player_save", new_callable=AsyncMock) as mock_verify:
            await persistence_handler._persist_player_dp_sync(player_id, 30)
            mock_persistence.save_player.assert_awaited_once()
            mock_verify.assert_awaited_once()


@pytest.mark.asyncio
async def test_persist_player_dp_sync_get_stats_error_new(persistence_handler):
    """Test _persist_player_dp_sync handles get_stats error gracefully."""
    player_id = uuid.uuid4()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(side_effect=AttributeError("No get_stats"))
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    with patch.object(persistence_handler, "_get_persistence_layer", return_value=mock_persistence):
        # Should not raise, just log error
        await persistence_handler._persist_player_dp_sync(player_id, 30)


@pytest.mark.asyncio
async def test_persist_player_dp_background(persistence_handler):
    """Test _persist_player_dp_background schedules background task."""
    player_id = uuid.uuid4()
    # Track created tasks to ensure they're awaited
    created_tasks: list[asyncio.Task[None]] = []
    original_create_task = asyncio.create_task

    def mock_create_task(coro):
        """Create a real task and track it."""
        task = original_create_task(coro)
        created_tasks.append(task)
        return task

    with patch("asyncio.create_task", side_effect=mock_create_task):
        # Should not raise
        persistence_handler._persist_player_dp_background(player_id, 30, 50, 100)
        # Background task should be created
        assert len(created_tasks) > 0
        # Await the task to avoid warnings
        if created_tasks:
            try:
                await asyncio.wait_for(created_tasks[0], timeout=0.1)
            except (TimeoutError, Exception):  # noqa: BLE001  # pylint: disable=broad-except  # Reason: Test cleanup - we don't care about specific error types, just ensuring task doesn't hang
                # Task may complete or error, that's fine for this test
                pass


@pytest.mark.asyncio
async def test_persist_player_dp_background_task_error(persistence_handler):
    """Test _persist_player_dp_background handles background task creation error."""
    player_id = uuid.uuid4()
    # Patch to raise error, which should be caught and logged
    # We need to capture the coroutine and await it to avoid warnings
    captured_coro = None

    def capture_and_raise(coro):
        nonlocal captured_coro
        captured_coro = coro
        raise RuntimeError("No event loop")

    with patch("asyncio.create_task", side_effect=capture_and_raise):
        # Should not raise, just log error
        persistence_handler._persist_player_dp_background(player_id, 30, 50, 100, None, None)

    # Await the captured coroutine to avoid "coroutine never awaited" warning
    if captured_coro:
        try:
            await asyncio.wait_for(captured_coro, timeout=0.1)
        except (TimeoutError, Exception):  # noqa: BLE001  # pylint: disable=broad-except  # Reason: Test cleanup - we don't care about specific error types, just ensuring coroutine doesn't hang
            # Expected - coroutine may error or timeout
            pass


@pytest.mark.asyncio
async def test_persist_player_dp_background_persistence_failure(persistence_handler):
    """Test _persist_player_dp_background sends correction event on persistence failure."""
    player_id = uuid.uuid4()
    with patch.object(
        persistence_handler, "_persist_player_dp_sync", new_callable=AsyncMock, side_effect=ValueError("Save error")
    ):
        with patch.object(
            persistence_handler, "_publish_player_dp_correction_event", new_callable=AsyncMock
        ) as mock_correction:
            # Track created tasks to ensure they're awaited
            created_tasks: list[asyncio.Task[None]] = []
            original_create_task = asyncio.create_task

            def mock_create_task(coro):
                """Create a real task and track it."""
                task = original_create_task(coro)
                created_tasks.append(task)
                return task

            with patch("asyncio.create_task", side_effect=mock_create_task):
                # Execute the background method
                persistence_handler._persist_player_dp_background(player_id, 30, 50, 100, "room_001", "combat_001")

                # Await the task to let it run and trigger the error path
                if created_tasks:
                    try:
                        await asyncio.wait_for(created_tasks[0], timeout=0.5)
                    except (TimeoutError, ValueError):
                        # Expected - task may complete or error
                        pass

                # Correction event should be published
                mock_correction.assert_awaited_once()
