#!/bin/bash
# MythosMUD PostgreSQL Connection Diagnostic Script (Linux/CI)
# Checks PostgreSQL connectivity and configuration for tests

set -euo pipefail

VERBOSE="${VERBOSE:-false}"
DATABASE_URL="${DATABASE_URL:-}"

echo "MythosMUD PostgreSQL Diagnostic"
echo "==============================="
echo ""

# Load database URL from .env.unit_test if not provided
if [ -z "$DATABASE_URL" ]; then
    TEST_ENV_PATH="server/tests/.env.unit_test"

    if [ -f "$TEST_ENV_PATH" ]; then
        echo "[INFO] Loading DATABASE_URL from $TEST_ENV_PATH"
        DATABASE_URL=$(grep "^DATABASE_URL=" "$TEST_ENV_PATH" | cut -d'=' -f2- | tr -d '\r\n' | xargs)
    else
        # Try environment variable from CI/Docker
        if [ -n "${DATABASE_URL:-}" ]; then
            echo "[INFO] Using DATABASE_URL from environment"
        else
            echo "[ERROR] DATABASE_URL not found in .env.unit_test or environment"
            echo "[SOLUTION] Set DATABASE_URL environment variable or create $TEST_ENV_PATH"
            exit 1
        fi
    fi
fi

# Parse PostgreSQL URL
# Format: postgresql+asyncpg://user:password@host:port/database
if [[ ! "$DATABASE_URL" =~ postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):([0-9]+)/(.+) ]]; then
    echo "[ERROR] Invalid PostgreSQL URL format: $DATABASE_URL"
    echo "[EXPECTED] postgresql+asyncpg://user:password@host:port/database"
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
echo "  Password: [REDACTED]"
echo ""

# Check if psql is available
if ! command -v psql &> /dev/null; then
    echo "[ERROR] psql command not found"
    echo "[SOLUTION] Install PostgreSQL client: sudo apt-get install postgresql-client"
    exit 1
fi

echo "[INFO] Using psql: $(which psql)"
echo ""

# Test 1: Check if PostgreSQL service is running
echo "Test 1: Checking PostgreSQL service status..."
if systemctl is-active --quiet postgresql 2>/dev/null || pg_isready -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" &>/dev/null; then
    echo "  [OK] PostgreSQL service is running"
else
    echo "  [WARNING] Could not verify PostgreSQL service status"
    echo "  [INFO] Attempting to connect anyway..."
fi

# Test 2: Check network connectivity
echo "Test 2: Checking network connectivity to $DB_HOST:$DB_PORT..."
if timeout 3 bash -c "echo > /dev/tcp/$DB_HOST/$DB_PORT" 2>/dev/null; then
    echo "  [OK] Can connect to PostgreSQL server"
else
    echo "  [ERROR] Cannot connect to PostgreSQL server"
    echo "  [SOLUTION] Ensure PostgreSQL is running and listening on $DB_HOST:$DB_PORT"
    exit 1
fi

# Test 3: Check authentication
echo "Test 3: Checking authentication..."
export PGPASSWORD="$DB_PASSWORD"
if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c "SELECT version();" &>/dev/null; then
    echo "  [OK] Authentication successful"
    if [ "$VERBOSE" = "true" ]; then
        psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -c "SELECT version();" 2>/dev/null | head -1
    fi
else
    echo "  [ERROR] Authentication failed"
    echo "  [SOLUTION] Check PostgreSQL password for user '$DB_USER'"
    echo "    You may need to reset the password:"
    echo "    psql -U postgres -c \"ALTER USER $DB_USER WITH PASSWORD '$DB_PASSWORD';\""
    unset PGPASSWORD
    exit 1
fi
unset PGPASSWORD

# Test 4: Check if database exists
echo "Test 4: Checking if database '$DB_NAME' exists..."
export PGPASSWORD="$DB_PASSWORD"
if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d postgres -t -c "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME';" 2>/dev/null | grep -q 1; then
    echo "  [OK] Database '$DB_NAME' exists"
else
    echo "  [WARNING] Database '$DB_NAME' does not exist"
    echo "  [SOLUTION] Create the database:"
    echo "    psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d postgres -c \"CREATE DATABASE $DB_NAME;\""
    echo "  Or run: scripts/setup_postgresql_test_db.sh"
fi
unset PGPASSWORD

# Test 5: Check database connection
echo "Test 5: Testing connection to database '$DB_NAME'..."
export PGPASSWORD="$DB_PASSWORD"
if psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -c "SELECT 1;" &>/dev/null; then
    echo "  [OK] Can connect to database '$DB_NAME'"
else
    echo "  [ERROR] Cannot connect to database '$DB_NAME'"
    echo "  [SOLUTION] Ensure database exists and user has permissions"
    unset PGPASSWORD
    exit 1
fi
unset PGPASSWORD

echo ""
echo "All diagnostic tests passed! âœ“"
echo "PostgreSQL is properly configured for tests."
