# infrastructure security rationale

> 2 nodes

## Key Concepts

- **test_profession_meets_stat_requirements_all_met()** (3 connections) — `server/tests/unit/models/test_profession.py`
- **Test meets_stat_requirements returns True when all requirements are met.** (1 connections) — `server/tests/unit/models/test_profession.py`

## Relationships

- [models profession available](models_profession_available.md) (1 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/models/test_profession.py`

## Audit Trail

- EXTRACTED: 4 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*