# Testing

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.

---

## 1. Canonical guide

**[SPEC]**

- Canonical testing documentation: [`docs/TESTING.md`](docs/TESTING.md)
- Daily fast suite from repo root: `make test`
- Full suite: `make test-comprehensive`
- Do not run tests from `/server/`; do not use `python -m pytest` directly

**[NOTE]**
The former root greenfield notes were archived at
`docs/archive/TESTING_GREENFIELD.md` after consolidation into `docs/TESTING.md`.

---

## 2. Changelog

**[SPEC]**
| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | HADS pointer after TESTING consolidation |
