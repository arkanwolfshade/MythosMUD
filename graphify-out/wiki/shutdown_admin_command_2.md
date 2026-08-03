# shutdown admin command

> 23 nodes

## Key Concepts

- **test_emote.py** (13 connections) — `server/tests/unit/models/test_emote.py`
- **Emote** (9 connections) — `server/models/emote.py`
- **test_emote_creation()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_repr()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_with_placeholders()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_alias_creation()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_alias_repr()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_alias_multiple_aliases()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_alias_case_sensitive()** (3 connections) — `server/tests/unit/models/test_emote.py`
- **Base** (2 connections)
- **test_emote_table_name()** (2 connections) — `server/tests/unit/models/test_emote.py`
- **test_emote_alias_table_name()** (2 connections) — `server/tests/unit/models/test_emote.py`
- **Predefined emote definitions.** (1 connections) — `server/models/emote.py`
- **Unit tests for emote models.  Tests the Emote and EmoteAlias SQLAlchemy models.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test Emote can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test Emote has correct table name.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test Emote __repr__ method.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test Emote can have placeholders in messages.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test EmoteAlias can be instantiated with required fields.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test EmoteAlias has correct table name.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test EmoteAlias __repr__ method.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test EmoteAlias can have different aliases for same emote.** (1 connections) — `server/tests/unit/models/test_emote.py`
- **Test EmoteAlias aliases are case sensitive.** (1 connections) — `server/tests/unit/models/test_emote.py`

## Relationships

- [world models rationale](world_models_rationale.md) (10 shared connections)

## Source Files

- `server/models/emote.py`
- `server/tests/unit/models/test_emote.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*