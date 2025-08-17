#!/usr/bin/env python3
"""
Test script to verify connection termination behavior.
"""

import time

import requests

BASE_URL = "http://localhost:54731"


def test_connection_termination():
    """Test that subsequent connections terminate previous ones."""

    print("🧪 Testing Connection Termination Behavior")
    print("=" * 50)

    # Test data - using existing account
    username = "Ithaqua"
    password = "Cthulhu1"

    # Step 1: First login
    print("\n1. First login...")
    login_data = {"username": username, "password": password}

    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data, timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            token1 = data.get("access_token")
            print(f"   ✅ Login successful, token: {token1[:20]}...")
        else:
            print(f"   ❌ Login failed: {response.text[:100]}")
            return
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return

    # Step 2: Second login (should terminate first connection)
    print("\n2. Second login (should terminate first connection)...")

    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data, timeout=10)
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            token2 = data.get("access_token")
            print(f"   ✅ Login successful, token: {token2[:20]}...")
        else:
            print(f"   ❌ Login failed: {response.text[:100]}")
            return
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return

    # Step 3: Test both tokens
    print("\n3. Testing token validity...")

    headers1 = {"Authorization": f"Bearer {token1}"}
    headers2 = {"Authorization": f"Bearer {token2}"}

    try:
        # Test token 1 (should still work for API calls)
        response1 = requests.get(f"{BASE_URL}/auth/me", headers=headers1, timeout=10)
        print(f"   Token 1 API works: {response1.status_code == 200}")

        # Test token 2 (should work for API calls)
        response2 = requests.get(f"{BASE_URL}/auth/me", headers=headers2, timeout=10)
        print(f"   Token 2 API works: {response2.status_code == 200}")

        if response1.status_code == 200 and response2.status_code == 200:
            user1 = response1.json()
            user2 = response2.json()
            print(f"   Both tokens access same user: {user1.get('username') == user2.get('username')}")

    except Exception as e:
        print(f"   ❌ Token test error: {e}")

    # Step 4: Test WebSocket connection termination
    print("\n4. Testing WebSocket connection termination...")

    try:
        import websocket

        # Create first WebSocket connection
        print("   Creating first WebSocket connection...")
        ws1 = websocket.create_connection(f"ws://localhost:54731/api/ws?token={token1}")
        print("   ✅ First WebSocket connected")

        # Wait a moment
        time.sleep(1)

        # Create second WebSocket connection (should terminate first)
        print("   Creating second WebSocket connection...")
        ws2 = websocket.create_connection(f"ws://localhost:54731/api/ws?token={token2}")
        print("   ✅ Second WebSocket connected")

        # Wait a moment for termination
        time.sleep(1)

        # Check if first connection is closed
        try:
            ws1.send("ping")
            print("   ❌ First WebSocket still active (should be terminated)")
        except Exception:
            print("   ✅ First WebSocket properly terminated")

        # Check if second connection is active
        try:
            ws2.send("ping")
            print("   ✅ Second WebSocket is active")
        except Exception:
            print("   ❌ Second WebSocket failed: {e}")

        # Clean up
        try:
            ws1.close()
        except Exception:
            pass
        try:
            ws2.close()
        except Exception:
            pass

    except ImportError:
        print("   ⚠️  websocket-client not available, skipping WebSocket test")
    except Exception as e:
        print(f"   ❌ WebSocket test error: {e}")

    print("\n" + "=" * 50)
    print("✅ Connection termination test completed!")

    # Summary
    print("\n📋 SUMMARY:")
    print("   • Multiple JWT tokens can be generated (this is fine)")
    print("   • Previous real-time connections should be terminated")
    print("   • Only one active WebSocket/SSE connection per user")
    print("   • New connections should have fresh state")


if __name__ == "__main__":
    test_connection_termination()
