---
name: mythosmud-code-quality-ai
description: Apply code quality targets that benefit AI-driven development: docstrings on public API, type hints, naming conventions, no assert in production, complexity targets, __all__ for public modules, client return types. Use when writing or reviewing code for maintainability, improving code for AI tooling, or when the user asks for AI-friendly code quality.
---

# MythosMUD Code Quality Targets for AI

Guidance and checklist to improve code for AI-driven development (agents, code generation, refactors). **Apply as behavioral targets and review criteria only**—do not change linter or formatter config (Ruff, ESLint, mypy, etc.) unless the user explicitly asks for config changes.

## Priority Tiers

- **High**: Docstrings (D), type hints (TCH + policy), naming (N)—apply whenever writing or touching code.
- **Medium**: No assert in production (S101), complexity policy—apply in new code and when refactoring.
- **As you touch**: `__all__` for public modules, client return types on exports—apply when editing those modules or exports.

---

## High Priority

### Docstrings (D)

- **Public modules**: Add a module docstring (at least one line) describing the module’s purpose.
- **Public functions and methods**: Add a short docstring (summary line; Args/Returns if non-obvious).
- **Skip**: Private helpers, tests, `__init__.py` re-exports, unless they are the main entry for a feature.
- **Why**: Gives AI clear intent and contracts so suggestions stay aligned.

### Type hints (TCH + policy)

- **New code and public API**: Add type annotations to parameters and return values. Rely on mypy for correctness; use this as a “presence” target.
- **When touching a file**: Add or fix missing annotations on the functions you change.
- **Why**: Annotated signatures improve AI suggestions, refactors, and catch wrong arguments.

### Naming (N)

- **Classes**: `CapWords`.
- **Functions/methods**: `lowercase_with_underscores`.
- **Arguments and locals**: `lowercase_with_underscores`.
- **Exceptions**: `CapWords` (e.g. `ValidationError`).
- **Why**: Consistent naming reduces wrong names in completions and makes renames/search more reliable.

---

## Medium Priority

### No assert in production (S101)

- **Production/application code**: Do not use `assert` for validation or control flow; use explicit checks and raise or return errors.
- **Tests**: `assert` is fine.
- **Why**: Assert can be stripped with `-O`; AI often suggests assert for validation—prefer explicit error handling.

### Complexity policy

- **Hard limit**: Existing Ruff C901 threshold (complexity ≤ 11) remains; do not add branches that would exceed it.
- **Target for new/refactored code**: Aim for complexity ≤ 7 so functions stay small and single-purpose.
- **When C901 would fire**: Refactor (extract helpers, simplify branches) before adding more logic.
- **Why**: Smaller functions are easier for AI to edit without breaking unrelated behavior.

---

## As You Touch

### `__all__` for public modules

- When editing a **public** package or module that other packages import from, define `__all__` listing the public names.
- **Why**: Declares the stable API so AI (and humans) don’t rely on internal helpers.

### Client return types (TypeScript)

- When adding or editing **exported** functions in the client, add an explicit return type.
- **Why**: Clear contract for the front-end API and better AI suggestions across the client.

---

## Review Checklist

When writing or reviewing code, use this checklist (tick what applies):

**High**

- [ ] Public modules have a module docstring.
- [ ] New or touched public functions/methods have docstrings.
- [ ] New or touched code has type annotations on parameters and return values.
- [ ] Names follow conventions: CapWords (classes, exceptions), lowercase_with_underscores (functions, args, locals).

**Medium**

- [ ] No `assert` used for validation or control flow in production code.
- [ ] New/refactored functions aim for complexity ≤ 7; none exceed the project’s C901 limit.

**As you touch**

- [ ] Public modules that are imported by others define `__all__`.
- [ ] New or touched exported client functions have explicit return types.

---

## Reference

- Project lint/format/mypy config is in [pyproject.toml](../../pyproject.toml) and [.pylintrc](../../.pylintrc); this skill does not require changing them.
- Complexity and lint alignment: [docs/LINTING_COMPLEXITY_ALIGNMENT.md](../../docs/LINTING_COMPLEXITY_ALIGNMENT.md).
