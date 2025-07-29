#!/usr/bin/env python3

import uuid

from fastapi.testclient import TestClient

from .main import app
from .persistence import get_persistence

client = TestClient(app)
# Set up the persistence layer manually since TestClient doesn't run lifespan
client.app.state.persistence = get_persistence()

# Test registration with unique username
unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
response = client.post(
    "/auth/register",
    json={
        "username": unique_username,
        "password": "testpass",
        "invite_code": "Dream800",
    },
)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Only test login if registration was successful
if response.status_code == 201:
    # Test login
    response = client.post("/auth/login", json={"username": unique_username, "password": "testpass"})
print(f"Login Status: {response.status_code}")
print(f"Login Response: {response.json()}")

# Check if player_id is returned
if response.status_code == 200:
    data = response.json()
    if "player_id" in data:
        print(f"✅ Player ID returned: {data['player_id']}")
    else:
        print("❌ Player ID not returned")
