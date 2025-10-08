import os
import sqlite3
import sys


def get_db_path():
    """Get database path based on environment or command line argument."""
    # Check for command line argument
    if len(sys.argv) > 1:
        db_type = sys.argv[1].lower()
        if db_type == "test":
            return "data/unit_test/players/test_players.db"
        elif db_type == "prod":
            return "data/local/players/local_players.db"
        else:
            print(f"Unknown database type: {db_type}")
            print("Usage: python bootstrap_db.py [prod|test]")
            sys.exit(1)

    # Use environment variable as fallback
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        print("No DATABASE_URL environment variable set and no database type specified.")
        print("Usage: python bootstrap_db.py [prod|test]")
        sys.exit(1)

    # Extract the file path from the SQLite URL
    if DATABASE_URL.startswith("sqlite+aiosqlite:///"):
        return DATABASE_URL.replace("sqlite+aiosqlite:///", "")
    else:
        raise ValueError(f"Unsupported database URL format: {DATABASE_URL}")


def load_schema():
    """Load schema from server/sql/schema.sql file."""
    schema_path = "server/sql/schema.sql"
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    with open(schema_path) as f:
        return f.read()


DB_PATH = get_db_path()
SCHEMA = load_schema()


def main():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    # Remove existing database if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database: {DB_PATH}")

    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(SCHEMA)
        conn.commit()

    print(f"Database bootstrapped successfully at {DB_PATH}")
    print("Schema includes: users, players, invites tables with proper indexes")


if __name__ == "__main__":
    main()
