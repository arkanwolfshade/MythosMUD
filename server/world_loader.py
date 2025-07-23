import os
import json
from typing import Dict, Any

ROOMS_BASE_PATH = os.path.join(os.path.dirname(__file__), "rooms")


def load_rooms() -> Dict[str, Any]:
    rooms = {}
    for zone in os.listdir(ROOMS_BASE_PATH):
        zone_path = os.path.join(ROOMS_BASE_PATH, zone)
        if not os.path.isdir(zone_path):
            continue
        for filename in os.listdir(zone_path):
            if filename.endswith(".json"):
                file_path = os.path.join(zone_path, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    room = json.load(f)
                    room_id = room.get("id")
                    if room_id:
                        rooms[room_id] = room
    return rooms


if __name__ == "__main__":
    all_rooms = load_rooms()
    print(f"Loaded {len(all_rooms)} rooms:")
    for room_id, room in all_rooms.items():
        print(f"- {room_id}: {room['name']}")
