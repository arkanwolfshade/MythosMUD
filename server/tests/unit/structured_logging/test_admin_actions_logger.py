"""Unit tests for AdminActionsLogger."""

import json
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from server.structured_logging.admin_actions_logger import AdminActionsLogger, get_admin_actions_logger


@pytest.fixture
def log_dir(tmp_path: Path) -> Path:
    return tmp_path / "admin_logs"


@pytest.fixture
def admin_logger(log_dir: Path) -> AdminActionsLogger:
    return AdminActionsLogger(log_directory=str(log_dir))


def test_log_teleport_action_success(admin_logger: AdminActionsLogger, log_dir: Path) -> None:
    admin_logger.log_teleport_action("Admin", "Bob", "teleport", "room-a", "room-b", True)
    entries = _read_log_entries(admin_logger.current_log_file)
    assert len(entries) == 1
    assert entries[0]["action_type"] == "teleport"
    assert entries[0]["success"] is True


def test_log_teleport_action_failure(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_teleport_action("Admin", "Bob", "goto", "room-a", "room-b", False, error_message="denied")
    entries = _read_log_entries(admin_logger.current_log_file)
    assert entries[0]["success"] is False
    assert entries[0]["error_message"] == "denied"


def test_log_admin_command(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_admin_command("Admin", "kick", target_player="Bob", success=True)
    entries = _read_log_entries(admin_logger.current_log_file)
    assert entries[0]["action_type"] == "admin_command"
    assert entries[0]["command"] == "kick"


def test_log_admin_command_failure(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_admin_command("Admin", "ban", success=False, error_message="fail")
    entries = _read_log_entries(admin_logger.current_log_file)
    assert entries[0]["success"] is False


def test_log_permission_check_denied(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_permission_check("Bob", "teleport", False)
    entries = _read_log_entries(admin_logger.current_log_file)
    assert entries[0]["has_permission"] is False


def test_get_recent_actions_filters(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_teleport_action("Admin1", "Bob", "teleport", "a", "b", True)
    admin_logger.log_admin_command("Admin2", "kick", success=True)
    recent = admin_logger.get_recent_actions(hours=24, action_type="teleport", admin_name="Admin1")
    assert len(recent) == 1
    assert recent[0]["teleport_type"] == "teleport"


def test_get_recent_actions_skips_old_entries(admin_logger: AdminActionsLogger) -> None:
    old_time = (datetime.now() - timedelta(hours=48)).isoformat()
    admin_logger._ensure_log_file_exists()
    with open(admin_logger.current_log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps({"timestamp": old_time, "action_type": "teleport", "admin_name": "Old"}) + "\n")
    admin_logger.log_teleport_action("Admin", "Bob", "teleport", "a", "b", True)
    recent = admin_logger.get_recent_actions(hours=24)
    assert all(entry.get("admin_name") != "Old" for entry in recent)


def test_get_recent_actions_skips_malformed_lines(admin_logger: AdminActionsLogger) -> None:
    admin_logger._ensure_log_file_exists()
    with open(admin_logger.current_log_file, "a", encoding="utf-8") as f:
        f.write("not-json\n")
    assert admin_logger.get_recent_actions(hours=24) == []


def test_get_teleport_statistics(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_teleport_action("Admin", "Bob", "teleport", "a", "b", True)
    admin_logger.log_teleport_action("Admin", "Carol", "goto", "a", "c", False)
    stats = admin_logger.get_teleport_statistics(hours=24)
    assert stats["total_teleports"] == 2
    assert stats["successful_teleports"] == 1
    assert stats["failed_teleports"] == 1
    assert stats["teleport_types"]["teleport"] == 1
    assert stats["admin_activity"]["Admin"] == 2


def test_log_entry_write_failure(admin_logger: AdminActionsLogger) -> None:
    with patch.object(admin_logger, "_ensure_log_file_exists", side_effect=OSError("disk full")):
        admin_logger.log_admin_command("Admin", "kick")


def test_admin_logger_init_from_config(log_dir: Path) -> None:
    with (
        patch("server.config.get_config") as mock_config,
        patch(
            "server.structured_logging.enhanced_logging_config._resolve_log_base",
            return_value=log_dir.parent,
        ),
    ):
        mock_config.return_value.logging.log_base = "logs"
        mock_config.return_value.logging.environment = "unit_test"
        logger = AdminActionsLogger()
    assert logger.log_directory == log_dir.parent / "unit_test"


def test_log_entry_rotates_on_new_day(admin_logger: AdminActionsLogger) -> None:
    admin_logger.log_admin_command("Admin", "kick")
    new_path = admin_logger.log_directory / "admin_actions_2099-01-01.log"
    with patch.object(admin_logger, "_get_log_file_path", return_value=new_path):
        admin_logger.log_admin_command("Admin", "ban")
    assert admin_logger.current_log_file == new_path


def test_get_recent_actions_read_failure(admin_logger: AdminActionsLogger) -> None:
    broken_dir = MagicMock()
    broken_dir.glob.side_effect = OSError("read fail")
    admin_logger.log_directory = broken_dir
    assert admin_logger.get_recent_actions(hours=24) == []


def test_get_admin_actions_logger_singleton(log_dir: Path) -> None:
    import server.structured_logging.admin_actions_logger as mod

    mod._admin_actions_logger = None
    with patch.object(AdminActionsLogger, "__init__", return_value=None):
        logger_a = AdminActionsLogger(log_directory=str(log_dir))
        logger_a.log_directory = log_dir
        mod._admin_actions_logger = logger_a
        assert get_admin_actions_logger() is logger_a
    mod._admin_actions_logger = None


def _read_log_entries(log_file: Path) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    with open(log_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                entries.append(json.loads(line))
    return entries
