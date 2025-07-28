#!/usr/bin/env python3
"""
Generate 100 unique Mythos-themed invite codes for testing.
"""

import json
import random
from pathlib import Path

# Mythos-themed words and concepts for invite codes
MYTHOS_WORDS = [
    "Cthulhu", "Nyarlathotep", "Azathoth", "YogSothoth", "ShubNiggurath",
    "Dagon", "Hastur", "Yig", "Tsathoggua", "Nodens", "Bokrug", "Glaaki",
    "Ithaqua", "AtlachNacha", "Cthugha", "Eihort", "Ghatanothoa", "Hypnos",
    "Lloigor", "Mnomquah", "RhanTegoth", "ShuddeMell", "Tulzscha", "Ycnagnnis",
    "Arkham", "Innsmouth", "Dunwich", "Kingsport", "Miskatonic", "Esoteric",
    "Necronomicon", "Pnakotic", "Rlyeh", "Kadath", "Leng", "Yuggoth", "Xoth",
    "Yaddith", "Zothique", "Hyperborea", "Mu", "Atlantis", "Lemuria",
    "Elder", "Great", "Outer", "Inner", "Deep", "Abyss", "Void", "Chaos",
    "Order", "Cosmos", "Dream", "Nightmare", "Madness", "Sanity", "Truth",
    "Lies", "Knowledge", "Secrets", "Forbidden", "Hidden", "Ancient",
    "Eternal", "Timeless", "Infinite", "Vast", "Profound", "Mysterious",
    "Cryptic", "Arcane", "Occult", "Mystical", "Eldritch", "Unspeakable",
    "Nameless", "Faceless", "Formless", "Shapeless", "Boundless", "Endless",
    "Limitless", "Infinite", "Eternal", "Immortal", "Undying", "Ageless",
    "Primordial", "Prehistoric", "Antediluvian", "Archaic", "Venerable",
    "Sublime", "Transcendent", "Divine", "Infernal", "Celestial", "Abyssal"
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

def main():
    """Generate 100 invite codes and update the invites.json file."""
    print("Generating 100 unique Mythos-themed invite codes...")

    # Generate new codes
    new_codes = generate_unique_codes(100)

    # Load existing invites
    invites_file = Path("server/invites.json")
    if invites_file.exists():
        with open(invites_file, 'r') as f:
            existing_invites = json.load(f)
    else:
        existing_invites = []

    # Get existing codes to avoid duplicates
    existing_codes = {invite["code"] for invite in existing_invites}

    # Filter out any duplicates
    unique_new_codes = [code for code in new_codes if code not in existing_codes]

    # Create new invite entries
    new_invites = [{"code": code, "used": False} for code in unique_new_codes]

    # Combine existing and new invites
    all_invites = existing_invites + new_invites

    # Save updated invites file
    with open(invites_file, 'w') as f:
        json.dump(all_invites, f, indent=2)

    print(f"✓ Generated {len(unique_new_codes)} new invite codes")
    print(f"✓ Total invite codes available: {len(all_invites)}")
    print(f"✓ Used codes: {sum(1 for invite in all_invites if invite['used'])}")
    print(f"✓ Available codes: {sum(1 for invite in all_invites if not invite['used'])}")

    # Show some examples
    print("\nExample invite codes:")
    for i, invite in enumerate(all_invites[-10:], 1):  # Show last 10
        status = "USED" if invite["used"] else "AVAILABLE"
        print(f"  {i:2d}. {invite['code']:<20} [{status}]")

if __name__ == "__main__":
    main()
