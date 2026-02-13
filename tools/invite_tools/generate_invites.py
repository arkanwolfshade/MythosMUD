#!/usr/bin/env python3
"""
Generate Mythos-themed invite codes for testing using the database.

This script generates unique Mythos-themed invite codes and stores them
in the database using the new FastAPI Users migration structure.
"""

import random
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

from anyio import run

# Load environment variables from .env.local
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent.parent
env_file = project_root / ".env.local"
if env_file.exists():
    load_dotenv(env_file)
else:
    # Try .env as fallback
    env_file = project_root / ".env"
    if env_file.exists():
        load_dotenv(env_file)

# Add server directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "server"))


# Now import server modules
from sqlalchemy import text  # noqa: E402
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine  # noqa: E402
from sqlalchemy.orm import sessionmaker  # noqa: E402

from server.config import get_config  # noqa: E402

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
    "Lucidity",
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
    engine = create_async_engine(config.database.url)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        # Get existing codes to avoid duplicates
        # Database column is 'invite_code' after migration
        result = await session.execute(text("SELECT invite_code FROM invites"))
        existing_codes = {row[0] for row in result.fetchall()}

        codes: set[str] = set()
        attempts = 0
        max_attempts = count * 10  # Prevent infinite loops

        while len(codes) < count and attempts < max_attempts:
            code = generate_invite_code()
            if code not in existing_codes and code not in codes:
                codes.add(code)
            attempts += 1

        if not codes:
            return []

        # Create invite records using raw SQL to match database schema
        # Database has: id (UUID), code, created_by_user, is_active, created_at, expires_at
        import uuid

        invites_data = []
        for code in codes:
            expires_at = (datetime.now(UTC) + timedelta(days=expires_in_days)).replace(tzinfo=None)
            invites_data.append(
                {
                    "id": str(uuid.uuid4()),
                    "invite_code": code,
                    "is_active": True,
                    "expires_at": expires_at,
                }
            )

        # Insert using raw SQL to match actual database schema
        for invite_data in invites_data:
            await session.execute(
                text("""
                    INSERT INTO invites (id, invite_code, is_active, expires_at, created_at)
                    VALUES (:id, :invite_code, :is_active, :expires_at, CURRENT_TIMESTAMP)
                """),
                invite_data,
            )

        await session.commit()

        return list(codes)


async def main():
    """Generate invite codes and store them in the database."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate Mythos-themed invite codes")
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of invite codes to generate (default: 10)",
    )
    parser.add_argument(
        "--expires-days",
        type=int,
        default=30,
        help="Number of days until expiration (default: 30)",
    )
    args = parser.parse_args()

    print(f"Generating {args.count} unique Mythos-themed invite codes...")

    # Generate new codes and store them
    new_codes = await generate_unique_codes(args.count, expires_in_days=args.expires_days)

    if not new_codes:
        print("Failed to generate unique codes (may already exist)")
        return

    print(f"Generated and stored {len(new_codes)} new invite codes in database")

    # Show all generated codes
    print("\nGenerated invite codes:")
    for i, code in enumerate(new_codes, 1):
        print(f"  {i:2d}. {code}")


if __name__ == "__main__":
    run(main)
