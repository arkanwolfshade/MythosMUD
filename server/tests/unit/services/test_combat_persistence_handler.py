"""
Unit tests for combat persistence handler.

Tests the CombatPersistenceHandler class for player DP persistence, verification,
and event publishing.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.combat_persistence_handler import CombatPersistenceHandler
from server.services.nats_exceptions import NATSError

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
    return player


def test_persistence_handler_init(persistence_handler, mock_combat_service):
    """Test CombatPersistenceHandler initialization."""
    assert persistence_handler._combat_service == mock_combat_service


def test_get_persistence_layer(persistence_handler):
    """Test _get_persistence_layer gets persistence from container."""
    mock_persistence = MagicMock()
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence = mock_persistence
        mock_container.get_instance.return_value = mock_instance
        result = persistence_handler._get_persistence_layer()
        assert result == mock_persistence


def test_get_persistence_layer_no_container(persistence_handler):
    """Test _get_persistence_layer returns None when container unavailable."""
    with patch("server.container.ApplicationContainer.get_instance", side_effect=ImportError("No container")):
        result = persistence_handler._get_persistence_layer()
        assert result is None


def test_update_player_dp_and_posture_drops_to_zero(persistence_handler, mock_player):
    """Test _update_player_dp_and_posture changes posture when DP drops to 0."""
    persistence_handler._update_player_dp_and_posture(mock_player, mock_player.player_id, 0, 50)
    mock_player.set_stats.assert_called_once()
    call_args = mock_player.set_stats.call_args[0][0]
    assert call_args["current_dp"] == 0
    assert call_args["position"] == "lying"


def test_update_player_dp_and_posture_negative_dp(persistence_handler, mock_player):
    """Test _update_player_dp_and_posture ensures lying when DP is already <= 0."""
    mock_player.get_stats.return_value = {"current_dp": -5, "max_dp": 100, "position": "standing"}
    persistence_handler._update_player_dp_and_posture(mock_player, mock_player.player_id, -5, -3)
    call_args = mock_player.set_stats.call_args[0][0]
    assert call_args["position"] == "lying"


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


def test_log_death_state_changes_death_threshold(persistence_handler):
    """Test _log_death_state_changes logs death threshold."""
    player_id = uuid.uuid4()
    # Should not raise, just log
    persistence_handler._log_death_state_changes(player_id, "TestPlayer", -10, 5)


def test_log_death_state_changes_mortally_wounded(persistence_handler):
    """Test _log_death_state_changes logs mortally wounded."""
    player_id = uuid.uuid4()
    persistence_handler._log_death_state_changes(player_id, "TestPlayer", 0, 5)


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
async def test_persist_player_dp_background(persistence_handler):
    """Test _persist_player_dp_background schedules background task."""
    player_id = uuid.uuid4()
    # Track created tasks to ensure they're awaited
    created_tasks = []
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
async def test_publish_player_dp_update_event(persistence_handler):
    """Test publish_player_dp_update_event publishes event."""
    player_id = uuid.uuid4()
    with patch.object(
        persistence_handler, "_publish_player_dp_update_event_impl", new_callable=AsyncMock
    ) as mock_publish:
        await persistence_handler.publish_player_dp_update_event(player_id, 50, 30, 100)
        mock_publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl publishes to event bus."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_no_event_bus(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles no event bus."""
    player_id = uuid.uuid4()
    mock_combat_service._event_bus = None
    # Should not raise, just log warning
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles errors gracefully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_event_bus.publish = MagicMock(side_effect=ValueError("Event bus error"))
    mock_combat_service._event_bus = mock_event_bus
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_with_nats(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl publishes to NATS when available."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_nats_service = AsyncMock()
    mock_subject_manager = MagicMock()
    mock_subject_manager.build_subject = MagicMock(return_value="combat.dp_update.test")
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = mock_nats_service
    mock_combat_service._combat_event_publisher = MagicMock()
    mock_combat_service._combat_event_publisher.subject_manager = mock_subject_manager
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event publishes correction event."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_correction_event(player_id, 50, 100, "room_001", "combat_001", "Error")
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event handles errors gracefully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_event_bus.publish = MagicMock(side_effect=ValueError("Event bus error"))
    mock_combat_service._event_bus = mock_event_bus
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_correction_event(player_id, 50, 100, None, None, "Error")


def test_persist_player_dp_background_public_api(persistence_handler):
    """Test persist_player_dp_background public API method."""
    player_id = uuid.uuid4()
    with patch.object(persistence_handler, "_persist_player_dp_background") as mock_persist:
        persistence_handler.persist_player_dp_background(player_id, 30, 50, 100)
        mock_persist.assert_called_once_with(player_id, 30, 50, 100, None, None)


def test_update_player_dp_and_posture_no_posture_change(persistence_handler, mock_player):
    """Test _update_player_dp_and_posture doesn't change posture when DP > 0."""
    persistence_handler._update_player_dp_and_posture(mock_player, mock_player.player_id, 30, 50)
    mock_player.set_stats.assert_called_once()
    call_args = mock_player.set_stats.call_args[0][0]
    assert call_args["current_dp"] == 30
    # Position should not change when DP > 0
    assert call_args.get("position") != "lying"


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
async def test_publish_player_dp_update_event_impl_legacy_subject(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl uses legacy subject when subject_manager unavailable."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_nats_service = AsyncMock()
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = mock_nats_service
    mock_combat_service._combat_event_publisher = None  # No subject manager
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)
    # Should still publish to NATS with legacy subject
    mock_nats_service.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_nats_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles NATS errors gracefully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_nats_service = AsyncMock()
    mock_nats_service.publish = AsyncMock(side_effect=ValueError("NATS error"))
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = mock_nats_service
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_no_nats(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles no NATS service."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    mock_combat_service._nats_service = None
    # Should not raise, just log warning
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event_no_event_bus(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event handles no event bus."""
    player_id = uuid.uuid4()
    mock_combat_service._event_bus = None
    # Should not raise, just log warning
    await persistence_handler._publish_player_dp_correction_event(player_id, 50, 100, None, None, "Error")


def test_get_persistence_layer_container_error(persistence_handler):
    """Test _get_persistence_layer handles container errors."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_container.get_instance.side_effect = RuntimeError("Container error")
        result = persistence_handler._get_persistence_layer()
        assert result is None


def test_get_persistence_layer_no_async_persistence(persistence_handler):
    """Test _get_persistence_layer handles container without async_persistence."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence = None
        mock_container.get_instance.return_value = mock_instance
        result = persistence_handler._get_persistence_layer()
        assert result is None


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
            created_tasks = []
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


@pytest.mark.asyncio
async def test_publish_player_dp_update_event_impl_all_parameters(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl with all optional parameters."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100, "combat_001", "room_001")
    mock_event_bus.publish.assert_called_once()


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
async def test_publish_player_dp_update_event_impl_event_bus_publish_error(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_update_event_impl handles event bus publish error."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_event_bus.publish = MagicMock(side_effect=NATSError("Event bus error"))
    mock_combat_service._event_bus = mock_event_bus
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_update_event_impl(player_id, 50, 30, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event_all_parameters(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event with all parameters."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_correction_event(
        player_id, 50, 100, "room_001", "combat_001", "Test error"
    )
    mock_event_bus.publish.assert_called_once()


def test_update_player_dp_and_posture_positive_to_positive(persistence_handler, mock_player):
    """Test _update_player_dp_and_posture when DP stays positive."""
    persistence_handler._update_player_dp_and_posture(mock_player, mock_player.player_id, 40, 50)
    call_args = mock_player.set_stats.call_args[0][0]
    assert call_args["current_dp"] == 40
    # Position should remain unchanged


def test_update_player_dp_and_posture_already_lying(persistence_handler, mock_player):
    """Test _update_player_dp_and_posture when player already at <= 0 DP."""
    mock_player.get_stats.return_value = {"current_dp": -5, "max_dp": 100, "position": "lying"}
    persistence_handler._update_player_dp_and_posture(mock_player, mock_player.player_id, -5, -3)
    call_args = mock_player.set_stats.call_args[0][0]
    assert call_args["position"] == "lying"


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event_success_new(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event publishes correction event successfully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_correction_event(
        player_id, 50, 100, "room_001", "combat_001", "Test error"
    )
    mock_event_bus.publish.assert_called_once()


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event_publish_error_new(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event handles publish errors gracefully."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_event_bus.publish = MagicMock(side_effect=ConnectionError("Connection error"))
    mock_combat_service._event_bus = mock_event_bus
    # Should not raise, just log error
    await persistence_handler._publish_player_dp_correction_event(player_id, 50, 100)


@pytest.mark.asyncio
async def test_publish_player_dp_correction_event_all_parameters_new(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event with all parameters set."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    mock_combat_service._event_bus = mock_event_bus
    await persistence_handler._publish_player_dp_correction_event(
        player_id, 50, 100, "room_001", "combat_001", "Test error message"
    )
    mock_event_bus.publish.assert_called_once()
    # Verify event was created with correct values
    call_args = mock_event_bus.publish.call_args[0][0]
    assert call_args.player_id == player_id
    assert call_args.old_dp == 50
    assert call_args.new_dp == 50
    assert call_args.max_dp == 100
    assert call_args.damage_taken == 0
    assert call_args.combat_id == "combat_001"
    assert call_args.room_id == "room_001"


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
async def test_publish_player_dp_correction_event_outer_exception(persistence_handler, mock_combat_service):
    """Test _publish_player_dp_correction_event handles outer exception."""
    player_id = uuid.uuid4()
    mock_event_bus = MagicMock()
    # Simulate error in event creation by patching the import inside the method
    with patch("server.events.event_types.PlayerDPUpdated", side_effect=ValueError("Event creation failed")):
        mock_combat_service._event_bus = mock_event_bus
        # Should not raise, just log error
        await persistence_handler._publish_player_dp_correction_event(player_id, 50, 100)
