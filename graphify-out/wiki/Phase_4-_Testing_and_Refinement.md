# Phase 4: Testing and Refinement

> 18 nodes

## Key Concepts

- **lint_raw_sql_in_python.py** (9 connections) — `scripts/lint_raw_sql_in_python.py`
- **scan()** (6 connections) — `scripts/lint_raw_sql_in_python.py`
- **_find_raw_sql_lines()** (4 connections) — `scripts/lint_raw_sql_in_python.py`
- **_overdue_message()** (4 connections) — `scripts/lint_raw_sql_in_python.py`
- **_strip_comments()** (4 connections) — `scripts/lint_raw_sql_in_python.py`
- **AllowlistEntry** (3 connections) — `scripts/lint_raw_sql_in_python.py`
- **_collect_python_files()** (3 connections) — `scripts/lint_raw_sql_in_python.py`
- **main()** (3 connections) — `scripts/lint_raw_sql_in_python.py`
- **_strip_line_comment()** (3 connections) — `scripts/lint_raw_sql_in_python.py`
- **Path** (1 connections)
- **Guard against raw table CRUD SQL string literals inside Python source. Replaces…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **Return line with a trailing '# ...' comment removed, so prose mentioning SQL…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **Return content with every '# ...' line comment blanked out, preserving line…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **Return 1-based line numbers containing a raw-SQL violation. Matches against the…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **Format an overdue-allowlist-entry message, as a GitHub Actions annotation in CI…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **Scan server/ for raw SQL. Returns (new_violations, overdue_warnings,…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **Run the raw-SQL guard and return 1 if any file's raw-SQL count doesn't match…** (1 connections) — `scripts/lint_raw_sql_in_python.py`
- **One file's grandfathered raw-SQL debt: expected site count, owning issue,…** (1 connections) — `scripts/lint_raw_sql_in_python.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/lint_raw_sql_in_python.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*