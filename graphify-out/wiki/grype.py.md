# grype.py

> 12 nodes · cohesion 0.26

## Key Concepts

- **grype.py** (8 connections) — `scripts/grype.py`
- **_run_grype_scan()** (5 connections) — `scripts/grype.py`
- **main()** (4 connections) — `scripts/grype.py`
- **_handle_grype_result()** (3 connections) — `scripts/grype.py`
- **merge_windows_machine_user_path_into_environ()** (3 connections) — `scripts/grype.py`
- **repo_root()** (3 connections) — `scripts/grype.py`
- **_resolve_grype_executable()** (3 connections) — `scripts/grype.py`
- **_grype_command()** (2 connections) — `scripts/grype.py`
- **CompletedProcess** (2 connections)
- **Path** (1 connections)
- **Append Machine and User Path from the registry (matches hadolint.ps1 behavior).** (1 connections) — `scripts/grype.py`
- **Return the MythosMUD project root (parent of scripts/).** (1 connections) — `scripts/grype.py`

## Relationships

- [safe_subprocess.py](safe_subprocess.py.md) (1 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)

## Source Files

- `scripts/grype.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*