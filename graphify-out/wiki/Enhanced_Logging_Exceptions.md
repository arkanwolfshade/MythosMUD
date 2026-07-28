# Enhanced Logging Exceptions

> 12 nodes · cohesion 0.24

## Key Concepts

- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_StubBoundLogger** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **BoundLogger** (2 connections)
- **Unit tests for enhanced_logging_config helpers.  Covers log_exception_once ded** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Minimal stand-in for BoundLogger: only what log_exception_once touches for these** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Adapt test double to the function param type (structural use only).** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Plain exceptions get _already_logged via __setattr__ fallback; second log is sup** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **LoggedException uses mark_logged(); repeat call does not log again.** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (4 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 40 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*