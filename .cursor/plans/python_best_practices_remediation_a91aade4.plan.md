---
name: Python Best Practices Remediation
overview: Review and remediate Python code anti-patterns, semantic problems, and bad code practices based on the Python best practices rules document. Focus on missing type hints, import organization, and code quality improvements.
todos:

  - id: "1"

    content: Add missing return type annotations to functions (starting with server/api/monitoring.py:_resolve_connection_manager_from_request)
    status: completed

  - id: "2"

    content: Review imports inside functions - only address those WITHOUT explicit linting suppressions (preserve all
    status: completed

  - id: "3"

    content: Verify all intentional imports inside functions are properly documented with suppression comments
    status: completed

  - id: "4"

    content: Run mypy type checker to verify all type annotations are correct
    status: completed

  - id: "5"

    content: Run test suite to ensure no regressions from changes
    status: completed
---

# Python Best Practices Code Review and Remediation Plan

## Overview

After reviewing the codebase against `.cursor/rules/python.mdc`, several categories of issues were identified that violate Python best practices. This plan addresses the most critical and actionable issues.

## Key Findings

### 1. Missing Return Type Annotations

**Issue**: Some functions are missing return type annotations, violating the rule that "All Function Signatures: Annotate parameters and return types."

**Examples**:

- `server/api/monitoring.py:42` - `_resolve_connection_manager_from_request()` missing return type
- `server/api/metrics.py:388` - `_get_nats_handler()` missing return type (though this may be intentional due to circular imports)

**Action**: Add return type annotations to all functions missing them, prioritizing public APIs and helper functions.

### 2. Imports Inside Functions

**Issue**: PEP 8 recommends imports at the top of the file, grouped properly. However, the codebase has many instances where imports inside functions are explicitly allowed via linting suppressions.

**Important**: The codebase has a pattern of intentionally placing imports inside functions for valid reasons (circular dependency avoidance, lazy loading, environment variable setup). These are marked with `# noqa: E402` or `# pylint: disable=wrong-import-position` with explanatory comments.

**Examples of intentional patterns (DO NOT CHANGE)**:

- `server/tests/conftest.py` - imports after environment variables (explicitly suppressed with `# noqa: E402`)
- `server/container/` (main.py or bundles) - imports after TYPE_CHECKING block (explicitly suppressed with `# pylint: disable=wrong-import-position`)
- Many files with lazy imports inside functions to avoid circular dependencies

**Action**: Only review imports inside functions that are NOT explicitly suppressed. If an import is inside a function with no suppression comment, evaluate if it should be moved to the top (e.g., standard library imports like `import inspect` that don't cause circular dependencies).

### 3. Relative Imports vs Absolute Imports

**Issue**: The codebase extensively uses relative imports (`from ..module`), while the rules prefer absolute imports (`from server.module`).

**Scope**: This is a large-scale change affecting hundreds of files. The codebase currently uses a mix of both patterns.

**Action**: Consider this as a lower-priority refactoring. Focus on new code first, or create a separate task for systematic migration. Relative imports are not incorrect, just not the preferred style per the rules.

### 4. Generic Type Hints

**Issue**: Many functions use bare `dict` instead of more specific types like `dict[str, Any]`.

**Examples**:

- Functions with `command_data: dict` instead of `command_data: dict[str, Any]`
- Functions with `current_user: dict` instead of more specific TypedDict types

**Note**: While `dict` is a valid type hint, the rules encourage more specific types for better type safety and IDE support.

**Action**: This is a lower-priority improvement. Can be addressed incrementally when modifying related code.

## Implementation Strategy

### Phase 1: High Priority - Missing Type Annotations

1. Search for functions missing return type annotations
2. Identify the return types (may require code analysis)
3. Add return type annotations systematically
4. Verify with mypy/type checkers

### Phase 2: Medium Priority - Import Organization

1. Identify imports inside functions that are NOT explicitly suppressed with linting comments
2. **PRESERVE ALL IMPORTS** that have `# noqa: E402` or `# pylint: disable=wrong-import-position` - these are intentional
3. Only evaluate moving imports that have no suppression comments and are clearly misplaced (e.g., standard library imports that don't cause circular dependencies)
4. Verify imports are alphabetically sorted within groups (use `ruff` with `--select I` to check)

### Phase 3: Lower Priority - Code Quality Improvements

1. Consider relative-to-absolute import migration (separate task)
2. Improve generic type hints incrementally
3. Address any other code quality issues found during review

## Files Requiring Immediate Attention

1. **server/api/monitoring.py**

- Add return type to `_resolve_connection_manager_from_request()`

1. **server/events/event_bus.py**

- Move `import inspect` to top of file (line 277)

1. **server/api/metrics.py**

- Review `_get_nats_handler()` for return type (may need to handle circular import differently)

## Testing Considerations

Run mypy type checker after adding type annotations

- Run existing test suite to ensure no regressions
- Verify imports still work correctly after reorganization
- Check for any circular import issues introduced by moving imports

## Notes

Some patterns (like relative imports) are widespread and may require a separate migration effort

- Focus on high-impact, low-risk changes first
- **CRITICAL**: Preserve ALL imports that are explicitly suppressed with linting comments (`# noqa: E402`, `# pylint: disable=wrong-import-position`) - these indicate intentional placement
- The codebase explicitly allows imports inside functions for valid reasons (circular dependencies, lazy loading, environment setup)
- Use tools like `ruff check --select I` to check import sorting without making changes
