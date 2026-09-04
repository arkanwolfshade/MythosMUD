---
name: ""
overview: ""
todos: []
isProject: false
---

# GitHub Actions Best-Practices Remediation Plan

**Source rule:** `.cursor/rules/github-actions.mdc`
**Scope:** `.github/workflows/*.yml`
**Created:** 2025-02-13

## Summary

Analysis of the four workflow files (`ci.yml`, `codeql.yml`, `dependency-review.yml`, `scorecards.yml`) against the
github-actions rule identified violations and improvement opportunities in workflow design, performance, security, and
maintainability. This plan lists concrete fixes with file and (where applicable) line references.

---

## 1. Workflow Design & Code Organization

### 1.1 Duplicated steps across workflows (Rule 1.1 – Reusable Workflows)

**Finding:** The same sequence (Harden runner → Checkout) is repeated in all four workflows with identical action refs.
No reusable workflow or composite action is used.

**Files:** All four workflows.

**Remediation:**

- **Option A (recommended for this repo):** Keep current structure but add a short comment in each workflow referencing
  the shared pattern (e.g. “Standard bootstrap: harden + checkout”). No file changes required beyond comments; avoids
  indirection while documenting intent.
- **Option B:** Introduce a reusable workflow (e.g. `.github/workflows/bootstrap.yml`) with `workflow_call` that
  performs checkout (and optionally harden-runner), and have ci/codeql/dependency-review/scorecards call it. Reduces
  duplication but adds another file and call semantics; only do this if you expect to add more workflows or change
  bootstrap often.

**Todo:**

- **ga-reuse-docs:** Add a one-line comment in each of the four workflow files after the first `uses:` step
  noting the shared bootstrap pattern (harden + checkout). If Option B is chosen instead, implement the reusable
  workflow and replace the duplicated steps with a single `uses: ./.github/workflows/bootstrap.yml` (or equivalent)
  and remove the duplicated steps.

### 1.2 Unnamed steps (Rule 1.2 – Name Jobs and Steps Consistently)

**Finding:** Some steps use `- uses:` without a preceding `- name:`, so logs show only the action name.

**Locations:**

- `ci.yml`: Backend job – checkout step (line ~51). Frontend job – checkout step (line ~267).

**Remediation:** Add a descriptive `name:` before each `uses:` for `actions/checkout` (e.g. “Checkout repository”).

**Todo:**

- **ga-name-steps:** In `ci.yml`, add `name: Checkout repository` (or equivalent) to the backend checkout step
  and to the frontend checkout step.

### 1.3 Job display name (Rule 1.2)

**Finding:** The dependency-review workflow job has an id but no human-readable `name:`.

**File:** `dependency-review.yml` – job `dependency-review`.

**Remediation:** Add `name: Dependency Review` (or similar) to the job.

**Todo:**

- **ga-name-job:** In `dependency-review.yml`, add `name: Dependency Review` to the `dependency-review` job.

### 1.4 Concurrency (Rule 1.4 – Set Explicit Concurrency Groups)

**Finding:** No workflow sets `concurrency`. For CI, multiple pushes/PR updates can run many concurrent runs.

**Remediation:** Add a concurrency group so that only the latest run per branch (or per PR) is active; cancel in-progress
runs when a new one is triggered. Apply only where it improves cost/clarity (e.g. CI), not necessarily to codeql/scorecards
schedule runs.

**Todo:**

- **ga-concurrency:** In `ci.yml`, add top-level `concurrency:` (e.g. `group: ci-${{ github.workflow }}-${{ github.ref }}`
  and `cancel-in-progress: true`). Optionally add similar group for codeql/dependency-review/scorecards if desired.

---

## 2. Performance

### 2.1 No dependency caching (Rule 2.1 – Cache Dependencies)

**Finding:** Backend and frontend jobs do not use `actions/cache`. Every run does a full `uv pip install` / `npm ci`,
increasing duration and API load.

**File:** `ci.yml` – backend job (uv/pip), frontend job (npm).

**Remediation:**

- **Backend:** Add a cache step using `actions/cache` with a key that includes `runner.os`, `hashFiles('**/pyproject.toml')`
  (and optionally `**/uv.lock` if present). Cache the uv environment directory (e.g. `.venv-ci` or the path uv uses).
  Restore cache before “Install dependencies” and use `uv pip install` as today (cache will restore venv when key
  hits).
- **Frontend:** Add a cache step for npm (e.g. `~/.npm` or `client/node_modules`) with key including
  `hashFiles('**/package-lock.json')` (scoped to `client/` if appropriate). Run before `npm ci`.

**Todo:**

- **ga-cache-backend:** In `ci.yml` backend job, add an `actions/cache` step before “Install dependencies” for the
  uv/venv directory; key must include `runner.os` and content hash of dependency files.
- **ga-cache-frontend:** In `ci.yml` frontend job, add an `actions/cache` step before “Install dependencies” for npm
  (path and key per rule 2.1); ensure `npm ci` runs after cache restore.

---

## 3. Code Quality & Maintainability

### 3.1 Lint / quality order (Rule 3.1 – Run Linters Early)

**Finding:** In the backend job, “Lint with ruff” and “Type check with mypy” run after heavy setup (PostgreSQL install,
DB init, Playwright). Failures in lint/mypy are discovered late.

**File:** `ci.yml` – backend job.

**Remediation:** Run lint and type-check as early as possible after dependency install (and before DB/Playwright), or
introduce a separate “lint” job that only does checkout → setup Python → install deps → ruff + mypy, and have “backend”
job `need: [lint]` (or equivalent) so that expensive backend steps run only if lint passes. Prefer reusing the same
venv (e.g. one job with reordered steps: deps → ruff → mypy → rest) to avoid duplicating setup.

**Todo:**

- **ga-lint-early:** In `ci.yml` backend job, move “Lint with ruff” and “Type check with mypy” to run immediately
  after “Install dependencies” (and after “Install uv”), and before “Install Playwright browsers” and “Install PostgreSQL
  18”. If a separate lint job is preferred, add a `lint` job and set `backend` to `needs: [lint]` and keep ruff/mypy
  only in `lint`.

### 3.2 Pin third-party action to SHA (Rule 3.2)

**Finding:** `codacy/codacy-coverage-reporter-action@v1.3.0` is pinned by tag only. The rule requires a specific version
tag or SHA to avoid supply-chain surprises.

**File:** `ci.yml` – line ~234.

**Remediation:** Resolve the `v1.3.0` tag to its full commit SHA on the
[codacy/codacy-coverage-reporter-action](https://github.com/codacy/codacy-coverage-reporter-action) repository and
replace `@v1.3.0` with `@<full-SHA> # v1.3.0` in the workflow.

**Todo:**

- **ga-pin-codacy:** In `ci.yml`, replace `codacy/codacy-coverage-reporter-action@v1.3.0` with
  `codacy/codacy-coverage-reporter-action@<SHA> # v1.3.0` (look up SHA from the action’s repo tag v1.3.0).

---

## 4. Security & Configuration

### 4.1 Debug flags always on (Rule 5.1 – Debugging with ACTIONS_STEP_DEBUG)

**Finding:** `ACTIONS_STEP_DEBUG: true` and `ACTIONS_RUNNER_DEBUG: true` are set in the workflow `env` for both backend
and frontend jobs. The rule says to enable debugging via a repository secret when needed and to remove it after
debugging; having them always on in the file produces noisy logs and is not recommended for normal runs.

**File:** `ci.yml` – backend job env (lines ~19–20), frontend job env (lines ~253–254).

**Remediation:** Remove `ACTIONS_STEP_DEBUG` and `ACTIONS_RUNNER_DEBUG` from the workflow. Document in a comment or
CONTRIBUTING that to debug Actions, add a repository secret `ACTIONS_STEP_DEBUG` (and optionally `ACTIONS_RUNNER_DEBUG`)
with value `true`, rerun the workflow, then delete the secret.

**Todo:**

- **ga-remove-debug-flags:** In `ci.yml`, remove the `ACTIONS_STEP_DEBUG` and `ACTIONS_RUNNER_DEBUG` entries from
  both the backend and frontend job `env` blocks. Optionally add a short comment or CONTRIBUTING note on enabling them
  via repo secret for debugging.

### 4.2 Hardcoded test credentials (Rule 4.1 – Store Secrets in GitHub Secrets)

**Finding:** `ci.yml` contains hardcoded test credentials: `DATABASE_URL` / `DATABASE_NPC_URL` with password
`Cthulhu1`, and fallback strings for `MYTHOSMUD_*` when secrets are unset. The rule states never to hardcode sensitive
values.

**File:** `ci.yml` – backend job `env` and the PostgreSQL init step.

**Remediation (pragmatic):** Keep CI self-contained and avoid requiring secrets for every run, while aligning with the
rule as far as possible:

- Move the PostgreSQL test password to a GitHub Actions secret (e.g. `POSTGRES_CI_PASSWORD`) with a default value
  configured in the repo (so CI works out of the box). In the workflow, use `${{ secrets.POSTGRES_CI_PASSWORD }}` and
  in the “Start PostgreSQL service…” step use the same secret (or an env var set from it) instead of the literal
  `Cthulhu1`. If you prefer not to add a secret, document in the workflow and in the rule’s “exceptions” that the
  hardcoded value is a CI-only test credential and that CodeQL/codeql-config exclusions already document this.
- For `MYTHOSMUD_*` fallbacks: either document that these are intentional CI test defaults and leave as-is, or use a
  single secret (e.g. `MYTHOSMUD_CI_TEST_DEFAULTS`) that holds a JSON or comma-separated set of test values, and
  parse in a prior step to set env vars. The minimal change is to add a comment that the fallbacks are CI-only and
  acceptable per project policy.

**Todo:**

- **ga-secrets-db:** In `ci.yml`, replace hardcoded PostgreSQL password `Cthulhu1` with
  `${{ secrets.POSTGRES_CI_PASSWORD }}` (and set `POSTGRES_CI_PASSWORD` in repo secrets to the current test value), and
  update the “Start PostgreSQL service…” step to use the same secret or an env var derived from it. If the project
  decides not to use a secret, add a single comment that the hardcoded value is a CI-only test credential and is
  documented in codeql-config.
- **ga-secrets-mythos:** Either document in `ci.yml` that the `MYTHOSMUD_*` fallbacks are CI-only test defaults
  and acceptable, or introduce a single secret for CI test defaults and use it instead of inline strings.

---

## 5. Optional / Nice-to-Have

- **Matrix strategy (Rule 1.3):** Consider adding a matrix for the frontend job (e.g. `node-version: ['20','22']`) or
  backend (e.g. `python-version: ['3.11','3.12']`) if you want to assert compatibility across versions. Not required
  for “fix all findings” but aligns with the rule.
- **Code scanning (Rule 6.1):** Already satisfied; CodeQL and Scorecards workflows are in place.
- **Least privilege (Rule 4.2):** Current workflows already use minimal permissions; no change required.
- **Script injection (Rule 4.4):** No untrusted input is passed directly into `run:` scripts; no change required.

---

## 6. Verification

After applying the plan:

- Run `act` or push a branch and open a PR to trigger the workflows; confirm CI, CodeQL, Dependency Review, and
  Scorecards all complete successfully.
- Confirm backend lint/mypy run before heavy setup (or that the lint job runs first and backend depends on it).
- Confirm dependency cache is used (check workflow run logs for “Cache restored” / “Cache saved” or equivalent).
- If you removed debug flags, confirm logs are less verbose; if you added secret-based debug instructions, confirm they
  are documented.

**Todo:**

- **ga-verify:** After implementing the above, trigger workflows (e.g. via push or PR), confirm green runs, and
  spot-check cache and lint order in logs.

---

## To-Do Checklist (ordered for implementation)

| Id                    | Description                                                                           |
| --------------------- | ------------------------------------------------------------------------------------- |
| ga-name-steps         | Add `name:` to checkout steps in ci.yml (backend + frontend).                         |
| ga-name-job           | Add `name: Dependency Review` to dependency-review.yml job.                           |
| ga-pin-codacy         | Pin codacy-coverage-reporter-action to full SHA in ci.yml.                            |
| ga-remove-debug-flags | Remove ACTIONS_STEP_DEBUG / ACTIONS_RUNNER_DEBUG from ci.yml.                         |
| ga-lint-early         | Move ruff + mypy before Playwright/PostgreSQL in ci.yml backend.                      |
| ga-cache-backend      | Add actions/cache for uv/venv in ci.yml backend.                                      |
| ga-cache-frontend     | Add actions/cache for npm in ci.yml frontend.                                         |
| ga-concurrency        | Add concurrency group to ci.yml.                                                      |
| ga-reuse-docs         | Add bootstrap-pattern comment to all four workflows (or implement reusable workflow). |
| ga-secrets-db         | Replace hardcoded DB password with secret or document exception.                      |
| ga-secrets-mythos     | Document or replace MYTHOSMUD fallbacks.                                              |
| ga-verify             | Trigger workflows and verify cache, lint order, and green runs.                       |
