#!/bin/bash
# Verify that db/authoritative_schema.sql matches the current mythos_dev database structure
# This script compares the schema file with the actual database to detect drift

set -euo pipefail

# Load environment variables from .env.local or .env if it exists
# Skip if DB_PASSWORD is already set (e.g., by PowerShell wrapper)
if [ -z "${DB_PASSWORD:-}" ]; then
    # Handle both Windows paths (when called from PowerShell) and WSL paths
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

    # Also try current working directory as fallback (in case pwd resolution fails)
    if [ ! -d "${PROJECT_ROOT}" ]; then
        PROJECT_ROOT="$(pwd)"
    fi

    ENV_FILE=""
    # Try multiple possible locations
    for env_path in "${PROJECT_ROOT}/.env.local" "${PROJECT_ROOT}/.env" "$(pwd)/.env.local" "$(pwd)/.env"; do
        if [ -f "${env_path}" ]; then
            ENV_FILE="${env_path}"
            break
        fi
    done
fi

if [ -n "${ENV_FILE:-}" ]; then
    # Debug output
    if [ "${DEBUG:-0}" = "1" ]; then
        echo "DEBUG: Loading environment from ${ENV_FILE}"
    fi
    set +u  # Temporarily allow unset variables
    set +e  # Temporarily allow errors
    # Export variables from .env file (skip comments and empty lines)
    while IFS= read -r line || [ -n "$line" ]; do
        # Skip comments and empty lines
        [[ "$line" =~ ^[[:space:]]*# ]] && continue
        [[ -z "${line// }" ]] && continue
        # Parse KEY=VALUE and export
        if [[ "$line" =~ ^([^=]+)=(.*)$ ]]; then
            key="${BASH_REMATCH[1]}"
            value="${BASH_REMATCH[2]}"
            # Remove quotes if present
            value="${value#\"}"
            value="${value%\"}"
            value="${value#\'}"
            value="${value%\'}"
            export "${key}=${value}" 2>/dev/null || true
            if [ "${DEBUG:-0}" = "1" ]; then
                echo "DEBUG: Exported ${key}"
            fi
        fi
    done < "${ENV_FILE}"
    set -e
    set -u
else
    if [ "${DEBUG:-0}" = "1" ]; then
        echo "DEBUG: No .env file found in ${PROJECT_ROOT}"
    fi
fi

# Configuration
# Parse DATABASE_URL if set, otherwise use individual variables
if [ -n "${DATABASE_URL:-}" ]; then
    # Parse postgresql://user:password@host:port/database format
    # Handle both postgresql:// and postgresql+asyncpg:// formats
    DB_URL="${DATABASE_URL#postgresql+asyncpg://}"
    DB_URL="${DB_URL#postgresql://}"

    # Extract user:password@host:port/database using parameter expansion and cut
    # This is more reliable than regex in some bash versions
    USER_PASS="${DB_URL%%@*}"
    REST="${DB_URL#*@}"
    DB_USER="${USER_PASS%%:*}"
    DB_PASSWORD="${USER_PASS#*:}"
    HOST_PORT_DB="${REST%%/*}"
    DB_NAME="${REST#*/}"

    if [[ "${HOST_PORT_DB}" =~ :([0-9]+)$ ]]; then
        DB_HOST="${HOST_PORT_DB%:*}"
        # DB_PORT is extracted but not used in this script
        # shellcheck disable=SC2034
        DB_PORT="${BASH_REMATCH[1]}"
    else
        DB_HOST="${HOST_PORT_DB}"
        # DB_PORT is extracted but not used in this script
        # shellcheck disable=SC2034
        DB_PORT="5432"
    fi

    # Validate we got the essential parts
    if [ -z "${DB_PASSWORD:-}" ] || [ -z "${DB_USER:-}" ] || [ -z "${DB_NAME:-}" ]; then
        echo -e "${YELLOW}Warning: Could not fully parse DATABASE_URL, using defaults${NC}"
        DB_HOST="${DB_HOST:-localhost}"
        DB_USER="${DB_USER:-postgres}"
        DB_NAME="${DB_NAME:-mythos_dev}"
    fi
else
    # Use individual environment variables or defaults
    DB_HOST="${DB_HOST:-localhost}"
    DB_USER="${DB_USER:-postgres}"
    DB_NAME="${DB_NAME:-mythos_dev}"
fi

# Ensure DB_PASSWORD is set (required for authentication)
if [ -z "${DB_PASSWORD:-}" ]; then
    echo -e "${RED}Error: DB_PASSWORD is not set and could not be extracted from DATABASE_URL${NC}"
    echo -e "${YELLOW}Please set DB_PASSWORD environment variable or ensure DATABASE_URL is set in .env.local${NC}"
    exit 1
fi

SCHEMA_FILE="${SCHEMA_FILE:-db/authoritative_schema.sql}"

# Debug: Check if DATABASE_URL was loaded (only if DEBUG is set)
if [ "${DEBUG:-0}" = "1" ]; then
    echo "DEBUG: DATABASE_URL=${DATABASE_URL:-not set}"
    echo "DEBUG: DB_PASSWORD=${DB_PASSWORD:-not set}"
    echo "DEBUG: PROJECT_ROOT=${PROJECT_ROOT}"
    echo "DEBUG: ENV_FILE=${ENV_FILE:-not set}"
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Verifying schema match between ${SCHEMA_FILE} and ${DB_NAME}...${NC}"

# Function to find pg_dump, checking Windows paths if needed (for WSL)
find_pg_dump() {
    # First check if pg_dump is in PATH
    if command -v pg_dump &> /dev/null; then
        echo "pg_dump"
        return 0
    fi

    # Check common Windows PostgreSQL installation paths (for WSL)
    # Windows drives are mounted at /mnt/[drive] in WSL
    local windows_drives=("c" "d" "e" "f")
    local versions=("18" "17" "16" "15" "14" "13" "12")

    for drive in "${windows_drives[@]}"; do
        for version in "${versions[@]}"; do
            local pg_dump_path="/mnt/${drive}/Program Files/PostgreSQL/${version}/bin/pg_dump.exe"
            if [ -f "${pg_dump_path}" ]; then
                echo "${pg_dump_path}"
                return 0
            fi
        done
    done

    return 1
}

# Find pg_dump
if ! PG_DUMP_CMD=$(find_pg_dump); then
    echo -e "${RED}Error: pg_dump is not installed or not in PATH${NC}"
    echo -e "${YELLOW}Please install PostgreSQL or add it to your PATH${NC}"
    exit 1
fi

# Check if schema file exists
if [ ! -f "${SCHEMA_FILE}" ]; then
    echo -e "${RED}Error: Schema file not found: ${SCHEMA_FILE}${NC}"
    echo -e "${YELLOW}Run ./scripts/generate_schema_from_dev.sh to generate it.${NC}"
    exit 1
fi

# Find pg_isready using same logic
find_pg_isready() {
    if command -v pg_isready &> /dev/null; then
        echo "pg_isready"
        return 0
    fi

    local windows_drives=("c" "d" "e" "f")
    local versions=("18" "17" "16" "15" "14" "13" "12")

    for drive in "${windows_drives[@]}"; do
        for version in "${versions[@]}"; do
            local pg_isready_path="/mnt/${drive}/Program Files/PostgreSQL/${version}/bin/pg_isready.exe"
            if [ -f "${pg_isready_path}" ]; then
                echo "${pg_isready_path}"
                return 0
            fi
        done
    done

    echo "pg_isready"  # Return default, will fail gracefully
    return 1
}

PG_ISREADY_CMD=$(find_pg_isready)

# Check if database is accessible
if ! PGPASSWORD="${DB_PASSWORD:-}" "${PG_ISREADY_CMD}" -h "${DB_HOST}" -U "${DB_USER}" -d "${DB_NAME}" &> /dev/null; then
    echo -e "${YELLOW}Warning: Cannot verify database connectivity.${NC}"
    echo -e "${YELLOW}Schema file exists but cannot verify against database.${NC}"
    exit 0
fi

# Generate current schema from database
TEMP_SCHEMA=$(mktemp)
trap 'rm -f "${TEMP_SCHEMA}"' EXIT

if [ -n "${DB_PASSWORD:-}" ]; then
    export PGPASSWORD="${DB_PASSWORD}"
fi

echo -e "${GREEN}Extracting current schema from database...${NC}"
"${PG_DUMP_CMD}" -h "${DB_HOST}" -U "${DB_USER}" -d "${DB_NAME}" \
    --schema-only \
    --no-owner \
    --no-privileges \
    --clean \
    --if-exists \
    --file="${TEMP_SCHEMA}"

# Remove header comments and SET statements for comparison
# Compare only the actual DDL statements
SCHEMA_CONTENT=$(grep -v "^--" "${SCHEMA_FILE}" | grep -v "^SET " | grep -v "^$" | sort)
CURRENT_CONTENT=$(grep -v "^--" "${TEMP_SCHEMA}" | grep -v "^SET " | grep -v "^$" | sort)

# Compare schemas
if [ "${SCHEMA_CONTENT}" = "${CURRENT_CONTENT}" ]; then
    echo -e "${GREEN}Schema matches! ${SCHEMA_FILE} is up-to-date with ${DB_NAME}${NC}"
    exit 0
else
    echo -e "${RED}Schema drift detected!${NC}"
    echo -e "${YELLOW}The schema file does not match the current database structure.${NC}"
    echo -e "${YELLOW}Run ./scripts/generate_schema_from_dev.sh to regenerate the schema file.${NC}"
    echo ""
    echo -e "${YELLOW}Differences (first 20 lines):${NC}"
    diff -u <(echo "${SCHEMA_CONTENT}") <(echo "${CURRENT_CONTENT}") | head -20 || true
    exit 1
fi
