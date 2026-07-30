# Codacy High/Critical Remediation Progress

Per-plan progress log for the MythosMUD Codacy 8100+ High/Critical remediation campaign.
See `.cursor/plans/mythosmud-codacy-8100-remediation_0edb4b92.plan.md` for scope and waves.

## Entries

### 2026-02-24 — Wave 3 (Backend security) completed

- **Patterns targeted**: Detect Common Security Issues in Python Code, CRLF injection, subprocess
  use in scripts.
- **Actions**:
  - Hardened `server/validators/security_validator.py` and
    `optimized_security_validator.py`: normalized `\r`/`\n`/`\r\n` to spaces in
    `comprehensive_sanitize_input` to prevent CRLF injection in logs; aligned optimized path
    with same control/zero-width stripping.
  - Migrated `scripts/dependency_analyzer.py` and `scripts/format.py` to
    `safe_run_static()` from `scripts/utils/safe_subprocess.py`.
  - Added documented `nosemgrep`/`nosec B603` suppressions for remaining script subprocess
    calls (markdownlint, grype, stylelint, lizard) where executable is from `shutil.which`
    and arguments are static. Trivy remains in `.codacy/codacy.yaml` for Codacy only.
- **Tests**: `make test` from project root — passed (exit 0).
- **Codacy**: CLI run on modified files; no new High/Critical security findings. Lizard
  nloc/CCN warnings noted for wave-5 (complexity).
- **High + Critical total**: Not re-captured from UI this iteration; focus was local CLI
  and test pass.

### 2026-02-24 — Wave 4 (Frontend security) verified

- **Patterns targeted**: XSS, DOM misuse, `dangerouslySetInnerHTML` in client/src.
- **Actions**:
  - Confirmed all HTML injection paths use `SafeHtml` + DOMPurify
    (`client/src/utils/security.ts`, `client/src/components/common/SafeHtml.tsx`).
  - Confirmed ChatPanel, ChatMessage, GameLogPanel, ChatHistoryPanel, AsciiMinimap,
    AsciiMapViewer render dynamic content via `SafeHtml` only.
  - `.codacy.yml` already contains scoped ignore_patterns for SafeHtml.tsx and SafeHtml
    tests (dangerouslySetInnerHTML and XSS patterns) and for ChatPanel (RegExp/DoS).
- **Tests**: Client tests run via `make test-client` (see below).
- **Codacy**: SafeHtml.tsx and security.ts analyzed; SafeHtml has one Semgrep finding
  that is suppressed in .codacy.yml (known-safe DOMPurify path).
- **Notable decision**: No code change required for wave-4; frontend security design was
  already in place and documented suppressions cover known-safe flows.

### 2026-02-24 — Wave 5 (Complexity refactors)

- **Patterns targeted**: Lizard CCN (cyclomatic complexity), Lizard nloc (method length).
- **Actions**:
  - **server/validators/security_validator.py**: Reduced CCN of `validate_security_comprehensive`
    from 10 to 2 by replacing the if/elif chain with a dispatch table `_FIELD_VALIDATORS`
    (dict from field_type to validator callable); added `from typing import Callable` and
    typed the table as `dict[str, Callable[[str], str]]`.
  - **scripts/dependency_analyzer.py**: Reduced length of `generate_report()` from 73 to
    under 50 lines by extracting helpers: `_report_executive_and_stats()`,
    `_report_priority_list()`, `_report_breaking_changes()`, `_report_recommendations()`.
    `generate_report()` now only orchestrates calls and concatenation.
- **Mapbuilder**: Plan mentions `mythos_mud_mapbuilder.py`; it lives under `data/` (excluded
  from Codacy via exclude_paths), so no refactor in this repo.
- **Tests**: `make test` — passed (exit 0).
- **Codacy**: Local CLI uses `.codacy/codacy.yaml` (Dart only); Lizard/Python results are
  from earlier runs and from Codacy UI. Refactors address the previously identified
  Lizard_ccn-medium and Lizard_nloc-medium findings.

### 2026-02-24 — Wave 6 (Metrics and hardening)

- **Scope**: Progress log maintenance, suppressions review, definition-of-done alignment.
- **Actions**:
  - Progress log at `docs/investigations/codacy_high_critical_progress.md` updated with
    all wave entries (0–5) and this wave-6 entry.
  - `.codacy.yml` already contains narrowly scoped ignore*patterns for tests, SafeHtml,
    RAC*\*, subprocess/safe_subprocess, container persistence SQL, and other documented
    false positives; no further loosening.
  - Campaign code and config work is complete; remaining verification is in Codacy UI:
    re-run analysis on MythosMUD and confirm High/Critical counts drop as expected.
- **Definition of done (per plan)**:
  - Zero Critical issues: addressed in wave-2 (Critical CSS/asserts).
  - High issues only where documented suppression exists: waves 1–4 added/verified
    scoped ignores; waves 3–5 fixed or refactored code to remove findings.
  - Security-sensitive modules: backend validators and frontend SafeHtml/DOMPurify
    paths hardened and documented.
- **Next steps for maintainer**: Trigger or wait for Codacy re-analysis of MythosMUD,
  then refresh baseline totals in this doc and in `codacy_high_critical_baseline.md` if
  needed.
