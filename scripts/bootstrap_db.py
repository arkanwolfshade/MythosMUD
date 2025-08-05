import os
import sqlite3

# Use environment variables for database paths - require it to be set
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable must be set. "
        "See server/env.example for configuration template."
    )

# Extract the file path from the SQLite URL
if DATABASE_URL.startswith("sqlite+aiosqlite:///"):
    DB_PATH = DATABASE_URL.replace("sqlite+aiosqlite:///", "")
else:
    raise ValueError(f"Unsupported database URL format: {DATABASE_URL}")

SCHEMA = """
CREATE TABLE IF NOT EXISTS players (
    id TEXT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    sanity INTEGER,
    occult_knowledge INTEGER,
    fear INTEGER,
    corruption INTEGER,
    cult_affiliation INTEGER,
    current_room_id TEXT,
    created_at TEXT,
    last_active TEXT,
    experience_points INTEGER,
    level INTEGER
);

CREATE TABLE IF NOT EXISTS rooms (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    exits TEXT,
    zone TEXT
);
"""


def main():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(SCHEMA)
        conn.commit()

    print(f"Production database bootstrapped at {DB_PATH}")
    print("Note: Tests use temporary databases created during test execution")


if __name__ == "__main__":
    main()
