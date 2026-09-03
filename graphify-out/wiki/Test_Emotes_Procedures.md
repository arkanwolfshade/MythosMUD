# Test Emotes Procedures

> 10 nodes

## Key Concepts

- **emote_row()** (6 connections) — `server/tests/integration/test_emotes_procedures.py`
- **test_emotes_procedures.py** (6 connections) — `server/tests/integration/test_emotes_procedures.py`
- **test_get_emote_aliases_joins_owning_emote()** (5 connections) — `server/tests/integration/test_emotes_procedures.py`
- **test_get_emotes_includes_the_new_row()** (5 connections) — `server/tests/integration/test_emotes_procedures.py`
- **async_sessionmaker** (3 connections)
- **AsyncSession** (3 connections)
- **asyncio** (2 connections)
- **fixture** (1 connections)
- **Integration tests for db/procedures/emotes.sql (#633). Replace raw SQL…** (1 connections) — `server/tests/integration/test_emotes_procedures.py`
- **Create one emote with one alias. Yields (stable_id, alias).** (1 connections) — `server/tests/integration/test_emotes_procedures.py`

## Relationships

- [Init](Init.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (1 shared connections)

## Source Files

- `server/tests/integration/test_emotes_procedures.py`

## Audit Trail

- EXTRACTED: 16 (84%)
- INFERRED: 3 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*