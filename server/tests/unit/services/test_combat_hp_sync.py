"""
Tests for combat HP/DP synchronization.

This module tests the CombatDPSync class which handles player DP persistence
and event publishing for combat operations.
"""

from unittest.mock import AsyncMock, MagicMock, Mock, patch
from uuid import uuid4

import pytest

from server.events.event_types import PlayerDPUpdated
from server.exceptions import DatabaseError
from server.models.game import PositionState
from server.services.combat_hp_sync import CombatDPSync


class TestCombatDPSyncInit:
    """Test CombatDPSync initialization."""

    def test_init_with_nats_service(self) -> None:
        """Test initialization with NATS service."""
        mock_combat_service = MagicMock()
        mock_combat_service._nats_service = MagicMock()
        mock_combat_service._combat_event_publisher = MagicMock()

        sync = CombatDPSync(mock_combat_service)

        assert sync._combat_service == mock_combat_service
        assert sync._nats_service == mock_combat_service._nats_service
        assert sync._combat_event_publisher == mock_combat_service._combat_event_publisher

    def test_init_without_nats_service(self) -> None:
        """Test initialization without NATS service."""
        mock_combat_service = MagicMock()
        # Use hasattr to check, then delete if it exists
        if hasattr(mock_combat_service, "_nats_service"):
            delattr(mock_combat_service, "_nats_service")
        if hasattr(mock_combat_service, "_combat_event_publisher"):
            delattr(mock_combat_service, "_combat_event_publisher")

        sync = CombatDPSync(mock_combat_service)

        assert sync._combat_service == mock_combat_service
        assert sync._nats_service is None
        assert sync._combat_event_publisher is None


class TestGetPersistence:
    """Test _get_persistence method."""

    def test_get_persistence_success(self) -> None:
        """Test successful retrieval of persistence."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        mock_container = MagicMock()
        mock_container.async_persistence = MagicMock()

        # ApplicationContainer is imported inside the function
        with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
            with patch("server.services.combat_hp_sync.logger"):
                result = sync._get_persistence(player_id)

                assert result == mock_container.async_persistence

    def test_get_persistence_no_container(self) -> None:
        """Test when container is None."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        with patch("server.container.ApplicationContainer.get_instance", return_value=None):
            with patch("server.services.combat_hp_sync.logger"):
                result = sync._get_persistence(player_id)

                assert result is None

    def test_get_persistence_import_error(self) -> None:
        """Test when ImportError occurs."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        # Simulate ImportError by making the import fail
        with patch("builtins.__import__", side_effect=ImportError("Import error")):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                result = sync._get_persistence(player_id)

                assert result is None
                mock_logger.warning.assert_called_once()

    def test_get_persistence_attribute_error(self) -> None:
        """Test when AttributeError occurs."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        # ApplicationContainer is imported inside the function
        with patch("server.container.ApplicationContainer.get_instance", side_effect=AttributeError("Attribute error")):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                result = sync._get_persistence(player_id)

                assert result is None
                mock_logger.warning.assert_called_once()


class TestUpdatePlayerPosition:
    """Test _update_player_position method."""

    def test_update_player_position_to_lying(self) -> None:
        """Test updating position to lying when DP drops to 0."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"

        stats = {"position": PositionState.STANDING, "current_dp": 50}
        current_dp = 0
        old_dp = 50

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            sync._update_player_position(stats, current_dp, old_dp, player_id, player_name)

            assert stats["position"] == PositionState.LYING
            mock_logger.info.assert_called_once()
            assert "lying" in str(mock_logger.info.call_args).lower()

    def test_update_player_position_already_lying(self) -> None:
        """Test updating position when already lying."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"

        stats = {"position": PositionState.LYING, "current_dp": -5}
        current_dp = -10
        old_dp = -5

        with patch("server.services.combat_hp_sync.logger"):
            sync._update_player_position(stats, current_dp, old_dp, player_id, player_name)

            assert stats["position"] == PositionState.LYING

    def test_update_player_position_no_change(self) -> None:
        """Test when position doesn't need to change."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"

        stats = {"position": PositionState.STANDING, "current_dp": 50}
        current_dp = 40
        old_dp = 50

        with patch("server.services.combat_hp_sync.logger"):
            sync._update_player_position(stats, current_dp, old_dp, player_id, player_name)

            assert stats["position"] == PositionState.STANDING

    def test_update_player_position_negative_to_negative(self) -> None:
        """Test updating position when DP goes from negative to more negative."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"

        stats = {"position": PositionState.LYING, "current_dp": -5}
        current_dp = -10
        old_dp = -5

        with patch("server.services.combat_hp_sync.logger"):
            sync._update_player_position(stats, current_dp, old_dp, player_id, player_name)

            assert stats["position"] == PositionState.LYING


class TestVerifyPlayerSave:
    """Test _verify_player_save method."""

    @pytest.mark.asyncio
    async def test_verify_player_save_success(self) -> None:
        """Test successful verification of player save."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"
        old_dp = 50
        current_dp = 40

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"current_dp": current_dp}
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            await sync._verify_player_save(mock_persistence, player_id, player_name, old_dp, current_dp)

            mock_logger.info.assert_called_once()
            assert "VERIFICATION" in str(mock_logger.info.call_args)

    @pytest.mark.asyncio
    async def test_verify_player_save_player_not_found(self) -> None:
        """Test verification when player is not found."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"
        old_dp = 50
        current_dp = 40

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=None)

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            await sync._verify_player_save(mock_persistence, player_id, player_name, old_dp, current_dp)

            mock_logger.error.assert_called_once()
            assert "not found" in str(mock_logger.error.call_args).lower()

    @pytest.mark.asyncio
    async def test_verify_player_save_mismatch(self) -> None:
        """Test verification when DP doesn't match."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"
        old_dp = 50
        current_dp = 40

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"current_dp": 35}  # Different from current_dp
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            await sync._verify_player_save(mock_persistence, player_id, player_name, old_dp, current_dp)

            mock_logger.info.assert_called_once()
            call_args_str = str(mock_logger.info.call_args)
            assert "save_successful" in call_args_str


class TestLogDeathThresholdEvents:
    """Test _log_death_threshold_events method."""

    def test_log_death_threshold_events_death_threshold(self) -> None:
        """Test logging when death threshold is reached."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"
        current_dp = -10
        old_dp = -5

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            sync._log_death_threshold_events(current_dp, old_dp, player_id, player_name)

            assert mock_logger.info.call_count >= 1
            assert mock_logger.debug.call_count >= 1
            call_args_str = str(mock_logger.info.call_args_list)
            assert "death threshold" in call_args_str.lower()

    def test_log_death_threshold_events_mortally_wounded(self) -> None:
        """Test logging when player becomes mortally wounded."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"
        current_dp = 0
        old_dp = 5

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            sync._log_death_threshold_events(current_dp, old_dp, player_id, player_name)

            mock_logger.info.assert_called_once()
            call_args_str = str(mock_logger.info.call_args)
            assert "mortally wounded" in call_args_str.lower()

    def test_log_death_threshold_events_no_change(self) -> None:
        """Test when no death threshold events occur."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()
        player_name = "TestPlayer"
        current_dp = 50
        old_dp = 60

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            sync._log_death_threshold_events(current_dp, old_dp, player_id, player_name)

            mock_logger.info.assert_not_called()
            mock_logger.debug.assert_not_called()


class TestUpdateAndSavePlayerDp:
    """Test _update_and_save_player_dp method."""

    @pytest.mark.asyncio
    async def test_update_and_save_player_dp_success(self) -> None:
        """Test successful update and save."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.stats = '{"current_dp": 50}'
        mock_player.get_stats.return_value = {"current_dp": 50, "position": PositionState.STANDING}
        mock_player.set_stats = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()

        with patch("server.services.combat_hp_sync.logger"):
            result = await sync._update_and_save_player_dp(mock_persistence, player_id, 40)

            assert result is not None
            player, old_dp = result
            assert player == mock_player
            assert old_dp == 50
            mock_persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_and_save_player_dp_player_not_found(self) -> None:
        """Test when player is not found."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=None)

        with patch("server.services.combat_hp_sync.logger") as mock_logger:
            result = await sync._update_and_save_player_dp(mock_persistence, player_id, 40)

            assert result is None
            mock_logger.warning.assert_called_once()


class TestPersistPlayerDpSync:
    """Test _persist_player_dp_sync method."""

    @pytest.mark.asyncio
    async def test_persist_player_dp_sync_success(self) -> None:
        """Test successful persistence."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        mock_persistence = MagicMock()
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.stats = '{"current_dp": 50}'
        mock_player.get_stats.return_value = {"current_dp": 50}
        mock_player.set_stats = MagicMock()

        with patch.object(sync, "_get_persistence", return_value=mock_persistence):
            with patch.object(sync, "_update_and_save_player_dp", return_value=(mock_player, 50)) as mock_update:
                with patch.object(sync, "_verify_player_save", new_callable=AsyncMock) as mock_verify:
                    with patch.object(sync, "_log_death_threshold_events") as mock_log_death:
                        with patch("server.services.combat_hp_sync.logger"):
                            await sync._persist_player_dp_sync(player_id, 40)

                            # Verify all methods were called
                            mock_update.assert_called_once()
                            mock_verify.assert_called_once()
                            mock_log_death.assert_called_once()

    @pytest.mark.asyncio
    async def test_persist_player_dp_sync_no_persistence(self) -> None:
        """Test when persistence is not available."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        with patch.object(sync, "_get_persistence", return_value=None):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                await sync._persist_player_dp_sync(player_id, 40)

                mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_persist_player_dp_sync_database_error(self) -> None:
        """Test when DatabaseError occurs."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        with patch.object(sync, "_get_persistence", return_value=MagicMock()):
            with patch.object(sync, "_update_and_save_player_dp", side_effect=DatabaseError("Database error")):
                with patch("server.services.combat_hp_sync.logger") as mock_logger:
                    await sync._persist_player_dp_sync(player_id, 40)

                    mock_logger.error.assert_called_once()


class TestPublishPlayerDpUpdateEvent:
    """Test _publish_player_dp_update_event method."""

    @pytest.mark.asyncio
    async def test_publish_player_dp_update_event_success(self) -> None:
        """Test successful event publishing."""
        mock_combat_service = MagicMock()
        mock_nats_service = AsyncMock()
        mock_combat_service._nats_service = mock_nats_service
        mock_combat_service._combat_event_publisher = MagicMock()
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        old_dp = 50
        new_dp = 40
        max_dp = 100

        mock_event_bus = MagicMock()
        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger"):
                await sync._publish_player_dp_update_event(player_id, old_dp, new_dp, max_dp)

                mock_event_bus.publish.assert_called_once()
                assert isinstance(mock_event_bus.publish.call_args[0][0], PlayerDPUpdated)

    @pytest.mark.asyncio
    async def test_publish_player_dp_update_event_with_nats(self) -> None:
        """Test event publishing with NATS service."""
        mock_combat_service = MagicMock()
        mock_nats_service = AsyncMock()
        mock_combat_service._nats_service = mock_nats_service
        mock_subject_manager = MagicMock()
        mock_subject_manager.build_subject.return_value = "combat.dp_update.test"
        mock_combat_event_publisher = MagicMock()
        mock_combat_event_publisher.subject_manager = mock_subject_manager
        mock_combat_service._combat_event_publisher = mock_combat_event_publisher
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        old_dp = 50
        new_dp = 40
        max_dp = 100

        mock_event_bus = MagicMock()
        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger"):
                await sync._publish_player_dp_update_event(player_id, old_dp, new_dp, max_dp)

                mock_nats_service.publish.assert_called_once()
                call_args = mock_nats_service.publish.call_args
                assert call_args[0][0] == "combat.dp_update.test"
                assert "event_type" in call_args[0][1]

    @pytest.mark.asyncio
    async def test_publish_player_dp_update_event_nats_legacy_subject(self) -> None:
        """Test event publishing with NATS using legacy subject construction."""
        mock_combat_service = MagicMock()
        mock_nats_service = AsyncMock()
        mock_combat_service._nats_service = mock_nats_service
        mock_combat_event_publisher = MagicMock()
        mock_combat_event_publisher.subject_manager = None
        mock_combat_service._combat_event_publisher = mock_combat_event_publisher
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        old_dp = 50
        new_dp = 40
        max_dp = 100

        mock_event_bus = MagicMock()
        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                await sync._publish_player_dp_update_event(player_id, old_dp, new_dp, max_dp)

                mock_nats_service.publish.assert_called_once()
                call_args = mock_nats_service.publish.call_args
                assert f"combat.dp_update.{player_id}" in call_args[0][0]
                mock_logger.warning.assert_called()
                assert "legacy" in str(mock_logger.warning.call_args).lower()

    @pytest.mark.asyncio
    async def test_publish_player_dp_update_event_event_bus_error(self) -> None:
        """Test when event bus publish fails."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        old_dp = 50
        new_dp = 40
        max_dp = 100

        mock_event_bus = MagicMock()
        mock_event_bus.publish.side_effect = ValueError("Event bus error")
        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                await sync._publish_player_dp_update_event(player_id, old_dp, new_dp, max_dp)

                mock_logger.error.assert_called()
                # Check that error was logged (either for event bus or general error)
                error_calls = [str(call) for call in mock_logger.error.call_args_list]
                assert any("Failed to publish" in call or "Error publishing" in call for call in error_calls)

    @pytest.mark.asyncio
    async def test_publish_player_dp_update_event_no_event_bus(self) -> None:
        """Test when event bus is None."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        old_dp = 50
        new_dp = 40
        max_dp = 100

        with patch("server.services.combat_hp_sync.EventBus", return_value=None):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                await sync._publish_player_dp_update_event(player_id, old_dp, new_dp, max_dp)

                mock_logger.warning.assert_called()
                assert "No event bus" in str(mock_logger.warning.call_args)


class TestPublishPlayerDpCorrectionEvent:
    """Test _publish_player_dp_correction_event method."""

    @pytest.mark.asyncio
    async def test_publish_player_dp_correction_event_success(self) -> None:
        """Test successful correction event publishing."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        correct_dp = 50
        max_dp = 100

        # EventBus.publish() is synchronous, so use Mock, not AsyncMock
        mock_event_bus = MagicMock()
        mock_event_bus.publish = Mock()  # Explicitly set as synchronous Mock
        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger"):
                await sync._publish_player_dp_correction_event(player_id, correct_dp, max_dp)

                mock_event_bus.publish.assert_called_once()
                event = mock_event_bus.publish.call_args[0][0]
                assert isinstance(event, PlayerDPUpdated)
                assert event.old_dp == correct_dp
                assert event.new_dp == correct_dp
                assert event.damage_taken == 0

    @pytest.mark.asyncio
    async def test_publish_player_dp_correction_event_error(self) -> None:
        """Test when event bus publish fails."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)

        player_id = uuid4()
        correct_dp = 50
        max_dp = 100

        mock_event_bus = MagicMock()
        mock_event_bus.publish.side_effect = RuntimeError("Event bus error")
        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                await sync._publish_player_dp_correction_event(player_id, correct_dp, max_dp)

                mock_logger.error.assert_called()
                assert "Failed to publish" in str(mock_logger.error.call_args)


class TestPersistPlayerDpBackground:
    """Test _persist_player_dp_background method."""

    def test_persist_player_dp_background_success(self) -> None:
        """Test successful background persistence."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        def create_task_side_effect(coro):
            # Close the coroutine to prevent "never awaited" warning
            coro.close()
            return MagicMock()

        with patch("asyncio.create_task", side_effect=create_task_side_effect) as mock_create_task:
            with patch.object(sync, "_persist_player_dp_sync", new_callable=AsyncMock):
                with patch("server.services.combat_hp_sync.logger"):
                    sync._persist_player_dp_background(player_id, 40, 50, 100)

                    mock_create_task.assert_called_once()

    def test_persist_player_dp_background_no_event_loop(self) -> None:
        """Test when no event loop is available."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        with patch("asyncio.create_task", side_effect=RuntimeError("No event loop")):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                sync._persist_player_dp_background(player_id, 40, 50, 100)

                mock_logger.error.assert_called_once()
                assert "no event loop" in str(mock_logger.error.call_args).lower()

    @pytest.mark.asyncio
    async def test_persist_player_dp_background_persistence_failure(self) -> None:
        """Test when persistence fails and correction event is sent."""
        import asyncio

        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        # Track created coroutines to await them
        created_coros = []

        def create_task_side_effect(coro):
            """Track and properly handle created tasks."""
            created_coros.append(coro)
            # Return a mock task that won't cause issues
            task = MagicMock()
            task.done.return_value = False
            return task

        with patch.object(sync, "_persist_player_dp_sync", side_effect=DatabaseError("Database error")):
            with patch.object(sync, "_publish_player_dp_correction_event", new_callable=AsyncMock) as mock_publish:
                with patch("server.services.combat_hp_sync.logger"):
                    with patch("asyncio.create_task", side_effect=create_task_side_effect):
                        # Call the actual method that creates the background task
                        sync._persist_player_dp_background(player_id, 40, 50, 100, None, None)

                        # Wait a bit for the task to be created
                        await asyncio.sleep(0.1)

                        # Await all created coroutines to prevent warnings
                        for coro in created_coros:
                            try:
                                await coro
                            except DatabaseError:
                                pass  # Expected

                        mock_publish.assert_called_once()

    @pytest.mark.asyncio
    async def test_persist_player_dp_background_correction_event_failure(self) -> None:
        """Test when correction event also fails."""
        mock_combat_service = MagicMock()
        sync = CombatDPSync(mock_combat_service)
        player_id = uuid4()

        # Test the error handling inside _publish_player_dp_correction_event
        # by making EventBus.publish raise an error
        mock_event_bus = MagicMock()
        mock_event_bus.publish.side_effect = RuntimeError("Event bus error")

        with patch("server.services.combat_hp_sync.EventBus", return_value=mock_event_bus):
            with patch("server.services.combat_hp_sync.logger") as mock_logger:
                await sync._publish_player_dp_correction_event(player_id, 50, 100, None, None, "Test error")

                # Should log error for correction event failure
                error_calls = [str(call) for call in mock_logger.error.call_args_list]
                assert any("correction event" in call.lower() or "Error publishing" in call for call in error_calls)
