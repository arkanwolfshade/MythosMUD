#!/usr/bin/env python3
"""
Test script for mute commands functionality.
"""

import requests

# Server configuration
SERVER_URL = "http://localhost:54731"
LOGIN_URL = f"{SERVER_URL}/auth/login"
COMMAND_URL = f"{SERVER_URL}/command"


def login(username, password):
    """Login and get access token."""
    login_data = {"username": username, "password": password}

    try:
        response = requests.post(LOGIN_URL, json=login_data)
        response.raise_for_status()

        data = response.json()
        return data.get("access_token")
    except requests.exceptions.RequestException as e:
        print(f"Login failed: {e}")
        return None


def send_command(token, command):
    """Send a command to the server."""
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    command_data = {"command": command}

    try:
        response = requests.post(COMMAND_URL, json=command_data, headers=headers)
        response.raise_for_status()

        data = response.json()
        return data.get("result", "No result")
    except requests.exceptions.RequestException as e:
        print(f"Command failed: {e}")
        if hasattr(e, "response") and e.response is not None:
            try:
                error_data = e.response.json()
                print(f"   Error details: {error_data}")
            except Exception:
                print(f"   Response text: {e.response.text}")
        return None


def test_mute_commands():
    """Test the mute command functionality."""
    print("🧪 Testing Mute Commands")
    print("=" * 50)

    # Test accounts
    accounts = [("ArkanWolfshade", "Cthulhu1"), ("Ithaqua", "Cthulhu1"), ("Azathoth", "Cthulhu1")]

    tokens = {}

    # Login all accounts
    print("\n1️⃣ Logging in accounts...")
    for username, password in accounts:
        token = login(username, password)
        if token:
            tokens[username] = token
            print(f"   ✅ {username} logged in successfully")
        else:
            print(f"   ❌ {username} login failed")

    if not tokens:
        print("❌ No accounts could log in. Exiting.")
        return

    # Test basic commands first
    print("\n2️⃣ Testing basic commands...")
    for username, token in tokens.items():
        result = send_command(token, "help mute")
        if result:
            print(f"   ✅ {username} can access help: {result[:50]}...")
        else:
            print(f"   ❌ {username} cannot access help")

    # Test mute command
    print("\n3️⃣ Testing mute command...")
    arkan_token = tokens.get("ArkanWolfshade")
    if arkan_token:
        # ArkanWolfshade mutes Ithaqua
        result = send_command(arkan_token, "mute Ithaqua 5 Testing mute command")
        if result:
            print(f"   ✅ Mute command result: {result}")
        else:
            print("   ❌ Mute command failed")

    # Test unmute command
    print("\n4️⃣ Testing unmute command...")
    if arkan_token:
        result = send_command(arkan_token, "unmute Ithaqua")
        if result:
            print(f"   ✅ Unmute command result: {result}")
        else:
            print("   ❌ Unmute command failed")

    # Test global mute command
    print("\n5️⃣ Testing global mute command...")
    if arkan_token:
        result = send_command(arkan_token, "mute_global Ithaqua 10 Testing global mute")
        if result:
            print(f"   ✅ Global mute command result: {result}")
        else:
            print("   ❌ Global mute command failed")

    # Test global unmute command
    print("\n6️⃣ Testing global unmute command...")
    if arkan_token:
        result = send_command(arkan_token, "unmute_global Ithaqua")
        if result:
            print(f"   ✅ Global unmute command result: {result}")
        else:
            print("   ❌ Global unmute command failed")

    # Test add admin command
    print("\n7️⃣ Testing add admin command...")
    if arkan_token:
        result = send_command(arkan_token, "add_admin Azathoth")
        if result:
            print(f"   ✅ Add admin command result: {result}")
        else:
            print("   ❌ Add admin command failed")

    print("\n🎉 Mute command testing completed!")


if __name__ == "__main__":
    test_mute_commands()
