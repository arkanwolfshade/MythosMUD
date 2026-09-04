---
name: Click Best-Practices Remediation
overview: Analyze the MythosMUD codebase against .cursor/rules/click.mdc and fix anti-patterns, semantic
  bugs (test/API mismatch), type hints, and structural/packaging improvements in the room validator CLI.
todos:
  - id: fix-json-test-reporter
    content: "test_reporter.py: replace parsed[\"summary\"] with parsed[\"stats\"] in assert and all
      parsed[\"summary\"][...] (lines ~79-87)"
    status: pending
  - id: fix-json-test-integration
    content: "test_validator_integration.py: replace parsed[\"summary\"] with parsed[\"stats\"] in
      test_reporter_integration (line ~147) and test_full_validation_pipeline (lines ~231, 234, 235)"
    status: pending
  - id: reporter-format-error-type
    content: "reporter.py: change format_error(..., suggestion: str = None) to suggestion: str | None
      = None"
    status: pending
  - id: reporter-return-types
    content: "reporter.py: add -> None to print_bidirectional_errors and print_parsing_errors"
    status: pending
  - id: reporter-generate-json-types
    content: "reporter.py: type generate_json_output params as dict[str, Any], list[dict[str, Any]];
      add typing.Any import if missing"
    status: pending
  - id: colorize-docstring
    content: "reporter.py: add docstring to colorize_output stating legacy/programmatic use; prefer
      click.secho for new code"
    status: pending
  - id: room-loader-import
    content: "room_loader.py: move 'import click' from inside build_room_database() to top of file
      with other imports"
    status: pending
  - id: structure-note-validator
    content: "validator.py: extend module docstring (or add comment after it) that CLI is
      single-command by design; refactor to cli group + commands/ package when subcommands added"
    status: pending
  - id: structure-note-readme
    content: "tools/room_toolkit/room_validator/: add or update README with one paragraph on
      single-command layout and future group/commands refactor if subcommands are added"
    status: pending
  - id: pyproject-scripts-section
    content: "pyproject.toml: add [project.scripts] section if missing"
    status: pending
  - id: pyproject-room-validator-entry
    content: "pyproject.toml: add room-validator = '<module.path>:main' entry; confirm module path
      (e.g. tools.room_toolkit.room_validator.validator or equivalent for install)"
    status: pending
  - id: verify-tests-and-lint
    content: "Run room validator tests and lint (ruff/mypy) after all edits; fix any regressions"
    status: pending
isProject: false
---

# Click Best-Practices Remediation Plan

## Scope

Click is used only in the **room validator** tool under [tools/room_toolkit/room_validator/](tools/room_toolkit/room_validator/). No other CLIs use click in the project. This plan addresses that tool and its tests.

---

## Findings and Remediation

### 1. Semantic bug: Tests expect wrong JSON key ("summary" vs "stats")

**Rule:** Tests must assert against the actual API contract.

**Current:** [core/reporter.py](tools/room_toolkit/room_validator/core/reporter.py) `generate_json_output()` returns
`{"stats": stats, "errors": errors, "warnings": warnings}`.

**Bug:** [tests/test_reporter.py](tools/room_toolkit/room_validator/tests/test_reporter.py) and
[tests/test_validator_integration.py](tools/room_toolkit/room_validator/tests/test_validator_integration.py)
assert `parsed["summary"]`, which does not exist. The correct key is `parsed["stats"]`.

**Action:** In both test files, replace every `parsed["summary"]` with `parsed["stats"]`.

**Files:** test_reporter.py, test_validator_integration.py.

---

### 2. Type hints in Reporter (Rule 4)

**Current:** `format_error(..., suggestion: str = None)`; missing return types on
`print_bidirectional_errors` and `print_parsing_errors`; bare `dict` in `generate_json_output`.

**Action:** Use `suggestion: str | None = None`; add `-> None` to the two print methods; optionally
use `dict[str, Any]` / `list[dict[str, Any]]` in `generate_json_output`.

**File:** [tools/room_toolkit/room_validator/core/reporter.py](tools/room_toolkit/room_validator/core/reporter.py).

---

### 3. Manual ANSI codes in Reporter (Rule 3)

**Current:** `colorize_output()` uses raw ANSI. Rest of Reporter uses `click.secho`; `colorize_output`
is only used in unit tests.

**Action:** Add a one-line docstring that it is legacy/programmatic use and that new code should use
click.secho.

**File:** [tools/room_toolkit/room_validator/core/reporter.py](tools/room_toolkit/room_validator/core/reporter.py).

---

### 4. Lazy import of click in room_loader

**Current:** [core/room_loader.py](tools/room_toolkit/room_validator/core/room_loader.py) does
`import click` inside `build_room_database()`.

**Action:** Move `import click` to the top of the file.

**File:** [tools/room_toolkit/room_validator/core/room_loader.py](tools/room_toolkit/room_validator/core/room_loader.py).

---

### 5. Code organization (Rule 1)

**Rule:** Use click.Group and command modules for non-trivial CLIs; document layout when
single-command is intentional.

**Current:** [validator.py](tools/room_toolkit/room_validator/validator.py) is a single ~400-line
file with one `@click.command()` and private helpers. No subcommands.

**Action:** Add a short note (in validator.py module docstring or in a README under
tools/room_toolkit/room_validator/) stating that the CLI is intentionally a single-command tool
and that if subcommands are added later (e.g. validate, report, fix), the layout will be refactored
to a `cli` group and a `commands/` package (e.g. `commands/validate.py`) with `cli.add_command(...)`.
No structural change required until subcommands exist.

**Files:** [tools/room_toolkit/room_validator/validator.py](tools/room_toolkit/room_validator/validator.py)
and/or README in that directory.

---

### 6. Packaging / entry point (Rule 6)

**Rule:** "Distribute your CLI tools reliably using pyproject.toml for metadata and entry points."

**Current:** Room validator is run as `python validator.py` from its directory. pyproject.toml has no
script entry for the room validator.

**Action:** Add a [project.scripts] entry in [pyproject.toml](pyproject.toml) so the validator can be
invoked as an installed command (e.g. `room-validator --base-path ./data/local/rooms`). Use the
correct callable path for the project layout (e.g. if the package is installed as mythosmud, the
entry might be `room-validator = "tools.room_toolkit.room_validator.validator:main"` or a path
that matches how the repo is run; confirm the installable package structure and adjust the
module path so `room-validator` resolves to the validator's `main`).

**File:** [pyproject.toml](pyproject.toml).

---

### 7. Already compliant

- Arguments vs options: only options; no optional positional misuse.
- Output: no `print()`; click.echo / click.secho throughout.
- Help text: main() has docstring and Examples; options have help=.
- Testing: CliRunner used; tests will align with API once JSON key is fixed.

---

## Detailed Todos (implementation order)

1. **test_reporter.py:** Replace every `parsed["summary"]` with `parsed["stats"]` (assert and
   `parsed["summary"][key]` usages around lines 79-87).
2. **test_validator_integration.py:** Replace `parsed["summary"]` with `parsed["stats"]` in
   test_reporter_integration (~line 147) and test_full_validation_pipeline (~lines 231, 234, 235).
3. **reporter.py:** In `format_error`, change `suggestion: str = None` to `suggestion: str | None =
   None`.
4. **reporter.py:** Add `-> None` return type to `print_bidirectional_errors` and
   `print_parsing_errors`.
5. **reporter.py:** In `generate_json_output`, use `stats: dict[str, Any]`, `errors: list[dict[str,
   Any]]`, `warnings: list[dict[str, Any]]`; add `from typing import Any` if missing.
6. **reporter.py:** Add docstring to `colorize_output` stating it is legacy/programmatic use and
   new code should use click.secho.
7. **room_loader.py:** Move `import click` from inside `build_room_database()` to the top of the
   file with other imports.
8. **validator.py:** Extend module docstring (or add a short comment) that the CLI is
   single-command by design and will be refactored to a cli group and commands/ package when
   subcommands are added.
9. **tools/room_toolkit/room_validator/:** Add or update README with one paragraph documenting
   single-command layout and future group/commands refactor if subcommands are added.
10. **pyproject.toml:** Add `[project.scripts]` section if not present.
11. **pyproject.toml:** Add entry `room-validator = "<module.path>:main"`; confirm module path
    for the project (e.g. `tools.room_toolkit.room_validator.validator:main` or equivalent).
12. **Verify:** Run room validator tests and lint (ruff/mypy); fix any regressions.

---

## Implementation order (summary)

1. Fix semantic bug: use `parsed["stats"]` in test_reporter.py and test_validator_integration.py.
2. Reporter type hints: suggestion, return types, optional dict/list in generate_json_output.
3. Reporter colorize_output: add docstring (legacy; prefer click.secho).
4. room_loader: move `import click` to top.
5. Add structure note: validator.py or README on single-command layout and future group/commands.
6. Add room-validator script entry to pyproject.toml.

---

## Success criteria

- All tests that parse Reporter JSON use `parsed["stats"]` and pass.
- Reporter has correct type hints and colorize_output docstring.
- room_loader has top-level click import.
- Validator/README documents single-command structure and future refactor if subcommands are added.
- pyproject.toml defines room-validator script entry for installable CLI.
- No new use of print() or raw ANSI in new code; click usage remains consistent.
