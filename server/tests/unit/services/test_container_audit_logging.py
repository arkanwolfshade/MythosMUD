"""
Tests for container interaction audit logging.

As documented in the restricted archives of Miskatonic University, container
interactions must be comprehensively audited for security and compliance.
"""

from __future__ import annotations

import json
import uuid
from unittest.mock import MagicMock

import pytest

from server.services.container_service import ContainerService
from server.utils.audit_logger import AuditLogger


@pytest.fixture
def audit_logger(tmp_path):
    """Create an audit logger with a temporary log directory."""
    log_dir = tmp_path / "audit_logs"
    return AuditLogger(log_directory=str(log_dir))


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def sample_player_id():
    """Generate a sample player UUID."""
    return uuid.uuid4()


@pytest.fixture
def sample_container_id():
    """Generate a sample container UUID."""
    return uuid.uuid4()


class TestContainerAuditLogging:
    """Test container interaction audit logging."""

    def test_audit_log_container_open(self, audit_logger, mock_persistence, sample_player_id, sample_container_id):
        """Test that opening a container is audited."""
        # Mock container data
        container_data = {
            "container_id": str(sample_container_id),
            "source_type": "environment",
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container.return_value = container_data

        # Mock player data
        player = MagicMock()
        player.player_id = sample_player_id
        player.name = "TestPlayer"
        mock_persistence.get_player.return_value = player

        service = ContainerService(persistence=mock_persistence)

        # Open container
        service.open_container(sample_container_id, sample_player_id)

        # Verify audit log was written
        log_file = audit_logger._get_log_file_path()
        assert log_file.exists()

        # Read and verify log entry
        with open(log_file) as f:
            lines = f.readlines()
            assert len(lines) > 0

            # Find the container open log entry
            found = False
            for line in lines:
                entry = json.loads(line)
                if entry.get("event_type") == "container_open":
                    assert entry["player_id"] == str(sample_player_id)
                    assert entry["container_id"] == str(sample_container_id)
                    assert entry["source_type"] == "environment"
                    found = True
                    break

            assert found, "Container open audit log entry not found"

    def test_audit_log_container_transfer(self, audit_logger, mock_persistence, sample_player_id, sample_container_id):
        """Test that transferring items to/from containers is audited."""
        # Mock container data
        container_data = {
            "container_id": str(sample_container_id),
            "source_type": "environment",
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container.return_value = container_data
        mock_persistence.update_container.return_value = container_data

        # Mock player data
        player = MagicMock()
        player.player_id = sample_player_id
        player.name = "TestPlayer"
        player.inventory = [
            {
                "item_instance_id": "inst_item_001",
                "prototype_id": "test_item",
                "item_id": "test_item",
                "item_name": "Test Item",
                "slot_type": "backpack",
                "quantity": 1,
            }
        ]
        mock_persistence.get_player.return_value = player

        service = ContainerService(persistence=mock_persistence)

        # Open container first
        open_result = service.open_container(sample_container_id, sample_player_id)
        mutation_token = open_result["mutation_token"]

        # Transfer item to container
        item = {
            "item_instance_id": "inst_item_001",
            "prototype_id": "test_item",
            "item_id": "test_item",
            "item_name": "Test Item",
            "slot_type": "backpack",
            "quantity": 1,
        }

        service.transfer_to_container(sample_container_id, sample_player_id, mutation_token, item)

        # Verify audit log was written
        log_file = audit_logger._get_log_file_path()
        assert log_file.exists()

        # Read and verify log entry
        with open(log_file) as f:
            lines = f.readlines()
            assert len(lines) > 0

            # Find the container transfer log entry
            found = False
            for line in lines:
                entry = json.loads(line)
                if entry.get("event_type") == "container_transfer":
                    assert entry["player_id"] == str(sample_player_id)
                    assert entry["container_id"] == str(sample_container_id)
                    assert entry["direction"] == "to_container"
                    assert entry["item_id"] == "test_item"
                    found = True
                    break

            assert found, "Container transfer audit log entry not found"

    def test_audit_log_container_close(self, audit_logger, mock_persistence, sample_player_id, sample_container_id):
        """Test that closing a container is audited."""
        # Mock container data
        container_data = {
            "container_id": str(sample_container_id),
            "source_type": "environment",
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container.return_value = container_data

        # Mock player data
        player = MagicMock()
        player.player_id = sample_player_id
        player.name = "TestPlayer"
        mock_persistence.get_player.return_value = player

        service = ContainerService(persistence=mock_persistence)

        # Open container first
        open_result = service.open_container(sample_container_id, sample_player_id)
        mutation_token = open_result["mutation_token"]

        # Close container
        service.close_container(sample_container_id, sample_player_id, mutation_token)

        # Verify audit log was written
        log_file = audit_logger._get_log_file_path()
        assert log_file.exists()

        # Read and verify log entry
        with open(log_file) as f:
            lines = f.readlines()
            assert len(lines) > 0

            # Find the container close log entry
            found = False
            for line in lines:
                entry = json.loads(line)
                if entry.get("event_type") == "container_close":
                    assert entry["player_id"] == str(sample_player_id)
                    assert entry["container_id"] == str(sample_container_id)
                    found = True
                    break

            assert found, "Container close audit log entry not found"

    def test_audit_log_container_loot_all(self, audit_logger, mock_persistence, sample_player_id, sample_container_id):
        """Test that looting all items from a container is audited."""
        # Mock container data with items
        container_data = {
            "container_id": str(sample_container_id),
            "source_type": "corpse",
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "capacity_slots": 10,
            "items": [
                {
                    "item_instance_id": "inst_item_001",
                    "prototype_id": "test_item",
                    "item_id": "test_item",
                    "item_name": "Test Item",
                    "slot_type": "backpack",
                    "quantity": 1,
                }
            ],
        }
        mock_persistence.get_container.return_value = container_data
        mock_persistence.update_container.return_value = container_data

        # Mock player data
        player = MagicMock()
        player.player_id = sample_player_id
        player.name = "TestPlayer"
        player.inventory = []
        mock_persistence.get_player.return_value = player

        service = ContainerService(persistence=mock_persistence)

        # Open container first
        open_result = service.open_container(sample_container_id, sample_player_id)
        mutation_token = open_result["mutation_token"]

        # Loot all items
        service.loot_all(sample_container_id, sample_player_id, mutation_token)

        # Verify audit log was written
        log_file = audit_logger._get_log_file_path()
        assert log_file.exists()

        # Read and verify log entry
        with open(log_file) as f:
            lines = f.readlines()
            assert len(lines) > 0

            # Find the container loot_all log entry
            found = False
            for line in lines:
                entry = json.loads(line)
                if entry.get("event_type") == "container_loot_all":
                    assert entry["player_id"] == str(sample_player_id)
                    assert entry["container_id"] == str(sample_container_id)
                    assert entry["items_count"] == 1
                    found = True
                    break

            assert found, "Container loot_all audit log entry not found"

    def test_audit_log_contains_security_fields(
        self, audit_logger, mock_persistence, sample_player_id, sample_container_id
    ):
        """Test that audit logs contain all required security fields."""
        # Mock container data
        container_data = {
            "container_id": str(sample_container_id),
            "source_type": "environment",
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "capacity_slots": 10,
            "items": [],
        }
        mock_persistence.get_container.return_value = container_data

        # Mock player data
        player = MagicMock()
        player.player_id = sample_player_id
        player.name = "TestPlayer"
        mock_persistence.get_player.return_value = player

        service = ContainerService(persistence=mock_persistence)

        # Open container
        service.open_container(sample_container_id, sample_player_id)

        # Verify audit log contains required security fields
        log_file = audit_logger._get_log_file_path()
        assert log_file.exists()

        with open(log_file) as f:
            lines = f.readlines()
            assert len(lines) > 0

            for line in lines:
                entry = json.loads(line)
                if entry.get("event_type") == "container_open":
                    # Verify required security fields
                    assert "timestamp" in entry
                    assert "player_id" in entry
                    assert "player_name" in entry
                    assert "container_id" in entry
                    assert "source_type" in entry
                    assert "room_id" in entry
                    assert "security_level" in entry
                    assert "compliance_required" in entry
                    break
