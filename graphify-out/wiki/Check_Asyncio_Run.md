# Check Asyncio Run

> 10 nodes · cohesion 0.27

## Key Concepts

- **check_file()** (6 connections) — `scripts/check_asyncio_run_guardrails.py`
- **check_asyncio_run_guardrails.py** (4 connections) — `scripts/check_asyncio_run_guardrails.py`
- **main()** (3 connections) — `scripts/check_asyncio_run_guardrails.py`
- **_strip_string_literals()** (3 connections) — `scripts/check_asyncio_run_guardrails.py`
- **_strip_triple_quoted_blocks()** (3 connections) — `scripts/check_asyncio_run_guardrails.py`
- **Path** (1 connections) — `scripts/check_asyncio_run_guardrails.py`
- **Remove triple-quoted string blocks from file content.** (1 connections) — `scripts/check_asyncio_run_guardrails.py`
- **Remove string literals from line to avoid false positives inside docs/strings.** (1 connections) — `scripts/check_asyncio_run_guardrails.py`
- **Return list of (line_no, line) where asyncio.run( appears in code.** (1 connections) — `scripts/check_asyncio_run_guardrails.py`
- **Return 0 if no asyncio.run( in server/, else 1.** (1 connections) — `scripts/check_asyncio_run_guardrails.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/check_asyncio_run_guardrails.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
