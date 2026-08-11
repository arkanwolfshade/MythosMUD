# Archive Planning Multiplayer

> 6 nodes

## Key Concepts

- **TestGetSpellRegistry** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_registry_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_registry_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_spell_registry dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_spell_registry returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_spell_registry raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [Player Domain Model](Player_Domain_Model.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*