# test_nats_service_health.py

> 51 nodes

## Key Concepts

- **safe_run_static()** (28 connections) — `scripts/utils/safe_subprocess.py`
- **safe_run()** (22 connections) — `scripts/utils/safe_subprocess.py`
- **safe_subprocess.py** (21 connections) — `scripts/utils/safe_subprocess.py`
- **worktree-ops.py** (11 connections) — `scripts/worktree-ops.py`
- **get_project_root()** (8 connections) — `scripts/worktree-ops.py`
- **get_current_worktree()** (7 connections) — `scripts/worktree-ops.py`
- **install_dependencies()** (6 connections) — `scripts/worktree-ops.py`
- **main()** (6 connections) — `scripts/worktree-ops.py`
- **run_format()** (6 connections) — `scripts/worktree-ops.py`
- **run_lint()** (6 connections) — `scripts/worktree-ops.py`
- **run_tests()** (6 connections) — `scripts/worktree-ops.py`
- **show_status()** (6 connections) — `scripts/worktree-ops.py`
- **validate_path()** (5 connections) — `scripts/utils/safe_subprocess.py`
- **sqlint.py** (5 connections) — `scripts/sqlint.py`
- **run_psql_command()** (4 connections) — `scripts/load_seed_data.py`
- **_resolve_sqlint_cmd()** (4 connections) — `scripts/sqlint.py`
- **validate_command()** (4 connections) — `scripts/utils/safe_subprocess.py`
- **run_command()** (4 connections) — `scripts/worktree-ops.py`
- **main()** (3 connections) — `scripts/load_seed_data.py`
- **_is_tool_crash()** (3 connections) — `scripts/sqlint.py`
- **install.py** (3 connections) — `scripts/install.py`
- **load_seed_data.py** (3 connections) — `scripts/load_seed_data.py`
- **Path** (3 connections)
- **get_project_root()** (2 connections) — `scripts/install.py`
- **bandit.py** (2 connections) — `scripts/bandit.py`
- *... and 26 more nodes in this community*

## Relationships

- [INDEX.md](INDEX.md.md) (6 shared connections)
- [test_validation.py](test_validation.py.md) (4 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (4 shared connections)
- [Domain Model Anemic Anti-Pattern Audit](Domain_Model_Anemic_Anti-Pattern_Audit.md) (3 shared connections)
- [test_connection_cleaner.py](test_connection_cleaner.py.md) (3 shared connections)
- [sample_container](sample_container.md) (3 shared connections)
- [P4 · Intent Sweep — Core Feature Issues](P4_·_Intent_Sweep_—_Core_Feature_Issues.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `scripts/bandit.py`
- `scripts/build.py`
- `scripts/format.py`
- `scripts/install.py`
- `scripts/lint.py`
- `scripts/load_seed_data.py`
- `scripts/run.py`
- `scripts/sqlfluff.py`
- `scripts/sqlint.py`
- `scripts/utils/safe_subprocess.py`
- `scripts/worktree-ops.py`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*