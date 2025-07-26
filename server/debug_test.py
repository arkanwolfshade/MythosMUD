#!/usr/bin/env python3

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Test registration
response = client.post(
    "/auth/register",
    json={
        "username": "testuser",
        "password": "testpass",
        "invite_code": "INVITE123",
    },
)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
