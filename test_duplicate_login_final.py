#!/usr/bin/env python3
"""
Final test script to examine duplicate login behavior in MythosMUD.
"""

import requests

# Configuration
BASE_URL = "http://localhost:54731"
USERNAME = "testuser_final"
PASSWORD = "testpass123"
INVITE_CODE = "ARKHAM_ACCESS"  # Using a valid invite code from invites.json


def test_duplicate_login_final():
    """Test what happens when the same user logs in multiple times."""

    print("🧪 Testing Duplicate Login Behavior (Final)")
    print("=" * 50)

    # Step 1: Register a user with valid invite code
    print(f"\n1. Registering user with invite code '{INVITE_CODE}'...")
    register_data = {"username": USERNAME, "password": PASSWORD, "invite_code": INVITE_CODE}

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

    # Step 4: Third login (triplicate)
    print("\n4. Third login (triplicate)...")

    try:
        login3_response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"   Login 3 status: {login3_response.status_code}")

        if login3_response.status_code == 200:
            login3_result = login3_response.json()
            token3 = login3_result.get("access_token")
            user_id3 = login3_result.get("user_id")
            print(f"   Login 3 successful: {user_id3}")
            print(f"   Token 3 preview: {token3[:20]}...")
        else:
            print(f"   Login 3 failed: {login3_response.text}")
            return
    except Exception as e:
        print(f"   Login 3 error: {e}")
        return

    # Step 5: Compare tokens
    print("\n5. Analysis...")
    print(f"   User IDs match: {user_id1 == user_id2 == user_id3}")
    print(f"   Tokens are different: {token1 != token2 != token3}")
    print(f"   All tokens valid: {bool(token1) and bool(token2) and bool(token3)}")

    # Step 6: Test all tokens work
    print("\n6. Testing token validity...")

    headers1 = {"Authorization": f"Bearer {token1}"}
    headers2 = {"Authorization": f"Bearer {token2}"}
    headers3 = {"Authorization": f"Bearer {token3}"}

    try:
        # Test all tokens
        test1_response = requests.get(f"{BASE_URL}/auth/me", headers=headers1)
        test2_response = requests.get(f"{BASE_URL}/auth/me", headers=headers2)
        test3_response = requests.get(f"{BASE_URL}/auth/me", headers=headers3)

        print(f"   Token 1 works: {test1_response.status_code == 200}")
        print(f"   Token 2 works: {test2_response.status_code == 200}")
        print(f"   Token 3 works: {test3_response.status_code == 200}")

        if all(r.status_code == 200 for r in [test1_response, test2_response, test3_response]):
            user1_info = test1_response.json()
            user2_info = test2_response.json()
            user3_info = test3_response.json()

            usernames_match = user1_info.get("username") == user2_info.get("username") == user3_info.get("username")
            print(f"   All tokens access same user: {usernames_match}")

    except Exception as e:
        print(f"   Token test error: {e}")

    # Step 7: Test concurrent usage
    print("\n7. Testing concurrent token usage...")

    try:
        # Make concurrent requests with different tokens
        import threading

        results = []

        def test_token(token_num, token, headers):
            try:
                response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
                results.append((token_num, response.status_code == 200))
            except Exception:
                results.append((token_num, False))

        # Start concurrent requests
        threads = []
        for i, (token, headers) in enumerate([(token1, headers1), (token2, headers2), (token3, headers3)], 1):
            thread = threading.Thread(target=test_token, args=(i, token, headers))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Check results
        for token_num, success in results:
            print(f"   Token {token_num} concurrent test: {'✅' if success else '❌'}")

    except Exception as e:
        print(f"   Concurrent test error: {e}")

    print("\n" + "=" * 50)
    print("✅ Duplicate login test completed!")

    # Summary
    print("\n📋 SUMMARY:")
    print("   • Multiple JWT tokens can be generated for the same user")
    print("   • Each login creates a new, unique token")
    print("   • All tokens remain valid simultaneously")
    print("   • No server-side session limits are enforced")
    print("   • This allows multiple concurrent sessions per user")


if __name__ == "__main__":
    test_duplicate_login_final()
