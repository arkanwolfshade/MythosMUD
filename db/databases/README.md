# Database Provisioning

This directory contains PostgreSQL database creation scripts.

## Active Infrastructure

**Status**: ✅ **ACTIVE** - Used in Docker and CI workflows

## Files

### `databases.sql`

Creates PostgreSQL databases for different environments:
- `mythos_dev` - Development database
- `mythos_unit` - Unit test database
- `mythos_e2e` - End-to-end test database

For each database, the script:
- Creates the database with UTF-8 encoding
- Sets the database owner
- Enables `pgcrypto` extension
- Configures security (revokes public access, grants to app roles)
- Sets timezone to UTC
- Configures default privileges for tables, sequences, and functions

## Usage

This script is executed **after** role creation and **before** schema application:

1. **Dockerfile.github-runner**: Creates databases during image build
2. **GitHub Actions CI**: Creates databases during workflow execution

## Execution Order

The correct order is:
1. `db/roles/roles.sql` - Create roles (users)
2. `db/databases/databases.sql` - Create databases with owners
3. `db/authoritative_schema.sql` - Apply schema
4. `data/db/*.sql` - Load seed data

## Security

- Databases use least-privilege access control
- Public access is revoked
- Only application roles can connect
- Default privileges are configured for future objects
