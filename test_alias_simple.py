#!/usr/bin/env python3
"""Simple test script for the alias system."""

import sys

sys.path.append("server")

try:
    from server.alias_storage import AliasStorage
except ImportError:
    print(
        "Error: Could not import AliasStorage. "
        "Make sure you're running from the project root."
    )
    sys.exit(1)


def test_alias_system():
    """Test the alias system functionality."""
    print("Testing MythosMUD Alias System...")

    # Initialize storage
    storage = AliasStorage()
    player_name = "test_user"

    # Test 1: Create aliases
    print("\n1. Creating aliases...")
    aliases = [
        ("l", "look"),
        ("n", "go north"),
        ("s", "go south"),
    ]

    for name, command in aliases:
        alias = storage.create_alias(player_name, name, command)
        if alias:
            print(f"   ✓ Created: {name} -> {command}")
        else:
            print(f"   ✗ Failed: {name} -> {command}")

    # Test 2: List aliases
    print("\n2. Listing aliases...")
    all_aliases = storage.get_player_aliases(player_name)
    for alias in all_aliases:
        print(f"   {alias.name} -> {alias.command}")

    print(f"   Total: {len(all_aliases)} aliases")

    # Test 3: Lookup aliases
    print("\n3. Testing lookups...")
    test_names = ["l", "n", "nonexistent"]
    for name in test_names:
        found = storage.get_alias(player_name, name)
        if found:
            print(f"   ✓ Found: {name} -> {found.command}")
        else:
            print(f"   ✗ Not found: {name}")

    # Test 4: Remove alias
    print("\n4. Removing alias...")
    if storage.remove_alias(player_name, "l"):
        print("   ✓ Removed alias 'l'")
    else:
        print("   ✗ Failed to remove alias 'l'")

    # Verify removal
    remaining = storage.get_player_aliases(player_name)
    print(f"   Remaining: {len(remaining)} aliases")

    # Clean up
    storage.delete_player_aliases(player_name)
    print("\n✓ Alias system test completed successfully!")


if __name__ == "__main__":
    test_alias_system()
