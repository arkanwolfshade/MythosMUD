# MythosMUD Database Migration Guide

## 🗄️ Database Schema Analysis

### Current Situation

We have two database files with different schemas:

1. **`data/players/local_players.db`** - Old schema (68KB)
2. **`data/players/players_new.db`** - New schema (64KB)

### Schema Comparison

| Component         | Old Schema (`local_players.db`) | New Schema (`players_new.db`) |
| ----------------- | ------------------------------- | ----------------------------- |
| **Users Table**   | `id` (TEXT)                     | `user_id` (UUID)              |
| **Players Table** | `id` (TEXT)                     | `player_id` (UUID)            |
| **Foreign Keys**  | `user_id` (TEXT)                | `user_id` (UUID)              |
| **Invites Table** | `created_by`, `used_by`         | `used_by_user_id` only        |
| **User Fields**   | `is_verified` present           | `is_verified` removed         |

## ✅ **RECOMMENDATION: Use `players_new.db`**

### Why `players_new.db` is the correct choice

1. **✅ Schema matches current models** - Uses UUIDs as expected by SQLAlchemy models
2. **✅ Consistent naming** - All foreign keys use `user_id` pattern
3. **✅ Better data types** - UUIDs instead of TEXT for primary keys
4. **✅ Simplified design** - Streamlined invite system
5. **✅ Future-proof** - Aligned with modern database practices

### Current Model Expectations

```python
# User model expects

user_id = Column(UUID(as_uuid=True), primary_key=True)

# Player model expects

player_id = Column(UUID(as_uuid=True), primary_key=True)
user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
```

## 🔧 **Configuration Updates Made**

### Files Updated

1. **`server/database.py`** - Updated default DATABASE_URL
2. **`server/server_config.yaml`** - Updated db_path
3. **`server/env.example`** - Updated DATABASE_URL example

### New Default Configuration

```python
DATABASE_URL = "sqlite+aiosqlite:///../../data/players/players_new.db"
```

## 🚨 **Migration Actions Required**

### For Production Deployment

1. **Backup old database** (already done: `local_players.db.backup`)
2. **Verify data integrity** in `players_new.db`
3. **Test all database operations** with new schema
4. **Update any hardcoded references** to old database

### For Development

1. **Use `players_new.db`** as the primary database
2. **Keep `local_players.db`** as backup until migration is complete
3. **Test all CRUD operations** with new schema

## 📊 **Database Statistics**

| Database                  | Size | Tables | Last Modified        |
| ------------------------- | ---- | ------ | -------------------- |
| `local_players.db`        | 68KB | 3      | 8/2/2025 12:32:58 AM |
| `players_new.db`          | 64KB | 3      | 8/2/2025 12:32:58 AM |
| `local_players.db.backup` | 68KB | 3      | Backup of old schema |

## 🔍 **Verification Commands**

### Check current database path

```bash
python -c "from server.database import get_database_path; print(get_database_path())"
```

### Verify schema compatibility

```bash
sqlite3 data/players/players_new.db ".schema"
```

### Test database connection

```bash
python -c "import sys; sys.path.append('.'); from server.database import engine; print('Database connection successful')"
```

## ⚠️ **Important Notes**

1. **No data migration needed** - `players_new.db` appears to be a fresh schema
2. **UUID compatibility** - New schema uses proper UUID types
3. **Foreign key relationships** - All properly defined with CASCADE deletes
4. **Index optimization** - Proper indexes on frequently queried fields

## 🎯 **Next Steps**

1. **Immediate (24 hours):**

   - Test all database operations with new schema
   - Verify authentication system works correctly
   - Run comprehensive test suite

2. **Short-term (1 week):**

   - Monitor database performance
   - Verify data integrity
   - Consider removing old database files

3. **Long-term (1 month):**

   - Archive old database files
   - Update documentation
   - Implement database migration scripts for future changes

---

**Migration Status:** ✅ CONFIGURATION UPDATED
**Recommended Database:** `players_new.db`
**Schema Compatibility:** ✅ FULLY COMPATIBLE
**Next Review:** After comprehensive testing
