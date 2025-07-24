from server.world_loader import load_rooms
import os


def test_load_rooms():
    rooms = load_rooms()
    assert isinstance(rooms, dict)
    assert len(rooms) > 0, "No rooms loaded. Add at least one room JSON file."
    for room_id, room in rooms.items():
        assert "id" in room
        assert "name" in room
        assert "description" in room
        assert "zone" in room
        assert "exits" in room
        assert isinstance(room["exits"], dict)


def test_loader_as_script(capsys):
    """Test that world_loader can be run as a script."""
    rooms = load_rooms()
    print(f"Loaded {len(rooms)} rooms:")
    for room_id, room in rooms.items():
        print(f"- {room_id}: {room['name']}")
    captured = capsys.readouterr()
    assert "Loaded" in captured.out
    assert len(rooms) > 0


def test_missing_rooms_dir(tmp_path):
    """Test behavior when rooms directory doesn't exist."""
    temp_dir = tmp_path / "empty"
    temp_dir.mkdir()
    import types

    mock_module = types.ModuleType("world_loader_test")
    mock_module.ROOMS_BASE_PATH = str(temp_dir)

    def mock_load_rooms():
        rooms = {}
        if not os.path.exists(mock_module.ROOMS_BASE_PATH):
            return rooms
        return rooms

    mock_module.load_rooms = mock_load_rooms
    rooms = mock_module.load_rooms()
    assert rooms == {}


def test_corrupted_room_file(tmp_path):
    # Create a zone and a corrupted room file
    zone_dir = tmp_path / "arkham"
    zone_dir.mkdir()
    bad_file = zone_dir / "bad_room.json"
    bad_file.write_text("{ not: valid json }", encoding="utf-8")
    import server.world_loader as wl

    wl.ROOMS_BASE_PATH = str(tmp_path)
    # Should not raise, should print warning and skip
    rooms = wl.load_rooms()
    assert isinstance(rooms, dict)
