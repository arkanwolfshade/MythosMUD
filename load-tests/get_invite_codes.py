#!/usr/bin/env python3
"""
Helper script to get 10 active invite codes from the database for load testing.

This script queries the database for 10 active invite codes and outputs them
in a format suitable for use in the load test.
"""

import asyncio
import sys
from pathlib import Path

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "server"))

from dotenv import load_dotenv
from sqlalchemy import text

from server.database import get_session_maker

# Load environment variables
load_dotenv(Path(".env.local"))


async def get_10_active_invites():
    """Get 10 active invite codes from the database."""
    async with get_session_maker()() as session:
        result = await session.execute(
            text("SELECT invite_code FROM invites WHERE is_active = true LIMIT 10")
        )
        codes = [row[0] for row in result.fetchall()]

        if len(codes) < 10:
            print(f"WARNING: Only found {len(codes)} active invite codes, need 10", file=sys.stderr)
            print("Please generate more invite codes before running the load test.", file=sys.stderr)
            return None

        return codes


async def main():
    """Main entry point."""
    print("Fetching 10 active invite codes from database...")

    codes = await get_10_active_invites()

    if not codes:
        print("Failed to get 10 invite codes", file=sys.stderr)
        sys.exit(1)

    print(f"\nFound {len(codes)} active invite codes:")
    print("-" * 80)
    for i, code in enumerate(codes, 1):
        print(f"Player {i}: {code}")
    print("-" * 80)
    print("\nInvite codes (comma-separated):")
    print(",".join(codes))
    print("\nInvite codes (JSON array):")
    import json
    print(json.dumps(codes, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
