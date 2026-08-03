"""Unit tests for npc_combat_grace login grace checks."""

import uuid
from unittest.mock import MagicMock, patch

from server.services.npc_combat_grace import (
    is_npc_attack_on_player_blocked_by_login_grace_period,
    is_player_attack_blocked_by_login_grace_period,
)


def test_player_attack_blocked_when_in_grace_period() -> None:
    player_id = str(uuid.uuid4())
    conn_mgr = MagicMock()
    with patch("server.services.npc_combat_grace.get_app_instance") as mock_app:
        mock_app.return_value = MagicMock(state=MagicMock(connection_manager=conn_mgr))
        with patch(
            "server.services.npc_combat_grace.is_player_in_login_grace_period",
            return_value=True,
        ):
            assert is_player_attack_blocked_by_login_grace_period(player_id) is True


def test_player_attack_fail_open_without_connection_manager() -> None:
    with patch("server.services.npc_combat_grace.get_app_instance", return_value=None):
        assert is_player_attack_blocked_by_login_grace_period(str(uuid.uuid4())) is False


def test_player_attack_fail_open_on_invalid_uuid() -> None:
    assert is_player_attack_blocked_by_login_grace_period("not-a-uuid") is False


def test_npc_attack_blocked_when_target_in_grace_period() -> None:
    target_uuid = uuid.uuid4()
    conn_mgr = MagicMock()
    with patch("server.services.npc_combat_grace.get_app_instance") as mock_app:
        mock_app.return_value = MagicMock(state=MagicMock(connection_manager=conn_mgr))
        with patch(
            "server.services.npc_combat_grace.is_player_in_login_grace_period",
            return_value=True,
        ):
            assert is_npc_attack_on_player_blocked_by_login_grace_period(target_uuid) is True


def test_npc_attack_fail_open_without_app() -> None:
    with patch("server.services.npc_combat_grace.get_app_instance", return_value=None):
        assert is_npc_attack_on_player_blocked_by_login_grace_period(uuid.uuid4()) is False
