# mock_data.py

# Mock room data has been moved to JSON files in server/tests/data/rooms/arkham/
# This file now only contains player-related mock data


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
