#!/bin/bash
# MythosMUD PostgreSQL Test Database Setup Script (Linux/CI)
# Creates and initializes the PostgreSQL test database

set -euo pipefail

FORCE="${FORCE:-false}"
VERBOSE="${VERBOSE:-false}"

echo "MythosMUD PostgreSQL Test Database Setup"
echo "========================================="
echo ""

# Load database URL from environment or .env.unit_test
TEST_ENV_PATH="server/tests/.env.unit_test"

if [ -f "$TEST_ENV_PATH" ]; then
    echo "[INFO] Loading configuration from $TEST_ENV_PATH"
    DATABASE_URL=$(grep "^DATABASE_URL=" "$TEST_ENV_PATH" | cut -d'=' -f2- | tr -d '\r\n' | xargs)
else
    DATABASE_URL="${DATABASE_URL:-}"
    if [ -z "$DATABASE_URL" ]; then
        echo "[ERROR] .env.unit_test file not found and DATABASE_URL not set"
        echo "[SOLUTION] Set DATABASE_URL environment variable or create $TEST_ENV_PATH"
        exit 1
    fi
    echo "[INFO] Using DATABASE_URL from environment"
fi

# Parse PostgreSQL URL
if [[ ! "$DATABASE_URL" =~ postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):([0-9]+)/(.+) ]]; then
    echo "[ERROR] Invalid PostgreSQL URL format: $DATABASE_URL"
    exit 1
fi

DB_USER="${BASH_REMATCH[1]}"
DB_PASSWORD="${BASH_REMATCH[2]}"
DB_HOST="${BASH_REMATCH[3]}"
DB_PORT="${BASH_REMATCH[4]}"
DB_NAME="${BASH_REMATCH[5]}"

echo "Database Configuration:"
echo "  Host:     $DB_HOST"
echo "  Port:     $DB_PORT"
echo "  User:     $DB_USER"
echo "  Database: $DB_NAME"
echo ""

# Check if psql is available
if ! command -v psql &> /dev/null; then
    echo "[ERROR] PostgreSQL client (psql) not found"
    echo "[SOLUTION] Install PostgreSQL client: sudo apt-get install postgresql-client"
    exit 1
fi

echo "[INFO] Using psql: $(which psql)"
echo ""

# Set password for psql
export PGPASSWORD="$DB_PASSWORD"

# Check if database exists
echo "Checking if database '$DB_NAME' exists..."
if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -t -c "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME';" 2>/dev/null | grep -q 1; then
    if [ "$FORCE" = "true" ]; then
        echo "[INFO] Database exists. Dropping (Force mode)..."
        psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c "DROP DATABASE $DB_NAME;" 2>&1 || {
            echo "[ERROR] Failed to drop database"
            unset PGPASSWORD
            exit 1
        }
        echo "[OK] Database dropped"
    else
        echo "[OK] Database '$DB_NAME' already exists"
        echo "[INFO] Use FORCE=true to recreate the database"
        unset PGPASSWORD
        exit 0
    fi
fi

# Create database
echo "Creating database '$DB_NAME'..."
if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c "CREATE DATABASE $DB_NAME;" 2>&1; then
    echo "[OK] Database '$DB_NAME' created successfully"
else
    # Check if error is "already exists" (may have been created concurrently)
    if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -t -c "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME';" 2>/dev/null | grep -q 1; then
        echo "[WARNING] Database already exists (may have been created concurrently)"
    else
        echo "[ERROR] Failed to create database"
        unset PGPASSWORD
        exit 1
    fi
fi

# Note: Schema initialization is handled by DDL scripts, not this script
# The database will be initialized when tests run or when DDL scripts are executed
echo ""
echo "[INFO] Database created. Schema will be initialized by DDL scripts or test fixtures."
echo "[INFO] You may need to run database initialization scripts separately."

echo ""
echo "Setup completed successfully! âœ“"
echo "You can now run: scripts/check_postgresql.sh to verify the connection"

unset PGPASSWORD
