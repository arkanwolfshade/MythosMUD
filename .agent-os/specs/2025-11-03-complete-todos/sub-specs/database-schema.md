# Database Schema

This is the database schema implementation for the spec detailed in @.agent-os/specs/2025-11-03-complete-todos/spec.md

## Schema Changes

### Invite Usage Tracking

**Purpose**: Prevent invite code reuse by tracking usage status

**New Columns for `invites` table**:

```sql
ALTER TABLE invites ADD COLUMN used_at TIMESTAMP NULL;
ALTER TABLE invites ADD COLUMN used_by_user_id INTEGER NULL;
ALTER TABLE invites ADD COLUMN used_by_character_name VARCHAR(50) NULL;

-- Add index for performance
CREATE INDEX idx_invites_used_at ON invites(used_at);
CREATE INDEX idx_invites_used_by_user ON invites(used_by_user_id);
```

**SQLAlchemy Model Updates**:

```python
# In server/models/invite.py (or wherever Invite model is defined)

class Invite(Base):
    # ... existing fields ...

    used_at = Column(DateTime, nullable=True)
    used_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    used_by_character_name = Column(String(50), nullable=True)
```

**Migration Strategy**:

- Existing invites: `used_at = NULL` indicates unused
- Apply via SQLite CLI: `sqlite3 data/players/player_data.db < migration.sql`
- No data loss expected (adding nullable columns)

**Rationale**:

- Prevents invite code sharing and abuse
- Provides audit trail for invite usage
- Supports future invite analytics
- Minimal performance impact (indexed columns)

**Data Integrity Rules**:

- `used_at` must be set atomically with `used_by_user_id`
- Once set, these fields are immutable
- Foreign key ensures referential integrity to users table

### Player Stats Enhancement (Optional Schema Change)

**Purpose**: Support player-specific max_health as explicit field (alternative to JSON stats)

**Note**: This is OPTIONAL - can also use existing stats JSON field

**If implementing as column**:

```sql
-- Option A: Add dedicated column
ALTER TABLE players ADD COLUMN max_health INTEGER DEFAULT 100 NOT NULL;

-- Add check constraint
ALTER TABLE players ADD CONSTRAINT check_max_health_positive CHECK (max_health > 0);
```

**SQLAlchemy Model Updates**:

```python
# In server/models/player.py

class Player(Base):
    # ... existing fields ...

    max_health = Column(Integer, default=100, nullable=False)
```

**Alternative**: Use existing stats JSON field (RECOMMENDED)

```python
# No schema change needed
# Use player.get_stats()["max_health"] with default of 100

stats = player.get_stats()
max_health = stats.get("max_health", 100)
```

**Recommendation**: Use JSON stats field to avoid schema change. This is more flexible for future stat additions and maintains consistency with other dynamic stats.

## No Schema Changes Required For

The following TODOs do not require database schema modifications:

- JWT Secret (configuration only)
- Admin Role Checking (uses existing role system)
- CSRF Validation (in-memory token storage)
- NPC Behavior Methods (uses existing NPC database structure)
- Damage Calculation (computed value, not stored)
- Name Resolution (lookup only, no new data)
- SQL Logging Config (configuration only)
- Death Handling (logic only)
- Teleport Confirmation (session state, not persisted)
- Room JSON Saving (file system, not database)
- Fresh Data Mechanism (cache invalidation, not schema)
- Legacy Pattern Removal (code only)
- Performance Test (test code only)

## Migration Execution Plan

1. **Backup Database**: `cp data/players/player_data.db data/players/player_data.db.backup-$(date +%Y%m%d)`
2. **Apply Invite Tracking Migration**: Execute SQL via sqlite3 CLI
3. **Verify Schema**: Run `sqlite3 data/players/player_data.db ".schema invites"`
4. **Test Migration**: Run unit tests for invite system
5. **Document Changes**: Update database documentation with new columns

## Rollback Plan

If migration fails:

```bash
# Restore backup

cp data/players/player_data.db.backup-YYYYMMDD data/players/player_data.db

# Verify restoration

sqlite3 data/players/player_data.db ".schema invites"
```
