"""
Unit tests for combat persistence handler - persistence operations.

Tests player DP persistence through the player registry, and background task handling.
"""

# pyright: reportPrivateUsage=false
# Reason: these tests drive the handler's private DP persistence helpers directly.

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.models.game import PositionState
from server.services.combat_persistence_handler import CombatPersistenceHandler
from server.tests.fixtures.shared.player_registry import lucidity_registry

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


@pytest.mark.asyncio
async def test_persist_player_dp_sync_writes_dp_and_posture_through_the_registry(
    persistence_handler: CombatPersistenceHandler,
):
    """A combat hit's DP goes through the player registry as one sync unit (ADR-029 step 6a)."""
    player_id = uuid.uuid4()
    harness = lucidity_registry({player_id: None}, stats={"current_dp": 5, "max_dp": 20, "position": "standing"})

    with patch.object(persistence_handler, "_get_player_registry", return_value=harness.registry):
        await persistence_handler._persist_player_dp_sync(player_id, -2)

    assert harness.stats(player_id)["current_dp"] == -2
    assert harness.stats(player_id)["position"] == PositionState.LYING  # mortally wounded lies down
    assert harness.db.executed, "committed before returning"


@pytest.mark.asyncio
async def test_persist_player_dp_sync_without_a_registry_does_nothing(persistence_handler: CombatPersistenceHandler):
    with patch.object(persistence_handler, "_get_player_registry", return_value=None):
        await persistence_handler._persist_player_dp_sync(uuid.uuid4(), 30)  # logs, never raises


@pytest.mark.asyncio
async def test_persist_player_dp_sync_unknown_player_is_skipped(persistence_handler: CombatPersistenceHandler):
    harness = lucidity_registry({})

    with patch.object(persistence_handler, "_get_player_registry", return_value=harness.registry):
        await persistence_handler._persist_player_dp_sync(uuid.uuid4(), 30)

    assert not harness.db.executed


@pytest.mark.asyncio
async def test_persist_player_dp_sync_raises_a_failed_commit(persistence_handler: CombatPersistenceHandler):
    """The background task needs the error to send its correction event."""
    with (
        patch.object(persistence_handler, "_get_player_registry", return_value=MagicMock()),
        patch(
            "server.services.combat_persistence_handler.PlayerHealthService.set_dp",
            new_callable=AsyncMock,
            side_effect=SQLAlchemyError("commit failed"),
        ),
    ):
        with pytest.raises(SQLAlchemyError):
            await persistence_handler._persist_player_dp_sync(uuid.uuid4(), 30)


@pytest.mark.asyncio
async def test_persist_player_dp_background_corrects_the_client_after_a_failed_commit(
    persistence_handler: CombatPersistenceHandler,
):
    with (
        patch.object(
            persistence_handler,
            "_persist_player_dp_sync",
            new_callable=AsyncMock,
            side_effect=SQLAlchemyError("commit failed"),
        ),
        patch.object(persistence_handler, "_publish_player_dp_correction_event", new_callable=AsyncMock) as correction,
    ):
        persistence_handler._persist_player_dp_background(uuid.uuid4(), 30, 50, 100, "room_001", "combat_001")
        await asyncio.sleep(0)  # let the background task run
        await asyncio.sleep(0)

    correction.assert_awaited_once()


@pytest.mark.asyncio
async def test_persist_player_dp_background(persistence_handler: CombatPersistenceHandler):
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
            except TimeoutError, Exception:  # noqa: BLE001  # pylint: disable=broad-except  # Reason: Test cleanup - we don't care about specific error types, just ensuring task doesn't hang
                # Task may complete or error, that's fine for this test
                pass


@pytest.mark.asyncio
async def test_persist_player_dp_background_task_error(persistence_handler: CombatPersistenceHandler):
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
        except TimeoutError, Exception:  # noqa: BLE001  # pylint: disable=broad-except  # Reason: Test cleanup - we don't care about specific error types, just ensuring coroutine doesn't hang
            # Expected - coroutine may error or timeout
            pass


@pytest.mark.asyncio
async def test_persist_player_dp_background_persistence_failure(persistence_handler: CombatPersistenceHandler):
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
                    except TimeoutError, ValueError:
                        # Expected - task may complete or error
                        pass

                # Correction event should be published
                mock_correction.assert_awaited_once()
