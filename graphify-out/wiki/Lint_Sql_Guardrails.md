# Lint Sql Guardrails

> 14 nodes · cohesion 0.23

## Key Concepts

- **lint_sql_guardrails.py** (7 connections) — `scripts/lint_sql_guardrails.py`
- **check_select_star()** (6 connections) — `scripts/lint_sql_guardrails.py`
- **check_not_in_subquery()** (5 connections) — `scripts/lint_sql_guardrails.py`
- **main()** (5 connections) — `scripts/lint_sql_guardrails.py`
- **_strip_block_comments()** (4 connections) — `scripts/lint_sql_guardrails.py`
- **_collect_sql_files()** (3 connections) — `scripts/lint_sql_guardrails.py`
- **Path** (3 connections) — `scripts/lint_sql_guardrails.py`
- **_strip_line_comment()** (3 connections) — `scripts/lint_sql_guardrails.py`
- **Lightweight guardrails for hand-maintained PostgreSQL SQL.  Warns on: - select *** (1 connections) — `scripts/lint_sql_guardrails.py`
- **Return line with line comment removed (-- ...).** (1 connections) — `scripts/lint_sql_guardrails.py`
- **Return content with block comments /* ... */ removed (simple, no nested).** (1 connections) — `scripts/lint_sql_guardrails.py`
- **Warn on select * outside comments.** (1 connections) — `scripts/lint_sql_guardrails.py`
- **Warn on 'not in (' when followed by a subquery (select).** (1 connections) — `scripts/lint_sql_guardrails.py`
- **Run SQL guardrail checks and return 1 if any issues found, 0 otherwise.** (1 connections) — `scripts/lint_sql_guardrails.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/lint_sql_guardrails.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
