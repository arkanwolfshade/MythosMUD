---
name: mythosmud-codacy-8100-remediation
overview: Systematically reduce and resolve all ~8,100+ High and Critical Codacy issues in the MythosMUD repository by fixing real problems in code and configuration, and closing verified false positives with narrowly scoped ignores.
todos:
  - id: wave-0-baseline
    content: Capture and document the current High/Critical Codacy baseline for the MythosMUD repo (total counts, top patterns, and distribution).
    status: completed
  - id: wave-1-config-noise-reduction
    content: Align .codacy.yml ignore patterns with actual Codacy pattern IDs for tests, RAC_* rules, CSS and other known-safe patterns to eliminate systematic noise (Bucket C).
    status: completed
  - id: wave-2-criticals-and-asserts
    content: Eliminate all Critical issues and remove or replace assert usage in production code so High "Use of assert detected" only applies (and is suppressed) in tests.
    status: completed
  - id: wave-3-security-backend
    content: Run iterative security remediation waves on Python backend patterns (Detect Common Security Issues in Python Code, SQL risks, subprocess) until High counts in those patterns are substantially reduced.
    status: completed
  - id: wave-4-security-frontend
    content: Run iterative remediation on High frontend security patterns (XSS, DOM misuse) in client/src, reinforcing SafeHtml and sanitization paths and suppressing only proven false positives.
    status: completed
  - id: wave-5-complexity-refactors
    content: Tackle the worst Lizard CCN and parameter-count findings with targeted refactors that preserve behavior and reduce design risk.
    status: completed
  - id: wave-6-metrics-and-hardening
    content: Maintain progress logs, tighten any remaining suppressions, and iterate until Codacy reports zero Criticals and only justified Highs for MythosMUD.
    status: completed
isProject: false
---

# MythosMUD Codacy 8100+ High/Critical Remediation

### 0. Scope and success criteria

- **Repository in scope**: `MythosMUD` (not the `mythosmud_data` submodule).
- **Issue classes in scope**: All Codacy issues currently marked **High** or **Error** severity in Codacy’s MythosMUD view.
- **Definition of "fix"**:
  - **Real problems** (security, correctness, robustness): fixed in code/config + covered by tests where relevant.
  - **Verified false positives or non-applicable rules**: resolved via **narrowly scoped ignores** (e.g. in `.codacy.yml` or fine-grained inline suppression) with clear justification.
- **End state**:
  - No Critical (Error-level) issues left.
  - High issues only remain where there is an explicit, documented suppression; all other Highs are cleared.

---

### 1. Baseline inventory and triage

- **1.1. Capture a frozen baseline from Codacy UI**
  - Use the Codacy UI for MythosMUD filtered to `levels=High,Error` to capture:
    - Total number of High + Critical issues.
    - List of all code patterns contributing to those issues, sorted by count.
    - Sample locations per pattern (a few representative files).
  - Save this snapshot (e.g. `docs/investigations/codacy_high_critical_baseline.md`) so subsequent waves can be compared.
- **1.2. Bucket patterns into A/B/C for strategy**
  - **Bucket A – Real risk (fix in code)**:
    - Security patterns (e.g. "Detect Common Security Issues in Python Code", XSS, SQL injection, dangerous subprocess usage).
    - Critical syntax/runtime errors (CSS, TS, Python, etc.).
  - **Bucket B – Design/complexity**:
    - Lizard CCN/parameter-count findings, deeply nested logic, etc.
  - **Bucket C – Noise / intentional patterns**:
    - Test-only `assert` usage.
    - RAC table rules (known to be non-applicable per `.codacy.yml`).
    - CSS Grid syntax that Codacy mis-parses, or intentional debug logging.
  - For each pattern, assign one of A/B/C and note it in the baseline doc.

---

### 2. Configuration pass: eliminate systematic noise (Bucket C)

Objective: Drop thousands of non-issues quickly by teaching Codacy what is intentional.

- **2.1. Align ignore configuration with actual Codacy pattern IDs**
  - For each Bucket C pattern, inspect a handful of Codacy issue details to learn the exact `pattern_id` Codacy uses.
  - In `[.codacy.yml](.codacy.yml)`, under `ignore_patterns`:
    - Ensure existing Bandit/Prospector `B101` / test-assert ignores cover _all_ test assert patterns Codacy uses.
    - Confirm RAC table rules are suppressed globally with the pattern IDs Codacy is currently using (they appear already, but verify).
    - For CSS Grid / modern CSS false positives, add ignore entries scoped to the specific CSS files or directories where patterns are known-safe.
    - For intentional debug logging (e.g. in `client/src/utils/debugLogger.ts`), keep or add scoped ignores for the specific Semgrep patterns Codacy uses.
- **2.2. Keep ignores narrow and documented**
  - For each ignore entry:
    - Restrict `file_paths` as tightly as possible (e.g., specific files or `**/tests/`** rather than `**/\*.py`).
    - Document the rationale in nearby comments (why this is safe and what prevents misuse).
- **2.3. Re-run Codacy and capture new baseline**
  - After merging the config changes, wait for Codacy to re-analyze MythosMUD.
  - Update the baseline doc with:
    - New High+Critical total.
    - New per-pattern counts.
  - Expect a substantial drop where Bucket C patterns dominated.

---

### 3. Critical and localized fixes (Bucket A, small surface/huge impact)

- **3.1. Fix all Critical (Error-level) issues first**
  - From the Codacy UI, enumerate all Critical issues:
    - Example: Critical CSS syntax error in `[client/src/index.css](client/src/index.css)` (`grid-template-columns` / `1fr 1fr` token at line ~983).
  - For each Critical:
    - Fix the underlying syntax or logic in the indicated file.
    - Add or adjust tests/build steps to prevent regression (e.g. run client CSS/TS build, Python static checks).
  - Re-run Codacy to ensure the Critical count reaches zero.
- **3.2. Remove `assert` in production code**
  - Search non-test code (`server/`**, `client/src/`**, `scripts/**`, excluding `tests`) for `assert` usage.
  - For each production assert:
    - Replace with explicit condition checks.
    - Raise appropriate exceptions on the server, using structured logging (`get_logger`) for observability.
    - On the client, handle failures via controlled UI states or error boundaries instead of top-level asserts.
  - Add tests that exercise new error-handling paths where appropriate.
  - Confirm via Codacy that High "Use of assert detected" findings now only appear (if at all) in tests, where they are suppressed by configuration.

---

### 4. Iterative security remediation waves (Bucket A bulk)

Operate in **small, repeatable waves** (e.g. 25–50 issues per wave) that each:

1. Select a pattern and a set of files.
2. Fix or suppress with justification.
3. Run tests.
4. Re-check Codacy.

- **4.1. Wave S1 – Python security patterns (backend)**
  - Focus patterns from "Detect Common Security Issues in Python Code" that affect:
    - Authentication/authorization modules (e.g. auth handlers, token/session logic).
    - Persistence (database access) and world/room loading.
    - Subprocess or external process invocation (`scripts/`, tooling helpers).
  - For each affected module:
    - Replace insecure API usage with safe equivalents (e.g. use `scripts/utils/safe_subprocess.py` instead of raw `subprocess` where applicable).
    - Ensure all DB access is parameterized; remove any string-concatenated SQL with user inputs.
    - Add input-validation and normalization where untrusted data enters the system.
  - For any finding that is clearly a false positive (e.g. SQL on trusted seed files with strong documentation), add a narrowly scoped ignore pattern with comments.
- **4.2. Wave S2 – Web/client security patterns (frontend)**
  - For High XSS and DOM-related issues Codacy flags in `client/src/`:
    - Ensure that all HTML injection paths go through `SafeHtml` or DOMPurify.
    - Confirm `ChatPanel` and other dynamic text rendering components escape user content correctly.
    - Where Codacy flags known-safe flows (e.g. previously documented and tested XSS protection paths), add targeted ignores.
  - Expand unit tests and integration tests to cover XSS-sensitive flows.
- **4.3. Wave S3 – Scripts and tooling security**
  - Review `scripts/`** and `tools/`** for High findings involving subprocess usage, file access, or environment handling.
  - Ensure CLI tools and migration scripts:
    - Use safeguarded helpers (e.g. `safe_subprocess` wrappers).
    - Validate arguments before performing filesystem or process operations.
  - Suppress High warnings only where the script is intentionally privileged and the usage is justified and documented.

Each wave ends with:

- Running `make test` from project root (and `make test-comprehensive` periodically).
- Checking Codacy to confirm the targeted pattern’s High counts drop in the modified files.

---

### 5. Complexity/design remediation (Bucket B) in parallel

While security and correctness issues are being driven down, run a parallel track to address High/CCN patterns.

- **5.1. Identify the worst offenders from Lizard reports**
  - Using Codacy’s Lizard findings, list functions with:
    - CCN well above the threshold (e.g. > 15).
    - Parameter count significantly above the limit (e.g. `_process_exit` and `main` in `mythos_mud_mapbuilder.py`).
  - Prioritize by:
    - Runtime criticality (e.g. server request handling vs. rarely used tooling).
    - Readability / maintainability payoff.
- **5.2. Apply structured refactors**
  - For CCN-heavy functions:
    - Extract coherent subroutines (e.g. parsing, validation, data transformation, side-effecting IO) into named helpers.
    - Replace complex nested conditionals with clearer structures (early returns, guard clauses, small state machines where appropriate).
  - For high parameter count functions:
    - Introduce configuration or context objects (e.g. small `@dataclass` or typed object) aggregating related arguments.
    - Ensure call sites remain clear and tests are updated accordingly.
- **5.3. Keep regressions at bay**
  - After each meaningful refactor, run the unit tests covering the affected modules.
  - Check Codacy to confirm the specific CCN/parameter findings are gone or below threshold.

---

### 6. Governance, tracking, and completion

- **6.1. Per-iteration metrics**
  - Maintain a simple markdown log (e.g. `docs/investigations/codacy_high_critical_progress.md`) with entries like:
    - Date / iteration.
    - Patterns targeted.
    - High + Critical total before/after.
    - Notable design/security decisions.
- **6.2. Targets and pacing**
  - Set concrete targets, for example:
    - **Phase 1 (Configuration + Criticals)**: Eliminate all Criticals and drop High count by 30–40% through configuration and obvious code fixes.
    - **Phase 2 (Security waves)**: In each 1–2 week wave, reduce Highs in targeted security patterns by a defined number.
    - **Phase 3 (Complexity waves)**: Chip away at the worst CCN/parameter findings while keeping security/regression risk low.
- **6.3. Definition of Done for the 8100+ campaign**
  - Codacy reports **0 Critical issues** for `MythosMUD`.
  - All remaining High issues are:
    - Either fixed in code, or
    - Resolved by documented, narrowly scoped suppressions in `.codacy.yml` or inline, with clear justification.
  - Security-sensitive modules (auth, persistence, networking, command processing) have **no unresolved High findings**.

---

### 7. Interaction with existing `codacy-high-critical-issues-remediation` plan

- The existing `codacy-high-critical-issues-remediation` plan can be treated as a **sub-plan** focused mainly on SQL/TSQLLint and the Python mapbuilder tooling.
- This new plan supersedes it at the top level by:
  - Focusing explicitly on the MythosMUD repo, not `mythosmud_data`.
  - Covering the full lifecycle from configuration, through security and complexity, to governance.
- Implementation work should:
  - First align the old plan’s todos with the buckets and waves defined here.
  - Then proceed wave-by-wave until Codacy shows the desired High/Critical profile.
