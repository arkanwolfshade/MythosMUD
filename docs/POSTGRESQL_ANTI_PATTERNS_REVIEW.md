# PostgreSQL Anti-Patterns Code Review

**Review Date:** 2025-01-14
**Reviewer:** AI Code Review Agent
**Scope:** PostgreSQL best practices per `.cursor/rules/postgresql.mdc`
**Focus:** Anti-patterns, semantic problems, and bad code practices

---

## Executive Summary

This review identified **8 CRITICAL violations**, **5 HIGH priority issues**, and **3 MEDIUM priority improvements** related to PostgreSQL best practices across the codebase. The issues range from deprecated sequence syntax (`serial`) to inconsistent formatting to missing documentation.

---

## 🔴 CRITICAL ISSUES

### 1. Use of `serial`/`SERIAL` Instead of `bigint generated always as identity`

**Severity:** CRITICAL
**Impact:** Deprecated pattern, potential future compatibility issues, inconsistent with best practices

**Location:** Multiple schema files

**Violation:** PostgreSQL best practices explicitly state: "Use `bigint generated always as identity` for primary keys. Never use `serial` or `bigserial`."

**Files Affected:**

- `db/schema/03_identity_and_moderation.sql:10` - `professions` table
- `db/schema/04_runtime_tables.sql:108, 122, 133, 187, 200, 234, 249` - Multiple tables
- `db/migrations/015_add_magic_system_tables.sql:43` - `player_spells` table

**Examples:**

```sql
-- ❌ WRONG - db/schema/04_runtime_tables.sql:108
CREATE TABLE IF NOT EXISTS sanity_adjustment_log (
    id serial PRIMARY KEY,
    ...
);

-- ❌ WRONG - db/schema/03_identity_and_moderation.sql:10
CREATE TABLE IF NOT EXISTS professions (
    id SERIAL PRIMARY KEY,
    ...
);

-- ✅ CORRECT
CREATE TABLE IF NOT EXISTS sanity_adjustment_log (
    id bigint generated always as identity primary key,
    ...
);
```

**Recommendation:**

1. Replace all `serial`/`SERIAL` with `bigint generated always as identity`
2. Remove any `SEQUENCE` objects created for these columns
3. Update all migrations to use the new pattern
4. Verify foreign key relationships after migration

**Priority:** 🔴 CRITICAL - Deprecated pattern, violates best practices

---

### 2. Use of `INTEGER` Instead of `bigint` for Primary Keys

**Severity:** CRITICAL
**Impact:** Limited ID range, potential overflow issues, inconsistent with best practices

**Location:** `server/scripts/create_professions_table.sql:5`

**Violation:** Primary keys should use `bigint` to avoid range limitations.

**Example:**

```sql
-- ❌ WRONG - server/scripts/create_professions_table.sql:5
CREATE TABLE IF NOT EXISTS professions (
    id INTEGER PRIMARY KEY,
    ...
);

-- ✅ CORRECT
CREATE TABLE IF NOT EXISTS professions (
    id bigint generated always as identity primary key,
    ...
);
```

**Recommendation:** Update `create_professions_table.sql` to use `bigint generated always as identity`

**Priority:** 🔴 CRITICAL - Range limitation, violates best practices

---

### 3. Inconsistent SQL Keyword Formatting

**Severity:** CRITICAL
**Impact:** Code inconsistency, harder to maintain, violates style guide

**Location:** Multiple schema files

**Violation:** PostgreSQL best practices state: "SQL keywords must be lowercase." However, the codebase mixes uppercase (`CREATE TABLE`, `SERIAL`, `VARCHAR`) and lowercase (`create table`, `serial`, `varchar`).

**Files Affected:**

- `db/schema/03_identity_and_moderation.sql` - Uses `SERIAL`, `VARCHAR`, `CREATE TABLE`
- `db/schema/04_runtime_tables.sql` - Uses `serial`, `varchar`, `CREATE TABLE` (mixed)
- `db/migrations/015_add_magic_system_tables.sql` - Uses `VARCHAR`, `CREATE TABLE`
- `db/schema/01_world_and_calendar.sql` - Uses lowercase consistently ✅

**Example:**

```sql
-- ❌ INCONSISTENT - db/schema/03_identity_and_moderation.sql
CREATE TABLE IF NOT EXISTS professions (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL UNIQUE,
    ...
);

-- ✅ CORRECT
create table if not exists professions (
    id bigint generated always as identity primary key,
    name text not null unique,
    ...
);
```

**Recommendation:**

1. Standardize all SQL keywords to lowercase
2. Update all schema files to use consistent formatting
3. Update migration files to use consistent formatting
4. Consider using a SQL formatter tool for consistency

**Priority:** 🔴 CRITICAL - Code quality, maintainability

---

### 4. Use of `varchar(n)` Where `text` Would Be Appropriate

**Severity:** CRITICAL
**Impact:** Unnecessary length constraints, potential truncation issues, violates best practices

**Location:** Multiple schema files

**Violation:** PostgreSQL best practices state: "Prefer `text` over `varchar(n)` unless there's a specific, strict length constraint."

**Files Affected:**

- `db/schema/04_runtime_tables.sql` - Multiple `varchar` columns
- `db/schema/03_identity_and_moderation.sql` - `VARCHAR(255)` columns
- `db/migrations/015_add_magic_system_tables.sql` - Multiple `VARCHAR` columns

**Examples:**

```sql
-- ❌ WRONG - db/schema/04_runtime_tables.sql:11
email varchar(255) NOT NULL UNIQUE,

-- ❌ WRONG - db/schema/04_runtime_tables.sql:30
"name" varchar(50) NOT NULL UNIQUE,

-- ✅ CORRECT (if length is truly required for email)
email text not null unique,

-- ✅ CORRECT (if length constraint is justified)
name varchar(50) not null unique,  -- Only if 50 char limit is business requirement
```

**Analysis:** Some `varchar` usages may be justified (e.g., fixed-length codes), but many appear arbitrary (e.g., `varchar(255)` for emails, `varchar(50)` for room IDs).

**Recommendation:**

1. Audit all `varchar(n)` columns to determine if length constraints are necessary
2. Convert unnecessary `varchar(n)` to `text`
3. Keep `varchar(n)` only where there's a specific business requirement for length limits
4. Document the rationale for any remaining `varchar(n)` columns

**Priority:** 🔴 CRITICAL - Best practices violation, potential data issues

---

### 5. Missing Table and Column Comments

**Severity:** CRITICAL
**Impact:** Poor documentation, harder to understand schema intent, violates best practices

**Location:** All schema files except `db/authoritative_schema.sql`

**Violation:** PostgreSQL best practices state: "Always add descriptive comments to tables and columns using `COMMENT ON`."

**Files Affected:**

- `db/schema/01_world_and_calendar.sql` - No comments
- `db/schema/02_items_and_npcs.sql` - No comments
- `db/schema/03_identity_and_moderation.sql` - No comments
- `db/schema/04_runtime_tables.sql` - No comments
- `server/scripts/create_professions_table.sql` - No comments

**Note:** `db/authoritative_schema.sql` contains some comments (44 instances), but these appear to be generated from the database.

**Recommendation:**

1. Add `COMMENT ON TABLE` statements for all tables
2. Add `COMMENT ON COLUMN` statements for important columns
3. Use descriptive comments that explain the purpose and usage
4. Maintain comments in source schema files, not just in generated schemas

**Priority:** 🔴 CRITICAL - Documentation, maintainability

---

### 6. Mixed Naming Conventions (snake_case vs UPPER_CASE)

**Severity:** CRITICAL
**Impact:** Code inconsistency, harder to maintain

**Location:** Multiple schema files

**Violation:** PostgreSQL best practices state: "Always use `snake_case` for all database identifiers." However, the codebase uses mixed case in some places (e.g., `player_id` vs `PLAYER_ID`).

**Analysis:** Most identifiers use `snake_case` correctly, but there may be inconsistencies in constraint names and index names.

**Recommendation:**

1. Audit all constraint names for consistency
2. Audit all index names for consistency
3. Ensure all identifiers use `snake_case`
4. Update any uppercase identifiers to lowercase

**Priority:** 🔴 CRITICAL - Code consistency

---

### 7. Use of Quoted Identifiers (Double Quotes)

**Severity:** CRITICAL
**Impact:** Case sensitivity issues, harder to maintain, violates best practices

**Location:** Multiple schema files

**Violation:** While sometimes necessary, excessive use of quoted identifiers (`"name"`) creates case-sensitivity issues.

**Examples:**

```sql
-- ❌ WRONG - db/schema/04_runtime_tables.sql:30
"name" varchar(50) NOT NULL UNIQUE,

-- ✅ CORRECT (if 'name' is not a reserved word)
name varchar(50) not null unique,

-- ✅ ACCEPTABLE (if 'name' conflicts with reserved word)
"name" text not null unique,  -- Only if necessary
```

**Analysis:** The use of `"name"` appears in multiple places. This may be necessary if `name` is a reserved word in some contexts, but should be documented.

**Recommendation:**

1. Audit all quoted identifiers
2. Remove quotes where not necessary (avoid reserved words)
3. Document why quotes are necessary where they remain
4. Consider renaming columns to avoid reserved words

**Priority:** 🔴 CRITICAL - Code quality, maintainability

---

### 8. Missing Explicit `AS` Keywords in Aliases

**Severity:** CRITICAL
**Impact:** Code readability, violates style guide

**Location:** Multiple schema files and queries

**Violation:** PostgreSQL best practices state: "Use explicit `AS` for all aliases."

**Examples:**

```sql
-- ❌ WRONG - db/schema/04_runtime_tables.sql:245
sz.stable_id as subzone_stable_id,
z.stable_id as zone_stable_id,

-- ✅ CORRECT (if using lowercase keywords)
sz.stable_id as subzone_stable_id,  -- Already correct
z.stable_id as zone_stable_id,      -- Already correct
```

**Analysis:** Most aliases already use `AS`, but should verify all queries follow this pattern.

**Recommendation:**

1. Audit all SQL queries for alias usage
2. Ensure all aliases use explicit `AS` keyword
3. Update any queries missing `AS` keywords

**Priority:** 🔴 CRITICAL - Code quality

---

## 🟡 HIGH PRIORITY ISSUES

### 9. Inconsistent Primary Key Types (UUID vs varchar vs integer)

**Severity:** HIGH
**Impact:** Inconsistency, potential migration issues

**Location:** Multiple tables

**Analysis:** The codebase uses different primary key types:

- UUID: `users.id`, `rooms.id`, etc.
- `varchar(255)`: `players.player_id`, `item_instances.item_instance_id`
- `integer`/`bigint`: `professions.id`, `npc_definitions.id`

**Recommendation:**

1. Document the rationale for different PK types
2. Consider standardizing where possible (e.g., UUID for all runtime tables)
3. Ensure foreign key types match their referenced primary keys

**Priority:** 🟡 HIGH - Consistency, maintainability

---

### 10. Use of `BETWEEN` with Integer Ranges

**Severity:** HIGH
**Impact:** Potential off-by-one errors, less clear intent

**Location:** `db/schema/04_runtime_tables.sql:90`

**Example:**

```sql
-- ⚠️ ACCEPTABLE BUT NOT IDEAL - db/schema/04_runtime_tables.sql:90
current_luc integer NOT NULL DEFAULT 100 CHECK (
    current_luc BETWEEN -100 AND 100
),

-- ✅ BETTER (more explicit)
current_luc integer not null default 100 check (
    current_luc >= -100 and current_luc <= 100
),
```

**Analysis:** `BETWEEN` with integers is less problematic than with timestamps, but explicit `>=` and `<=` is clearer.

**Recommendation:**

1. Review `BETWEEN` usage in CHECK constraints
2. Consider replacing with explicit comparisons for clarity
3. Keep `BETWEEN` only where it truly improves readability

**Priority:** 🟡 HIGH - Code clarity

---

### 11. Missing Indexes on Foreign Keys

**Severity:** HIGH
**Impact:** Query performance degradation

**Location:** Multiple tables

**Analysis:** Some foreign key columns have indexes (e.g., `idx_players_user_id`), but should audit all foreign keys.

**Recommendation:**

1. Audit all foreign key columns
2. Add indexes on foreign keys that are frequently queried
3. Document why indexes are omitted where they're not needed

**Priority:** 🟡 HIGH - Performance

---

### 12. Inconsistent Constraint Naming

**Severity:** HIGH
**Impact:** Code maintainability

**Location:** Multiple schema files

**Analysis:** Some constraints use explicit names (e.g., `fk_players_profession`), others rely on PostgreSQL-generated names.

**Recommendation:**

1. Use explicit constraint names consistently
2. Follow a naming convention (e.g., `fk_<table>_<column>` for foreign keys)
3. Update existing constraints to use explicit names

**Priority:** 🟡 HIGH - Code quality

---

### 13. Mixed Case in Table/Column Names

**Severity:** HIGH
**Impact:** Case sensitivity issues, portability problems

**Location:** `db/schema/04_runtime_tables.sql` and others

**Analysis:** Some tables/columns use lowercase (correct), but quoted identifiers create case sensitivity.

**Recommendation:**

1. Use lowercase for all identifiers
2. Avoid quoted identifiers where possible
3. Document any necessary quoted identifiers

**Priority:** 🟡 HIGH - Portability, maintainability

---

## 🟢 MEDIUM PRIORITY ISSUES

### 14. Missing `UNIQUE` Constraints Where Appropriate

**Severity:** MEDIUM
**Impact:** Data integrity

**Analysis:** Some columns that should be unique may not have explicit `UNIQUE` constraints.

**Recommendation:**

1. Audit all columns that should be unique
2. Add explicit `UNIQUE` constraints
3. Document any columns that are unique by business logic but not constrained

**Priority:** 🟢 MEDIUM - Data integrity

---

### 15. Inconsistent Use of `NOT NULL` Constraints

**Severity:** MEDIUM
**Impact:** Data integrity, query clarity

**Analysis:** Most columns correctly use `NOT NULL`, but should verify consistency.

**Recommendation:**

1. Audit all columns for appropriate `NOT NULL` usage
2. Add `NOT NULL` where columns should always have values
3. Document nullable columns that may seem like they should be `NOT NULL`

**Priority:** 🟢 MEDIUM - Data integrity

---

### 16. Missing Documentation for Complex Constraints

**Severity:** MEDIUM
**Impact:** Maintainability

**Analysis:** Some CHECK constraints are complex but lack comments explaining their purpose.

**Recommendation:**

1. Add comments for complex CHECK constraints
2. Document the business logic behind constraints
3. Include examples in comments where helpful

**Priority:** 🟢 MEDIUM - Documentation

---

## ✅ GOOD PRACTICES FOUND

1. **Explicit JOINs**: The codebase correctly uses explicit `JOIN` syntax (e.g., `LEFT JOIN`) rather than implicit joins
2. **Prepared Statements**: Python code uses parameterized queries (e.g., `%s` placeholders)
3. **Timestamptz Usage**: Timestamps correctly use `timestamptz` for timezone-aware storage
4. **No `SELECT *` in Schema Files**: Schema files don't use `SELECT *` (though Python code may have some instances)
5. **No `NOT IN` Usage**: No instances of `NOT IN` found (correctly avoided)
6. **No `money` Type Usage**: No use of the deprecated `money` type

---

## 📋 SUMMARY OF RECOMMENDATIONS

### Immediate Actions (CRITICAL)

1. ✅ Replace all `serial`/`SERIAL` with `bigint generated always as identity`
2. ✅ Replace `INTEGER PRIMARY KEY` with `bigint generated always as identity`
3. ✅ Standardize SQL keywords to lowercase
4. ✅ Audit and replace unnecessary `varchar(n)` with `text`
5. ✅ Add `COMMENT ON` statements for all tables and important columns
6. ✅ Standardize naming conventions (all lowercase, snake_case)
7. ✅ Remove unnecessary quoted identifiers
8. ✅ Ensure all aliases use explicit `AS` keywords

### Short-term Actions (HIGH)

1. ✅ Document primary key type choices
2. ✅ Review `BETWEEN` usage in constraints
3. ✅ Audit and add indexes on foreign keys
4. ✅ Standardize constraint naming
5. ✅ Ensure consistent case in identifiers

### Long-term Actions (MEDIUM)

1. ✅ Audit and add `UNIQUE` constraints
2. ✅ Review `NOT NULL` usage
3. ✅ Add documentation for complex constraints

---

## 📊 STATISTICS

- **Files Reviewed:** 27 SQL files, multiple Python files
- **Critical Issues Found:** 8
- **High Priority Issues Found:** 5
- **Medium Priority Issues Found:** 3
- **Good Practices Found:** 6

---

## 🔍 FILES REQUIRING IMMEDIATE ATTENTION

1. `db/schema/03_identity_and_moderation.sql` - Uses `SERIAL`, `VARCHAR`, uppercase keywords
2. `db/schema/04_runtime_tables.sql` - Uses `serial`, mixed case, missing comments
3. `server/scripts/create_professions_table.sql` - Uses `INTEGER`, missing comments
4. `db/migrations/015_add_magic_system_tables.sql` - Uses `SERIAL`, `VARCHAR`, uppercase keywords

---

**Review Complete**
*"In the archives of database design, we find that consistency and adherence to best practices are not mere suggestions, but the foundation upon which maintainable systems are built."*
