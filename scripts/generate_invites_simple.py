#!/usr/bin/env python3
"""
Generate 100 unique Mythos-themed invite codes in the SQLite database.

This script creates invite codes directly in the database table
instead of the JSON file, which is the correct approach for
the MythosMUD authentication system.
"""

import random
import sqlite3
import uuid
from datetime import datetime, timedelta
from pathlib import Path

# Mythos-themed words and concepts for invite codes
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
    "Immortal", "Undying", "Ageless", "Primordial", "Prehistoric", "Antediluvian",
    "Archaic", "Venerable", "Sublime", "Transcendent", "Divine", "Infernal",
    "Celestial", "Abyssal",
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


def generate_unique_codes(count: int = 100) -> list[str]:
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


def check_existing_codes(conn: sqlite3.Connection) -> set[str]:
    """Get all existing invite codes from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT invite_code FROM invites")
    return {row[0] for row in cursor.fetchall()}


def create_invites_in_db(count: int = 100) -> None:
    """Create new invites in the database."""
    print(f"Generating {count} unique Mythos-themed invite codes in database...")

    # Connect to database
    db_path = Path("data/players/players.db")
    if not db_path.exists():
        print(f"❌ Database not found at {db_path}")
        print("Please run the database initialization script first.")
        return

    conn = sqlite3.connect(db_path)

    try:
        # Get existing codes to avoid duplicates
        existing_codes = check_existing_codes(conn)
        print(f"Found {len(existing_codes)} existing invite codes")

        # Generate new codes
        new_codes = generate_unique_codes(count)

        # Filter out any duplicates
        unique_new_codes = [
            code for code in new_codes if code not in existing_codes
        ]

        # Create new invite entries
        invites_created = 0
        expires_at = datetime.utcnow() + timedelta(days=365)  # 1 year expiration

        cursor = conn.cursor()
        for code in unique_new_codes:
            invite_id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO invites (id, invite_code, is_used, expires_at, created_at) VALUES (?, ?, ?, ?, ?)",
                (invite_id, code, False, expires_at.isoformat(), datetime.utcnow().isoformat())
            )
            invites_created += 1

        # Commit to database
        conn.commit()

        print(f"✓ Generated {invites_created} new invite codes")

        # Get updated counts
        cursor.execute("SELECT COUNT(*) FROM invites")
        total_invites = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM invites WHERE is_used = 1")
        used_count = cursor.fetchone()[0]

        available_count = total_invites - used_count

        print(f"✓ Total invite codes available: {total_invites}")
        print(f"✓ Used codes: {used_count}")
        print(f"✓ Available codes: {available_count}")

        # Show some examples
        print("\nExample invite codes:")
        cursor.execute("SELECT invite_code, is_used FROM invites ORDER BY created_at DESC LIMIT 10")
        for i, (code, is_used) in enumerate(cursor.fetchall(), 1):
            status = "USED" if is_used else "AVAILABLE"
            print(f"  {i:2d}. {code:<20} [{status}]")

    finally:
        conn.close()


def main():
    """Main function to generate invites."""
    print("MythosMUD Database Invite Generator")
    print("=" * 40)

    create_invites_in_db(100)


if __name__ == "__main__":
    main()
