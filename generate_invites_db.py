#!/usr/bin/env python3
"""
Generate Mythos-themed invite codes and store them in the database.

This script creates invite codes using the database storage system
instead of the old JSON file approach.
"""

import asyncio
import os
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add the server directory to the path so we can import models
sys.path.append(str(Path(__file__).parent / "server"))

from server.database import async_session_maker
from server.models.invite import Invite

MYTHOS_WORDS = [
    "Cthulhu", "Nyarlathotep", "Azathoth", "YogSothoth", "ShubNiggurath",
    "Dagon", "Hastur", "Yig", "Tsathoggua", "Nodens", "Bokrug", "Glaaki",
    "Ithaqua", "AtlachNacha", "Cthugha", "Eihort", "Ghatanothoa", "Hypnos",
    "Lloigor", "Mnomquah", "RhanTegoth", "ShuddeMell", "Tulzscha", "Ycnagnnis",
    "Arkham", "Innsmouth", "Dunwich", "Kingsport", "Miskatonic", "Esoteric",
    "Necronomicon", "Pnakotic", "Rlyeh", "Kadath", "Leng", "Yuggoth", "Xoth",
    "Yaddith", "Zothique", "Hyperborea", "Mu", "Atlantis", "Lemuria", "Elder",
    "Great", "Outer", "Inner", "Deep", "Abyss", "Void", "Chaos", "Order",
    "Cosmos", "Dream", "Nightmare", "Madness", "Sanity", "Truth", "Lies",
    "Knowledge", "Secrets", "Forbidden", "Hidden", "Ancient", "Eternal",
    "Timeless", "Infinite", "Vast", "Profound", "Mysterious", "Cryptic",
    "Arcane", "Occult", "Mystical", "Eldritch", "Unspeakable", "Nameless",
    "Faceless", "Formless", "Shapeless", "Boundless", "Endless", "Limitless",
    "Infinite", "Eternal", "Immortal", "Undying", "Ageless", "Primordial",
    "Prehistoric", "Antediluvian", "Archaic", "Venerable", "Sublime",
    "Transcendent", "Divine", "Infernal", "Celestial", "Abyssal",
]

# Additional components for variety
PREFIXES = ["MYTHOS", "ELDER", "GREAT", "DEEP", "VOID", "COSMOS", "DREAM"]
SUFFIXES = ["2025", "ACCESS", "GATE", "PORTAL", "KEY", "CODE", "PASS", "INITIATE"]


def generate_invite_code():
    """Generate a unique Mythos-themed invite code."""
    # 50% chance to use a Mythos word
    if random.random() < 0.5:
        word = random.choice(MYTHOS_WORDS)
        # 30% chance to add a number
        if random.random() < 0.3:
            number = random.randint(100, 999)
            return f"{word}{number}"
        return word
    else:
        # Use prefix + suffix combination
        prefix = random.choice(PREFIXES)
        suffix = random.choice(SUFFIXES)
        # 40% chance to add a number
        if random.random() < 0.4:
            number = random.randint(10, 99)
            return f"{prefix}{suffix}{number}"
        return f"{prefix}{suffix}"


def generate_unique_codes(count=100):
    """Generate a list of unique invite codes."""
    codes = set()
    attempts = 0
    max_attempts = count * 10  # Prevent infinite loops

    while len(codes) < count and attempts < max_attempts:
        code = generate_invite_code()
        if code not in codes:
            codes.add(code)
        attempts += 1

    return list(codes)


async def get_existing_codes():
    """Get existing invite codes from the database."""
    from sqlalchemy import text
    async with async_session_maker() as session:
        result = await session.execute(
            text("SELECT invite_code FROM invites")
        )
        return {row[0] for row in result.fetchall()}


async def create_invite_in_db(invite_code: str, expires_in_days: int = 30):
    """Create an invite in the database."""
    async with async_session_maker() as session:
        # Create new invite
        invite = Invite(
            invite_code=invite_code,
            is_used=False,
            expires_at=datetime.utcnow() + timedelta(days=expires_in_days),
            created_at=datetime.utcnow(),
        )

        session.add(invite)
        await session.commit()
        return invite


async def main():
    """Generate invite codes and store them in the database."""
    print("Generating Mythos-themed invite codes for database storage...")

    # Set environment variable for database connection
    if not os.getenv("MYTHOSMUD_SECRET_KEY"):
        os.environ["MYTHOSMUD_SECRET_KEY"] = "dev-secret-key-for-invite-generation"

    # Generate new codes
    new_codes = generate_unique_codes(100)

    # Get existing codes to avoid duplicates
    try:
        existing_codes = await get_existing_codes()
        print(f"Found {len(existing_codes)} existing invite codes in database")
    except Exception as e:
        print(f"Warning: Could not fetch existing codes: {e}")
        existing_codes = set()

    # Filter out duplicates
    unique_new_codes = [code for code in new_codes if code not in existing_codes]

    if not unique_new_codes:
        print("No new unique codes to generate!")
        return

    # Create invites in database
    created_count = 0
    for code in unique_new_codes:
        try:
            await create_invite_in_db(code)
            created_count += 1
        except Exception as e:
            print(f"Warning: Could not create invite {code}: {e}")

    print(f"✓ Generated {created_count} new invite codes")
    print("✓ Stored in database successfully")

    # Show some examples
    print("\nExample invite codes:")
    for i, code in enumerate(unique_new_codes[:10], 1):
        print(f"  {i:2d}. {code}")

    print(f"\nTotal new codes created: {created_count}")
    print("These codes are now available for user registration.")


if __name__ == "__main__":
    asyncio.run(main())
