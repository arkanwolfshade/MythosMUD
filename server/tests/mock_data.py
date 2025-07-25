# mock_data.py

MOCK_ROOMS = {
    "arkham_001": {
        "id": "arkham_001",
        "name": "Arkham Town Square",
        "description": "You are standing in the bustling heart of Arkham. The Miskatonic River flows nearby.",
        "zone": "arkham",
        "exits": {
            "north": "arkham_002",
            "south": "arkham_003",
            "east": "arkham_004",
            "west": "arkham_005",
        },
    },
    "arkham_002": {
        "id": "arkham_002",
        "name": "Miskatonic University Gates",
        "description": (
            "The grand wrought-iron gates of Miskatonic University loom here, "
            "with ivy crawling up the stone pillars."
        ),
        "zone": "arkham",
        "exits": {"south": "arkham_001", "north": "arkham_006"},
    },
    "arkham_003": {
        "id": "arkham_003",
        "name": "Old South Docks",
        "description": (
            "Weathered planks creak underfoot at the bustling river docks, "
            "where fishermen haul in their catch."
        ),
        "zone": "arkham",
        "exits": {"north": "arkham_001", "south": "arkham_007"},
    },
    "arkham_004": {
        "id": "arkham_004",
        "name": "East Market Bazaar",
        "description": (
            "Colorful tents and exotic wares fill the lively bazaar, "
            "with merchants hawking their goods to passersby."
        ),
        "zone": "arkham",
        "exits": {"west": "arkham_001"},
    },
    "arkham_005": {
        "id": "arkham_005",
        "name": "West Alley Shadows",
        "description": (
            "A narrow, dimly-lit alley where shadows flicker and the scent of pipe smoke lingers in the air."
        ),
        "zone": "arkham",
        "exits": {"east": "arkham_001"},
    },
    "arkham_006": {
        "id": "arkham_006",
        "name": "University Quad",
        "description": (
            "A broad green lawn surrounded by academic halls, "
            "with students hurrying between classes."
        ),
        "zone": "arkham",
        "exits": {"south": "arkham_002"},
    },
    "arkham_007": {
        "id": "arkham_007",
        "name": "Foggy Riverside Path",
        "description": (
            "A misty path along the riverbank, where the fog rolls in thick "
            "and the water laps quietly at the shore."
        ),
        "zone": "arkham",
        "exits": {"north": "arkham_003"},
    },
}


class MockPlayer:
    def __init__(self, name, current_room_id="arkham_001"):
        self.name = name
        self.current_room_id = current_room_id


class MockPlayerManager:
    def __init__(self):
        self.players = {"cmduser": MockPlayer("cmduser", "arkham_001")}
        print(
            f"[MockPlayerManager] Initialized with cmduser in {self.players['cmduser'].current_room_id}"
        )

    def get_player_by_name(self, name):
        return self.players.get(name)

    def update_player(self, player):
        self.players[player.name] = player

    def list_players(self):
        return list(self.players.values())

    def create_player(self, name, starting_room_id="arkham_001"):
        self.players[name] = MockPlayer(name, starting_room_id)
        return self.players[name]
