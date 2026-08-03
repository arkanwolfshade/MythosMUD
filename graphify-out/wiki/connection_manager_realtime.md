# connection manager realtime

> 12 nodes

## Key Concepts

- **SkillUseLog** (8 connections) — `server/models/skill_use_log.py`
- **test_skill_use_log.py** (6 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **test_skill_use_log_creation()** (3 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **test_skill_use_log_repr()** (3 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **test_skill_use_log_table_name()** (2 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **Base** (1 connections)
- **.__repr__()** (1 connections) — `server/models/skill_use_log.py`
- **One recorded successful use of a skill by a character at a given level.      cha** (1 connections) — `server/models/skill_use_log.py`
- **Unit tests for SkillUseLog ORM model.** (1 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **SkillUseLog can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **SkillUseLog maps to the expected table.** (1 connections) — `server/tests/unit/models/test_skill_use_log.py`
- **SkillUseLog __repr__ includes key identifiers.** (1 connections) — `server/tests/unit/models/test_skill_use_log.py`

## Relationships

- [world models rationale](world_models_rationale.md) (3 shared connections)

## Source Files

- `server/models/skill_use_log.py`
- `server/tests/unit/models/test_skill_use_log.py`

## Audit Trail

- EXTRACTED: 28 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*