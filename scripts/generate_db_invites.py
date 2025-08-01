#!/usr/bin/env python3
"""
Generate 100 unique Mythos-themed invite codes in the SQLite database.

This script creates invite codes directly in the database table
instead of the JSON file, which is the correct approach for
the MythosMUD authentication system.
"""

import asyncio
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Add the server directory to the Python path
server_path = str(Path(__file__).parent.parent / "server")
sys.path.insert(0, server_path)

# Import server modules
from database import get_async_session  # noqa: E402
from models.invite import Invite  # noqa: E402
from sqlalchemy import select  # noqa: E402
from sqlalchemy.ext.asyncio import AsyncSession  # noqa: E402

# Mythos-themed words and concepts for invite codes
MYTHOS_WORDS = [
    "Cthulhu",
    "Nyarlathotep",
    "Azathoth",
    "YogSothoth",
    "ShubNiggurath",
    "Dagon",
    "Hastur",
    "Yig",
    "Tsathoggua",
    "Nodens",
    "Bokrug",
    "Glaaki",
    "Ithaqua",
    "AtlachNacha",
    "Cthugha",
    "Eihort",
    "Ghatanothoa",
    "Hypnos",
    "Lloigor",
    "Mnomquah",
    "RhanTegoth",
    "ShuddeMell",
    "Tulzscha",
    "Ycnagnnis",
    "Arkham",
    "Innsmouth",
    "Dunwich",
    "Kingsport",
    "Miskatonic",
    "Esoteric",
    "Necronomicon",
    "Pnakotic",
    "Rlyeh",
    "Kadath",
    "Leng",
    "Yuggoth",
    "Xoth",
    "Yaddith",
    "Zothique",
    "Hyperborea",
    "Mu",
    "Atlantis",
    "Lemuria",
    "Elder",
    "Great",
    "Outer",
    "Inner",
    "Deep",
    "Abyss",
    "Void",
    "Chaos",
    "Order",
    "Cosmos",
    "Dream",
    "Nightmare",
    "Madness",
    "Sanity",
    "Truth",
    "Lies",
    "Knowledge",
    "Secrets",
    "Forbidden",
    "Hidden",
    "Ancient",
    "Eternal",
    "Timeless",
    "Infinite",
    "Vast",
    "Profound",
    "Mysterious",
    "Cryptic",
    "Arcane",
    "Occult",
    "Mystical",
    "Eldritch",
    "Unspeakable",
    "Nameless",
    "Faceless",
    "Formless",
    "Shapeless",
    "Boundless",
    "Endless",
    "Limitless",
    "Infinite",
    "Eternal",
    "Immortal",
    "Undying",
    "Ageless",
    "Primordial",
    "Prehistoric",
    "Antediluvian",
    "Archaic",
    "Venerable",
    "Sublime",
    "Transcendent",
    "Divine",
    "Infernal",
    "Celestial",
    "Abyssal",
]

# Additional components for variety
PREFIXES = ["MYTHOS", "ELDER", "GREAT", "DEEP", "VOID", "COSMOS", "DREAM"]
SUFFIXES = ["2025", "ACCESS", "GATE", "PORTAL", "KEY", "CODE", "PASS", "INITIATE"]


def generate_mythos_invite_code() -> str:
    """Generate a Mythos-themed invite code."""

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


async def generate_unique_codes(count: int = 100) -> list[str]:
    """Generate a list of unique Mythos-themed invite codes."""
    codes = set()
    attempts = 0
    max_attempts = count * 10  # Prevent infinite loops

    while len(codes) < count and attempts < max_attempts:
        code = generate_mythos_invite_code()
        if code not in codes:
            codes.add(code)
        attempts += 1

    return list(codes)


async def check_existing_codes(session: AsyncSession) -> set[str]:
    """Get all existing invite codes from the database."""
    result = await session.execute(select(Invite.invite_code))
    return {row[0] for row in result.fetchall()}


async def create_invites_in_db(count: int = 100) -> None:
    """Create new invites in the database."""
    print(f"Generating {count} unique Mythos-themed invite codes in database...")

    # Get database session
    session = await get_async_session().__anext__()

    try:
        # Get existing codes to avoid duplicates
        existing_codes = await check_existing_codes(session)
        print(f"Found {len(existing_codes)} existing invite codes")

        # Generate new codes
        new_codes = await generate_unique_codes(count)

        # Filter out any duplicates
        unique_new_codes = [
            code for code in new_codes if code not in existing_codes
        ]

        # Create new invite entries
        invites_created = 0
        expires_at = datetime.utcnow() + timedelta(days=365)  # 1 year expiration

        for code in unique_new_codes:
            invite = Invite(
                invite_code=code,
                is_used=False,
                expires_at=expires_at
            )
            session.add(invite)
            invites_created += 1

        # Commit to database
        await session.commit()

        print(f"✓ Generated {invites_created} new invite codes")

        # Get updated counts
        result = await session.execute(select(Invite))
        all_invites = result.scalars().all()

        used_count = sum(1 for invite in all_invites if invite.is_used)
        available_count = sum(1 for invite in all_invites if not invite.is_used)

        print(f"✓ Total invite codes available: {len(all_invites)}")
        print(f"✓ Used codes: {used_count}")
        print(f"✓ Available codes: {available_count}")

        # Show some examples
        print("\nExample invite codes:")
        for i, invite in enumerate(all_invites[-10:], 1):  # Show last 10
            status = "USED" if invite.is_used else "AVAILABLE"
            print(f"  {i:2d}. {invite.invite_code:<20} [{status}]")

    finally:
        await session.close()


async def main():
    """Main function to generate invites."""
    print("MythosMUD Database Invite Generator")
    print("=" * 40)

    await create_invites_in_db(100)


if __name__ == "__main__":
    asyncio.run(main())
