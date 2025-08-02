#!/usr/bin/env python3
"""
Debug script to test SSE endpoint directly.
"""

from fastapi.testclient import TestClient

from main import app


def test_sse_endpoint():
    """Test SSE endpoint directly."""
    client = TestClient(app)

    print("Testing SSE endpoint with invalid token...")
    try:
        response = client.get("/events/testplayer?token=invalid")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

    print("\nTesting SSE endpoint with no token...")
    try:
        response = client.get("/events/testplayer")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    test_sse_endpoint()
