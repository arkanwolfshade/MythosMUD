# Test Run Test Ci

> 17 nodes

## Key Concepts

- **test_run_test_ci.py** (9 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **_script_source()** (5 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_combine_call_never_targets_the_bare_coverage_file()** (3 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_run1_coverage_file_is_not_the_bare_coverage_filename()** (3 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_run1_subprocess_uses_the_dedicated_env()** (3 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_run1_uses_serial_execution()** (3 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_coverage_step_has_pipefail()** (2 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_excessive_warnings_step_deselects_the_flaky_xdist_module()** (2 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **test_excessive_warnings_step_uses_serial_execution()** (2 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **Regression tests for scripts/run_test_ci.py's coverage-combine sequence and the…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **Run 1 (the main suite) must write to a COVERAGE_FILE distinct from the bare…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **Run 1's safe_run_static call must pass env=env_unit, not the base env (which…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **The `coverage combine` call's two data-file arguments must be coverage_unit and…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **ci.yml's 'Check for excessive warnings' step re-runs the suite under -n auto;…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **ci.yml's 'Run tests with coverage' step pipes through `tee`; without pipefail…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **Run 1 must pass -n 0, overriding server/pytest.ini's default -n auto. pytest-…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`
- **ci.yml's 'Check for excessive warnings' step is CI-gating (a real crash now…** (1 connections) — `server/tests/unit/scripts/test_run_test_ci.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/tests/unit/scripts/test_run_test_ci.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*