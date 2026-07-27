# Filter Static Dml

> 9 nodes · cohesion 0.31

## Key Concepts

- **_filter_lines()** (5 connections) — `scripts/filter_static_dml.py`
- **filter_static_dml.py** (4 connections) — `scripts/filter_static_dml.py`
- **main()** (3 connections) — `scripts/filter_static_dml.py`
- **_skip_sequence_set_block()** (3 connections) — `scripts/filter_static_dml.py`
- **_skip_table_data_block()** (3 connections) — `scripts/filter_static_dml.py`
- **Skip a TABLE DATA block (COPY ... \\.). Return index after the block.** (1 connections) — `scripts/filter_static_dml.py`
- **Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after th** (1 connections) — `scripts/filter_static_dml.py`
- **Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences.** (1 connections) — `scripts/filter_static_dml.py`
- **Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back.** (1 connections) — `scripts/filter_static_dml.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/filter_static_dml.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
