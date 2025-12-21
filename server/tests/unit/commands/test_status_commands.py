"""
Tests for status command handlers.

This module tests the status and whoami command handlers.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.status_commands import (
    _add_additional_stats_lines,
    _add_profession_lines,
    _build_base_status_lines,
    _get_combat_status,
    _get_profession_info,
    handle_status_command,
    handle_whoami_command,
)


class TestGetProfessionInfo:
    """Test _get_profession_info function."""

    @pytest.mark.asyncio
    async def test_get_profession_info_with_profession_id_attr(self) -> None:
        """Test getting profession info when player has profession_id attribute."""
        mock_player = MagicMock()
        mock_player.profession_id = 1

        mock_profession = MagicMock()
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"

        mock_persistence = AsyncMock()
        mock_persistence.get_profession_by_id.return_value = mock_profession

        result = await _get_profession_info(mock_player, mock_persistence)

        assert result["name"] == "Scholar"
        assert result["description"] == "A learned academic"
        assert result["flavor_text"] == "Knowledge is power"
        mock_persistence.get_profession_by_id.assert_called_once_with(1)

    @pytest.mark.asyncio
    async def test_get_profession_info_with_profession_id_dict(self) -> None:
        """Test getting profession info when player is a dict with profession_id."""
        mock_player = {"profession_id": 2}

        mock_profession = MagicMock()
        mock_profession.name = "Investigator"
        mock_profession.description = "A detective"
        mock_profession.flavor_text = "Seek the truth"

        mock_persistence = AsyncMock()
        mock_persistence.get_profession_by_id.return_value = mock_profession

        result = await _get_profession_info(mock_player, mock_persistence)

        assert result["name"] == "Investigator"
        mock_persistence.get_profession_by_id.assert_called_once_with(2)

    @pytest.mark.asyncio
    async def test_get_profession_info_with_profession_id_zero(self) -> None:
        """Test getting profession info when profession_id is 0."""
        mock_player = MagicMock()
        mock_player.profession_id = 0

        mock_persistence = AsyncMock()

        result = await _get_profession_info(mock_player, mock_persistence)

        assert result["name"] is None
        assert result["description"] is None
        assert result["flavor_text"] is None
        mock_persistence.get_profession_by_id.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_profession_info_with_profession_id_none(self) -> None:
        """Test getting profession info when profession_id is None (defaults to 0)."""
        mock_player = MagicMock()
        mock_player.profession_id = None

        mock_persistence = AsyncMock()

        result = await _get_profession_info(mock_player, mock_persistence)

        assert result["name"] is None
        mock_persistence.get_profession_by_id.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_profession_info_profession_not_found(self) -> None:
        """Test getting profession info when profession is not found."""
        mock_player = MagicMock()
        mock_player.profession_id = 5

        mock_persistence = AsyncMock()
        mock_persistence.get_profession_by_id.return_value = None

        result = await _get_profession_info(mock_player, mock_persistence)

        assert result["name"] is None
        assert result["description"] is None
        assert result["flavor_text"] is None

    @pytest.mark.asyncio
    async def test_get_profession_info_attribute_error(self) -> None:
        """Test getting profession info when AttributeError occurs."""
        mock_player = MagicMock()
        mock_player.profession_id = 1

        mock_persistence = AsyncMock()
        mock_persistence.get_profession_by_id.side_effect = AttributeError("Error")

        with patch("server.commands.status_commands.logger"):
            result = await _get_profession_info(mock_player, mock_persistence)

            assert result["name"] is None
            assert result["description"] is None
            assert result["flavor_text"] is None

    @pytest.mark.asyncio
    async def test_get_profession_info_type_error(self) -> None:
        """Test getting profession info when TypeError occurs."""
        mock_player = MagicMock()
        mock_player.profession_id = 1

        mock_persistence = AsyncMock()

        # Use a coroutine that raises TypeError when awaited
        async def raise_type_error(*args, **kwargs):
            raise TypeError("Error")

        mock_persistence.get_profession_by_id = raise_type_error

        with patch("server.commands.status_commands.logger"):
            result = await _get_profession_info(mock_player, mock_persistence)

            assert result["name"] is None


class TestGetCombatStatus:
    """Test _get_combat_status function."""

    @pytest.mark.asyncio
    async def test_get_combat_status_in_combat(self) -> None:
        """Test getting combat status when player is in combat."""
        mock_app = MagicMock()
        mock_combat_service = AsyncMock()
        mock_combat = MagicMock()
        mock_combat_service.get_combat_by_participant.return_value = mock_combat
        mock_app.state.combat_service = mock_combat_service

        mock_player = MagicMock()
        mock_player.player_id = uuid4()

        with patch("server.commands.status_commands.logger"):
            result = await _get_combat_status(mock_app, mock_player)

            assert result is True
            mock_combat_service.get_combat_by_participant.assert_called_once_with(mock_player.player_id)

    @pytest.mark.asyncio
    async def test_get_combat_status_not_in_combat(self) -> None:
        """Test getting combat status when player is not in combat."""
        mock_app = MagicMock()
        mock_combat_service = AsyncMock()
        mock_combat_service.get_combat_by_participant.return_value = None
        mock_app.state.combat_service = mock_combat_service

        mock_player = MagicMock()
        mock_player.player_id = uuid4()

        with patch("server.commands.status_commands.logger"):
            result = await _get_combat_status(mock_app, mock_player)

            assert result is False

    @pytest.mark.asyncio
    async def test_get_combat_status_no_app(self) -> None:
        """Test getting combat status when app is None."""
        with patch("server.commands.status_commands.logger"):
            result = await _get_combat_status(None, MagicMock())

            assert result is False

    @pytest.mark.asyncio
    async def test_get_combat_status_no_combat_service(self) -> None:
        """Test getting combat status when combat service is not available."""
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Set combat_service to None to simulate it not being available
        mock_app.state.combat_service = None

        with patch("server.commands.status_commands.logger"):
            result = await _get_combat_status(mock_app, MagicMock())

            assert result is False


class TestBuildBaseStatusLines:
    """Test _build_base_status_lines function."""

    def test_build_base_status_lines_basic(self) -> None:
        """Test building basic status lines."""
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.experience_points = 100

        room_name = "Test Room"
        stats = {
            "position": "standing",
            "current_dp": 80,
            "max_dp": 100,
            "lucidity": 90,
            "max_lucidity": 100,
        }
        in_combat = False

        result = _build_base_status_lines(mock_player, room_name, stats, in_combat)

        assert "Name: TestPlayer" in result
        assert "Location: Test Room" in result
        assert "Position: Standing" in result
        assert "Health: 80/100" in result
        assert "lucidity: 90/100" in result
        assert "XP: 100" in result
        assert "In Combat: No" in result

    def test_build_base_status_lines_in_combat(self) -> None:
        """Test building status lines when in combat."""
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.experience_points = 50

        room_name = "Combat Room"
        stats = {
            "position": "lying",
            "current_dp": 20,
            "max_dp": 100,
            "lucidity": 50,
            "max_lucidity": 100,
        }
        in_combat = True

        result = _build_base_status_lines(mock_player, room_name, stats, in_combat)

        assert "In Combat: Yes" in result
        assert "Position: Lying" in result

    def test_build_base_status_lines_position_underscore(self) -> None:
        """Test building status lines with underscore in position."""
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.experience_points = 0

        room_name = "Room"
        stats = {"position": "sitting_down", "current_dp": 100, "max_dp": 100, "lucidity": 100, "max_lucidity": 100}
        in_combat = False

        result = _build_base_status_lines(mock_player, room_name, stats, in_combat)

        assert "Position: Sitting down" in result


class TestAddProfessionLines:
    """Test _add_profession_lines function."""

    def test_add_profession_lines_with_all_fields(self) -> None:
        """Test adding profession lines with all fields."""
        status_lines: list[str] = []
        profession_info = {
            "name": "Scholar",
            "description": "A learned academic",
            "flavor_text": "Knowledge is power",
        }

        _add_profession_lines(status_lines, profession_info)

        assert "Profession: Scholar" in status_lines
        assert "Description: A learned academic" in status_lines
        assert "Background: Knowledge is power" in status_lines

    def test_add_profession_lines_with_name_only(self) -> None:
        """Test adding profession lines with only name."""
        status_lines: list[str] = []
        profession_info = {"name": "Investigator", "description": None, "flavor_text": None}

        _add_profession_lines(status_lines, profession_info)

        assert "Profession: Investigator" in status_lines
        assert len(status_lines) == 1

    def test_add_profession_lines_with_name_and_description(self) -> None:
        """Test adding profession lines with name and description."""
        status_lines: list[str] = []
        profession_info = {"name": "Detective", "description": "A sleuth", "flavor_text": None}

        _add_profession_lines(status_lines, profession_info)

        assert "Profession: Detective" in status_lines
        assert "Description: A sleuth" in status_lines
        assert len(status_lines) == 2

    def test_add_profession_lines_no_name(self) -> None:
        """Test adding profession lines when name is None."""
        status_lines: list[str] = []
        profession_info = {"name": None, "description": "Some description", "flavor_text": "Some text"}

        _add_profession_lines(status_lines, profession_info)

        assert len(status_lines) == 0


class TestAddAdditionalStatsLines:
    """Test _add_additional_stats_lines function."""

    def test_add_additional_stats_lines_with_fear(self) -> None:
        """Test adding additional stats lines with fear."""
        status_lines: list[str] = []
        stats = {"fear": 25, "corruption": 0, "occult_knowledge": 0}

        _add_additional_stats_lines(status_lines, stats)

        assert "Fear: 25" in status_lines
        assert len(status_lines) == 1

    def test_add_additional_stats_lines_with_corruption(self) -> None:
        """Test adding additional stats lines with corruption."""
        status_lines: list[str] = []
        stats = {"fear": 0, "corruption": 15, "occult_knowledge": 0}

        _add_additional_stats_lines(status_lines, stats)

        assert "Corruption: 15" in status_lines

    def test_add_additional_stats_lines_with_occult_knowledge(self) -> None:
        """Test adding additional stats lines with occult knowledge."""
        status_lines: list[str] = []
        stats = {"fear": 0, "corruption": 0, "occult_knowledge": 30}

        _add_additional_stats_lines(status_lines, stats)

        assert "Occult Knowledge: 30" in status_lines

    def test_add_additional_stats_lines_with_all(self) -> None:
        """Test adding additional stats lines with all stats."""
        status_lines: list[str] = []
        stats = {"fear": 10, "corruption": 20, "occult_knowledge": 5}

        _add_additional_stats_lines(status_lines, stats)

        assert "Fear: 10" in status_lines
        assert "Corruption: 20" in status_lines
        assert "Occult Knowledge: 5" in status_lines
        assert len(status_lines) == 3

    def test_add_additional_stats_lines_with_zero_values(self) -> None:
        """Test adding additional stats lines with zero values (should not add)."""
        status_lines: list[str] = []
        stats = {"fear": 0, "corruption": 0, "occult_knowledge": 0}

        _add_additional_stats_lines(status_lines, stats)

        assert len(status_lines) == 0

    def test_add_additional_stats_lines_missing_keys(self) -> None:
        """Test adding additional stats lines with missing keys."""
        status_lines: list[str] = []
        stats: dict[str, Any] = {}

        _add_additional_stats_lines(status_lines, stats)

        assert len(status_lines) == 0


class TestHandleStatusCommand:
    """Test handle_status_command function."""

    @pytest.mark.asyncio
    async def test_handle_status_command_success(self) -> None:
        """Test successful status command."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.experience_points = 100
        mock_player.current_room_id = "room-123"
        mock_player.get_stats.return_value = {
            "position": "standing",
            "current_dp": 80,
            "max_dp": 100,
            "lucidity": 90,
            "max_lucidity": 100,
        }
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = MagicMock()
        mock_room.name = "Test Room"
        # get_room_by_id is synchronous, not async
        mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)

        # get_profession_by_id is async
        mock_profession = MagicMock()
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"
        mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

        mock_combat_service = AsyncMock()
        mock_combat_service.get_combat_by_participant.return_value = None
        mock_app.state.combat_service = mock_combat_service

        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.status_commands.get_username_from_user", return_value="testuser"):
            with patch("server.commands.status_commands.logger"):
                result = await handle_status_command(command_data, current_user, mock_request, None, "testuser")

                assert "result" in result
                assert "Name: TestPlayer" in result["result"]
                assert "Location: Test Room" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_status_command_no_persistence(self) -> None:
        """Test status command when persistence is not available."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_app.state = MagicMock()
        # Set persistence to None to simulate it not being available
        mock_app.state.persistence = None
        mock_request.app = mock_app

        with patch("server.commands.status_commands.logger"):
            result = await handle_status_command(command_data, current_user, mock_request, None, "testuser")

            assert "Status information is not available" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_status_command_no_request(self) -> None:
        """Test status command when request is None."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}

        with patch("server.commands.status_commands.logger"):
            result = await handle_status_command(command_data, current_user, None, None, "testuser")

            assert "Status information is not available" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_status_command_player_not_found(self) -> None:
        """Test status command when player is not found."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name.return_value = None
        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.status_commands.get_username_from_user", return_value="testuser"):
            with patch("server.commands.status_commands.logger"):
                result = await handle_status_command(command_data, current_user, mock_request, None, "testuser")

                assert "Player information not found" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_status_command_no_room(self) -> None:
        """Test status command when room is not found."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.experience_points = 100
        mock_player.current_room_id = "room-123"
        mock_player.get_stats.return_value = {
            "position": "standing",
            "current_dp": 80,
            "max_dp": 100,
            "lucidity": 90,
            "max_lucidity": 100,
        }
        mock_persistence.get_player_by_name.return_value = mock_player
        # get_room_by_id is synchronous, not async
        mock_persistence.get_room_by_id = MagicMock(return_value=None)

        # get_profession_by_id is async
        mock_persistence.get_profession_by_id = AsyncMock(return_value=None)

        mock_combat_service = AsyncMock()
        mock_combat_service.get_combat_by_participant.return_value = None
        mock_app.state.combat_service = mock_combat_service

        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.status_commands.get_username_from_user", return_value="testuser"):
            with patch("server.commands.status_commands.logger"):
                result = await handle_status_command(command_data, current_user, mock_request, None, "testuser")

                assert "Location: Unknown location" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_status_command_attribute_error(self) -> None:
        """Test status command when AttributeError occurs."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.get_stats.side_effect = AttributeError("Error")
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.status_commands.get_username_from_user", return_value="testuser"):
            with patch("server.commands.status_commands.logger"):
                result = await handle_status_command(command_data, current_user, mock_request, None, "testuser")

                assert "Error retrieving status information" in result["result"]


class TestHandleWhoamiCommand:
    """Test handle_whoami_command function."""

    @pytest.mark.asyncio
    async def test_handle_whoami_command_success(self) -> None:
        """Test successful whoami command."""
        command_data: dict[str, Any] = {"args": []}
        current_user = {"username": "testuser"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_persistence = AsyncMock()

        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        mock_player.experience_points = 100
        mock_player.current_room_id = "room-123"
        mock_player.get_stats.return_value = {
            "position": "standing",
            "current_dp": 80,
            "max_dp": 100,
            "lucidity": 90,
            "max_lucidity": 100,
        }
        mock_persistence.get_player_by_name.return_value = mock_player

        mock_room = MagicMock()
        mock_room.name = "Test Room"
        # get_room_by_id is synchronous, not async
        mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)

        # get_profession_by_id is async
        mock_profession = MagicMock()
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"
        mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

        mock_combat_service = AsyncMock()
        mock_combat_service.get_combat_by_participant.return_value = None
        mock_app.state.combat_service = mock_combat_service

        mock_app.state.persistence = mock_persistence
        mock_request.app = mock_app

        with patch("server.commands.status_commands.get_username_from_user", return_value="testuser"):
            with patch("server.commands.status_commands.logger"):
                result = await handle_whoami_command(command_data, current_user, mock_request, None, "testuser")

                assert "result" in result
                assert "Name: TestPlayer" in result["result"]
