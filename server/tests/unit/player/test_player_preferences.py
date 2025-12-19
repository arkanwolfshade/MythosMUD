"""
Tests for player channel preferences functionality.

This module tests the player channel preferences table and service
for the Advanced Chat Channels feature using PostgreSQL.
"""

import uuid
from collections.abc import AsyncGenerator
from typing import Any

import pytest
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.database import get_database_url
from server.models.player import Player, PlayerChannelPreferences
from server.models.user import User
from server.services.player_preferences_service import PlayerPreferencesService


@pytest.fixture(name="session_factory")
async def _session_factory() -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
    """Create an async session factory for testing."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    engine = create_async_engine(database_url, future=True)
    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


@pytest.fixture(autouse=True)
async def cleanup_players(session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[None, None]:
    """Delete all players, preferences, users, and lucidity records before each test to ensure isolation."""
    yield
    # Cleanup after test
    async with session_factory() as session:
        from sqlalchemy import text

        try:
            # Delete in order to respect foreign key constraints
            await session.execute(text("DELETE FROM player_channel_preferences"))
            await session.execute(text("DELETE FROM player_Lucidity"))
            await session.execute(text("DELETE FROM players"))
            await session.execute(text("DELETE FROM users"))
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            # Ignore cleanup errors - test might have already cleaned up


async def create_test_player(session: AsyncSession, player_id: str) -> Player:
    """Create a test player for preferences testing.

    Args:
        session: Database session
        player_id: String identifier used only for generating unique username (not used as actual player_id)

    Returns:
        Player object with valid UUID player_id
    """
    # Generate valid UUID for player_id (PostgreSQL requires UUID type)
    # Use player_id string as seed for username only, not for the actual player_id
    unique_player_id = uuid.uuid4()  # Generate UUID object
    unique_username = f"{player_id}-{str(uuid.uuid4())[:8]}"
    user_uuid = uuid.uuid4()
    user = User(
        id=str(user_uuid),
        email=f"{unique_username}@example.com",
        username=unique_username,
        display_name=unique_username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=str(unique_player_id),  # Convert UUID to string for UUID(as_uuid=False) column
        user_id=str(user_uuid),
        name=unique_username,  # Use unique username to avoid duplicate key violations
    )
    session.add_all([user, player])
    await session.flush()
    return player


class TestPlayerChannelPreferencesTable:
    """Test the player_channel_preferences table schema and operations."""

    @pytest.mark.asyncio
    async def test_preferences_table_exists(self, session_factory: Any) -> None:
        """Test that the preferences table exists in the database."""
        from sqlalchemy import text

        async with session_factory() as session:
            # Check table exists using PostgreSQL information_schema
            result = await session.execute(
                text(
                    """
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public' AND table_name = 'player_channel_preferences'
                """
                )
            )
            table_exists = result.fetchone() is not None
            assert table_exists

    @pytest.mark.asyncio
    async def test_preferences_table_schema(self, session_factory: Any) -> None:
        """Test that the preferences table has the correct schema."""
        from sqlalchemy import text

        async with session_factory() as session:
            # Use PostgreSQL information_schema to check columns
            result = await session.execute(
                text(
                    """
                    SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = 'player_channel_preferences'
                    ORDER BY ordinal_position
                """
                )
            )
            columns = {row[0]: row[1] for row in result.fetchall()}

            # Check required columns exist
            assert "player_id" in columns
            assert "default_channel" in columns
            assert "muted_channels" in columns
            assert "created_at" in columns
            assert "updated_at" in columns

    @pytest.mark.asyncio
    async def test_preferences_table_constraints(self, session_factory: Any) -> None:
        """Test that the preferences table has correct constraints."""
        async with session_factory() as session:
            # Create a test player first
            player = await create_test_player(session, "test-constraints-player")

            # Test primary key constraint
            preferences1 = PlayerChannelPreferences(
                player_id=str(player.player_id),
                default_channel="local",
                muted_channels=[],
            )
            session.add(preferences1)
            await session.commit()

            # Try to create duplicate - should fail
            with pytest.raises(IntegrityError):
                preferences2 = PlayerChannelPreferences(
                    player_id=str(player.player_id),
                    default_channel="global",
                    muted_channels=[],
                )
                session.add(preferences2)
                await session.commit()


class TestPlayerPreferencesService:
    """Test the PlayerPreferencesService functionality."""

    @pytest.mark.asyncio
    async def test_create_player_preferences(self, session_factory: Any) -> None:
        """Test creating preferences for a new player."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-123")
            service = PlayerPreferencesService()

            # Create preferences
            result = await service.create_player_preferences(session, str(player.player_id))
            assert result["success"] is True

            # Verify preferences were created with defaults
            preferences = await service.get_player_preferences(session, str(player.player_id))
            assert preferences["success"] is True
            assert preferences["data"]["player_id"] == str(player.player_id)
            assert preferences["data"]["default_channel"] == "local"
            assert preferences["data"]["muted_channels"] == []

    @pytest.mark.asyncio
    async def test_get_player_preferences_not_found(self, session_factory: Any) -> None:
        """Test getting preferences for non-existent player."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            # Use a valid UUID format for non-existent player
            non_existent_id = uuid.uuid4()
            result = await service.get_player_preferences(session, non_existent_id)
            assert result["success"] is False
            assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_update_default_channel(self, session_factory: Any) -> None:
        """Test updating a player's default channel."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-456")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Update default channel
            result = await service.update_default_channel(session, str(player.player_id), "global")
            assert result["success"] is True

            # Verify update
            preferences = await service.get_player_preferences(session, str(player.player_id))
            assert preferences["data"]["default_channel"] == "global"

    @pytest.mark.asyncio
    async def test_update_default_channel_invalid(self, session_factory: Any) -> None:
        """Test updating default channel with invalid value."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-789")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Try to update with invalid channel
            result = await service.update_default_channel(session, str(player.player_id), "invalid_channel")
            assert result["success"] is False
            assert "invalid" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_mute_channel(self, session_factory: Any) -> None:
        """Test muting a channel for a player."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-mute")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Mute global channel
            result = await service.mute_channel(session, str(player.player_id), "global")
            assert result["success"] is True

            # Verify channel is muted
            preferences = await service.get_player_preferences(session, str(player.player_id))
            muted_channels = preferences["data"]["muted_channels"]
            assert "global" in muted_channels

    @pytest.mark.asyncio
    async def test_unmute_channel(self, session_factory: Any) -> None:
        """Test unmuting a channel for a player."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-unmute")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Mute global channel first
            await service.mute_channel(session, str(player.player_id), "global")

            # Unmute global channel
            result = await service.unmute_channel(session, str(player.player_id), "global")
            assert result["success"] is True

            # Verify channel is unmuted
            preferences = await service.get_player_preferences(session, str(player.player_id))
            muted_channels = preferences["data"]["muted_channels"]
            assert "global" not in muted_channels

    @pytest.mark.asyncio
    async def test_mute_system_channel(self, session_factory: Any) -> None:
        """Test that system channel cannot be muted."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-system")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Try to mute system channel
            result = await service.mute_channel(session, str(player.player_id), "system")
            assert result["success"] is False
            assert "system channel cannot be muted" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_get_muted_channels(self, session_factory: Any) -> None:
        """Test getting list of muted channels for a player."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-muted-list")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Mute multiple channels
            await service.mute_channel(session, str(player.player_id), "global")
            await service.mute_channel(session, str(player.player_id), "whisper")

            # Get muted channels
            result = await service.get_muted_channels(session, str(player.player_id))
            assert result["success"] is True
            muted_channels = result["data"]
            assert "global" in muted_channels
            assert "whisper" in muted_channels
            assert "local" not in muted_channels

    @pytest.mark.asyncio
    async def test_is_channel_muted(self, session_factory: Any) -> None:
        """Test checking if a specific channel is muted."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-check-mute")
            service = PlayerPreferencesService()

            # Create initial preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Initially not muted
            result = await service.is_channel_muted(session, str(player.player_id), "global")
            assert result["success"] is True
            assert result["data"] is False

            # Mute the channel
            await service.mute_channel(session, str(player.player_id), "global")

            # Now should be muted
            result = await service.is_channel_muted(session, str(player.player_id), "global")
            assert result["success"] is True
            assert result["data"] is True

    @pytest.mark.asyncio
    async def test_delete_player_preferences(self, session_factory: Any) -> None:
        """Test deleting player preferences."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-delete")
            service = PlayerPreferencesService()

            # Create preferences
            await service.create_player_preferences(session, str(player.player_id))

            # Verify they exist
            preferences = await service.get_player_preferences(session, str(player.player_id))
            assert preferences["success"] is True

            # Delete preferences
            result = await service.delete_player_preferences(session, str(player.player_id))
            assert result["success"] is True

            # Verify they're gone
            preferences = await service.get_player_preferences(session, str(player.player_id))
            assert preferences["success"] is False

    @pytest.mark.asyncio
    async def test_preferences_persistence(self, session_factory: Any) -> None:
        """Test that preferences persist across service instances."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-persistence")
            service1 = PlayerPreferencesService()

            # Create preferences with first service instance
            await service1.create_player_preferences(session, str(player.player_id))
            await service1.update_default_channel(session, str(player.player_id), "global")

            # Create new service instance
            service2 = PlayerPreferencesService()

            # Verify preferences persist
            preferences = await service2.get_player_preferences(session, str(player.player_id))
            assert preferences["success"] is True
            assert preferences["data"]["default_channel"] == "global"

    @pytest.mark.asyncio
    async def test_concurrent_access(self, session_factory: Any) -> None:
        """Test concurrent access to preferences."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-concurrent")
            service1 = PlayerPreferencesService()
            service2 = PlayerPreferencesService()

            # Create preferences with first service
            await service1.create_player_preferences(session, str(player.player_id))

            # Both services should see the preferences
            prefs1 = await service1.get_player_preferences(session, str(player.player_id))
            prefs2 = await service2.get_player_preferences(session, str(player.player_id))

            assert prefs1["success"] is True
            assert prefs2["success"] is True
            assert prefs1["data"]["player_id"] == prefs2["data"]["player_id"]


class TestPlayerPreferencesValidation:
    """Test validation of player preferences data."""

    @pytest.fixture
    def preferences_service(self) -> PlayerPreferencesService:
        """Create a PlayerPreferencesService instance."""
        return PlayerPreferencesService()

    def test_valid_channel_names(self, preferences_service: PlayerPreferencesService) -> None:
        """Test that valid channel names are accepted."""
        valid_channels = ["local", "global", "whisper", "system"]

        for channel in valid_channels:
            # This should not raise an exception
            assert preferences_service._is_valid_channel(channel) is True

    def test_invalid_channel_names(self, preferences_service: PlayerPreferencesService) -> None:
        """Test that invalid channel names are rejected."""
        invalid_channels = ["invalid", "test", "random", "chat", ""]

        for channel in invalid_channels:
            assert preferences_service._is_valid_channel(channel) is False

    def test_player_id_validation(self, preferences_service: PlayerPreferencesService) -> None:
        """Test player ID validation."""
        # Valid player IDs (UUID objects)
        valid_ids = [uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]

        for player_id in valid_ids:
            assert preferences_service._is_valid_player_id(player_id) is True

        # Invalid player IDs (non-UUID types)
        invalid_ids: list[Any] = [None, "", "not-a-uuid", 123]

        for p_id in invalid_ids:
            assert preferences_service._is_valid_player_id(p_id) is False

    def test_json_validation(self, preferences_service: PlayerPreferencesService) -> None:
        """Test JSON validation for muted_channels field."""
        # Valid JSON arrays
        valid_jsons = ["[]", '["local"]', '["global", "whisper"]']

        for json_str in valid_jsons:
            assert preferences_service._is_valid_json_array(json_str) is True

        # Invalid JSON
        invalid_jsons = ["", "invalid", '{"key": "value"}']

        for json_str in invalid_jsons:
            assert preferences_service._is_valid_json_array(json_str) is False


class TestPlayerPreferencesServiceErrorPaths:
    """Test error handling paths in PlayerPreferencesService."""

    @pytest.mark.asyncio
    async def test_create_player_preferences_invalid_player_id(self, session_factory: Any) -> None:
        """Test creating preferences with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.create_player_preferences(session, "")
            assert result["success"] is False
            assert "error" in result

    @pytest.mark.asyncio
    async def test_create_player_preferences_already_exists(self, session_factory: Any) -> None:
        """Test creating preferences when they already exist."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-duplicate")
            service = PlayerPreferencesService()

            # Create once
            result1 = await service.create_player_preferences(session, str(player.player_id))
            assert result1["success"] is True

            # Try to create again
            result2 = await service.create_player_preferences(session, str(player.player_id))
            assert result2["success"] is False
            assert "already exist" in result2["error"].lower()

    @pytest.mark.asyncio
    async def test_get_player_preferences_invalid_player_id(self, session_factory: Any) -> None:
        """Test getting preferences with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.get_player_preferences(session, "")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_get_player_preferences_not_found(self, session_factory: Any) -> None:
        """Test getting preferences for nonexistent player."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            # Use a valid UUID format for non-existent player
            non_existent_id = uuid.uuid4()
            result = await service.get_player_preferences(session, non_existent_id)
            assert result["success"] is False
            assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_update_default_channel_invalid_player_id(self, session_factory: Any) -> None:
        """Test updating channel with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.update_default_channel(session, "", "local")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_update_default_channel_invalid_channel(self, session_factory: Any) -> None:
        """Test updating to invalid channel."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-channel")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            result = await service.update_default_channel(session, str(player.player_id), "invalid_channel")
            assert result["success"] is False
            assert "invalid" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_mute_channel_invalid_player_id(self, session_factory: Any) -> None:
        """Test muting channel with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.mute_channel(session, "", "local")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_mute_channel_invalid_channel(self, session_factory: Any) -> None:
        """Test muting invalid channel."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-mute")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            result = await service.mute_channel(session, str(player.player_id), "invalid_channel")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_unmute_channel_invalid_player_id(self, session_factory: Any) -> None:
        """Test unmuting channel with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.unmute_channel(session, "", "local")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_unmute_channel_invalid_channel(self, session_factory: Any) -> None:
        """Test unmuting invalid channel."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-unmute")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            result = await service.unmute_channel(session, str(player.player_id), "invalid_channel")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_get_muted_channels_invalid_player_id(self, session_factory: Any) -> None:
        """Test getting muted channels with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.get_muted_channels(session, "")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_get_muted_channels_not_found(self, session_factory: Any) -> None:
        """Test getting muted channels for nonexistent player."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            # Use a valid UUID format for non-existent player
            non_existent_id = uuid.uuid4()
            result = await service.get_muted_channels(session, non_existent_id)
            assert result["success"] is False
            assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_is_channel_muted_invalid_player_id(self, session_factory: Any) -> None:
        """Test checking if channel muted with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.is_channel_muted(session, "", "local")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_is_channel_muted_invalid_channel(self, session_factory: Any) -> None:
        """Test checking if invalid channel is muted."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-check")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            result = await service.is_channel_muted(session, str(player.player_id), "invalid_channel")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_is_channel_muted_not_found(self, session_factory: Any) -> None:
        """Test checking if channel muted for nonexistent player."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            # Use a valid UUID format for non-existent player
            non_existent_id = uuid.uuid4()
            result = await service.is_channel_muted(session, non_existent_id, "local")
            assert result["success"] is False
            assert "not found" in result["error"].lower()

    @pytest.mark.asyncio
    async def test_delete_player_preferences_invalid_player_id(self, session_factory: Any) -> None:
        """Test deleting preferences with invalid player ID."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.delete_player_preferences(session, "")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_delete_player_preferences_not_found(self, session_factory: Any) -> None:
        """Test deleting preferences for nonexistent player."""
        async with session_factory() as session:
            service = PlayerPreferencesService()
            result = await service.delete_player_preferences(session, "nonexistent-player")
            # Service handles this gracefully - check that it returns a result
            assert "success" in result

    @pytest.mark.asyncio
    async def test_database_exception_in_get_preferences(self, session_factory: Any) -> None:
        """Test database exception handling in get_player_preferences."""
        async with session_factory() as session:
            service = PlayerPreferencesService()

            # Close the session to cause an exception
            await session.close()

            # Try to use closed session
            result = await service.get_player_preferences(session, "test-player")
            assert result["success"] is False
            assert "error" in result

    @pytest.mark.asyncio
    async def test_database_exception_in_update_channel(self, session_factory: Any) -> None:
        """Test database exception handling in update_default_channel."""
        from unittest.mock import patch

        async with session_factory() as session:
            player = await create_test_player(session, "test-player-update")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            # Mock session.execute to raise an exception
            with patch.object(session, "execute", side_effect=SQLAlchemyError("Database connection error")):
                result = await service.update_default_channel(session, str(player.player_id), "global")
                assert result["success"] is False
                assert "error" in result

    @pytest.mark.asyncio
    async def test_database_exception_in_mute_channel(self, session_factory: Any) -> None:
        """Test database exception handling in mute_channel."""
        from unittest.mock import patch

        async with session_factory() as session:
            player = await create_test_player(session, "test-player-mute")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            # Mock session.execute to raise an exception
            with patch.object(session, "execute", side_effect=SQLAlchemyError("Database connection error")):
                result = await service.mute_channel(session, str(player.player_id), "local")
                assert result["success"] is False
                assert "error" in result

    @pytest.mark.asyncio
    async def test_unmute_channel_not_in_muted_list(self, session_factory: Any) -> None:
        """Test unmuting a channel that isn't muted."""
        async with session_factory() as session:
            player = await create_test_player(session, "test-player-unmute-none")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            # Try to unmute a channel that was never muted
            result = await service.unmute_channel(session, str(player.player_id), "local")
            # Should still succeed
            assert result["success"] is True

    @pytest.mark.asyncio
    async def test_database_exception_in_unmute_channel(self, session_factory: Any) -> None:
        """Test database exception handling in unmute_channel."""
        from unittest.mock import patch

        async with session_factory() as session:
            player = await create_test_player(session, "test-player-unmute-err")
            service = PlayerPreferencesService()
            await service.create_player_preferences(session, str(player.player_id))

            # Mock session.execute to raise an exception
            with patch.object(session, "execute", side_effect=SQLAlchemyError("Database connection error")):
                result = await service.unmute_channel(session, str(player.player_id), "local")
                assert result["success"] is False
                assert "error" in result

    @pytest.mark.asyncio
    async def test_database_exception_in_get_muted_channels(self, session_factory: Any) -> None:
        """Test database exception handling in get_muted_channels."""
        async with session_factory() as session:
            service = PlayerPreferencesService()

            # Close the session to cause an exception
            await session.close()

            # Try to use closed session
            result = await service.get_muted_channels(session, "test-player")
            assert result["success"] is False

    @pytest.mark.asyncio
    async def test_database_exception_in_is_channel_muted(self, session_factory: Any) -> None:
        """Test database exception handling in is_channel_muted."""
        async with session_factory() as session:
            service = PlayerPreferencesService()

            # Close the session to cause an exception
            await session.close()

            # Try to use closed session
            result = await service.is_channel_muted(session, "test-player", "local")
            assert result["success"] is False
