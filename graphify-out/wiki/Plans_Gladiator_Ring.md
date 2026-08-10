# Plans Gladiator Ring

> 9 nodes

## Key Concepts

- **populate_test_npc_databases.py** (6 connections) — `scripts/populate_test_npc_databases.py`
- **main()** (5 connections) — `scripts/populate_test_npc_databases.py`
- **get_npc_data_from_source()** (4 connections) — `scripts/populate_test_npc_databases.py`
- **populate_database()** (4 connections) — `scripts/populate_test_npc_databases.py`
- **get_npc_database_url()** (3 connections) — `scripts/populate_test_npc_databases.py`
- **Get NPC database URL for the specified environment.      Args:         environme** (1 connections) — `scripts/populate_test_npc_databases.py`
- **Extract NPC data from the source PostgreSQL database.      Args:         source_** (1 connections) — `scripts/populate_test_npc_databases.py`
- **Populate a PostgreSQL database with NPC data.      Args:         target_url: Pos** (1 connections) — `scripts/populate_test_npc_databases.py`
- **Main function to populate test NPC databases.** (1 connections) — `scripts/populate_test_npc_databases.py`

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)

## Source Files

- `scripts/populate_test_npc_databases.py`

## Audit Trail

- EXTRACTED: 24 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*