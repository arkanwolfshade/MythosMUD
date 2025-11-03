#!/usr/bin/env python3
"""
Check and list invite codes in the database.

This script provides utilities to check the status of invite codes,
list existing codes, and verify their validity.
"""

import asyncio
import sys
from datetime import UTC, datetime
from pathlib import Path

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "server"))

from sqlalchemy import text

from server.database import get_session_maker


async def list_all_invites():
    """List all invite codes in the database with their status."""
    async with get_session_maker()() as session:
        result = await session.execute(
            text("""
                SELECT invite_code, used, expires_at, created_at
                FROM invites
                ORDER BY created_at DESC
            """)
        )
        invites = result.fetchall()

        if not invites:
            print("No invite codes found in database.")
            return

        print(f"Found {len(invites)} invite codes:")
        print("-" * 80)
        print(f"{'Code':<20} {'Used':<6} {'Expires':<20} {'Created':<20}")
        print("-" * 80)

        for invite in invites:
            code, used, expires_at, created_at = invite
            used_str = "Yes" if used else "No"

            # Handle date strings from database
            if expires_at and isinstance(expires_at, str):
                try:
                    expires_at = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
                except ValueError:
                    expires_at = None

            if created_at and isinstance(created_at, str):
                try:
                    created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
                except ValueError:
                    created_at = None

            expires_str = expires_at.strftime("%Y-%m-%d %H:%M") if expires_at else "Never"
            created_str = created_at.strftime("%Y-%m-%d %H:%M") if created_at else "Unknown"
            print(f"{code:<20} {used_str:<6} {expires_str:<20} {created_str:<20}")


async def check_invite_status(invite_code: str):
    """Check the status of a specific invite code."""
    async with get_session_maker()() as session:
        result = await session.execute(
            text("SELECT used, expires_at, created_at FROM invites WHERE invite_code = :code"), {"code": invite_code}
        )
        invite = result.fetchone()

        if not invite:
            print(f"❌ Invite code '{invite_code}' not found in database.")
            return

        used, expires_at, created_at = invite
        now = datetime.now(UTC)

        # Handle date strings from database
        if expires_at and isinstance(expires_at, str):
            try:
                expires_at = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
            except ValueError:
                expires_at = None

        if created_at and isinstance(created_at, str):
            try:
                created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            except ValueError:
                created_at = None

        print(f"Invite Code: {invite_code}")
        print(f"Used: {'Yes' if used else 'No'}")
        print(f"Created: {created_at.strftime('%Y-%m-%d %H:%M:%S') if created_at else 'Unknown'}")

        if expires_at:
            print(f"Expires: {expires_at.strftime('%Y-%m-%d %H:%M:%S')}")
            # Ensure both dates are timezone-aware for comparison
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=UTC)
            if expires_at < now:
                print("❌ EXPIRED")
            else:
                print("✅ Valid")
        else:
            print("Expires: Never")


async def count_invites():
    """Count invite codes by status."""
    async with get_session_maker()() as session:
        # Total count
        result = await session.execute(text("SELECT COUNT(*) FROM invites"))
        total = result.scalar()

        # Used count
        result = await session.execute(text("SELECT COUNT(*) FROM invites WHERE used = 1"))
        used = result.scalar()

        # Unused count
        result = await session.execute(text("SELECT COUNT(*) FROM invites WHERE used = 0"))
        unused = result.scalar()

        # Expired count
        result = await session.execute(
            text("SELECT COUNT(*) FROM invites WHERE expires_at < :now"), {"now": datetime.now(UTC)}
        )
        expired = result.scalar()

        print("Invite Code Statistics:")
        print(f"  Total: {total}")
        print(f"  Used: {used}")
        print(f"  Unused: {unused}")
        print(f"  Expired: {expired}")


async def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python check_invites.py list          - List all invite codes")
        print("  python check_invites.py count         - Show invite statistics")
        print("  python check_invites.py check <code>  - Check specific invite code")
        return

    command = sys.argv[1].lower()

    if command == "list":
        await list_all_invites()
    elif command == "count":
        await count_invites()
    elif command == "check":
        if len(sys.argv) < 3:
            print("Error: Please provide an invite code to check")
            return
        await check_invite_status(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        print("Available commands: list, count, check")


if __name__ == "__main__":
    asyncio.run(main())
