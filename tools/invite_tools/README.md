# Invite Management Tools

This directory contains tools for managing Mythos-themed invite codes for the MythosMUD project.

## Scripts

### `run_invite_tools.ps1` (Recommended)

PowerShell script that sets up the environment and runs the invite tools. This is the easiest way to use the tools.

**Usage:**

```powershell
# Generate new invite codes
.\tools\invite_tools\run_invite_tools.ps1 generate

# Generate codes using alternative method
.\tools\invite_tools\run_invite_tools.ps1 generate_db

# List all invite codes
.\tools\invite_tools\run_invite_tools.ps1 list

# Show invite statistics
.\tools\invite_tools\run_invite_tools.ps1 count

# Check specific invite code
.\tools\invite_tools\run_invite_tools.ps1 check "Cthulhu"
```

### `generate_invites.py`

Generates Mythos-themed invite codes using the database storage system with FastAPI Users migration structure.

**Usage:**

```bash
# Set environment variable first
$env:DATABASE_URL="sqlite+aiosqlite:///./data/local/players/players.db"
python generate_invites.py
```

**Features:**

- Generates 100 unique Mythos-themed invite codes
- Stores codes in the database with 30-day expiration
- Avoids duplicate codes by checking existing database entries
- Uses Mythos-themed words and concepts for code generation

### `generate_invites_db.py`

Alternative invite generation script using the database storage system.

**Usage:**

```bash
# Set environment variable first
$env:DATABASE_URL="sqlite+aiosqlite:///./data/local/players/players.db"
python generate_invites_db.py
```

**Features:**

- Similar functionality to `generate_invites.py`
- Uses different database connection approach
- Generates 100 unique codes with 30-day expiration

### `check_invites.py`

Utility script to check and list invite codes in the database.

**Usage:**

```bash
# Set environment variable first
$env:DATABASE_URL="sqlite+aiosqlite:///./data/local/players/players.db"

# List all invite codes
python check_invites.py list

# Show invite statistics
python check_invites.py count

# Check specific invite code
python check_invites.py check <invite_code>
```

**Features:**

- List all invite codes with their status (used/unused, expiration)
- Show statistics (total, used, unused, expired counts)
- Check validity of specific invite codes
- Display creation and expiration dates

## Requirements

These scripts require:

- Python 3.8+
- Access to the MythosMUD server database
- Server modules (models, database, config_loader)

## Database Schema

The scripts work with the `invites` table which should contain:

- `invite_code` (TEXT, PRIMARY KEY)
- `used` (BOOLEAN)
- `expires_at` (DATETIME)
- `created_at` (DATETIME)

## Mythos Theme

All generated codes use Mythos-themed words and concepts from:

- Lovecraftian entities (Cthulhu, Nyarlathotep, etc.)
- Mythos locations (Arkham, Innsmouth, R'lyeh, etc.)
- Occult and forbidden knowledge terms
- Cosmic and eldritch concepts

## Notes

- Scripts automatically handle path resolution to find the server directory
- All database operations use async/await patterns
- Codes are generated with expiration dates for security
- Duplicate prevention ensures unique codes across multiple runs
