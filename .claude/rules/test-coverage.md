---
paths:
  - "server/tests/**"
  - "client/**/*.test.*"
  - "client/**/*.spec.*"
  - "client/**/__tests__/**"
---

# Test Coverage Requirements

## Minimum Coverage Standard

**All new code must have at least 70% test coverage.**

**Critical files must have at least 90% test coverage.** Critical files include:

- Security-related code (authentication, authorization, data protection)
- Core game features (combat, magic, persistence)
- User-facing functionality (API endpoints, real-time messaging)
- Business logic and critical paths

## Coverage Measurement

- Python: `pytest-cov` (`make test-server-coverage`)
- TypeScript/JavaScript: `vitest --coverage` (`make test-client-coverage`)

## Test Quality Standards

### Forbidden Test Patterns

- Testing Python built-ins or test infrastructure
- Testing mock behavior instead of server code
- Testing test utilities instead of application code
- Only verifying exceptions can be raised without testing actual behavior

### Required Test Patterns

- Tests must call actual server code
- Tests must verify server behavior, not just that exceptions work
- Tests must use mocks to test server code, not to test mocks
- Tests must exercise real code paths that contribute to coverage

See the `mythosmud-test-writing` skill for layout conventions and how to run the test suites.

---

*Ported from `.cursor/rules/test_coverage_requirements.mdc` and `.cursor/rules/testwriting.mdc` (merged; the
latter was a near-duplicate).*
