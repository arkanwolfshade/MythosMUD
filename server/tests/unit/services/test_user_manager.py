"""
Tests for user management service.

This module tests the UserManager class which provides comprehensive
user management including muting, permissions, and user state tracking.
"""

import tempfile
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.services.user_manager import UserManager


class TestUserManagerInit:
    """Test UserManager initialization."""

    def test_init_default(self) -> None:
        """Test UserManager initialization with default parameters."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))

            assert manager._player_mutes == {}
            assert manager._channel_mutes == {}
            assert manager._global_mutes == {}
            assert manager._admin_players == set()
            assert manager.data_dir == Path(tmpdir)
            assert manager._mute_cache_ttl == timedelta(seconds=300)

    def test_init_custom_cache_ttl(self) -> None:
        """Test UserManager initialization with custom cache TTL."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir), mute_cache_ttl=600)

            assert manager._mute_cache_ttl == timedelta(seconds=600)


class TestNormalizeToUuid:
    """Test _normalize_to_uuid method."""

    def test_normalize_to_uuid_uuid_object(self) -> None:
        """Test normalizing UUID object."""
        manager = UserManager()
        player_id = uuid4()

        result = manager._normalize_to_uuid(player_id)

        assert result == player_id
        assert isinstance(result, type(player_id))

    def test_normalize_to_uuid_string(self) -> None:
        """Test normalizing UUID string."""
        manager = UserManager()
        player_id = uuid4()
        player_id_str = str(player_id)

        result = manager._normalize_to_uuid(player_id_str)

        assert result == player_id
        assert isinstance(result, type(player_id))

    def test_normalize_to_uuid_invalid(self) -> None:
        """Test normalizing invalid UUID."""
        manager = UserManager()

        with pytest.raises(ValueError):
            manager._normalize_to_uuid("invalid-uuid")


class TestAddAdmin:
    """Test add_admin method."""

    @pytest.mark.asyncio
    async def test_add_admin_success(self) -> None:
        """Test successfully adding admin."""
        manager = UserManager()
        player_id = uuid4()

        mock_player = MagicMock()
        mock_player.set_admin_status = MagicMock()

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()

        mock_container = MagicMock()
        mock_container.async_persistence = mock_persistence

        with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
            with patch("server.services.user_manager.logger"):
                result = await manager.add_admin(player_id, "TestPlayer")

                assert result is True
                assert player_id in manager._admin_players
                mock_player.set_admin_status.assert_called_once_with(True)
                mock_persistence.save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_add_admin_no_container(self) -> None:
        """Test adding admin when container is not available."""
        manager = UserManager()
        player_id = uuid4()

        with patch("server.container.ApplicationContainer.get_instance", return_value=None):
            with patch("server.services.user_manager.logger"):
                result = await manager.add_admin(player_id)

                assert result is False

    @pytest.mark.asyncio
    async def test_add_admin_player_not_found(self) -> None:
        """Test adding admin when player is not found."""
        manager = UserManager()
        player_id = uuid4()

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=None)

        mock_container = MagicMock()
        mock_container.async_persistence = mock_persistence

        with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
            with patch("server.services.user_manager.logger"):
                result = await manager.add_admin(player_id)

                # When player is None, the code logs info but still adds to cache and returns True
                # This is the actual behavior - it adds to cache even if player not found
                assert result is True
                assert player_id in manager._admin_players


class TestRemoveAdmin:
    """Test remove_admin method."""

    @pytest.mark.asyncio
    async def test_remove_admin_success(self) -> None:
        """Test successfully removing admin."""
        manager = UserManager()
        player_id = uuid4()
        manager._admin_players.add(player_id)

        mock_player = MagicMock()
        mock_player.set_admin_status = MagicMock()

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()

        mock_container = MagicMock()
        mock_container.async_persistence = mock_persistence

        with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
            with patch("server.services.user_manager.logger"):
                result = await manager.remove_admin(player_id, "TestPlayer")

                assert result is True
                assert player_id not in manager._admin_players
                mock_player.set_admin_status.assert_called_once_with(False)


class TestIsAdminSync:
    """Test is_admin_sync method."""

    def test_is_admin_sync_true(self) -> None:
        """Test checking admin when player is admin."""
        manager = UserManager()
        player_id = uuid4()
        manager._admin_players.add(player_id)

        result = manager.is_admin_sync(player_id)

        assert result is True

    def test_is_admin_sync_false(self) -> None:
        """Test checking admin when player is not admin."""
        manager = UserManager()
        player_id = uuid4()

        result = manager.is_admin_sync(player_id)

        assert result is False


class TestIsAdmin:
    """Test is_admin method."""

    @pytest.mark.asyncio
    async def test_is_admin_in_cache(self) -> None:
        """Test checking admin when player is in cache."""
        manager = UserManager()
        player_id = uuid4()
        manager._admin_players.add(player_id)

        result = await manager.is_admin(player_id)

        assert result is True

    @pytest.mark.asyncio
    async def test_is_admin_in_database(self) -> None:
        """Test checking admin when player is in database."""
        manager = UserManager()
        player_id = uuid4()

        mock_player = MagicMock()
        mock_player.is_admin_user.return_value = True

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)

        mock_container = MagicMock()
        mock_container.async_persistence = mock_persistence

        with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
            with patch("server.services.user_manager.logger"):
                result = await manager.is_admin(player_id)

                assert result is True
                assert player_id in manager._admin_players

    @pytest.mark.asyncio
    async def test_is_admin_not_found(self) -> None:
        """Test checking admin when player is not found."""
        manager = UserManager()
        player_id = uuid4()

        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        mock_persistence = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=None)

        mock_container = MagicMock()
        mock_container.async_persistence = mock_persistence

        with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
            with patch("server.services.user_manager.logger"):
                result = await manager.is_admin(player_id)

                assert result is False


class TestMutePlayer:
    """Test mute_player method."""

    def test_mute_player_success(self) -> None:
        """Test successfully muting a player."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            muter_id = uuid4()
            target_id = uuid4()

            with patch.object(manager, "is_admin_sync", return_value=False):
                with patch.object(manager, "save_player_mutes", return_value=True):
                    with patch("server.services.user_manager.logger"):
                        result = manager.mute_player(
                            muter_id, "Muter", target_id, "Target", duration_minutes=60, reason="Test"
                        )

                        assert result is True
                        assert muter_id in manager._player_mutes
                        assert target_id in manager._player_mutes[muter_id]

    def test_mute_player_admin_immune(self) -> None:
        """Test that admin players are immune to mutes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            muter_id = uuid4()
            target_id = uuid4()

            with patch.object(manager, "is_admin_sync", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.mute_player(muter_id, "Muter", target_id, "Target")

                    assert result is False
                    assert muter_id not in manager._player_mutes


class TestUnmutePlayer:
    """Test unmute_player method."""

    def test_unmute_player_success(self) -> None:
        """Test successfully unmuting a player."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            unmuter_id = uuid4()
            target_id = uuid4()

            # Set up mute
            manager._player_mutes[unmuter_id] = {
                target_id: {
                    "target_id": target_id,
                    "target_name": "Target",
                    "muted_by": unmuter_id,
                    "muted_by_name": "Unmuter",
                    "muted_at": datetime.now(UTC),
                    "expires_at": None,
                    "reason": "",
                    "is_permanent": True,
                }
            }

            with patch.object(manager, "load_player_mutes", return_value=True):
                with patch.object(manager, "save_player_mutes", return_value=True):
                    with patch("server.services.user_manager.logger"):
                        result = manager.unmute_player(unmuter_id, "Unmuter", target_id, "Target")

                        assert result is True
                        assert unmuter_id not in manager._player_mutes

    def test_unmute_player_not_muted(self) -> None:
        """Test unmuting a player that is not muted."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            unmuter_id = uuid4()
            target_id = uuid4()

            with patch.object(manager, "load_player_mutes", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.unmute_player(unmuter_id, "Unmuter", target_id, "Target")

                    assert result is False


class TestMuteChannel:
    """Test mute_channel method."""

    def test_mute_channel_success(self) -> None:
        """Test successfully muting a channel."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            player_id = uuid4()

            with patch.object(manager, "save_player_mutes", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.mute_channel(player_id, "Player", "general", duration_minutes=60, reason="Test")

                    assert result is True
                    assert player_id in manager._channel_mutes
                    assert "general" in manager._channel_mutes[player_id]


class TestUnmuteChannel:
    """Test unmute_channel method."""

    def test_unmute_channel_success(self) -> None:
        """Test successfully unmuting a channel."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            player_id = uuid4()

            # Set up channel mute
            manager._channel_mutes[player_id] = {
                "general": {
                    "channel": "general",
                    "muted_at": datetime.now(UTC),
                    "expires_at": None,
                    "reason": "",
                    "is_permanent": True,
                }
            }

            with patch.object(manager, "save_player_mutes", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.unmute_channel(player_id, "Player", "general")

                    assert result is True
                    assert player_id not in manager._channel_mutes


class TestMuteGlobal:
    """Test mute_global method."""

    def test_mute_global_success(self) -> None:
        """Test successfully applying global mute."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            muter_id = uuid4()
            target_id = uuid4()

            # mute_global now uses is_admin_sync (fixed in code)
            with patch.object(manager, "is_admin_sync", return_value=False):
                with patch.object(manager, "save_player_mutes", return_value=True):
                    with patch("server.services.user_manager.logger"):
                        result = manager.mute_global(
                            muter_id, "Muter", target_id, "Target", duration_minutes=60, reason="Test"
                        )

                        assert result is True
                        assert target_id in manager._global_mutes

    @pytest.mark.asyncio
    async def test_mute_global_admin_immune(self) -> None:
        """Test that admin players are immune to global mutes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            muter_id = uuid4()
            target_id = uuid4()

            with patch.object(manager, "is_admin_sync", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.mute_global(muter_id, "Muter", target_id, "Target")

                    assert result is False
                    assert target_id not in manager._global_mutes


class TestIsPlayerMuted:
    """Test is_player_muted method."""

    def test_is_player_muted_true(self) -> None:
        """Test checking if player is muted when muted."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            player_id = uuid4()
            target_id = uuid4()

            # Set up mute
            manager._player_mutes[player_id] = {
                target_id: {
                    "target_id": target_id,
                    "target_name": "Target",
                    "muted_by": player_id,
                    "muted_by_name": "Player",
                    "muted_at": datetime.now(UTC),
                    "expires_at": None,
                    "reason": "",
                    "is_permanent": True,
                }
            }

            with patch.object(manager, "load_player_mutes", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.is_player_muted(player_id, target_id)

                    assert result is True

    def test_is_player_muted_expired(self) -> None:
        """Test checking if player is muted when mute is expired."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            player_id = uuid4()
            target_id = uuid4()

            # Set up expired mute
            manager._player_mutes[player_id] = {
                target_id: {
                    "target_id": target_id,
                    "target_name": "Target",
                    "muted_by": player_id,
                    "muted_by_name": "Player",
                    "muted_at": datetime.now(UTC) - timedelta(hours=2),
                    "expires_at": datetime.now(UTC) - timedelta(hours=1),  # Expired
                    "reason": "",
                    "is_permanent": False,
                }
            }

            with patch.object(manager, "load_player_mutes", return_value=True):
                with patch("server.services.user_manager.logger"):
                    result = manager.is_player_muted(player_id, target_id)

                    assert result is False
                    assert player_id not in manager._player_mutes


class TestIsChannelMuted:
    """Test is_channel_muted method."""

    def test_is_channel_muted_true(self) -> None:
        """Test checking if channel is muted when muted."""
        manager = UserManager()
        player_id = uuid4()

        # Set up channel mute
        manager._channel_mutes[player_id] = {
            "general": {
                "channel": "general",
                "muted_at": datetime.now(UTC),
                "expires_at": None,
                "reason": "",
                "is_permanent": True,
            }
        }

        result = manager.is_channel_muted(player_id, "general")

        assert result is True

    def test_is_channel_muted_expired(self) -> None:
        """Test checking if channel is muted when mute is expired."""
        manager = UserManager()
        player_id = uuid4()

        # Set up expired channel mute
        manager._channel_mutes[player_id] = {
            "general": {
                "channel": "general",
                "muted_at": datetime.now(UTC) - timedelta(hours=2),
                "expires_at": datetime.now(UTC) - timedelta(hours=1),  # Expired
                "reason": "",
                "is_permanent": False,
            }
        }

        result = manager.is_channel_muted(player_id, "general")

        assert result is False
        assert player_id not in manager._channel_mutes


class TestIsGloballyMuted:
    """Test is_globally_muted method."""

    def test_is_globally_muted_true(self) -> None:
        """Test checking if player is globally muted when muted."""
        manager = UserManager()
        player_id = uuid4()

        # Set up global mute
        manager._global_mutes[player_id] = {
            "target_id": player_id,
            "target_name": "Player",
            "muted_by": uuid4(),
            "muted_by_name": "Admin",
            "muted_at": datetime.now(UTC),
            "expires_at": None,
            "reason": "",
            "is_permanent": True,
        }

        result = manager.is_globally_muted(player_id)

        assert result is True

    def test_is_globally_muted_expired(self) -> None:
        """Test checking if player is globally muted when mute is expired."""
        manager = UserManager()
        player_id = uuid4()

        # Set up expired global mute
        manager._global_mutes[player_id] = {
            "target_id": player_id,
            "target_name": "Player",
            "muted_by": uuid4(),
            "muted_by_name": "Admin",
            "muted_at": datetime.now(UTC) - timedelta(hours=2),
            "expires_at": datetime.now(UTC) - timedelta(hours=1),  # Expired
            "reason": "",
            "is_permanent": False,
        }

        result = manager.is_globally_muted(player_id)

        assert result is False
        assert player_id not in manager._global_mutes


class TestCanSendMessage:
    """Test can_send_message method."""

    def test_can_send_message_admin(self) -> None:
        """Test that admins can always send messages."""
        manager = UserManager()
        player_id = uuid4()

        with patch.object(manager, "is_admin_sync", return_value=True):
            result = manager.can_send_message(player_id)

            assert result is True

    def test_can_send_message_globally_muted(self) -> None:
        """Test that globally muted players cannot send messages."""
        manager = UserManager()
        player_id = uuid4()

        with patch.object(manager, "is_admin_sync", return_value=False):
            with patch.object(manager, "is_globally_muted", return_value=True):
                result = manager.can_send_message(player_id)

                assert result is False

    def test_can_send_message_channel_muted(self) -> None:
        """Test that channel muted players cannot send to that channel."""
        manager = UserManager()
        player_id = uuid4()

        with patch.object(manager, "is_admin_sync", return_value=False):
            with patch.object(manager, "is_globally_muted", return_value=False):
                with patch.object(manager, "is_channel_muted", return_value=True):
                    result = manager.can_send_message(player_id, channel="general")

                    assert result is False


class TestGetSystemStats:
    """Test get_system_stats method."""

    def test_get_system_stats(self) -> None:
        """Test getting system statistics."""
        manager = UserManager()
        player_id1 = uuid4()
        player_id2 = uuid4()

        # Set up some mutes
        manager._player_mutes[player_id1] = {player_id2: {}}
        manager._channel_mutes[player_id1] = {"general": {}}
        manager._global_mutes[player_id2] = {}
        manager._admin_players.add(player_id1)

        with patch.object(manager, "_cleanup_expired_mutes"):
            result = manager.get_system_stats()

            assert result["total_players_with_mutes"] == 1
            assert result["total_channel_mutes"] == 1
            assert result["total_global_mutes"] == 1
            assert result["total_admin_players"] == 1
            assert str(player_id1) in result["admin_players"]


class TestSaveAndLoadPlayerMutes:
    """Test save_player_mutes and load_player_mutes methods."""

    def test_save_and_load_player_mutes(self) -> None:
        """Test saving and loading player mutes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = UserManager(data_dir=Path(tmpdir))
            player_id = uuid4()
            target_id = uuid4()

            # Set up mute
            manager._player_mutes[player_id] = {
                target_id: {
                    "target_id": target_id,
                    "target_name": "Target",
                    "muted_by": player_id,
                    "muted_by_name": "Player",
                    "muted_at": datetime.now(UTC),
                    "expires_at": None,
                    "reason": "Test",
                    "is_permanent": True,
                }
            }

            # Save
            with patch("server.services.user_manager.logger"):
                save_result = manager.save_player_mutes(player_id)
                assert save_result is True

            # Clear in-memory data
            manager._player_mutes.clear()

            # Load
            with patch("server.services.user_manager.logger"):
                load_result = manager.load_player_mutes(player_id)
                assert load_result is True
                assert player_id in manager._player_mutes
                assert target_id in manager._player_mutes[player_id]
