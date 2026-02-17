"""
Unit tests for character creation API endpoints.

Tests roll stats, create character, and validate stats endpoints.
"""
# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which pylint incorrectly flags as redefining names from outer scope, this is standard pytest usage
# Pytest fixtures are injected as function parameters, which triggers
# "redefined-outer-name" warnings. This is standard pytest pattern.

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request

# Ensure module under test is loaded so patch("server.api.character_creation.*") can resolve.
import server.api.character_creation  # noqa: F401

# Lazy imports to avoid circular import issues
# Import inside functions that need them to avoid triggering circular import chain
from server.exceptions import LoggedHTTPException, RateLimitError
from server.models import Stats
from server.models.user import User
from server.schemas.players import CreateCharacterRequest, RollStatsRequest


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = Mock(spec=Request)
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_user():
    """Create a mock user."""
    user = User(
        id=uuid.uuid4(),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    return user


@pytest.fixture
def mock_stats():
    """Create mock stats."""
    return Stats(
        str=10,
        int=10,
        wis=10,
        dex=10,
        con=10,
        cha=10,
    )


@pytest.fixture
def mock_stats_generator():
    """Create a mock stats generator."""
    generator = MagicMock()
    return generator


@pytest.fixture
def mock_profession_service():
    """Create a mock profession service."""
    service = AsyncMock()
    return service


class TestRollCharacterStats:
    """Test roll_character_stats() endpoint."""

    @pytest.mark.asyncio
    async def test_roll_character_stats_shutdown_pending(self, mock_request, mock_user, mock_stats_generator):
        """Test roll_character_stats() blocks when server is shutting down."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = RollStatsRequest(method="4d6")
        mock_profession_service = AsyncMock()
        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
            with patch("server.commands.admin_shutdown_command.get_shutdown_blocking_message", return_value="Shutdown"):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await roll_character_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        stats_generator=mock_stats_generator,
                        profession_service=mock_profession_service,
                    )
                assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_roll_character_stats_not_authenticated(self, mock_request, mock_stats_generator):
        """Test roll_character_stats() requires authentication."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = RollStatsRequest(method="4d6")
        mock_profession_service = AsyncMock()
        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await roll_character_stats(
                    request_data=request_data,
                    request=mock_request,
                    # Reason: Intentionally passing None to test unauthenticated scenario
                    current_user=None,  # type: ignore[arg-type]
                    stats_generator=mock_stats_generator,
                    profession_service=mock_profession_service,
                )
                assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_roll_character_stats_rate_limit(self, mock_request, mock_user, mock_stats_generator):
        """Test roll_character_stats() enforces rate limiting."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = RollStatsRequest(method="4d6")
        mock_profession_service = AsyncMock()
        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.stats_roll_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await roll_character_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        stats_generator=mock_stats_generator,
                        profession_service=mock_profession_service,
                    )
                assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_roll_character_stats_with_profession(
        self, mock_request, mock_user, mock_stats_generator, mock_stats
    ):
        """Test roll_character_stats() with profession_id."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = RollStatsRequest(method="4d6", profession_id=1)
        mock_profession = MagicMock()
        mock_stats_generator.roll_stats_with_profession = Mock(return_value=(mock_stats, True))
        mock_stats_generator.get_stat_summary = Mock(return_value={"total_points": 60, "average_stat": 10.0})

        mock_profession_service = AsyncMock()
        mock_profession_service.validate_and_get_profession = AsyncMock(return_value=mock_profession)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.stats_roll_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.return_value = None

                result = await roll_character_stats(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    stats_generator=mock_stats_generator,
                    profession_service=mock_profession_service,
                )

                assert result.stats is not None
                assert result.profession_id == 1
                assert result.meets_requirements is True

    @pytest.mark.asyncio
    async def test_roll_character_stats_profession_not_found(self, mock_request, mock_user, mock_stats_generator):
        """Test roll_character_stats() when profession not found."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        profession_id = 999
        request_data = RollStatsRequest(method="4d6", profession_id=profession_id)

        mock_profession_service = AsyncMock()
        from server.exceptions import ValidationError

        mock_profession_service.validate_and_get_profession = AsyncMock(
            side_effect=ValidationError("Profession not found")
        )

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.stats_roll_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.return_value = None

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await roll_character_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        stats_generator=mock_stats_generator,
                        profession_service=mock_profession_service,
                    )
                assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_roll_character_stats_with_class(self, mock_request, mock_user, mock_stats_generator, mock_stats):
        """Test roll_character_stats() with required_class."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = RollStatsRequest(method="4d6", required_class="warrior")
        mock_stats_generator.roll_stats_with_validation = Mock(return_value=(mock_stats, ["warrior", "mage"]))
        mock_stats_generator.get_stat_summary = Mock(return_value={"total_points": 60, "average_stat": 10.0})

        mock_profession_service = AsyncMock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.stats_roll_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.return_value = None

                result = await roll_character_stats(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    stats_generator=mock_stats_generator,
                    profession_service=mock_profession_service,
                )

                assert result.stats is not None
                assert result.available_classes == ["warrior", "mage"]
                assert result.meets_class_requirements is True

    @pytest.mark.asyncio
    async def test_roll_character_stats_persistence_not_available(self, mock_request, mock_user, mock_stats_generator):
        """Test roll_character_stats() when persistence not available."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            roll_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = RollStatsRequest(method="4d6", profession_id=1)
        mock_profession_service = AsyncMock()
        mock_profession_service.validate_and_get_profession = AsyncMock(side_effect=Exception("Persistence error"))

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.stats_roll_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.return_value = None

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await roll_character_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        stats_generator=mock_stats_generator,
                        profession_service=mock_profession_service,
                    )
                assert exc_info.value.status_code == 500


class TestCreateCharacterWithStats:
    """Test create_character_with_stats() endpoint."""

    @pytest.mark.asyncio
    async def test_create_character_shutdown_pending(self, mock_request, mock_user):
        """Test create_character_with_stats() blocks when server is shutting down."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            create_character_with_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = CreateCharacterRequest(
            name="TestCharacter",
            stats={
                "str": 10,
                "int": 10,
                "wis": 10,
                "dex": 10,
                "con": 10,
                "cha": 10,
            },
        )
        mock_player_service = MagicMock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
            with patch("server.commands.admin_shutdown_command.get_shutdown_blocking_message", return_value="Shutdown"):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await create_character_with_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        player_service=mock_player_service,
                    )
                assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_create_character_not_authenticated(self, mock_request):
        """Test create_character_with_stats() requires authentication."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            create_character_with_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = CreateCharacterRequest(
            name="TestCharacter",
            stats={
                "str": 10,
                "int": 10,
                "wis": 10,
                "dex": 10,
                "con": 10,
                "cha": 10,
            },
        )
        mock_player_service = MagicMock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await create_character_with_stats(
                    request_data=request_data,
                    request=mock_request,
                    # Reason: Intentionally passing None to test unauthenticated scenario
                    current_user=None,  # type: ignore[arg-type]
                    player_service=mock_player_service,
                )
                assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_create_character_rate_limit(self, mock_request, mock_user):
        """Test create_character_with_stats() enforces rate limiting."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            create_character_with_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = CreateCharacterRequest(
            name="TestCharacter",
            stats={
                "str": 10,
                "int": 10,
                "wis": 10,
                "dex": 10,
                "con": 10,
                "cha": 10,
            },
        )
        mock_player_service = MagicMock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.character_creation_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=300)
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await create_character_with_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        player_service=mock_player_service,
                    )
                assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_create_character_success(self, mock_request, mock_user):
        """Test create_character_with_stats() successfully creates character."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            create_character_with_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = CreateCharacterRequest(
            name="TestCharacter",
            stats={
                "str": 10,
                "int": 10,
                "wis": 10,
                "dex": 10,
                "con": 10,
                "cha": 10,
            },
        )
        from datetime import UTC, datetime

        from server.schemas.players import PlayerRead, PositionState

        mock_player = PlayerRead(
            id=uuid.uuid4(),
            name="TestCharacter",
            user_id=mock_user.id,
            profession_id=0,
            profession_name=None,
            profession_description=None,
            profession_flavor_text=None,
            stats={"str": 10, "int": 10, "wis": 10, "dex": 10, "con": 10, "cha": 10},
            inventory=[],
            status_effects=[],
            created_at=datetime.now(UTC),
            last_active=datetime.now(UTC),
            is_admin=False,
            in_combat=False,
            position=PositionState.STANDING,
            current_room_id="earth_arkhamcity_room",
        )
        mock_player_service = MagicMock()
        mock_player_service.create_player_with_stats = AsyncMock(return_value=mock_player)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.api.character_creation.character_creation_limiter") as mock_limiter:
                mock_limiter.enforce_rate_limit.return_value = None
                with patch("server.config.get_config") as mock_get_config:
                    mock_config = MagicMock()
                    mock_config.game.default_player_room = "earth_arkhamcity_room"
                    mock_get_config.return_value = mock_config

                    result = await create_character_with_stats(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        player_service=mock_player_service,
                    )

                    assert result.player is not None
                    mock_player_service.create_player_with_stats.assert_awaited_once()


class TestValidateCharacterStats:
    """Test validate_character_stats() endpoint."""

    @pytest.mark.asyncio
    async def test_validate_stats_with_class(self, mock_user, mock_stats_generator):
        """Test validate_character_stats() with class_name."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            validate_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        stats = {
            "str": 15,
            "int": 10,
            "wis": 10,
            "dex": 10,
            "con": 10,
            "cha": 10,
        }
        mock_stats_generator.validate_class_prerequisites = Mock(return_value=(True, []))
        mock_stats_generator.get_available_classes = Mock(return_value=["warrior", "mage"])

        result = await validate_character_stats(
            stats=stats,
            class_name="warrior",
            current_user=mock_user,
            stats_generator=mock_stats_generator,
        )

        assert result.meets_prerequisites is True
        assert result.requested_class == "warrior"
        assert result.available_classes == ["warrior", "mage"]

    @pytest.mark.asyncio
    async def test_validate_stats_without_class(self, mock_user, mock_stats_generator):
        """Test validate_character_stats() without class_name."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            validate_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        stats = {
            "str": 10,
            "int": 10,
            "wis": 10,
            "dex": 10,
            "con": 10,
            "cha": 10,
        }
        mock_stats_generator.get_available_classes = Mock(return_value=["warrior", "mage"])
        mock_stats_generator.get_stat_summary = Mock(return_value={"total_points": 60, "average_stat": 10.0})

        result = await validate_character_stats(
            stats=stats,
            class_name=None,
            current_user=mock_user,
            stats_generator=mock_stats_generator,
        )

        assert result.available_classes == ["warrior", "mage"]
        assert result.stat_summary is not None
        assert result.stat_summary.total == 60

    @pytest.mark.asyncio
    async def test_validate_stats_invalid_input(self, mock_user, mock_stats_generator):
        """Test validate_character_stats() handles invalid stats."""
        # Lazy import to avoid circular import
        from server.api.character_creation import (
            validate_character_stats,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        # Stats requires numeric values, passing a non-numeric string should trigger validation error
        invalid_stats = {"strength": "not_a_number", "intelligence": 10, "wisdom": 10}

        with pytest.raises(LoggedHTTPException) as exc_info:
            await validate_character_stats(
                stats=invalid_stats,
                class_name=None,
                current_user=mock_user,
                stats_generator=mock_stats_generator,
            )
        assert exc_info.value.status_code == 400
