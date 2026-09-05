"""
Regression tests for scripts/run_test_ci.py's CI-gating pytest invocation, the CI workflow
steps it depends on, and the other CI-adjacent scripts that shared its now-removed pytest-xdist
dependency (see #668, #724).

run_test_ci.py's coverage-producing logic lives inside a module-level `if IN_CI:` block that
shells out to real pytest/coverage subprocesses -- there is no pure function to call directly
without either executing that side-effecting block (recursive, slow, unsafe in a test run) or
refactoring it into a testable unit (out of scope for this fix). Following this repo's existing
precedent for scripts in this shape (test_run_make_stages.py's Makefile-content assertions),
these tests instead assert on the source text.

pytest-xdist has been removed from the project entirely (#724): its worker restart/shutdown
protocol produced false "worker crashed" reports for workers that exited cleanly (Exit Status:
0, no OS-level fault) -- an unresolved, decade-old upstream xdist/execnet gap with no fix to
adopt. The suite now runs serially everywhere, which also retired the two-run coverage-combine
split this file used to guard (that split existed only because one module crashed xdist
*workers*, not because it was unsafe running in-process -- see #668's original bug for why the
combine step was dangerous, now moot since there is only one coverage-producing run left).
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = PROJECT_ROOT / "scripts" / "run_test_ci.py"
CI_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "ci.yml"
INSTALL_CI_DEPENDENCIES = PROJECT_ROOT / "scripts" / "install_ci_dependencies.sh"
PLAYWRIGHT_INTEGRATION_RUNNER = PROJECT_ROOT / "scripts" / "run_integration_tests_playwright.ps1"


def _script_source() -> str:
    return SCRIPT.read_text(encoding="utf-8")


def _workflow_source() -> str:
    return CI_WORKFLOW.read_text(encoding="utf-8")


def test_run_test_ci_never_passes_an_xdist_worker_count() -> None:
    """pytest-xdist is removed (#724); no invocation in this script may pass -n, which xdist
    itself provides -- once the dependency is gone, that flag is a hard pytest error."""
    source = _script_source()
    assert '"-n",' not in source
    assert "-n auto" not in source
    assert "-n 0" not in source


def test_run_test_ci_no_longer_splits_coverage_into_two_runs() -> None:
    """The Run 1 / Run 2 / `coverage combine` split existed only because one module crashed
    xdist *workers*; with xdist gone there is a single coverage-producing pytest invocation and
    no combine step, so the #668 combine-clobber failure mode (an input sharing combine's own
    default output filename) is structurally unreachable."""
    source = _script_source()
    assert "combine" not in source
    assert "coverage_unit" not in source
    assert "coverage_serial" not in source


def test_run_test_ci_coverage_file_is_the_default() -> None:
    """With only one coverage-producing run, COVERAGE_FILE can safely be the bare default --
    there is no second run's data for it to collide with (see #668's original hazard, now moot)."""
    source = _script_source()
    assert 'env["COVERAGE_FILE"] = coverage_file' in source
    assert 'coverage_file = os.path.join(PROJECT_ROOT, ".coverage")' in source


def test_excessive_warnings_step_no_longer_deselects_the_flaky_module() -> None:
    """test_logging_file_setup.py only ever crashed xdist *workers* (QueueListener/root logger
    teardown in a forked process). With xdist removed the whole suite -- that module included --
    runs in-process, which the issue's own full-tree -n0 measurement already proved clean
    (10,789 passed, 0 failed, no deselect). The deselect is no longer needed."""
    workflow = _workflow_source()
    warnings_step_start = workflow.index("Check for excessive warnings")
    warnings_step_end = workflow.index("Cache benchmark", warnings_step_start)
    step_body = workflow[warnings_step_start:warnings_step_end]
    assert "--deselect" not in step_body
    assert "-n 0" not in step_body
    assert "-n auto" not in step_body


def test_excessive_warnings_step_preserves_the_731_timeout_override() -> None:
    """--override-ini replaces server/pytest.ini's whole addopts string (it does not merge), so
    --timeout=30 --timeout-method=thread must still be listed explicitly here -- its absence
    once let this step hang for 1h45m+ on an unrelated docs-only commit (#731)."""
    workflow = _workflow_source()
    invocation_start = workflow.index("WARNING_OUTPUT=$(uv run pytest")
    invocation_end = workflow.index("\n", invocation_start)
    invocation = workflow[invocation_start:invocation_end]
    assert "--timeout=30" in invocation
    assert "--timeout-method=thread" in invocation


def test_coverage_step_has_pipefail() -> None:
    """ci.yml's 'Run tests with coverage' step pipes through `tee`; without pipefail the step's
    exit code is tee's (always 0), masking a real crash in run_test_ci.py (see #668)."""
    workflow = _workflow_source()
    coverage_step_start = workflow.index("Run tests with coverage")
    coverage_step_end = workflow.index("Upload pytest log", coverage_step_start)
    step_body = workflow[coverage_step_start:coverage_step_end]
    assert "set -o pipefail" in step_body


def test_ci_workflow_does_not_install_pytest_xdist() -> None:
    """pytest-xdist is removed from the project (#724); no CI step should reinstall it out from
    under pyproject.toml. (Comments documenting the removal legitimately mention the name, so
    this checks the actual install invocation, not the whole file.)"""
    workflow = _workflow_source()
    assert 'uv pip install --python .venv-ci/bin/python "pytest-mock>=3.14.0"' in workflow
    assert "pytest-xdist" not in workflow.split("uv pip install")[-1].split("\n")[0]


def test_run_test_ci_does_not_install_pytest_xdist() -> None:
    """Same guarantee as the CI workflow check, for the local Docker branch of this script."""
    source = _script_source()
    assert "uv pip install pytest-mock>=3.14.0 && " in source
    assert "pytest-xdist" not in source.split('"uv pip install')[-1].split('"')[0]


def test_install_ci_dependencies_does_not_install_pytest_xdist() -> None:
    """scripts/install_ci_dependencies.sh is the shared installer Dockerfile.github-runner
    calls; it must not reinstall pytest-xdist out from under pyproject.toml's removal (#724)."""
    source = INSTALL_CI_DEPENDENCIES.read_text(encoding="utf-8")
    assert 'uv pip install --python "$PYTHON_EXE" "pytest-mock>=3.14.0"' in source
    assert "pytest-xdist" not in source


def test_playwright_integration_runner_does_not_pass_xdist_worker_count() -> None:
    """run_integration_tests_playwright.ps1 used to force -n 1 to keep integration tests off
    xdist workers; with xdist removed entirely (#724) that flag is a hard pytest error."""
    source = PLAYWRIGHT_INTEGRATION_RUNNER.read_text(encoding="utf-8")
    assert '"-n",' not in source
    assert "-n 1" not in source
