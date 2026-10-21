# npcs.sql

> 15 nodes · cohesion 0.18

## Key Concepts

- **test_hallucination_category_ban.py** (9 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **category_violations()** (6 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **_import_violations()** (5 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **test_scanner_flags_each_way_of_choosing_a_category()** (4 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **test_hallucination_module_never_chooses_a_category()** (3 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **parametrize** (2 connections)
- **test_every_hallucination_named_module_is_listed()** (2 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **test_scanner_ignores_ordinary_code()** (2 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **Import** (1 connections)
- **ImportFrom** (1 connections)
- **ADR-024: hallucination code never chooses a message category. A hallucinated…** (1 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **What an import statement pulls in that chooses a message category.** (1 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **What in ``source`` chooses or names a message category: imports of it, or…** (1 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **A new module named for hallucination or phantoms must be added to the audited…** (1 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`
- **Guard the scanner itself so the ban cannot pass vacuously.** (1 connections) — `server/tests/unit/services/test_hallucination_category_ban.py`

## Relationships

- [look_container.py](look_container.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_hallucination_category_ban.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*