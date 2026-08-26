# Dead Code Definition and Tooling

**Version 1.1.0** · MythosMUD · 2026-08-26

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
This document describes how MythosMUD defines and manages dead code, and where allowlists live.

## 2. Definition

**[NOTE]**

- **Truly dead**: Code unreachable from application entry points and not referenced by tests or
  tooling. Safe to remove.
- **Unused exports / optional dead**: Symbols exported but never imported (including from tests).
  Treat separately; remove only after confirming they are not public API or reserved for future use.

**[SPEC]**
Code reachable only from its own test file **is** dead by default (ADR-022, decided 2026-08-26).
The prior blanket exemption for test-only code was removed: a module kept alive by tests alone
must carry an explicit comment naming it a stub for future implementation *and* reference a
GitHub Issue tracking that work, or it is removed. This closes the false-negative class where a
component and its test form a closed reachable loop that neither vulture nor knip's default
Vitest-integration flags as unused.

## 3. Entry Points

**[SPEC]**

- **Server:** `server/main.py` → `server/app/factory.py` `create_app` and registered routers/lifespan.
- **Client:** `client/src/main.tsx` → AppRouter → App (and lazy Map/Skills).

## 4. Tooling

**[NOTE]**

- **Server (Python):** [vulture](https://github.com/jendrikseipp/vulture). Config and paths in
  `pyproject.toml` under `[tool.vulture]`. Allowlist file: **`vulture_allowlist.py`** at repo root
  (valid Python that references intentional "unused" names).
- **Client (TypeScript):** [knip](https://github.com/webpro/knip). Run with `npm run knip` in
  `client/`. Config: **`client/knip.json`** (entry, project, ignoreDependencies). The `files` rule
  is `"error"` (was `"off"` until 2026-08-26 — the unused-file check never ran before then).
  Knip's own file-unused report is one-hop only: a module whose sole importer is itself unused
  (e.g. an orphaned component's sibling helper) will not surface without a transitive check. CI's
  `.github/workflows/ci.yml` knip step still carries `continue-on-error: true` pending the ui-v2
  legacy-cluster removals tracked from #637/ADR-022; removing it is that sequence's final step.

## 5. Allowlist / Do Not Remove

**[NOTE]**

- **Server:** Side-effect imports (e.g. router registration, `server/models` re-exports), reserved
  stubs (`combat_service`, `command_parser`), FastAPI `_request` convention. See
  `vulture_allowlist.py` and `pyproject.toml` `[tool.vulture]`.
- **Client:** `_`-prefixed args/vars. Components only used in tests are **not** on this list by
  default as of 2026-08-26 (see §2) — a test-only module needs a stub comment plus a referenced
  GitHub Issue to be kept, entered in `client/knip.json` as needed.

## 6. Reports

**[SPEC]**

Neither of the report files below is committed to the repo, and neither is gitignored — this
section documented a convention that was never practised. Both regenerate on demand instead:

- **Server:** `uv run vulture` from repo root.
- **Client:** `npm run knip` (or `npm run dead-code`, an alias) in `client/`.

## 7. Plan Reference

**[NOTE]**
Full workflow and phases: `.cursor/plans/dead_code_analysis_and_removal_746bc5c1.plan.md`.

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-26 | Test-only code no longer exempt by default (ADR-022); knip `files` rule enabled; removed the never-produced report-file convention. |
