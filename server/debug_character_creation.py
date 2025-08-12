#!/usr/bin/env python3
"""Debug character creation issue."""

import sys
from pathlib import Path

# Add server directory to path
sys.path.insert(0, str(Path(__file__).parent))

from fastapi.testclient import TestClient
from main import app


def test_character_creation():
    """Test character creation directly."""
    client = TestClient(app)

    # First, let's test the roll-stats endpoint
    print("Testing roll-stats endpoint...")

    # We need a valid JWT token, so let's create a simple test
    # For now, let's just test the endpoint structure

    # Test without authentication (should fail)
    response = client.post("/players/roll-stats", json={"method": "3d6"})
    print(f"Roll stats without auth: {response.status_code}")
    if response.status_code != 401:
        print(f"Unexpected response: {response.json()}")

    # Test create-character endpoint structure
    print("\nTesting create-character endpoint...")
    response = client.post(
        "/players/create-character",
        json={
            "name": "testuser",
            "stats": {
                "strength": 10,
                "dexterity": 10,
                "constitution": 10,
                "intelligence": 10,
                "wisdom": 10,
                "charisma": 10,
            },
        },
    )
    print(f"Create character without auth: {response.status_code}")
    if response.status_code != 401:
        print(f"Unexpected response: {response.json()}")


if __name__ == "__main__":
    test_character_creation()
