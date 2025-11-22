# Import the module to ensure coverage tracking
from pathlib import Path

import pytest

import server.world_loader

# Note: load_rooms has been removed - rooms are now loaded from database


@pytest.mark.skip(reason="load_rooms removed - rooms now loaded from database")
def test_load_rooms():
    """Test loading rooms from the unit_test environment."""
    # Configure path to unit_test environment rooms
    # Path: server/tests/unit/world/test_world_loader.py -> project root
    project_root = Path(__file__).parent.parent.parent.parent.parent
    unit_test_rooms_path = project_root / "data" / "unit_test" / "rooms"

    # Temporarily patch ROOMS_BASE_PATH to use unit_test environment
    original_path = server.world_loader.ROOMS_BASE_PATH
    try:
        server.world_loader.ROOMS_BASE_PATH = str(unit_test_rooms_path)

        rooms = load_rooms()  # noqa: F821
        assert isinstance(rooms, dict)
        assert len(rooms) > 0, "No rooms loaded. Add at least one room JSON file."
        for _room_id, room in rooms.items():
            assert "id" in room
            assert "name" in room
            assert "description" in room
            assert "zone" in room
            assert "exits" in room
            isinstance(room["exits"], dict)
    finally:
        # Restore original path
        server.world_loader.ROOMS_BASE_PATH = original_path


@pytest.mark.skip(reason="load_rooms removed - rooms now loaded from database")
def test_loader_as_script(capsys):
    """Test that world_loader can be run as a script."""
    # Configure path to unit_test environment rooms
    # Path: server/tests/unit/world/test_world_loader.py -> project root
    project_root = Path(__file__).parent.parent.parent.parent.parent
    unit_test_rooms_path = project_root / "data" / "unit_test" / "rooms"

    # Temporarily patch ROOMS_BASE_PATH to use unit_test environment
    original_path = server.world_loader.ROOMS_BASE_PATH
    try:
        server.world_loader.ROOMS_BASE_PATH = str(unit_test_rooms_path)

        rooms = load_rooms()  # noqa: F821
        print(f"Loaded {len(rooms)} rooms:")
        for _room_id, room in rooms.items():
            print(f"- {_room_id}: {room['name']}")
        captured = capsys.readouterr()
        assert "Loaded" in captured.out
        assert len(rooms) > 0
    finally:
        # Restore original path
        server.world_loader.ROOMS_BASE_PATH = original_path


@pytest.mark.skip(reason="load_rooms removed - rooms now loaded from database")
def test_corrupted_room_file(tmp_path):
    # Create a zone and a corrupted room file
    zone_dir = tmp_path / "arkham"
    zone_dir.mkdir()
    bad_file = zone_dir / "bad_room.json"
    bad_file.write_text("{ not: valid json }", encoding="utf-8")

    # Use the already imported module
    server.world_loader.ROOMS_BASE_PATH = str(tmp_path)
    # Should not raise, should print warning and skip
    rooms = server.world_loader.load_rooms()
    assert isinstance(rooms, dict)


def test_module_coverage():
    """Test to ensure world_loader module is properly imported for coverage."""
    # This test ensures the module is executed and tracked by coverage
    # Note: load_rooms, load_hierarchical_world, and resolve_room_reference have been removed
    # as rooms are now loaded from database instead of files
    assert hasattr(server.world_loader, "generate_room_id")
    assert hasattr(server.world_loader, "get_room_environment")
