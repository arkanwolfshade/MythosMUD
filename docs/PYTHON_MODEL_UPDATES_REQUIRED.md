# Python Model Updates Required for Migration 019

**Date:** 2025-01-14
**Related Migration:** `db/migrations/019_postgresql_anti_patterns_fixes.sql`

## Overview

The database migration changes several column types from `integer`/`serial` to `bigint` and from `varchar(n)` to `text`. These changes must be reflected in the SQLAlchemy models to ensure compatibility.

## Required Changes

### 1. Import BigInteger

All affected model files need to import `BigInteger` from SQLAlchemy:

```python
from sqlalchemy import BigInteger, Integer, ...
```

### 2. Files Requiring Updates

#### `server/models/profession.py`
- **Line 40**: `id = Column(Integer, primary_key=True)` → `id = Column(BigInteger, primary_key=True)`

#### `server/models/npc.py`
- **Line 64**: `id = Column(Integer, primary_key=True, autoincrement=True)` → `id = Column(BigInteger, primary_key=True, autoincrement=True)`
- **Line 171-172**: `npc_definition_id = Column(Integer, ...)` → `npc_definition_id = Column(BigInteger, ...)`
- **Line 168**: `id = Column(Integer, primary_key=True, autoincrement=True)` → `id = Column(BigInteger, primary_key=True, autoincrement=True)` (NPCSpawnRule)
- **Line 301**: `id = Column(Integer, primary_key=True, autoincrement=True)` → `id = Column(BigInteger, primary_key=True, autoincrement=True)` (NPCRelationship)
- **Line 304**: `npc_id_1 = Column(Integer, ...)` → `npc_id_1 = Column(BigInteger, ...)`
- **Line 305**: `npc_id_2 = Column(Integer, ...)` → `npc_id_2 = Column(BigInteger, ...)`

#### `server/models/lucidity.py`
- **Line 63**: `id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)` → `id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)` (LucidityAdjustmentLog)
- **Line 71**: `reason_code: Mapped[str] = mapped_column(String(length=64), ...)` → `reason_code: Mapped[str] = mapped_column(Text(), ...)`
- **Line 88**: `id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)` → `id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)` (LucidityExposureState)
- **Line 95**: `entity_archetype: Mapped[str] = mapped_column(String(length=128), ...)` → `entity_archetype: Mapped[str] = mapped_column(Text(), ...)`
- **Line 111**: `id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)` → `id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)` (LucidityCooldown)
- **Line 118**: `action_code: Mapped[str] = mapped_column(String(length=64), ...)` → `action_code: Mapped[str] = mapped_column(Text(), ...)`

#### `server/models/player.py`
- **Line 110**: `profession_id: Mapped[int] = mapped_column(Integer(), ...)` → `profession_id: Mapped[int] = mapped_column(BigInteger(), ...)`

#### `server/models/player_spells.py`
- **Line 34**: `id = Column(Integer, primary_key=True, autoincrement=True)` → `id = Column(BigInteger, primary_key=True, autoincrement=True)`

## Type Compatibility Notes

### Integer → BigInteger

- **Python Type**: Both map to Python `int`, so no runtime type changes needed
- **SQLAlchemy**: Change `Integer()` to `BigInteger()` in column definitions
- **Type Hints**: `Mapped[int]` remains correct (Python int handles bigint values)

### String(length=n) → Text

- **Python Type**: Both map to Python `str`, so no runtime type changes needed
- **SQLAlchemy**: Change `String(length=n)` to `Text()` in column definitions
- **Type Hints**: `Mapped[str]` remains correct

## Testing Checklist

After making these changes:

- [ ] Run `make lint` to check for any type errors
- [ ] Run database tests to ensure models work correctly
- [ ] Verify that queries using these columns still work
- [ ] Check that foreign key relationships are preserved
- [ ] Test that existing data can be read correctly
- [ ] Verify that new records can be created with the updated types

## Impact Assessment

### Low Risk Changes
- **Integer → BigInteger**: Safe, Python `int` handles both
- **String(length=n) → Text**: Safe, Python `str` handles both

### No Breaking Changes Expected
- Python code using these models should continue to work
- Type hints remain the same (`Mapped[int]`, `Mapped[str]`)
- Only SQLAlchemy column definitions change

## Related Files

- Migration script: `db/migrations/019_postgresql_anti_patterns_fixes.sql`
- Schema files: `db/schema/03_identity_and_moderation.sql`, `db/schema/04_runtime_tables.sql`
- Review document: `docs/POSTGRESQL_ANTI_PATTERNS_REVIEW.md`
