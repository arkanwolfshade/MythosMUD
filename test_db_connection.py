#!/usr/bin/env python3
"""Test database connection and invite creation."""

import asyncio
import os
import sys
from pathlib import Path

# Add the server directory to the path
sys.path.append(str(Path(__file__).parent / "server"))

from server.database import async_session_maker
from server.models.invite import Invite
from datetime import datetime, timedelta
from sqlalchemy import text


async def test_connection():
    """Test database connection."""
    try:
        async with async_session_maker() as session:
            result = await session.execute(text("SELECT 1"))
            print("✓ Database connection successful")
            return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False


async def test_invite_creation():
    """Test creating an invite in the database."""
    try:
        async with async_session_maker() as session:
            # Create a test invite
            invite = Invite(
                invite_code="TESTCODE123",
                is_used=False,
                expires_at=datetime.utcnow() + timedelta(days=30),
                created_at=datetime.utcnow(),
            )

            session.add(invite)
            await session.commit()
            print("✓ Invite creation successful")

            # Verify it was created
            result = await session.execute(
                text("SELECT invite_code FROM invites WHERE invite_code = 'TESTCODE123'")
            )
            row = result.fetchone()
            if row:
                print("✓ Invite verification successful")
                return True
            else:
                print("✗ Invite verification failed")
                return False

    except Exception as e:
        print(f"✗ Invite creation failed: {e}")
        return False


async def main():
    """Run database tests."""
    print("Testing database connection and invite creation...")

    # Set environment variable
    if not os.getenv("MYTHOSMUD_SECRET_KEY"):
        os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key"

    # Test connection
    if await test_connection():
        # Test invite creation
        await test_invite_creation()
    else:
        print("Cannot proceed with invite creation test")


if __name__ == "__main__":
    asyncio.run(main())
