---
name: client-test-remediation
description: Systematically fix failing client (React/TypeScript) tests, most-critical first. Use when `make test-client` fails or the user asks to fix client test failures.
disable-model-invocation: true
---

# Client Test Remediation

Fixes failing React/TypeScript test suite runs. Manual-trigger workflow
(`disable-model-invocation: true`) since remediation touches multiple files. Can delegate to the
`test-analyzer` agent for coverage/gap analysis when the failures are widespread rather than a
handful of isolated breaks.

## Entry point

Run `make test-client` from the project root. If it passes, stop; nothing to do.

## Priority

| Tier | Category | Example |
|---|---|---|
| 🔴 Critical | TypeScript compilation errors, JSX syntax errors, missing imports, hook rule violations | build-breaking |
| 🟡 High | Component rendering failures, prop validation errors, context provider issues, query failures | UI broken |
| 🟢 Medium | Hook dependency warnings, async timeouts, mock isolation, type mismatches | flaky/DX |
| 🔵 Low | Coverage below threshold, ESLint warnings, non-critical perf | polish |

## Fix-verify loop

1. `cd client && npx tsc --noEmit --strict` — fix ALL TypeScript errors first, they block
   everything downstream
2. `make test-client` — run the suite
3. `cd client && npm run lint` — confirm no new lint violations
4. Repeat per tier

## Never

- Fix a test by changing the assertion to match broken behavior instead of fixing the behavior
- Use `screen.getByText(...)` when `screen.getByRole(...)` would be more reliable — prefer role
  queries for interactive elements

See [reference.md](reference.md) for fix patterns.
