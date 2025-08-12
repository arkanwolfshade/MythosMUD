#!/usr/bin/env python3
"""
Simple test script for the StatsGenerator functionality.
"""

import os
import sys

# Add the server directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

try:
    from server.game.stats_generator import StatsGenerator

    print("✓ StatsGenerator imported successfully")

    # Test initialization
    sg = StatsGenerator()

    print("✓ StatsGenerator initialized successfully")

    # Test rolling stats
    stats = sg.roll_stats("3d6")

    print(f"✓ Rolled stats: {stats.model_dump()}")

    # Test class validation
    available_classes = sg.get_available_classes(stats)

    print(f"✓ Available classes: {available_classes}")

    # Test stat summary
    summary = sg.get_stat_summary(stats)

    print(f"✓ Stat summary generated: {summary['total_points']} total points")

    print("\n🎉 All tests passed! StatsGenerator is working correctly.")

except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
