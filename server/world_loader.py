import json
import os
from typing import Any

ROOMS_BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "rooms"))


def load_rooms() -> dict[str, Any]:
    rooms = {}

    # Check if rooms directory exists
    if not os.path.exists(ROOMS_BASE_PATH):
        return rooms

    try:
        for zone in os.listdir(ROOMS_BASE_PATH):
            zone_path = os.path.join(ROOMS_BASE_PATH, zone)
            if not os.path.isdir(zone_path):
                continue
            for filename in os.listdir(zone_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(zone_path, filename)
                    try:
                        with open(file_path, encoding="utf-8") as f:
                            room = json.load(f)
                            room_id = room.get("id")
                            if room_id:
                                rooms[room_id] = room
                    except (OSError, json.JSONDecodeError) as e:
                        # Log error but continue loading other files
                        print(f"Warning: Could not load room file {file_path}: {e}")
                        continue
    except OSError as e:
        # Handle permission errors or other OS issues
        print(f"Warning: Could not access rooms directory {ROOMS_BASE_PATH}: {e}")

    return rooms


if __name__ == "__main__":
    all_rooms = load_rooms()
    print(f"Loaded {len(all_rooms)} rooms:")
    for room_id, room in all_rooms.items():
        print(f"- {room_id}: {room['name']}")
