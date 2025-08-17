#!/usr/bin/env python3
"""
Simple test script to examine duplicate login behavior in MythosMUD.
"""

import requests

# Configuration
BASE_URL = "http://localhost:54731"
USERNAME = "testuser_simple"
PASSWORD = "testpass123"


def test_duplicate_login_simple():
    """Test what happens when the same user logs in multiple times."""

    print("🧪 Testing Duplicate Login Behavior (Simple)")
    print("=" * 50)

    # Step 1: Try to login (will fail if user doesn't exist)
    print("\n1. First login attempt...")
    login_data = {"username": USERNAME, "password": PASSWORD}

    try:
        login1_response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"   Login 1 status: {login1_response.status_code}")

        if login1_response.status_code == 200:
            login1_result = login1_response.json()
            token1 = login1_result.get("access_token")
            user_id1 = login1_result.get("user_id")
            print(f"   Login 1 successful: {user_id1}")
            print(f"   Token 1 preview: {token1[:20]}...")
        else:
            print(f"   Login 1 failed: {login1_response.text}")
            print("   (This is expected if user doesn't exist)")
            return
    except Exception as e:
        print(f"   Login 1 error: {e}")
        return

    # Step 2: Second login (duplicate)
    print("\n2. Second login (duplicate)...")

    try:
        login2_response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"   Login 2 status: {login2_response.status_code}")

        if login2_response.status_code == 200:
            login2_result = login2_response.json()
            token2 = login2_result.get("access_token")
            user_id2 = login2_result.get("user_id")
            print(f"   Login 2 successful: {user_id2}")
            print(f"   Token 2 preview: {token2[:20]}...")
        else:
            print(f"   Login 2 failed: {login2_response.text}")
            return
    except Exception as e:
        print(f"   Login 2 error: {e}")
        return

    # Step 3: Compare tokens
    print("\n3. Analysis...")
    print(f"   User IDs match: {user_id1 == user_id2}")
    print(f"   Tokens are different: {token1 != token2}")
    print(f"   Both tokens valid: {bool(token1) and bool(token2)}")

    # Step 4: Test both tokens work
    print("\n4. Testing token validity...")

    headers1 = {"Authorization": f"Bearer {token1}"}
    headers2 = {"Authorization": f"Bearer {token2}"}

    try:
        # Test first token
        test1_response = requests.get(f"{BASE_URL}/auth/me", headers=headers1)
        print(f"   Token 1 works: {test1_response.status_code == 200}")

        # Test second token
        test2_response = requests.get(f"{BASE_URL}/auth/me", headers=headers2)
        print(f"   Token 2 works: {test2_response.status_code == 200}")

        if test1_response.status_code == 200 and test2_response.status_code == 200:
            user1_info = test1_response.json()
            user2_info = test2_response.json()
            print(f"   Both tokens access same user: {user1_info.get('username') == user2_info.get('username')}")

    except Exception as e:
        print(f"   Token test error: {e}")

    print("\n" + "=" * 50)
    print("✅ Duplicate login test completed!")


def test_existing_user():
    """Test with an existing user if available."""
    print("\n🔍 Testing with existing users...")

    # Try some common usernames
    test_users = ["admin", "test", "user", "player", "demo"]

    for username in test_users:
        print(f"\n   Trying username: {username}")
        login_data = {"username": username, "password": "password"}

        try:
            response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
            if response.status_code == 200:
                print(f"   ✅ Found existing user: {username}")
                return username
            else:
                print(f"   ❌ User not found: {username}")
        except Exception as e:
            print(f"   ❌ Error: {e}")

    print("   No existing users found")
    return None


if __name__ == "__main__":
    # First try with existing user
    existing_user = test_existing_user()

    if existing_user:
        USERNAME = existing_user
        test_duplicate_login_simple()
    else:
        print("\n⚠️  No existing users found. Cannot test duplicate login behavior.")
        print("   Please create a user first or check the server logs for issues.")
