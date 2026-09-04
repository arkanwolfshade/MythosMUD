# Logging best practices (pointer)

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.

---

## 1. Canonical guide

**[SPEC]**

- Canonical logging guide: [`ENHANCED_LOGGING_GUIDE.md`](ENHANCED_LOGGING_GUIDE.md)
- Import: `from server.structured_logging.enhanced_logging_config import get_logger`
- Prefer structured key-value logging; never f-string log messages

**[NOTE]**
Former `LOGGING_BEST_PRACTICES.md` content is under `archive/LOGGING_BEST_PRACTICES.md`.

---

## 2. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | HADS pointer after logging consolidation |
