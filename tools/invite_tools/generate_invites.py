#!/usr/bin/env python3
"""
Generate Mythos-themed invite codes for testing using the database.

This script generates unique Mythos-themed invite codes and stores them
in the database using the new FastAPI Users migration structure.
"""

import asyncio
import random
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "server"))

# Now import server modules
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from server.config_loader import get_config
from server.models.invite import Invite

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


async def generate_unique_codes(count=100, expires_in_days: int = 30):
    """Generate a list of unique invite codes and store them in the database."""
    config = get_config()
    engine = create_async_engine(config["database_url"])
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        # Get existing codes to avoid duplicates
        result = await session.execute(text("SELECT invite_code FROM invites"))
        existing_codes = {row[0] for row in result.fetchall()}

        codes = set()
        attempts = 0
        max_attempts = count * 10  # Prevent infinite loops

        while len(codes) < count and attempts < max_attempts:
            code = generate_invite_code()
            if code not in existing_codes and code not in codes:
                codes.add(code)
            attempts += 1

        if not codes:
            return []

        # Create invite records
        invites = []
        for code in codes:
            invite = Invite(
                invite_code=code,
                # Persist naive UTC for DB
                expires_at=(datetime.now(UTC) + timedelta(days=expires_in_days)).replace(tzinfo=None),
            )
            invites.append(invite)

        # Add all invites to session
        session.add_all(invites)
        await session.commit()

        return list(codes)


async def main():
    """Generate 100 invite codes and store them in the database."""
    print("Generating 100 unique Mythos-themed invite codes...")

    # Generate new codes and store them
    new_codes = await generate_unique_codes(100)

    if not new_codes:
        print("❌ Failed to generate unique codes (may already exist)")
        return

    print(f"✓ Generated and stored {len(new_codes)} new invite codes in database")

    # Show some examples
    print("\nExample invite codes:")
    for i, code in enumerate(new_codes[:10], 1):
        print(f"  {i:2d}. {code}")

    if len(new_codes) > 10:
        print(f"  ... and {len(new_codes) - 10} more")


if __name__ == "__main__":
    asyncio.run(main())
