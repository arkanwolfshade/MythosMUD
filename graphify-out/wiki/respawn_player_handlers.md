# respawn player handlers

> 9 nodes

## Key Concepts

- **run_make_stages.py** (5 connections) — `scripts/run_make_stages.py`
- **main()** (5 connections) — `scripts/run_make_stages.py`
- **keep_going_requested()** (3 connections) — `scripts/run_make_stages.py`
- **stage_failed_from_output()** (3 connections) — `scripts/run_make_stages.py`
- **run_stage()** (3 connections) — `scripts/run_make_stages.py`
- **_print_fail()** (2 connections) — `scripts/run_make_stages.py`
- **Return True when Make was invoked with -k / --keep-going.** (1 connections) — `scripts/run_make_stages.py`
- **Return a short failure reason, or None if the stage is OK.** (1 connections) — `scripts/run_make_stages.py`
- **Run `make <stage>`, stream output, return (exit_code, captured_output).** (1 connections) — `scripts/run_make_stages.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/run_make_stages.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*