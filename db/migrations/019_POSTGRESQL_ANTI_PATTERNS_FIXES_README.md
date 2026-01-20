# Migration 019: PostgreSQL Anti-Patterns Fixes

**Date:** 2025-01-14
**Migration File:** `019_postgresql_anti_patterns_fixes.sql`
**Status:** Ready for testing

## Overview

This migration fixes critical PostgreSQL best practices violations identified in the code review. It converts deprecated patterns to modern PostgreSQL standards and improves code consistency.

## Changes Applied

### 1. Serial to Identity Conversion

Converts all `serial`/`SERIAL` columns to `bigint generated always as identity`:

- `sanity_adjustment_log.id`
- `sanity_exposure_state.id`
- `sanity_cooldowns.id`
- `item_component_states.id`
- `npc_definitions.id`
- `npc_spawn_rules.id`
- `npc_relationships.id`
- `player_spells.id`
- `professions.id` (INTEGER PRIMARY KEY → bigint generated always as identity)

**Why:** `serial` is deprecated. `bigint generated always as identity` is the modern standard and provides better control over ID generation.

### 2. Foreign Key Type Updates

Updates foreign key columns to match new `bigint` primary keys:

- `npc_spawn_rules.npc_definition_id`: integer → bigint
- `npc_relationships.npc_id_1`: integer → bigint
- `npc_relationships.npc_id_2`: integer → bigint
- `players.profession_id`: integer → bigint

**Why:** Foreign keys must match the type of their referenced primary keys.

### 3. Varchar to Text Conversion

Converts unnecessary `varchar(n)` columns to `text`:

- `users.display_name`: varchar(255) → text
- `users.password_hash`: varchar(255) → text
- `sanity_adjustment_log.reason_code`: varchar(64) → text
- `sanity_exposure_state.entity_archetype`: varchar(128) → text
- `sanity_cooldowns.action_code`: varchar(64) → text

**Why:** PostgreSQL best practices recommend `text` over `varchar(n)` unless there's a specific business requirement for length constraints.

**Note:** Some `varchar` columns are kept (e.g., `users.email`, `users.username`, `invites.invite_code`) because they may have business requirements for length limits. These can be converted later if needed.

### 4. Table and Column Comments

Adds descriptive comments to tables and important columns for documentation.

**Why:** Comments improve maintainability and help developers understand schema intent.

### 5. SQL Formatting Standardization

Schema files have been updated to use lowercase SQL keywords consistently.

**Why:** Consistent formatting improves code readability and maintainability.

## Migration Safety

### Idempotent Design

The migration uses conditional checks (`IF EXISTS`, `IF NOT EXISTS`) to ensure it can be run multiple times safely:

```sql
if exists (
    select 1
    from information_schema.columns
    where table_schema = 'public'
    and table_name = 'table_name'
    and column_name = 'column_name'
    and data_type = 'integer'
) then
    -- Perform conversion
end if;
```

### Data Preservation

- Sequence values are preserved during conversion
- Identity columns start from the next value after the current maximum
- No data loss occurs during type conversions

### Rollback Considerations

**Important:** This migration modifies table structures. While it's designed to be safe, consider:

1. **Backup:** Always backup the database before running migrations
2. **Testing:** Test thoroughly in development/staging before production
3. **Downtime:** Some operations may require brief table locks
4. **Application Code:** Ensure application code is compatible with `bigint` types

## Testing Checklist

Before applying to production:

- [ ] Test migration on development database
- [ ] Verify all tables convert correctly
- [ ] Check that foreign key relationships remain intact
- [ ] Verify sequence values are preserved correctly
- [ ] Test application queries with new `bigint` types
- [ ] Verify comments are added correctly
- [ ] Check that varchar→text conversions work as expected
- [ ] Test rollback procedure (if needed)

## Files Modified

### Schema Files (Updated to Match Migration)

- `db/schema/03_identity_and_moderation.sql`
- `db/schema/04_runtime_tables.sql`
- `db/migrations/015_add_magic_system_tables.sql`
- `server/scripts/create_professions_table.sql`

### Migration File

- `db/migrations/019_postgresql_anti_patterns_fixes.sql` (new)

## Application Code Impact

### Python/SQLAlchemy

If using SQLAlchemy models, ensure:

1. **Type Declarations:** Update model definitions to use `BigInteger` instead of `Integer` for affected columns
2. **Foreign Keys:** Update foreign key type declarations to match
3. **Queries:** Test queries that filter by these columns

### Example Model Update

```python
# Before
id = Column(Integer, primary_key=True)

# After
id = Column(BigInteger, primary_key=True)
```

## Post-Migration Steps

1. **Update Schema Files:** Schema files have been updated to match the migration
2. **Update Application Code:** Review and update any hardcoded type assumptions
3. **Update Documentation:** Update any documentation referencing the old types
4. **Monitor:** Watch for any issues in production after deployment

## Related Documentation

- [PostgreSQL Anti-Patterns Review](../docs/POSTGRESQL_ANTI_PATTERNS_REVIEW.md)
- [PostgreSQL Best Practices](../../.cursor/rules/postgresql.mdc)

## Support

If you encounter issues:

1. Check the migration logs for specific errors
2. Verify database version compatibility (PostgreSQL 10+ required for identity columns)
3. Review the migration script comments for detailed explanations
4. Test the conversion function manually if needed

---

**Migration Author:** AI Code Review Agent
**Review Status:** Ready for testing
**Production Ready:** After thorough testing in development/staging
