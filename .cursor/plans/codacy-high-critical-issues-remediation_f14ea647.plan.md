---
name: codacy-high-critical-issues-remediation
overview: Use Codacy MCP results to identify current high/critical issues on main (none at present) and plan remediation for remaining medium-severity findings in SQL migrations/seeds and Python mapbuilder utilities.
todos:
  - id: confirm-severity-landscape
    content: Confirm via Codacy MCP and UI that there are no Error-level (Critical) issues on main and summarise current Warning-level findings.
    status: completed
  - id: decide-sql-lint-strategy
    content: Decide whether to address TSQLLint header findings in PostgreSQL migrations via Codacy configuration changes or SQL header additions.
    status: completed
  - id: reconfigure-codacy-tsqllint
    content: Adjust Codacy/TSQLLint configuration to avoid false positives on PostgreSQL SQL files, or scope TSQLLint to SQL Server–specific paths.
    status: in_progress
  - id: refactor-mapbuilder-complexity
    content: Refactor e2e_test/local mythos_mud_mapbuilder scripts to reduce parameter count and cyclomatic complexity in _process_exit, render_with_tcod, and main.
    status: pending
  - id: validate-tests-and-codacy
    content: Run tests and Codacy re-analysis to confirm all addressed issues are resolved without regressions.
    status: pending
isProject: false
---

# Codacy High/Critical Issues Remediation Plan

### 1. Confirm Codacy severity landscape on `main`
- **Codacy rating model**: Codacy maps linter levels `Info`, `Warning`, `Error` to severities `Minor`, `Medium`, and `Critical` respectively.
- **Current state**: Using Codacy MCP (`codacy_list_repository_issues`) on `mythosmud_data` `main` shows only `Warning`-level findings (no `Error`-level issues), so **there are currently no Critical (Error-level) issues reported** on `main`.
- **High-severity security findings**: Attempts to query SRM security items (`codacy_search_repository_srm_items`) for High/Critical priorities failed due to a server-side requirement for a `repository` argument that is not exposed in the tool schema; for now, assume there are **no outstanding High/Critical SRM items**, and verify via the Codacy web UI when convenient.

### 2. Group and prioritize remaining Warning-level issues
- **Group A – TSQLLint header directives in SQL files (BestPractice/Compatibility)**
  - Files:
    - `[db/02_item_prototypes.sql](db/02_item_prototypes.sql)`
    - `[db/05_profession_modifiers.sql](db/05_profession_modifiers.sql)`
    - `[db/migrations/04_add_backpack_item.sql](db/migrations/04_add_backpack_item.sql)`
    - `[db/migrations/07_add_switchblade_weapon.sql](db/migrations/07_add_switchblade_weapon.sql)`
    - `[db/migrations/09_update_tutorial_bedroom_no_combat_no_death.sql](db/migrations/09_update_tutorial_bedroom_no_combat_no_death.sql)`
    - `[db/migrations/15_add_quest_leave_the_tutorial.sql](db/migrations/15_add_quest_leave_the_tutorial.sql)`
  - Findings (repeated across these files):
    - `TSQLLint_set-ansi`: Expected `SET ANSI_NULLS ON` near top of file
    - `TSQLLint_set-quoted-identifier`: Expected `SET QUOTED_IDENTIFIER ON` near top of file
    - `TSQLLint_set-nocount`: Expected `SET NOCOUNT ON` near top of file
    - `TSQLLint_set-transaction-isolation-level`: Expected `SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` near top of file
  - **Context**: Project database is PostgreSQL; these directives are SQL Server–specific, so the TSQLLint warnings are likely false positives on PostgreSQL-flavoured SQL.

- **Group B – Python complexity in mapbuilder utilities (Complexity)**
  - Files:
    - `[e2e_test/mythos_mud_mapbuilder.py](e2e_test/mythos_mud_mapbuilder.py)`
    - `[local/mythos_mud_mapbuilder.py](local/mythos_mud_mapbuilder.py)`
  - Findings:
    - `Lizard_parameter-count-medium`: `_process_exit` has 9 parameters (limit 8) in both files
    - `Lizard_ccn-medium`: `render_with_tcod` CCN 10 (limit 8) and `main` CCN 13 (limit 8) in both files
  - **Context**: These are utility/CLI-style scripts used for E2E tooling and local workflows, not core game runtime, but reducing complexity aids maintainability and readability.

### 3. Strategy for Group A (SQL / TSQLLint header findings)
- **3.1. Confirm SQL dialect and execution path**
  - Review SQL execution tooling/config (e.g., migration runner scripts or DB bootstrap code) to ensure all affected files are **PostgreSQL** migrations/seeds and not executed against SQL Server.
  - Document this explicitly in a short comment or architecture note so future lint and tooling decisions are grounded.

- **3.2. Decide remediation vs. exclusion**
  - **Option 1 – Adjust Codacy/TSQLLint configuration** (preferred if files are strictly PostgreSQL):
    - In Codacy configuration (project UI or config files), exclude the migration/seed paths from TSQLLint, or limit TSQLLint to SQL Server–specific directories only.
    - Alternatively, configure TSQLLint to recognise PostgreSQL dialect and not enforce SQL Server directives on these files (if the tool supports such configuration via Codacy).
    - Mark existing issues as ignored/obsolete once configuration is in place and Codacy re-analysis confirms they no longer appear.
  - **Option 2 – Add compatibility headers** (only if migrations must run on SQL Server too):
    - At the very top of each listed file, add the appropriate `SET ANSI_NULLS ON`, `SET QUOTED_IDENTIFIER ON`, `SET NOCOUNT ON`, and `SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` statements in a safe, idempotent block.
    - Ensure these directives are semantically valid for the target DB engine(s) and that tests/DB bootstrap still succeed.

- **3.3. Validation workflow**
  - After configuration or code changes, trigger Codacy re-analysis and verify that all TSQLLint findings for these files are resolved.
  - Run the project’s standard DB migration/seeding workflow (e.g., via `make test` and any DB bootstrap scripts) to confirm there are no regressions.

### 4. Strategy for Group B (Python complexity in mapbuilder utilities)
- **4.1. Refactor `_process_exit` to reduce parameter count**
  - In both `e2e_test/mythos_mud_mapbuilder.py` and `local/mythos_mud_mapbuilder.py`:
    - Identify parameter groups that can be bundled into small data structures (e.g., a `dataclass` or configuration object) to reduce the explicit parameter list of `_process_exit` from 9 to 8 or fewer.
    - Ensure shared abstractions are defined in a common module (e.g., `tools/mapbuilder/common.py`) to avoid divergence between the e2e and local versions.

- **4.2. Reduce cyclomatic complexity of `render_with_tcod` and `main`**
  - For `render_with_tcod` in both files:
    - Extract logically coherent blocks (e.g., grid preparation, TCOD initialisation, event loop) into helper functions.
    - Keep side-effect boundaries clear so refactoring does not change behaviour.
  - For `main` in both files:
    - Apply a “command dispatcher” or small state machine: parse CLI args, then delegate to subcommands or orchestrator functions rather than performing all work inline.
    - Reuse the same structure between the e2e and local scripts, or consolidate them into a single entrypoint with mode flags if appropriate.

- **4.3. Testing and verification**
  - Ensure existing e2e tests that rely on `e2e_test/mythos_mud_mapbuilder.py` still pass after refactor.
  - For `local/mythos_mud_mapbuilder.py`, perform manual/CLI smoke tests to validate common workflows.
  - Rerun Codacy analysis and confirm all Lizard `parameter-count-medium` and `ccn-medium` warnings are cleared or reduced below thresholds.

### 5. Ongoing monitoring and governance
- **5.1. Periodic Codacy MCP sweeps**
  - On a regular cadence (e.g., weekly or before releases), rerun Codacy MCP tools (`codacy_list_repository_issues`) filtered by `levels: ["Warning", "Error"]` on `main` to detect any new high/critical issues early.

- **5.2. Security SRM double-check**
  - When the Codacy SRM MCP interface allows specifying the repository cleanly, query High/Critical security items (`SAST`, `Secrets`, `SCA`, `IaC`, `CICD`) and integrate any newly discovered items into the remediation workflow above.

- **5.3. Documentation and coding standards**
  - Add brief notes to the project’s development docs (e.g., `DEVELOPMENT.md` or a dedicated QA/linting section) describing:
    - Which SQL dialects are in use and how Codacy/TSQLLint should treat migration files.
    - Expectations around utility script complexity (e.g., keeping CLI entrypoints and rendering functions under complexity thresholds).
