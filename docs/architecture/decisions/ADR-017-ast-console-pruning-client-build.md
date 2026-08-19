# ADR-017: AST-Based Console Pruning in Client Production Build

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Proposed
**Date:** 2026-03-25
**Provenance:** Recorded by the 2026-08 design/implementation audit. This ADR set was authored after the
systems it describes: the structural architecture documents it draws on predate it by months, and
`DOCUMENTATION_AUDIT.md` records that the design documentation was reverse-engineered with code treated as
the source of truth. Read it as a description of a decision already in force, not a record made at decision
time.

## 2. Context

**[NOTE]**
The client build currently keeps a TODO in `client/vite.userConfig.ts` for console pruning:
regex-based removal was considered but disabled because it can remove important diagnostics. In
practice, we want smaller and quieter production bundles while preserving critical observability.

Specifically:

- Remove low-value console calls in production (`log`, `info`, `debug`, `trace`).
- Preserve incident-relevant output (`warn`, `error`).
- Avoid brittle string/regex transforms that can break valid code paths.

## 3. Decision

**[SPEC]**
Adopt an AST-based production-only transform in the Vite pipeline for console pruning.

The transform will:

- Run only for production builds.
- Remove `console.log`, `console.info`, `console.debug`, and `console.trace`.
- Keep `console.warn` and `console.error` intact.
- Be deterministic and syntax-aware, avoiding regex text replacement.

## 4. Alternatives Considered

**[NOTE]**

1. **Regex replacement in built output**
   Rejected: unsafe and prone to false positives/negatives.
2. **No pruning at all**
   Rejected: keeps avoidable noise and bundle overhead in production.
3. **Minifier-only approach**
   Rejected for now: not explicit enough for allowlist behavior (`warn`/`error` preservation).

## 5. Consequences

**[SPEC]**

- **Positive:** Better production signal-to-noise, smaller output, and safer transformation behavior.
- **Negative:** Adds one more build concern to maintain and test.
- **Neutral:** Development and test behavior remain unchanged.

## 6. Acceptance Criteria

**[SPEC]**

- Production build removes `console.log/info/debug/trace` from app code.
- `console.warn/error` remain present and functional.
- `npm run build` passes with no new runtime regressions.
- TODO in `client/vite.userConfig.ts` is replaced by configured plugin wiring.

## 7. References

**[SPEC]**

- `client/vite.userConfig.ts`
- Existing TODO comments near the `plugins` array in `createViteUserConfig()`

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
