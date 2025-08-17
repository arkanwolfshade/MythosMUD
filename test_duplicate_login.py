#!/usr/bin/env python3
"""
Test script to examine duplicate login behavior in MythosMUD.
"""

import requests

# Configuration
BASE_URL = "http://localhost:54731"
USERNAME = "testuser_duplicate"
PASSWORD = "testpass123"


def test_duplicate_login():
    """Test what happens when the same user logs in multiple times."""

    print("🧪 Testing Duplicate Login Behavior")
    print("=" * 50)

    # Step 1: Register a user
    print("\n1. Registering user...")
    register_data = {"username": USERNAME, "password": PASSWORD, "invite_code": "test123"}

    try:
        register_response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        print(f"   Register status: {register_response.status_code}")

        if register_response.status_code == 200:
            register_result = register_response.json()
            print(f"   Registration successful: {register_result.get('user_id')}")
        else:
            print(f"   Registration failed: {register_response.text}")
            return
    except Exception as e:
        print(f"   Registration error: {e}")
        return

    # Step 2: First login
    print("\n2. First login...")
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
            return
    except Exception as e:
        print(f"   Login 1 error: {e}")
        return

    # Step 3: Second login (duplicate)
    print("\n3. Second login (duplicate)...")

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

    # Step 4: Compare tokens
    print("\n4. Analysis...")
    print(f"   User IDs match: {user_id1 == user_id2}")
    print(f"   Tokens are different: {token1 != token2}")
    print(f"   Both tokens valid: {bool(token1) and bool(token2)}")

    # Step 5: Test both tokens work
    print("\n5. Testing token validity...")

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


if __name__ == "__main__":
    test_duplicate_login()
