#!/usr/bin/env python3
"""
Simple script to create an admin user for testing the shutdown command.
"""

import asyncio
import os
import sys

# Add the server directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "server"))

from server.auth.argon2_utils import hash_password
from server.database import _async_session_maker, _initialize_database
from server.models.user import User


async def create_admin_user():
    """Create an admin user for testing."""
    # Initialize the database session maker
    _initialize_database()

    async with _async_session_maker() as session:
        # Check if user already exists
        existing_user = await session.get(User, "ArkanWolfshade")
        if existing_user:
            print("User ArkanWolfshade already exists. Updating to admin...")
            existing_user.is_admin = True
            existing_user.hashed_password = hash_password("password123")
            await session.commit()
            print("User updated to admin successfully!")
            return

        # Create new admin user
        user = User(
            id="ArkanWolfshade",
            email="arkan@example.com",
            hashed_password=hash_password("password123"),
            is_admin=True,
            is_active=True,
            is_verified=True,
        )

        session.add(user)
        await session.commit()
        print("Admin user created successfully!")


if __name__ == "__main__":
    asyncio.run(create_admin_user())
