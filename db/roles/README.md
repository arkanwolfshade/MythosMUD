# Database Roles

This directory contains PostgreSQL role (user) creation scripts.

## Active Infrastructure

**Status**: ✅ **ACTIVE** - Used in Docker and CI workflows

## Files

### `roles.sql`

Creates PostgreSQL roles (users) for different environments:
- `mythos_owner_dev` - Database owner for development
- `mythos_app_dev` - Application user for development
- `mythos_owner_unit` - Database owner for unit tests
- `mythos_app_unit` - Application user for unit tests
- `mythos_owner_e2e` - Database owner for E2E tests
- `mythos_app_e2e` - Application user for E2E tests

## Usage

This script is executed **before** database creation and schema application:

1. **Dockerfile.github-runner**: Creates roles before creating databases
2. **GitHub Actions CI**: Creates roles as part of database initialization

## Execution Order

The correct order is:
1. `db/roles/roles.sql` - Create roles (users)
2. `db/databases/databases.sql` - Create databases with owners
3. `db/authoritative_schema.sql` - Apply schema
4. `data/db/*.sql` - Load seed data

## Security

- Roles use least-privilege principles
- Application roles have only necessary permissions
- Owner roles have full access to their respective databases
- No public access granted
