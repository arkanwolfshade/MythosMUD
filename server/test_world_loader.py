from world_loader import load_rooms


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


def test_loader_as_script(monkeypatch, capsys):
    # Simulate running world_loader as __main__
    import importlib
    import sys
    import world_loader

    monkeypatch.setattr(sys, "argv", ["world_loader.py"])
    importlib.reload(world_loader)
    captured = capsys.readouterr()
    assert "Loaded" in captured.out


def test_missing_rooms_dir(tmp_path, monkeypatch):
    # Simulate missing rooms directory
    monkeypatch.setattr("world_loader.ROOMS_BASE_PATH", str(tmp_path / "nonexistent"))
    from world_loader import load_rooms as test_load

    rooms = test_load()
    assert rooms == {}
