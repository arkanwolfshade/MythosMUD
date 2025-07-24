#!/usr/bin/env python3
"""
Test script for the player stats system.
"""

import pytest

try:
    import requests

    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Warning: requests module not available. Integration tests will be skipped.")

BASE_URL = "http://localhost:8000"


def test_player_creation():
    """Test creating a new player."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    print("Testing player creation...")

    # Create a test player
    response = requests.post(f"{BASE_URL}/players", params={"name": "TestPlayer"})

    if response.status_code == 200:
        player = response.json()
        print(f"✅ Created player: {player['name']} (ID: {player['id']})")
        print(
            f"   Stats: STR={player['stats']['strength']}, "
            f"DEX={player['stats']['dexterity']}, "
            f"CON={player['stats']['constitution']}"
        )
        print(f"   Sanity: {player['stats']['sanity']}/100")
        print(
            f"   Health: {player['stats']['current_health']}/{player['stats']['max_health']}"
        )
        return player["id"]
    else:
        print(f"❌ Failed to create player: {response.text}")
        return None


def test_sanity_loss(player_id):
    """Test applying sanity loss to a player."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    print(f"\nTesting sanity loss for player {player_id}...")

    # Apply sanity loss
    response = requests.post(
        f"{BASE_URL}/players/{player_id}/sanity-loss",
        params={"amount": 25, "source": "test"},
    )

    if response.status_code == 200:
        print(f"✅ Applied sanity loss: {response.json()['message']}")

        # Check player stats
        player_response = requests.get(f"{BASE_URL}/players/{player_id}")
        if player_response.status_code == 200:
            player = player_response.json()
            print(f"   Current sanity: {player['stats']['sanity']}/100")
            print(f"   Status effects: {len(player['status_effects'])} active")
            for effect in player["status_effects"]:
                print(
                    f"     - {effect['effect_type']} (intensity: {effect['intensity']})"
                )
    else:
        print(f"❌ Failed to apply sanity loss: {response.text}")


def test_fear_and_corruption(player_id):
    """Test applying fear and corruption."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    print(f"\nTesting fear and corruption for player {player_id}...")

    # Apply fear
    response = requests.post(
        f"{BASE_URL}/players/{player_id}/fear", params={"amount": 30, "source": "test"}
    )
    if response.status_code == 200:
        print(f"✅ Applied fear: {response.json()['message']}")

    # Apply corruption
    response = requests.post(
        f"{BASE_URL}/players/{player_id}/corruption",
        params={"amount": 20, "source": "test"},
    )
    if response.status_code == 200:
        print(f"✅ Applied corruption: {response.json()['message']}")

    # Check player stats
    player_response = requests.get(f"{BASE_URL}/players/{player_id}")
    if player_response.status_code == 200:
        player = player_response.json()
        print(f"   Current fear: {player['stats']['fear']}/100")
        print(f"   Current corruption: {player['stats']['corruption']}/100")
        print(f"   Status effects: {len(player['status_effects'])} active")


def test_occult_knowledge(player_id):
    """Test gaining occult knowledge (which should cause sanity loss)."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    print(f"\nTesting occult knowledge gain for player {player_id}...")

    # Get initial stats
    player_response = requests.get(f"{BASE_URL}/players/{player_id}")
    if player_response.status_code == 200:
        player = player_response.json()
        initial_sanity = player["stats"]["sanity"]
        initial_knowledge = player["stats"]["occult_knowledge"]
        print(
            f"   Initial sanity: {initial_sanity}, occult knowledge: {initial_knowledge}"
        )

    # Gain occult knowledge
    response = requests.post(
        f"{BASE_URL}/players/{player_id}/occult-knowledge",
        params={"amount": 10, "source": "forbidden tome"},
    )
    if response.status_code == 200:
        print(f"✅ Gained occult knowledge: {response.json()['message']}")

    # Check final stats
    player_response = requests.get(f"{BASE_URL}/players/{player_id}")
    if player_response.status_code == 200:
        player = player_response.json()
        final_sanity = player["stats"]["sanity"]
        final_knowledge = player["stats"]["occult_knowledge"]
        print(f"   Final sanity: {final_sanity}, occult knowledge: {final_knowledge}")
        print(f"   Sanity lost: {initial_sanity - final_sanity}")
        print(f"   Knowledge gained: {final_knowledge - initial_knowledge}")


def test_health_operations(player_id):
    """Test health damage and healing."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    print(f"\nTesting health operations for player {player_id}...")

    # Damage player
    response = requests.post(
        f"{BASE_URL}/players/{player_id}/damage",
        params={"amount": 15, "damage_type": "physical"},
    )
    if response.status_code == 200:
        print(f"✅ Applied damage: {response.json()['message']}")

    # Check health
    player_response = requests.get(f"{BASE_URL}/players/{player_id}")
    if player_response.status_code == 200:
        player = player_response.json()
        print(
            f"   Health after damage: {player['stats']['current_health']}/{player['stats']['max_health']}"
        )

    # Heal player
    response = requests.post(
        f"{BASE_URL}/players/{player_id}/heal", params={"amount": 10}
    )
    if response.status_code == 200:
        print(f"✅ Applied healing: {response.json()['message']}")

    # Check final health
    player_response = requests.get(f"{BASE_URL}/players/{player_id}")
    if player_response.status_code == 200:
        player = player_response.json()
        print(
            f"   Final health: {player['stats']['current_health']}/{player['stats']['max_health']}"
        )


def test_list_players():
    """Test listing all players."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    print("\nTesting player listing...")

    response = requests.get(f"{BASE_URL}/players")
    if response.status_code == 200:
        players = response.json()
        print(f"✅ Found {len(players)} players:")
        for player in players:
            print(
                f"   - {player['name']} (ID: {player['id']}) - Sanity: {player['stats']['sanity']}"
            )
    else:
        print(f"❌ Failed to list players: {response.text}")


def test_server_connection():
    """Test server connection."""
    if not REQUESTS_AVAILABLE:
        pytest.skip("requests module not available")

    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            pytest.skip("Server not responding")
        return True
    except requests.exceptions.ConnectionError:
        pytest.skip("Cannot connect to server")


def main():
    """Run all tests."""
    if not REQUESTS_AVAILABLE:
        print(
            "❌ requests module not available. Please install it to run integration tests."
        )
        return

    print("🧪 Testing MythosMUD Player Stats System")
    print("=" * 50)

    # Test server connection
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print(
                "❌ Server not responding. Make sure the server is running on localhost:8000"
            )
            return
        print("✅ Server is responding")
    except requests.exceptions.ConnectionError:
        print(
            "❌ Cannot connect to server. Make sure the server is running on localhost:8000"
        )
        return

    # Run tests
    player_id = test_player_creation()
    if player_id:
        test_sanity_loss(player_id)
        test_fear_and_corruption(player_id)
        test_occult_knowledge(player_id)
        test_health_operations(player_id)
        test_list_players()

    print("\n" + "=" * 50)
    print("🏁 Testing complete!")


if __name__ == "__main__":
    main()
