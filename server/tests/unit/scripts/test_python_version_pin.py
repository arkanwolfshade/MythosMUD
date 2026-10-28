"""Guards for the Python version uplift (#748): one pin, derived everywhere else.

`.python-version` is the single source of truth. These tests fail if a tool config, the CI workflows,
or the runner image drift from it (e.g. a stale 3.12 venv cache restored by CI, or a hardcoded
`lib/python3.12/site-packages` path).
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
PYTHON_VERSION_FILE = PROJECT_ROOT / ".python-version"
PYPROJECT = PROJECT_ROOT / "pyproject.toml"
PYRIGHT_CONFIG = PROJECT_ROOT / "pyrightconfig.json"
CI_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "ci.yml"
PR_ISSUE_REFS_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "pr-issue-refs.yml"
RUNNER_DOCKERFILE = PROJECT_ROOT / "Dockerfile.github-runner"
RUN_TEST_CI = PROJECT_ROOT / "scripts" / "run_test_ci.py"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _pinned_version() -> str:
    return _read(PYTHON_VERSION_FILE).strip()


def _pinned_minor() -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.\d+", _pinned_version())
    assert match is not None, f".python-version must be an exact X.Y.Z pin, got {_pinned_version()!r}"
    return int(match.group(1)), int(match.group(2))


def test_python_version_file_is_an_exact_patch_pin() -> None:
    _ = _pinned_minor()


def test_requires_python_floor_matches_the_pin() -> None:
    major, minor = _pinned_minor()
    assert f'requires-python = ">={major}.{minor}"' in _read(PYPROJECT)


def test_tool_target_versions_match_the_pin() -> None:
    major, minor = _pinned_minor()
    pyproject = _read(PYPROJECT)
    assert f'target-version = "py{major}{minor}"' in pyproject  # ruff
    assert f'python_version = "{major}.{minor}"' in pyproject  # mypy
    assert f'pythonVersion = "{major}.{minor}"' in pyproject  # basedpyright
    assert f'"pythonVersion": "{major}.{minor}"' in _read(PYRIGHT_CONFIG)


def test_workflows_read_python_from_the_pin_file_not_a_literal() -> None:
    for workflow in (CI_WORKFLOW, PR_ISSUE_REFS_WORKFLOW):
        source = _read(workflow)
        assert 'python-version-file: ".python-version"' in source, workflow.name
        assert not re.search(r'python-version:\s*"?3\.\d+', source), f"{workflow.name} hardcodes a Python version"


def test_pr_issue_refs_sparse_checkout_includes_the_pin_file() -> None:
    """The workflow sparse-checks-out one script; setup-python cannot read a file that is not on disk."""
    sparse = _read(PR_ISSUE_REFS_WORKFLOW).split("sparse-checkout:", 1)[1].split("sparse-checkout-cone-mode", 1)[0]
    assert ".python-version" in sparse


def test_ci_venv_cache_is_keyed_on_the_interpreter_version() -> None:
    """The install step skips rebuilding any venv that looks valid, so a restored 3.12 `.venv-ci` would
    silently be reused. Both the key and the restore prefix must carry the interpreter version."""
    source = _read(CI_WORKFLOW)
    assert "id: setup-python" in source
    key_lines = [line for line in source.splitlines() if "runner.os }}-" in line and "-uv-" in line]
    assert len(key_lines) == 2, "expected one cache key and one restore-key"
    for line in key_lines:
        assert "steps.setup-python.outputs.python-version" in line, line


def test_ci_fails_when_the_venv_python_differs_from_the_pin() -> None:
    source = _read(CI_WORKFLOW)
    guard = source.split("- name: Verify venv Python matches .python-version", 1)[1].split("- name:", 1)[0]
    assert ".venv-ci/bin/python --version" in guard
    assert ".python-version" in guard
    assert "exit 1" in guard


def test_runner_image_installs_the_pinned_python_via_uv_not_apt() -> None:
    source = _read(RUNNER_DOCKERFILE)
    arg = re.search(r"^ARG PYTHON_VERSION=(\S+)$", source, flags=re.MULTILINE)
    assert arg is not None, "Dockerfile.github-runner must declare ARG PYTHON_VERSION"
    assert arg.group(1) == _pinned_version(), "image Python must match .python-version"
    assert 'uv python install "${PYTHON_VERSION}"' in source
    assert not re.search(r"\bpython3\.\d+\b", source), "Python must not come from apt"


def test_run_test_ci_derives_site_packages_from_the_running_interpreter() -> None:
    source = _read(RUN_TEST_CI)
    assert "python3.12" not in source
    assert "sys.version_info.major" in source and "sys.version_info.minor" in source
    assert source.count('"lib", PY_LIB_DIR, "site-packages"') == 2
