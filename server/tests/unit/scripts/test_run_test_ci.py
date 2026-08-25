"""
Regression tests for scripts/run_test_ci.py's coverage-combine sequence and the CI workflow
steps it depends on (see #668).

run_test_ci.py's coverage-producing logic lives inside a module-level `if IN_CI:` block that
shells out to real pytest/coverage subprocesses -- there is no pure function to call directly
without either executing that side-effecting block (recursive, slow, unsafe in a test run) or
refactoring it into a testable unit (out of scope for this fix). Following this repo's existing
precedent for scripts in this shape (test_run_make_stages.py's Makefile-content assertions),
these tests instead assert on the source text: the specific invariant that regressed is that
`coverage combine`'s two input files must never include the bare ".coverage" (its own default
output filename) -- combine overwrites that path as its output before finishing reading it as
an input, silently discarding whichever run wrote there. See #668 for the reproduced bug.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "run_test_ci.py"
CI_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "ci.yml"


def _script_source() -> str:
    return SCRIPT.read_text(encoding="utf-8")


def test_run1_coverage_file_is_not_the_bare_coverage_filename() -> None:
    """Run 1 (the main suite) must write to a COVERAGE_FILE distinct from the bare ".coverage" --
    that name collides with `coverage combine`'s own default output file (#668)."""
    source = _script_source()
    assert 'env_unit["COVERAGE_FILE"] = coverage_unit' in source
    assert 'coverage_unit = os.path.join(PROJECT_ROOT, ".coverage")' not in source
    assert 'coverage_unit = os.path.join(PROJECT_ROOT, ".coverage.unit")' in source


def test_run1_subprocess_uses_the_dedicated_env() -> None:
    """Run 1's safe_run_static call must pass env=env_unit, not the base env (which would fall
    back to the bare .coverage default COVERAGE_FILE)."""
    source = _script_source()
    run1_start = source.index('"server/tests/",')
    run1_end = source.index("env=env_unit,", run1_start)
    assert run1_end > run1_start, "Run 1's safe_run_static call must be passed env=env_unit"


def test_combine_call_never_targets_the_bare_coverage_file() -> None:
    """The `coverage combine` call's two data-file arguments must be coverage_unit and
    coverage_serial -- never the literal bare ".coverage" path, which is combine's own default
    output filename (see the module docstring / #668)."""
    source = _script_source()
    combine_start = source.index('"combine",')
    combine_args_end = source.index("cwd=PROJECT_ROOT,", combine_start)
    combine_args = source[combine_start:combine_args_end]
    assert "coverage_unit" in combine_args
    assert "coverage_serial" in combine_args
    assert 'os.path.join(PROJECT_ROOT, ".coverage")' not in combine_args


def test_excessive_warnings_step_deselects_the_flaky_xdist_module() -> None:
    """ci.yml's 'Check for excessive warnings' step re-runs the suite under -n auto; without
    deselecting the module run_test_ci.py's own comments document as crashing pytest-xdist
    workers, this step hangs instead of failing fast (observed directly, see #668)."""
    workflow = CI_WORKFLOW.read_text(encoding="utf-8")
    warnings_step_start = workflow.index("Check for excessive warnings")
    warnings_step_end = workflow.index("Cache benchmark", warnings_step_start)
    step_body = workflow[warnings_step_start:warnings_step_end]
    assert "--deselect tests/unit/structured_logging/test_logging_file_setup.py" in step_body


def test_coverage_step_has_pipefail() -> None:
    """ci.yml's 'Run tests with coverage' step pipes through `tee`; without pipefail the step's
    exit code is tee's (always 0), masking a real crash in run_test_ci.py (see #668)."""
    workflow = CI_WORKFLOW.read_text(encoding="utf-8")
    coverage_step_start = workflow.index("Run tests with coverage")
    coverage_step_end = workflow.index("Upload pytest log", coverage_step_start)
    step_body = workflow[coverage_step_start:coverage_step_end]
    assert "set -o pipefail" in step_body
