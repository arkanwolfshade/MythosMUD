---
name: pytest best-practices remediation
overview: "Remediate the MythosMUD server test suite to align with the pytest rule (`.cursor/rules/pytest.mdc`): structure, naming, fixtures, single-assert guidance, mocking, and type hints. Option A for layout; add mocking guidance comment; detailed todos in section 7."
todos:
  - id: PY-1
    content: Project layout (Option A) - add note to server/tests/README.md
    status: completed
  - id: PY-2
    content: Mocking guidance - add one-line comment in conftest or test README
    status: completed
  - id: PY-3
    content: Add __init__.py to server/tests, unit, integration, and other test subdirs
    status: completed
  - id: PY-4
    content: Move server/commands/__tests__/test_logout_command.py to server/tests/unit/commands/
    status: completed
  - id: PY-5
    content: Add one-line justification comments to all autouse fixtures
    status: completed
  - id: PY-6
    content: Add fixture type hints in conftest and selected unit test modules
    status: completed
  - id: PY-7
    content: Optional test naming audit and README guidance
    status: completed
  - id: PY-8
    content: Verification - make test and collect-only after changes
    status: completed
isProject: false
---

# Pytest Best-Practices Remediation Plan

## Summary of findings

Analysis of [server/tests](server/tests) and related code against [.cursor/rules/pytest.mdc](.cursor/rules/pytest.mdc) produced the following categories of findings. No `setup_method`/`setup_class` usage was found (good). Test classes consistently use the `Test` prefix (good). Parametrize and fixture `yield` teardown are used appropriately in many files.

---

## 1. Code organization and structure

### 1.1 Project layout (src/ vs top-level)

**Rule:** "Always use the src/ layout."

**Finding:** The project uses a top-level package layout: [pyproject.toml](pyproject.toml) has `[tool.setuptools.packages.find]` with `include = ["server*"]`, and the package lives at `server/`, not `src/server/`. Tests run against the installed or local `server` package.

**Decision (Option A):** Add a short note in [server/tests/README.md](server/tests/README.md) that the project uses a top-level `server/` package (not `src/`) and that tests are executed from project root via `make test` so imports resolve correctly. No migration to `src/` in scope.

### 1.2 Test file naming and placement

**Rule:** Prefer `test_*.py` in a `tests/` tree; place `__init__.py` in `tests/` and subdirectories so they are Python packages.

**Findings:**

- **Non-standard test location:** [server/commands/**tests**/test_logout_command.py](server/commands/__tests__/test_logout_command.py) lives under the package (`server/commands/__tests__/`) instead of under [server/tests/](server/tests/). This diverges from the rule and can confuse discovery and tooling.
- **Missing init.py:** Only [server/tests/fixtures/](server/tests/fixtures/) subpackages (shared, unit, integration) have `__init__.py`. The directories [server/tests/](server/tests/), [server/tests/unit/](server/tests/unit/), and [server/tests/integration/](server/tests/integration/) do **not** have `__init__.py`, so they are not declared as packages. The rule recommends adding `__init__.py` to avoid name collisions and support structured imports.

**Actions:**

- Add `__init__.py` (empty or with a short docstring) to:
  - `server/tests/`
  - `server/tests/unit/`
  - `server/tests/integration/`
  - Any other test subdirectory that is a direct parent of `test_*.py` and does not yet have one (e.g. `server/tests/unit/api/`, `server/tests/unit/commands/`, etc.) so that all test directories are consistent packages.
- Move the contents of [server/commands/**tests**/test_logout_command.py](server/commands/__tests__/test_logout_command.py) into a new (or existing) module under `server/tests/unit/commands/` (e.g. `test_logout_command.py`), update imports and any references (e.g. pytest collection, CI), then remove `server/commands/__tests__/` or leave it empty with a note. Ensure the test class and fixtures (e.g. `mock_request`, `mock_current_user`) are preserved and still discovered.

### 1.3 Test naming (multiple behaviors in one test name)

**Rule:** Test names should read like sentences; avoid names that suggest testing multiple unrelated behaviors (e.g. "test_create_user_and_email").

**Finding:** Some test names use "and" in a way that could imply two behaviors (e.g. [server/tests/unit/realtime/test_websocket_handler_core.py](server/tests/unit/realtime/test_websocket_handler_core.py) has `test_validate_player_and_persistence_*`, [server/tests/integration/test_party_flow.py](server/tests/integration/test_party_flow.py) has `test_party_invite_join_leave_disband_state_and_events`). Several of these are a single flow or single concern; the name is just long. No strict violation if each test still has one logical behavior.

**Action:** Light audit only. Rename or split tests where the name clearly describes two distinct behaviors and the test body actually asserts both. Leave names that describe one scenario (e.g. one flow with multiple steps) as-is. Document in the plan or in a short test-style note: "Prefer one logical behavior per test; names with 'and' are acceptable when they describe a single scenario."

---

## 2. Fixtures and dependency injection

### 2.1 autouse fixtures

**Rule:** "Avoid autouse=True unless truly global, non-interfering setups."

**Finding:** Multiple `autouse=True` fixtures exist:

| Location                                                                                                                             | Fixture                             | Purpose                             |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ----------------------------------- |
| [server/tests/conftest.py](server/tests/conftest.py)                                                                                 | `ensure_test_environment_variables` | Set env vars before each test       |
| [server/tests/conftest.py](server/tests/conftest.py)                                                                                 | `reset_config_singleton`            | Reset config before/after each test |
| [server/tests/conftest.py](server/tests/conftest.py)                                                                                 | `deterministic_random_seed`         | `random.seed(42)`                   |
| [server/tests/conftest.py](server/tests/conftest.py)                                                                                 | `configure_event_loop_policy`       | Event loop policy (session)         |
| [server/tests/fixtures/integration/**init**.py](server/tests/fixtures/integration/__init__.py)                                       | `db_cleanup`                        | Truncate DB after each test         |
| [server/tests/unit/auth/conftest.py](server/tests/unit/auth/conftest.py)                                                             | `set_auth_epoch_for_tests`          | Set auth epoch for token tests      |
| [server/tests/unit/auth/test_auth_utils.py](server/tests/unit/auth/test_auth_utils.py)                                               | `setup_jwt_secret`                  | Set JWT secret env                  |
| [server/tests/unit/infrastructure/test_npc_database.py](server/tests/unit/infrastructure/test_npc_database.py)                       | `reset_state`                       | Reset NPC DB state                  |
| [server/tests/unit/infrastructure/test_database_init.py](server/tests/unit/infrastructure/test_database_init.py)                     | `reset_db`                          | Reset DatabaseManager state         |
| [server/tests/unit/infrastructure/test_database_helpers.py](server/tests/unit/infrastructure/test_database_helpers.py)               | `reset_db`                          | Same                                |
| [server/tests/unit/infrastructure/test_database_extended.py](server/tests/unit/infrastructure/test_database_extended.py)             | (similar)                           | Same                                |
| [server/tests/unit/infrastructure/test_database_error_handling.py](server/tests/unit/infrastructure/test_database_error_handling.py) | (similar)                           | Same                                |

**Action:** For each autouse fixture, add a one-line comment above the decorator justifying that it is "truly global" or "required for test isolation in this module." Conftest and integration cleanup fixtures are good candidates for "truly global / isolation." Module-level resets (e.g. `reset_db`, `reset_state`) can be justified as "module-level isolation." No need to remove autouse where the comment documents the rationale.

### 2.2 Fixture type hints

**Rule:** "Apply type hints to test code, especially for fixtures and complex test functions."

**Finding:** Root [server/tests/conftest.py](server/tests/conftest.py) uses `Generator[None, None, None]` for some fixtures (good). Many fixtures elsewhere lack return or parameter types (e.g. [server/tests/unit/test_alias_storage.py](server/tests/unit/test_alias_storage.py) `temp_storage_dir`, `alias_storage`; [server/tests/unit/services/test_combat_turn_processor.py](server/tests/unit/services/test_combat_turn_processor.py) `mock_combat_service`, `combat_turn_processor`).

**Action:** Add return type hints to fixtures in high-traffic or recently touched test modules first (e.g. `Path`, `AliasStorage`, `MagicMock`, `CombatTurnProcessor`, or appropriate unions). Prefer incremental rollout: conftest and one or two representative unit modules, then expand. Use `Generator[...]` or `Iterator[...]` for fixtures that `yield`, and concrete types where possible.

---

## 3. Single-assert and test focus

**Rule:** "Each test should verify one specific behavior."

**Finding:** Some tests use multiple asserts to describe one behavior (e.g. [server/tests/unit/auth/test_auth_utils.py](server/tests/unit/auth/test_auth_utils.py) and [server/tests/unit/auth/test_argon2_utils.py](server/tests/unit/auth/test_argon2_utils.py): `test_hash_password_success` asserts `isinstance`, `!= password`, and `len(hashed) > 0`). [server/tests/unit/services/test_combat_turn_processor.py](server/tests/unit/services/test_combat_turn_processor.py) `test_combat_turn_processor_init` has two asserts on `_combat_service`. These are single-behavior tests with multiple checks; the rule’s anti-pattern is one test that asserts two different behaviors (e.g. "user creation and email sending").

**Action:** No mandatory refactor. Optionally, where multiple asserts clearly represent one outcome (e.g. "hash is non-empty string different from input"), consider a single compound check or a short comment: "# Single behavior: hash output shape." Do not split into multiple tests that each assert one of these unless it improves clarity. Prefer splitting only when a test name and body clearly cover two distinct behaviors.

---

## 4. Mocking: monkeypatch vs mocker

**Rule:** Prefer the `mocker` fixture (pytest-mock) for mocking; "monkeypatch is fine for simple cases."

**Finding:** Four files use `monkeypatch`: [server/tests/unit/services/test_combat_turn_processor.py](server/tests/unit/services/test_combat_turn_processor.py), [server/tests/unit/test_alias_storage.py](server/tests/unit/test_alias_storage.py), [server/tests/unit/auth/test_auth_utils.py](server/tests/unit/auth/test_auth_utils.py), [server/tests/unit/auth/test_argon2_utils.py](server/tests/unit/auth/test_argon2_utils.py). Uses are mostly simple (e.g. `setenv`, `setattr`). The rule allows simple cases to stay with monkeypatch.

**Action:** Keep current monkeypatch usage for simple env/attr patches. When adding new tests that need multiple patches or mock assertions (e.g. `assert_called_once`), use the `mocker` fixture. Add a one-line comment in [server/tests/conftest.py](server/tests/conftest.py) or [server/tests/README.md](server/tests/README.md): "Use mocker for multi-patch or call assertions; monkeypatch for simple setenv/setattr."

---

## 5. Implementation order and risk

- **Low risk:** Add `__init__.py` files; add justification comments to autouse fixtures; add fixture type hints in a few modules.
- **Medium risk:** Move [server/commands/**tests**/test_logout_command.py](server/commands/__tests__/test_logout_command.py) to [server/tests/unit/commands/](server/tests/unit/commands/) and update imports/CI so all tests still run and collection is unchanged.
- **Documentation only:** Project layout note (Option A); mocking guidance comment in conftest or test README.

---

## 7. Detailed Todos

- **PY-1 — Project layout (Option A)**
  - PY-1.1 Add to [server/tests/README.md](server/tests/README.md) a short note that the project uses a top-level `server/` package (not `src/`) and that tests are run from project root via `make test` so imports resolve correctly.
- **PY-2 — Mocking guidance**
  - PY-2.1 Add one-line comment to [server/tests/conftest.py](server/tests/conftest.py) or [server/tests/README.md](server/tests/README.md): "Use mocker for multi-patch or call assertions; monkeypatch for simple setenv/setattr."
- **PY-3 — Test package init.py**
  - PY-3.1 Add `__init__.py` to `server/tests/`.
  - PY-3.2 Add `__init__.py` to `server/tests/unit/`.
  - PY-3.3 Add `__init__.py` to `server/tests/integration/`.
  - PY-3.4 Add `__init__.py` to any other test subdirectory that is a direct parent of `test_*.py` and does not have one (e.g. `server/tests/unit/api/`, `server/tests/unit/commands/`, etc.); enumerate once and add in batch.
- **PY-4 — Move logout command tests**
  - PY-4.1 Create or identify target file under `server/tests/unit/commands/` (e.g. `test_logout_command.py`).
  - PY-4.2 Move/copy contents of [server/commands/**tests**/test_logout_command.py](server/commands/__tests__/test_logout_command.py) into that file; fix imports to use `server.*` from project root.
  - PY-4.3 Verify pytest collects the moved tests; update CI or references if needed.
  - PY-4.4 Remove or empty [server/commands/**tests**/](server/commands/__tests__/) and add a note if the directory is kept.
- **PY-5 — autouse fixture justification**
  - PY-5.1 Add one-line justification comment above each autouse fixture in [server/tests/conftest.py](server/tests/conftest.py) (ensure_test_environment_variables, reset_config_singleton, deterministic_random_seed, configure_event_loop_policy).
  - PY-5.2 Add one-line justification for `db_cleanup` in [server/tests/fixtures/integration/**init**.py](server/tests/fixtures/integration/__init__.py).
  - PY-5.3 Add one-line justification for `set_auth_epoch_for_tests` in [server/tests/unit/auth/conftest.py](server/tests/unit/auth/conftest.py).
  - PY-5.4 Add one-line justification for `setup_jwt_secret` in [server/tests/unit/auth/test_auth_utils.py](server/tests/unit/auth/test_auth_utils.py).
  - PY-5.5 Add one-line justification for `reset_state` in [server/tests/unit/infrastructure/test_npc_database.py](server/tests/unit/infrastructure/test_npc_database.py).
  - PY-5.6 Add one-line justification for `reset_db` in test_database_init.py, test_database_helpers.py, test_database_extended.py, test_database_error_handling.py.
- **PY-6 — Fixture type hints**
  - PY-6.1 Add return type hints to fixtures in [server/tests/conftest.py](server/tests/conftest.py) where missing.
  - PY-6.2 Add return type hints to fixtures in [server/tests/unit/test_alias_storage.py](server/tests/unit/test_alias_storage.py) (e.g. temp_storage_dir, alias_storage).
  - PY-6.3 Add return type hints to fixtures in [server/tests/unit/services/test_combat_turn_processor.py](server/tests/unit/services/test_combat_turn_processor.py) (e.g. mock_combat_service, combat_turn_processor).
- **PY-7 — Test naming audit (optional)**
  - PY-7.1 Light audit: identify tests whose names clearly describe two distinct behaviors and whose body asserts both; rename or split only those. Leave single-flow long names as-is.
  - PY-7.2 Add to plan or [server/tests/README.md](server/tests/README.md): "Prefer one logical behavior per test; names with 'and' are acceptable when they describe a single scenario."
- **PY-8 — Verification**
  - PY-8.1 Run `make test` from project root after all changes.
  - PY-8.2 After PY-4: confirm `test_logout_command` (or equivalent) is collected and run; run `pytest --collect-only` if needed.

---

## 8. Verification

- Run `make test` (and, if applicable, `make test-comprehensive`) from project root after any move or structural change.
- Confirm no duplicate test IDs and that `test_logout_command` (or equivalent) is still collected after the move.
- Optionally run pytest with `--collect-only` to ensure all intended tests are discovered under the new layout.
