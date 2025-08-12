#!/usr/bin/env python3
"""Test Stats object serialization."""

import json

from game.stats_generator import Stats


def test_stats_serialization():
    """Test if Stats objects can be serialized to JSON."""
    # Create a Stats object
    stats = Stats(strength=10, dexterity=12, constitution=14, intelligence=16, wisdom=8, charisma=10)

    print("Stats object:", stats)
    print("Stats type:", type(stats))

    # Try to serialize to dict
    try:
        stats_dict = stats.model_dump()
        print("Stats dict:", stats_dict)
        print("Stats dict type:", type(stats_dict))

        # Try to serialize to JSON
        stats_json = json.dumps(stats_dict)
        print("Stats JSON:", stats_json)
        print("✅ Stats serialization successful!")

    except Exception as e:
        print(f"❌ Stats serialization failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_stats_serialization()
