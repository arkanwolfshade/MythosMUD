# Apply Quest Migrations To Dev

> 8 nodes

## Key Concepts

- **main()** (4 connections) — `scripts/apply_quest_migrations_to_dev.py`
- **_run_quest_ddl()** (4 connections) — `scripts/apply_quest_migrations_to_dev.py`
- **_seed_leave_the_tutorial()** (4 connections) — `scripts/apply_quest_migrations_to_dev.py`
- **apply_quest_migrations_to_dev.py** (3 connections) — `scripts/apply_quest_migrations_to_dev.py`
- **cursor** (2 connections)
- **Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial),…** (1 connections) — `scripts/apply_quest_migrations_to_dev.py`
- **Create quest_definitions, quest_instances, quest_offers tables and indexes.** (1 connections) — `scripts/apply_quest_migrations_to_dev.py`
- **Insert leave_the_tutorial quest definition and room offer (idempotent).** (1 connections) — `scripts/apply_quest_migrations_to_dev.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/apply_quest_migrations_to_dev.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*