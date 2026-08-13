"""Unit tests for skills command helpers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import skills_commands as cmd
from server.game.skill_service import SkillService


def test_format_skills_output() -> None:
    skills = [{"skill_name": "Brawl", "value": 55}, {"skill_key": "dodge", "value": 30}]
    text = cmd._format_skills_output(skills)
    assert "Brawl: 55%" in text
    assert "dodge: 30%" in text


def test_resolve_player_id_from_string() -> None:
    pid = uuid.uuid4()
    player = MagicMock(player_id=str(pid))
    assert cmd._resolve_player_id(player) == pid


def test_resolve_user_id_from_dict() -> None:
    assert cmd._resolve_user_id({"id": "user-1"}, MagicMock()) == "user-1"


def test_get_container_services_missing() -> None:
    assert cmd._get_container_services(None) is None


def test_get_container_services_ok() -> None:
    request = MagicMock()
    request.app.state.container.async_persistence = MagicMock()
    request.app.state.container.skill_service = MagicMock(spec=SkillService)
    services = cmd._get_container_services(request)
    assert services is not None


@pytest.mark.asyncio
async def test_handle_skills_command_no_services() -> None:
    result = await cmd.handle_skills_command({}, {}, None, None, "Player")
    assert result["result"] == "Skills are not available."


@pytest.mark.asyncio
async def test_handle_skills_command_success() -> None:
    player_id = uuid.uuid4()
    player = MagicMock(player_id=str(player_id), user_id="user-1")
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    skill_service = MagicMock()
    skill_service.get_player_skills = AsyncMock(return_value=[{"skill_name": "Brawl", "value": 40}])
    request = MagicMock()
    with patch.object(cmd, "_get_container_services", return_value=(MagicMock(), persistence, skill_service)):
        with patch("server.commands.skills_commands.get_username_from_user", return_value="Alice"):
            result = await cmd.handle_skills_command({}, {"id": "user-1"}, request, None, "Alice")
    assert "Brawl: 40%" in result["result"]
