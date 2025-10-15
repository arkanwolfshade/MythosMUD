#!/usr/bin/env python3
"""
Generate unique Mythos-themed invite codes in the SQLite database.

This script creates invite codes directly in the database table
with customizable expiration dates and database paths.

Usage:
    python generate_invites_local.py <db_path> <count> <expiration_date>

Example:
    python generate_invites_local.py data/local/players/local_players.db 100 "2026-12-31"
"""

import random
import sqlite3
import sys
import uuid
from datetime import datetime
from pathlib import Path

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
SUFFIXES = ["2026", "ACCESS", "GATE", "PORTAL", "KEY", "CODE", "PASS", "INITIATE"]


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


def create_invites_in_db(db_path: str, count: int = 100, expires_at_str: str = None) -> None:
    """Create new invites in the database.

    Args:
        db_path: Path to the SQLite database file
        count: Number of invites to generate
        expires_at_str: Expiration date in YYYY-MM-DD format
    """
    print(f"Generating {count} unique Mythos-themed invite codes...")
    print(f"Database: {db_path}")

    # Parse expiration date
    if expires_at_str:
        try:
            expires_at = datetime.strptime(expires_at_str, "%Y-%m-%d")
            print(f"Expiration date: {expires_at.strftime('%B %d, %Y')}")
        except ValueError:
            print(f"[ERROR] Invalid date format: {expires_at_str}. Use YYYY-MM-DD")
            sys.exit(1)
    else:
        # Default to 1 year from now
        from datetime import timedelta

        expires_at = datetime.now() + timedelta(days=365)
        print(f"Expiration date: {expires_at.strftime('%B %d, %Y')} (1 year from now)")

    # Connect to database
    db_path_obj = Path(db_path)
    if not db_path_obj.exists():
        print(f"[ERROR] Database not found at {db_path}")
        print("Please run the database initialization script first.")
        sys.exit(1)

    conn = sqlite3.connect(db_path)

    try:
        # Get existing codes to avoid duplicates
        existing_codes = check_existing_codes(conn)
        print(f"Found {len(existing_codes)} existing invite codes")

        # Generate new codes
        new_codes = generate_unique_codes(count)

        # Filter out any duplicates
        unique_new_codes = [code for code in new_codes if code not in existing_codes]

        if len(unique_new_codes) < count:
            print(f"[WARNING] Could only generate {len(unique_new_codes)} unique codes (requested {count})")

        # Create new invite entries
        invites_created = 0
        cursor = conn.cursor()

        for code in unique_new_codes:
            invite_id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO invites (id, invite_code, used, expires_at, created_at) VALUES (?, ?, ?, ?, ?)",
                (
                    invite_id,
                    code,
                    0,  # SQLite uses 0/1 for boolean
                    expires_at.isoformat(),
                    datetime.now().isoformat(),
                ),
            )
            invites_created += 1

        # Commit to database
        conn.commit()

        print(f"[SUCCESS] Generated {invites_created} new invite codes")

        # Get updated counts
        cursor.execute("SELECT COUNT(*) FROM invites")
        total_invites = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM invites WHERE used = 1")
        used_count = cursor.fetchone()[0]

        available_count = total_invites - used_count

        print(f"[INFO] Total invite codes in database: {total_invites}")
        print(f"[INFO] Used codes: {used_count}")
        print(f"[INFO] Available codes: {available_count}")

        # Show some examples
        print("\nExample invite codes (last 10 created):")
        cursor.execute("SELECT invite_code, used, expires_at FROM invites ORDER BY created_at DESC LIMIT 10")
        for i, (code, used, exp_date) in enumerate(cursor.fetchall(), 1):
            status = "USED" if used else "AVAILABLE"
            exp_formatted = datetime.fromisoformat(exp_date).strftime("%Y-%m-%d")
            print(f"  {i:2d}. {code:<20} [{status}] Expires: {exp_formatted}")

    finally:
        conn.close()


def main():
    """Main function to generate invites."""
    print("=" * 60)
    print("MythosMUD Database Invite Generator")
    print("=" * 60)
    print()

    # Parse command line arguments
    if len(sys.argv) < 4:
        print("Usage: python generate_invites_local.py <db_path> <count> <expiration_date>")
        print()
        print("Arguments:")
        print("  db_path          Path to the SQLite database file")
        print("  count            Number of invites to generate")
        print("  expiration_date  Expiration date in YYYY-MM-DD format")
        print()
        print("Example:")
        print('  python generate_invites_local.py data/local/players/local_players.db 100 "2026-12-31"')
        sys.exit(1)

    db_path = sys.argv[1]
    try:
        count = int(sys.argv[2])
    except ValueError:
        print(f"[ERROR] Invalid count: {sys.argv[2]}. Must be an integer.")
        sys.exit(1)

    expiration_date = sys.argv[3]

    create_invites_in_db(db_path, count, expiration_date)


if __name__ == "__main__":
    main()
