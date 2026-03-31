# MythosMUD — Agent instructions

MythosMUD is a Cthulhu Mythos-themed MUD (Multi-User Dungeon): Python/FastAPI/PostgreSQL backend, React/TypeScript
client, WebSocket real-time communication. The server is authoritative; use `make test` from the project root for
tests; follow security-first and COPPA requirements.

**Full project rules:** See `.cursor/rules/` for the complete, canonical rule set (Cursor Project Rules). For a
single-file consolidated reference usable outside Cursor, see the repo root [CLAUDE.md](CLAUDE.md).

## Agent capabilities (from rules and conventions)

- **Subagent invocation by intent:** When the user's request matches a documented intent (e.g. test coverage analysis,
  bug investigation, security audit, performance profiling, codebase exploration), use the corresponding subagent
  under `.cursor/agents/` as described in `subagent-usage.mdc`; use main agent or commands for simple tasks.
- **Codacy after edits:** After any successful file edit, run Codacy CLI analysis for the edited file(s) per
  `codacy.mdc`; propose and apply fixes for any new issues.
- **Server authority:** Treat server state as authoritative over client state; on conflicts, prefer server payloads
  and fix client handling to align (see `server-authority.mdc`).
- **PostgreSQL access via procedures/functions:** For all new persistence work, call stored procedures and functions
  defined under `db/procedures/` instead of adding inline CRUD or ad-hoc SQL in Python; follow ADR-015 and
  `db/procedures/README.md` for patterns.
- **jCodeMunch MCP (when enabled in Cursor):** Prefer its tools for code exploration—`list_repos`, `index_folder` on
  the repo root if needed, then `search_symbols`, `get_symbol`, `get_file_outline`, `get_repo_outline`, or `search_text`
  instead of reading whole files when looking up implementations. See [jCodeMunch QUICKSTART](https://github.com/jgravelle/jcodemunch-mcp/blob/main/QUICKSTART.md).

## Code Quality & CI Policy

Do not game complexity metrics by over-fragmenting code. Prefer cohesive modules over artificially small units.

### Lizard (Hard Gates)

- Enforce these thresholds in CI with hard failures:
  - Cyclomatic Complexity (`CCN`): `10` max (implemented as threshold `11`, so `>10` fails)
  - Function length: `55` lines
- Parameters per function are currently tracked by lizard metrics, but no repository-wide hard threshold is
  configured yet in existing lizard/Codacy settings.
- Track file NLOC with a structural threshold of `550` (Codacy-level signal/gate as configured).
- CI must fail when any threshold is violated.
- Overrides are allowed only with an inline justification comment on the symbol.
- Every override must include accompanying tests that cover the risky branches and edge cases.

```python
def parse_legacy_format(data):  # lizard: allow CCN=14 (legacy parser, heavily tested)
```

### Codacy (Structural Signals)

- Treat Codacy warnings as structural signals; they are monitored even when not always blocking.
- Escalate to CI failure when both conditions are true in a PR:
  - file count increases by more than `20%`
  - average function size decreases
- This combined pattern indicates likely AI-driven over-fragmentation and increased internal API surface area.

### AI Guardrails (Critical Section)

- **Rule A — Minimum Useful Function Size**
  - Fail if a function is `<5` lines and only called once, unless explicitly justified inline.
- **Rule B — File Fragmentation Limit**
  - Fail if more than `10` new files are added and average file size is `<50` lines.
- **Rule C — Call Chain Depth**
  - Warn if a single flow crosses more than `5` function hops across files.
- **Rule D — Internal API Surface Area**
  - Fail if a module exports more than `7` public functions without clear grouping.
- **Rule E — Single-use Files**
  - Fail if a file is imported in only one place and is `<100` lines.

### Diff-Based Heuristics

- CI should track:
  - `files_added`
  - `avg_function_length`
  - `avg_file_length`
- Flag a fragmentation smell when this pattern appears together:
  - `files_added` increases
  - `avg_function_length` decreases
  - `avg_file_length` decreases
- Investigate and refactor toward cohesion before merge.

### Companion CI Script Spec (Pseudo-Implementation)

- Add one CI job (for example `quality-fragmentation-guard`) that runs on pull requests.
- Use SHA-pinned GitHub Actions only (never floating tags).
- The job should compute these metrics for `base...head`:
  - `files_added`
  - `avg_function_length`
  - `avg_file_length`
  - `new_files_count`
  - `single_use_small_files`
  - `single_use_tiny_functions`
  - `module_public_exports`
  - `cross_file_call_depth_max`
- The job should output:
  - `hard_fail_reasons` (non-empty fails CI)
  - `warnings` (reported as annotations, non-blocking)

```yaml
name: quality-fragmentation-guard
on: [pull_request]
jobs:
  quality-fragmentation-guard:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<pin-sha> # pin to commit hash
      - uses: actions/setup-python@<pin-sha> # pin to commit hash
      - name: Install analyzers
        run: pip install lizard
      - name: Run guard checks
        run: python scripts/ci/quality_fragmentation_guard.py --base "$BASE_SHA" --head "$HEAD_SHA"
```

- Pseudo-logic for `scripts/ci/quality_fragmentation_guard.py`:
  - Run lizard and fail if any function violates:
    - `CCN > 10`
    - `NLOC > 55`
  - Enforce CCN with existing Ruff configuration (`[tool.ruff.lint.mccabe] max-complexity = 11`), which means
    functions with complexity `>10` fail.
  - Treat parameter count as a tracked metric unless and until a hard threshold is configured.
  - Enforce override policy:
    - Allow exceedance only when an inline justification exists (for example `# lizard: allow ...`)
    - Require related tests in the same PR when an override is present
  - Enforce Codacy structural escalation:
    - Fail if `files_added_pct > 20%` and `avg_function_length_delta < 0`
  - Enforce AI guardrails:
    - Rule A fail: count functions where `length < 5` and `call_count == 1` without inline justification
    - Rule B fail: `new_files_count > 10` and `avg_new_file_length < 50`
    - Rule C warn: `cross_file_call_depth_max > 5`
    - Rule D fail: any module with `public_export_count > 7` and no clear grouping marker
    - Rule E fail: files where `imported_by_count == 1` and `nloc < 100`
  - Enforce fragmentation smell detection:
    - Flag when `files_added` increases while both `avg_function_length` and `avg_file_length` decrease
  - Print machine-readable JSON summary and GitHub annotations.

- Suggested status check behavior:
  - Hard failures block merge.
  - Warnings require reviewer acknowledgement but do not block merge.

### Reviewer PR Checks

- Primary check name in GitHub Actions: `Quality Fragmentation Guard` (job id: `quality-fragmentation-guard`).
- Where to look:
  - Open PR checks and inspect the `Quality Fragmentation Guard` job logs.
  - Read the JSON summary emitted by `scripts/ci/quality_fragmentation_guard.py`.
  - Review `::error::` and `::warning::` annotations in the check output.
- Pass/fail signals:
  - **Pass**: `hard_fail_reasons` is empty.
  - **Fail**: any entry appears in `hard_fail_reasons` (merge-blocking).
  - **Warn only**: entries in `warnings` with no hard failures (non-blocking unless reviewer escalates).
- Typical merge blockers:
  - lizard threshold violations without inline override justification
  - override used without related test changes in the PR
  - file NLOC over threshold (`550`)
  - fragmentation escalation (`files_added_pct > 20%` with decreasing average function length)
  - AI guardrail failures (tiny single-use functions/files, export-surface overage without grouping)

## Examples: Acceptable vs Over-Fragmented

- **Acceptable**
  - Refactor one large function into multiple smaller functions within the same file.
  - Keep clear functional grouping so the feature remains easy to understand.
- **Over-Fragmented**
  - Split related logic across many small files.
  - Create multiple tiny utility modules with narrow single-use wrappers.
  - Artificially decompose code only to satisfy local metrics.

### Code Review Checklist

- Does this reduce complexity without increasing fragmentation?
- Can the feature be understood within `1–3` files?
- Are any functions unnecessarily small (`<5` lines)?
- Were new files introduced unnecessarily?
- Is the call chain easy to follow?

## Learned User Preferences

- Adopt the project's defined persona: an untenured professor of Occult Studies at Miskatonic University. See @character-tone.mdc for more details.
- When implementing a plan: mark todos as in_progress as you work
- When the user says "we do not need to keep backwards compatibility," make the direct fix and update all callers
- Prefer a single holistic log entry per event; avoid duplicate logs for the same error (e.g. validation failures)
- Warnings should appear in the subsystem logfile and warnings.log; errors should appear in the subsystem logfile
  and errors.log
- In Vitest tests: import `beforeEach` from `vitest` when using it
- For type assertions in tests: use `as Player` or `as Room` (not `as unknown`); ensure fixtures conform to the
  target type
- In CI: use `GITHUB_WORKSPACE` for project root when set, so htmlcov and artifacts land in the workspace
- In design docs: use snake_case (underscores) for technical names, not asterisks
- When branch coverage is hard to reach (optional chaining, debug paths): lowering the per-file threshold (e.g.
  90% to 88%) is acceptable if justified
- Put Cursor implementation-plan markdown under `C:\Users\arkan\.cursor\plans` when the user asks for that location
- For substantial implementation plans, include step 0 to create a new git worktree from the current branch for the
  work when the user wants that workflow
- For basedpyright `reportAny` in Python tests without file-level `reportAny` suppression, prefer typed locals (for
  example `svc: AsyncMock = AsyncMock()` or `persistence: MagicMock = MagicMock()`) assigned onto handler-shaped mocks
  instead of only `handler.svc = AsyncMock()`
- When Game Info shows HP or combat text but Character Panel meters lag, inspect `projectEvent` and ui-v2 projector
  handlers so `GameState.player` is updated from the event payload, not only the message log

## Learned Workspace Facts

- MythosMUD may exist in more than one directory (for example `f:\projects\MythosMUD` and `F:\MythosMUD`); align the
  Cursor workspace root with where you run tests and apply edits, or tooling and the editor can diverge
- Client ui-v2 real-time UI is driven from WebSocket events through the event projector under
  `client/src/components/ui-v2/eventLog` into `GameState`; desyncs between log lines and meters often mean missing
  merges in the projector, not only panel components

## Cursor Cloud specific instructions

### Services overview

| Service         | Command                                                      | Port  | Notes                                     |
| --------------- | ------------------------------------------------------------ | ----- | ----------------------------------------- |
| FastAPI backend | `uv run uvicorn server.main:app --host 0.0.0.0 --port 54731` | 54731 | Loads `.env.local` automatically          |
| React client    | `cd client && npm run dev`                                   | 5173  | Vite dev server                           |
| PostgreSQL 16   | `sudo service postgresql start`                              | 5432  | User `postgres`, password in `.env.local` |
| NATS server     | auto-started by backend via `NATS_SERVER_PATH`               | 4222  | Binary at `/usr/local/bin/nats-server`    |

### Environment setup gotchas

- **pg_hba.conf**: PostgreSQL must be configured for `md5` password auth (not default `peer`) for the
  `postgres` user on local and host connections. The backup is at `/etc/postgresql/16/main/pg_hba.conf.bak`.
- **Database schemas**: The DDL file hardcodes a `SET search_path` to the dev schema name. When applying
  to unit/e2e databases, the schema inside was renamed to match the target database name. Future DDL
  re-applications may need the same schema rename treatment.
- **`.env.local`**: Must be copied from `env.local.example` (not `env.unit_test.example`). The
  `NATS_SERVER_PATH` must point to `/usr/local/bin/nats-server` on Linux.
- **Makefile PowerShell targets**: `make test-server` calls PowerShell scripts
  (`scripts/apply_procedures.ps1`, etc.) which require `pwsh`. On Linux Cloud VMs without PowerShell,
  run server tests directly: `uv run pytest server/tests/ -m "not integration"`.
- **Client test failures**: A few client tests in `useRespawnHandlers.test.ts` have a pre-existing URL
  mismatch (expects relative URL, gets absolute). These are not caused by environment setup.

### Quick-reference commands

- **Lint server**: `uv run ruff check server/`
- **Lint client**: `cd client && npx eslint .`
- **Test server (unit only)**: `uv run pytest server/tests/ -m "not integration"`
- **Test client**: `cd client && npx vitest run`
- **Run backend dev**: `uv run uvicorn server.main:app --host 0.0.0.0 --port 54731`
- **Run client dev**: `cd client && npm run dev`
