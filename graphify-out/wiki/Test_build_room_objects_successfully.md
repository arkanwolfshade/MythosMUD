# Test build room objects successfully

> 6 nodes

## Key Concepts

- **.get_stat_requirements()** (5 connections) — `server/models/profession.py`
- **.meets_stat_requirements()** (3 connections) — `server/models/profession.py`
- **.get_requirement_display_text()** (3 connections) — `server/models/profession.py`
- **Get profession stat requirements as dictionary.** (1 connections) — `server/models/profession.py`
- **Check if given stats meet the profession requirements.          Args:** (1 connections) — `server/models/profession.py`
- **Get formatted text for displaying stat requirements.          Returns:** (1 connections) — `server/models/profession.py`

## Relationships

- [Integration tests for the main](Integration_tests_for_the_main.md) (3 shared connections)
- [game](game.md) (1 shared connections)

## Source Files

- `server/models/profession.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*