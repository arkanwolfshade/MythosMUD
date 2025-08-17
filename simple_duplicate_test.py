#!/usr/bin/env python3
"""
Simple test to demonstrate duplicate login behavior.
"""

import requests

BASE_URL = "http://localhost:54731"


def simple_test():
    """Simple test of duplicate login behavior."""

    print("🧪 Simple Duplicate Login Test")
    print("=" * 40)

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

    # Step 2: Second login (duplicate)
    print("\n2. Second login (duplicate)...")

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

    # Step 3: Analysis
    print("\n3. Analysis...")
    print(f"   Tokens are different: {token1 != token2}")
    print(f"   Both tokens valid: {bool(token1) and bool(token2)}")

    # Step 4: Test both tokens
    print("\n4. Testing both tokens...")

    headers1 = {"Authorization": f"Bearer {token1}"}
    headers2 = {"Authorization": f"Bearer {token2}"}

    try:
        # Test token 1
        response1 = requests.get(f"{BASE_URL}/auth/me", headers=headers1, timeout=10)
        print(f"   Token 1 works: {response1.status_code == 200}")

        # Test token 2
        response2 = requests.get(f"{BASE_URL}/auth/me", headers=headers2, timeout=10)
        print(f"   Token 2 works: {response2.status_code == 200}")

        if response1.status_code == 200 and response2.status_code == 200:
            user1 = response1.json()
            user2 = response2.json()
            print(f"   Both access same user: {user1.get('username') == user2.get('username')}")

    except Exception as e:
        print(f"   ❌ Token test error: {e}")

    print("\n" + "=" * 40)
    print("✅ Test completed!")


if __name__ == "__main__":
    simple_test()
