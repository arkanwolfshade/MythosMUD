#!/bin/bash
# Verify that db/authoritative_schema.sql matches the current mythos_dev database structure
# This script compares the schema file with the actual database to detect drift

set -euo pipefail

# Configuration
DB_HOST="${DB_HOST:-localhost}"
DB_USER="${DB_USER:-postgres}"
DB_NAME="${DB_NAME:-mythos_dev}"
SCHEMA_FILE="${SCHEMA_FILE:-db/authoritative_schema.sql}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Verifying schema match between ${SCHEMA_FILE} and ${DB_NAME}...${NC}"

# Check if pg_dump is available
if ! command -v pg_dump &> /dev/null; then
    echo -e "${RED}Error: pg_dump is not installed or not in PATH${NC}"
    exit 1
fi

# Check if schema file exists
if [ ! -f "${SCHEMA_FILE}" ]; then
    echo -e "${RED}Error: Schema file not found: ${SCHEMA_FILE}${NC}"
    echo -e "${YELLOW}Run ./scripts/generate_schema_from_dev.sh to generate it.${NC}"
    exit 1
fi

# Check if database is accessible
if ! PGPASSWORD="${DB_PASSWORD:-}" pg_isready -h "${DB_HOST}" -U "${DB_USER}" -d "${DB_NAME}" &> /dev/null; then
    echo -e "${YELLOW}Warning: Cannot verify database connectivity.${NC}"
    echo -e "${YELLOW}Schema file exists but cannot verify against database.${NC}"
    exit 0
fi

# Generate current schema from database
TEMP_SCHEMA=$(mktemp)
trap "rm -f ${TEMP_SCHEMA}" EXIT

if [ -n "${DB_PASSWORD:-}" ]; then
    export PGPASSWORD="${DB_PASSWORD}"
fi

echo -e "${GREEN}Extracting current schema from database...${NC}"
pg_dump -h "${DB_HOST}" -U "${DB_USER}" -d "${DB_NAME}" \
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
    echo -e "${GREEN}✓ Schema matches! ${SCHEMA_FILE} is up-to-date with ${DB_NAME}${NC}"
    exit 0
else
    echo -e "${RED}✗ Schema drift detected!${NC}"
    echo -e "${YELLOW}The schema file does not match the current database structure.${NC}"
    echo -e "${YELLOW}Run ./scripts/generate_schema_from_dev.sh to regenerate the schema file.${NC}"
    echo ""
    echo -e "${YELLOW}Differences (first 20 lines):${NC}"
    diff -u <(echo "${SCHEMA_CONTENT}") <(echo "${CURRENT_CONTENT}") | head -20 || true
    exit 1
fi
