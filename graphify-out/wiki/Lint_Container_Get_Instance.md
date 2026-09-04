# Lint Container Get Instance

> 23 nodes

## Key Concepts

- **lint_container_get_instance.py** (11 connections) — `scripts/lint_container_get_instance.py`
- **scan()** (6 connections) — `scripts/lint_container_get_instance.py`
- **_collect_get_instance_counts()** (5 connections) — `scripts/lint_container_get_instance.py`
- **_find_get_instance_lines()** (5 connections) — `scripts/lint_container_get_instance.py`
- **_code_tokens()** (4 connections) — `scripts/lint_container_get_instance.py`
- **_is_application_container_get_instance()** (4 connections) — `scripts/lint_container_get_instance.py`
- **_allowlist_count_violations()** (3 connections) — `scripts/lint_container_get_instance.py`
- **_collect_python_files()** (3 connections) — `scripts/lint_container_get_instance.py`
- **main()** (3 connections) — `scripts/lint_container_get_instance.py`
- **_stale_allowlist_violations()** (3 connections) — `scripts/lint_container_get_instance.py`
- **AllowlistEntry** (2 connections) — `scripts/lint_container_get_instance.py`
- **TokenInfo** (2 connections)
- **Path** (1 connections)
- **Guard against new `ApplicationContainer.get_instance()` service-location debt…** (1 connections) — `scripts/lint_container_get_instance.py`
- **Tokenize Python source, omitting comments, strings, and whitespace tokens.** (1 connections) — `scripts/lint_container_get_instance.py`
- **True when tokens[index:index+5] is ApplicationContainer.get_instance().** (1 connections) — `scripts/lint_container_get_instance.py`
- **Return 1-based line numbers of real `ApplicationContainer.get_instance()`…** (1 connections) — `scripts/lint_container_get_instance.py`
- **Walk server/*.py and count get_instance() hits per file; collect read errors.** (1 connections) — `scripts/lint_container_get_instance.py`
- **Compare per-file hit counts to allowlist; return violations and confirmed…** (1 connections) — `scripts/lint_container_get_instance.py`
- **Flag allowlist entries whose file no longer contains any get_instance() call.** (1 connections) — `scripts/lint_container_get_instance.py`
- **Scan server/ for ApplicationContainer.get_instance() calls. Returns…** (1 connections) — `scripts/lint_container_get_instance.py`
- **Run the container-injection guard and return 1 if any file's get_instance()…** (1 connections) — `scripts/lint_container_get_instance.py`
- **One file's confirmed get_instance() call-site count, and why it's there.** (1 connections) — `scripts/lint_container_get_instance.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/lint_container_get_instance.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*