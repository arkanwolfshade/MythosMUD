# conftest mock rationale

> 10 nodes

## Key Concepts

- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **BoundLogger** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Minimal stand-in for BoundLogger: only what log_exception_once touches for these** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Adapt test double to the function param type (structural use only).** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Plain exceptions get _already_logged via __setattr__ fallback; second log is sup** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **LoggedException uses mark_logged(); repeat call does not log again.** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [Spell Validation](Spell_Validation.md) (3 shared connections)
- [player death service](player_death_service.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*