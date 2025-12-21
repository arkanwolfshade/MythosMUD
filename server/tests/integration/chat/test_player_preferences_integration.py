"""
Integration tests for player channel preferences functionality.

This module tests the integration between the PlayerPreferencesService
and the PostgreSQL database, including persistence and real-world usage scenarios.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.database import get_database_url
from server.models.player import Player, PlayerChannelPreferences
from server.models.user import User
from server.services.player_preferences_service import PlayerPreferencesService


class TestPlayerPreferencesIntegration:
    """Integration tests for player preferences system."""

    @pytest.fixture
    async def async_session_factory(self):
        """Create an async session factory for testing."""
        database_url = get_database_url()
        if not database_url:
            raise ValueError("DATABASE_URL must be set for this integration test")

        engine = create_async_engine(database_url, future=True)
        factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        try:
            yield factory
        finally:
            # Clean up test data instead of dropping tables (safer for shared test DB)
            async with factory() as cleanup_session:
                try:
                    # Delete test data in reverse dependency order using raw SQL
                    await cleanup_session.execute(
                        text(
                            "DELETE FROM player_channel_preferences WHERE player_id::text LIKE 'integration-test-player%' OR player_id::text LIKE 'player%' OR player_id::text LIKE 'error-test-player%'"
                        )
                    )
                    await cleanup_session.execute(
                        text(
                            "DELETE FROM players WHERE player_id::text LIKE 'integration-test-player%' OR player_id::text LIKE 'player%' OR player_id::text LIKE 'error-test-player%'"
                        )
                    )
                    await cleanup_session.execute(text("DELETE FROM users WHERE email LIKE '%@example.com'"))
                    await cleanup_session.commit()
                except SQLAlchemyError:
                    await cleanup_session.rollback()
            await engine.dispose()

    @pytest.fixture
    async def test_player(self, async_session_factory):
        """Create a test player in the database."""
        async with async_session_factory() as session:
            # Create test user first with valid UUID and unique identifiers
            user_id = str(uuid.uuid4())
            unique_suffix = str(uuid.uuid4())[:8]
            user = User(
                id=user_id,
                email=f"test-prefs-{unique_suffix}@example.com",
                username=f"testprefs-{unique_suffix}",
                display_name=f"testprefs-{unique_suffix}",
                hashed_password="hashed_password",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
            session.add(user)

            # Create test player with unique ID (UUID)
            player_id = uuid.uuid4()
            player = Player(
                player_id=player_id,
                user_id=user_id,
                name=f"TestPlayer-{unique_suffix}",
                level=1,
            )
            session.add(player)
            await session.commit()
            # Store player_id instead of player object to avoid session issues
            yield player_id

    @pytest.fixture
    def preferences_service(self):
        """Create a PlayerPreferencesService instance."""
        return PlayerPreferencesService()

    @pytest.mark.asyncio
    async def test_full_player_lifecycle(self, async_session_factory, test_player, preferences_service):
        """Test complete player lifecycle with preferences."""
        player_id = test_player  # test_player fixture now yields player_id directly

        async with async_session_factory() as session:
            # 1. Create preferences
            result = await preferences_service.create_player_preferences(session, player_id)
            assert result["success"] is True

            # 2. Verify default preferences
            prefs = await preferences_service.get_player_preferences(session, player_id)
            assert prefs["success"] is True
            assert prefs["data"]["default_channel"] == "local"
            assert prefs["data"]["muted_channels"] == []

            # 3. Update default channel
            result = await preferences_service.update_default_channel(session, player_id, "global")
            assert result["success"] is True

            # 4. Mute some channels
            await preferences_service.mute_channel(session, player_id, "whisper")
            await preferences_service.mute_channel(session, player_id, "local")

            # 5. Verify final state
            prefs = await preferences_service.get_player_preferences(session, player_id)
            assert prefs["success"] is True
            assert prefs["data"]["default_channel"] == "global"

            muted_channels = prefs["data"]["muted_channels"]
            assert "whisper" in muted_channels
            assert "local" in muted_channels
            assert "global" not in muted_channels  # Should not be muted

            # 6. Verify foreign key constraint works
            # Load player object first, then delete

            player = await session.get(Player, player_id)
            if player:
                await session.delete(player)
            await session.commit()

            # Preferences should be automatically deleted due to CASCADE
            prefs = await preferences_service.get_player_preferences(session, player_id)
            assert prefs["success"] is False

    @pytest.mark.asyncio
    @pytest.mark.serial  # Mark as serial to prevent database transaction conflicts in parallel execution
    @pytest.mark.xdist_group(name="serial_integration_tests")  # Force serial execution with pytest-xdist
    async def test_multiple_players_preferences(self, async_session_factory, preferences_service):
        """Test managing preferences for multiple players."""
        async with async_session_factory() as session:
            # Generate unique player IDs (UUIDs) to avoid constraint violations on repeated test runs
            unique_suffix = str(uuid.uuid4())[:8]

            # Create test users and players with unique identifiers
            players_data = [
                (uuid.uuid4(), f"Player1-{unique_suffix}"),
                (uuid.uuid4(), f"Player2-{unique_suffix}"),
                (uuid.uuid4(), f"Player3-{unique_suffix}"),
            ]

            for player_id, name in players_data:
                user_id = str(uuid.uuid4())
                user = User(
                    id=user_id,
                    email=f"{name.lower()}@example.com",
                    username=name.lower(),
                    display_name=name,
                    hashed_password="hashed",
                    is_active=True,
                    is_superuser=False,
                    is_verified=True,
                )
                session.add(user)

                player = Player(player_id=player_id, user_id=user_id, name=name, level=1)
                session.add(player)
                # Flush after each player to avoid sentinel value issues
                await session.flush()

            await session.commit()

            # Create preferences for all players
            for player_id, _ in players_data:
                result = await preferences_service.create_player_preferences(session, player_id)
                assert result["success"] is True

            # Set different default channels
            await preferences_service.update_default_channel(session, players_data[0][0], "local")
            await preferences_service.update_default_channel(session, players_data[1][0], "global")
            await preferences_service.update_default_channel(session, players_data[2][0], "whisper")

            # Mute different channels for each player
            await preferences_service.mute_channel(session, players_data[0][0], "global")
            await preferences_service.mute_channel(session, players_data[1][0], "whisper")
            await preferences_service.mute_channel(session, players_data[2][0], "local")

            # Verify each player has correct preferences
            prefs1 = await preferences_service.get_player_preferences(session, players_data[0][0])
            prefs2 = await preferences_service.get_player_preferences(session, players_data[1][0])
            prefs3 = await preferences_service.get_player_preferences(session, players_data[2][0])

            assert prefs1["data"]["default_channel"] == "local"
            assert prefs2["data"]["default_channel"] == "global"
            assert prefs3["data"]["default_channel"] == "whisper"

            muted1 = prefs1["data"]["muted_channels"]
            muted2 = prefs2["data"]["muted_channels"]
            muted3 = prefs3["data"]["muted_channels"]

            assert "global" in muted1
            assert "whisper" in muted2
            assert "local" in muted3

    @pytest.mark.asyncio
    async def test_preferences_persistence_across_restarts(
        self, async_session_factory, test_player, preferences_service
    ):
        """Test that preferences persist when service is restarted."""
        player_id = test_player  # test_player fixture now yields player_id directly

        # Create preferences with first service instance
        async with async_session_factory() as session:
            await preferences_service.create_player_preferences(session, player_id)
            await preferences_service.update_default_channel(session, player_id, "global")
            await preferences_service.mute_channel(session, player_id, "whisper")

        # Simulate service restart by creating new instance
        service2 = PlayerPreferencesService()

        # Verify preferences persist
        async with async_session_factory() as session:
            prefs = await service2.get_player_preferences(session, player_id)
            assert prefs["success"] is True
            assert prefs["data"]["default_channel"] == "global"

            muted_channels = prefs["data"]["muted_channels"]
            assert "whisper" in muted_channels

    @pytest.mark.asyncio
    async def test_concurrent_preferences_access(self, async_session_factory, test_player):
        """Test concurrent access to preferences from multiple service instances."""
        player_id = test_player  # test_player fixture now yields player_id directly

        # Create multiple service instances
        services = [PlayerPreferencesService() for _ in range(3)]

        # Create preferences with first service
        async with async_session_factory() as session:
            await services[0].create_player_preferences(session, player_id)

            # All services should see the preferences
            for i, service in enumerate(services):
                prefs = await service.get_player_preferences(session, player_id)
                assert prefs["success"] is True, f"Service {i} failed to see preferences"

            # Update preferences from different service
            await services[1].update_default_channel(session, player_id, "global")

            # All services should see the update
            for i, service in enumerate(services):
                prefs = await service.get_player_preferences(session, player_id)
                assert prefs["data"]["default_channel"] == "global", f"Service {i} failed to see update"

    @pytest.mark.asyncio
    async def test_database_constraints_and_indexes(self, async_session_factory, test_player, preferences_service):
        """Test that database constraints and indexes work correctly."""
        player_id = test_player  # test_player fixture now yields player_id directly

        async with async_session_factory() as session:
            # Test primary key constraint
            await preferences_service.create_player_preferences(session, player_id)

            # Try to create duplicate - should fail
            with pytest.raises(IntegrityError):
                duplicate_prefs = PlayerChannelPreferences(
                    player_id=player_id,
                    default_channel="local",
                    muted_channels=[],
                )
                session.add(duplicate_prefs)
                await session.commit()

            # Rollback after the first IntegrityError
            await session.rollback()

            # Test foreign key constraint
            with pytest.raises(IntegrityError):
                invalid_prefs = PlayerChannelPreferences(
                    player_id=uuid.uuid4(),  # Non-existent player ID
                    default_channel="local",
                    muted_channels=[],
                )
                session.add(invalid_prefs)
                await session.commit()

    @pytest.mark.asyncio
    async def test_error_handling_and_recovery(self, async_session_factory, preferences_service):
        """Test error handling and recovery scenarios."""
        # Generate unique suffix to avoid constraint violations on repeated test runs
        unique_suffix = str(uuid.uuid4())[:8]
        async with async_session_factory() as session:
            # Create test user and player with unique identifiers
            unique_suffix = str(uuid.uuid4())[:8]
            user_id = str(uuid.uuid4())
            user = User(
                id=user_id,
                email=f"error-{unique_suffix}@example.com",
                username=f"erroruser-{unique_suffix}",
                display_name=f"erroruser-{unique_suffix}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
            session.add(user)

            player_id = uuid.uuid4()
            player = Player(player_id=player_id, user_id=user_id, name=f"ErrorPlayer-{unique_suffix}", level=1)
            session.add(player)
            await session.commit()

            # Test with invalid player ID
            result = await preferences_service.create_player_preferences(session, "")
            assert result["success"] is False
            assert "Invalid player ID" in result["error"]

            # Test with invalid channel
            await preferences_service.create_player_preferences(session, player_id)
            result = await preferences_service.update_default_channel(session, player_id, "invalid_channel")
            assert result["success"] is False
            assert "Invalid channel name" in result["error"]

            # Test with non-existent player (use valid UUID format)
            from uuid import uuid4

            nonexistent_uuid = str(uuid4())
            result = await preferences_service.get_player_preferences(session, nonexistent_uuid)
            assert result["success"] is False
            # Service validates UUID format first, so "not found" or "Invalid player ID" are both valid
            assert "not found" in result["error"] or "Invalid player ID" in result["error"]

            # Test system channel muting
            result = await preferences_service.mute_channel(session, player_id, "system")
            assert result["success"] is False
            assert "System channel cannot be muted" in result["error"]

    @pytest.mark.asyncio
    async def test_json_handling_edge_cases(self, async_session_factory, test_player, preferences_service):
        """Test edge cases in JSON handling for muted channels."""
        player_id = test_player  # test_player fixture now yields player_id directly

        async with async_session_factory() as session:
            # Create preferences
            await preferences_service.create_player_preferences(session, player_id)

            # Test with empty muted channels
            prefs = await preferences_service.get_player_preferences(session, player_id)
            muted_channels = prefs["data"]["muted_channels"]
            assert muted_channels == []

            # Test adding and removing channels multiple times
            await preferences_service.mute_channel(session, player_id, "global")
            await preferences_service.mute_channel(session, player_id, "whisper")
            await preferences_service.unmute_channel(session, player_id, "global")
            await preferences_service.mute_channel(session, player_id, "local")

            # Verify final state
            prefs = await preferences_service.get_player_preferences(session, player_id)
            muted_channels = prefs["data"]["muted_channels"]
            assert "whisper" in muted_channels
            assert "local" in muted_channels
            assert "global" not in muted_channels

            # Test removing non-muted channel (should not error)
            result = await preferences_service.unmute_channel(session, player_id, "global")
            assert result["success"] is True

    @pytest.mark.asyncio
    async def test_timestamp_handling(self, async_session_factory, test_player, preferences_service):
        """Test that timestamps are handled correctly."""
        player_id = test_player  # test_player fixture now yields player_id directly

        async with async_session_factory() as session:
            # Create preferences
            await preferences_service.create_player_preferences(session, player_id)

            # Get initial timestamps
            prefs1 = await preferences_service.get_player_preferences(session, player_id)
            created_at1 = prefs1["data"]["created_at"]
            updated_at1 = prefs1["data"]["updated_at"]

            # Update preferences
            await preferences_service.update_default_channel(session, player_id, "global")

            # Get updated timestamps
            prefs2 = await preferences_service.get_player_preferences(session, player_id)
            created_at2 = prefs2["data"]["created_at"]
            updated_at2 = prefs2["data"]["updated_at"]

            # Created timestamp should not change
            assert created_at1 == created_at2

            # Updated timestamp should be different (or at least not older)
            assert updated_at2 >= updated_at1

    @pytest.mark.asyncio
    async def test_service_cleanup_and_cleanup(self, async_session_factory, test_player, preferences_service):
        """Test service cleanup and database cleanup."""
        player_id = test_player  # test_player fixture now yields player_id directly

        async with async_session_factory() as session:
            # Create service and preferences
            await preferences_service.create_player_preferences(session, player_id)
            await preferences_service.update_default_channel(session, player_id, "global")

            # Delete preferences
            result = await preferences_service.delete_player_preferences(session, player_id)
            assert result["success"] is True

            # Verify preferences are gone
            prefs = await preferences_service.get_player_preferences(session, player_id)
            assert prefs["success"] is False

            # Try to delete again - should fail
            result = await preferences_service.delete_player_preferences(session, player_id)
            assert result["success"] is False
            assert "not found" in result["error"]
