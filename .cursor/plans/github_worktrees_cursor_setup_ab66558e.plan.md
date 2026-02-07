---
name: GitHub Worktrees Cursor Setup
overview: Add Cursor-native worktree setup so new worktrees get dependencies and optional .env from the root worktree, and document how this coexists with the existing worktree-manager.ps1 and worktree-ops.py.
todos:
  - id: verify-schema
    content: Verify Cursor worktrees.json schema (Context7 or docs) for key names and array vs script path
    status: pending
  - id: create-worktrees-json
    content: Create .cursor/worktrees.json with setup-worktree, setup-worktree-windows, setup-worktree-unix (copy .env + python scripts/install.py)
    status: pending
  - id: optional-setup-scripts
    content: If schema requires script path, add scripts/setup_worktree.ps1 and scripts/setup_worktree.sh
    status: pending
  - id: doc-worktrees
    content: Add docs/development-worktrees.md (or README section) documenting Cursor worktrees and worktree-manager.ps1
    status: pending
  - id: quickstart-guide
    content: Create a quickstart guide for using worktrees to improve development (create branch, open in Cursor, run/tests)
    status: pending
  - id: verify-worktree
    content: "Verification: create a test worktree, open in Cursor or run setup manually, confirm deps install"
    status: pending
isProject: false
---

# GitHub Worktrees + Cursor Native Support

## Goal

- **Match CI/clean environments**: Each worktree gets a real install (uv + npm) so behavior matches CI and avoids symlink issues.
- **Use Cursor's Worktrees UI**: Add `.cursor/worktrees.json` so Cursor runs setup when a worktree is created or opened.

## Current State

- **Existing scripts**: [scripts/worktree-manager.ps1](scripts/worktree-manager.ps1) manages named worktrees (main, client, server, docs, testing) with fixed sibling paths; [scripts/worktree-ops.py](scripts/worktree-ops.py) and [scripts/install.py](scripts/install.py) are worktree-aware (they resolve project root and run `uv sync` + `npm install`).
- **Install flow**: [scripts/install.py](scripts/install.py) runs from project root: `uv sync --project server --all-extras --dev`, `uv run --active pre-commit install -f`, then `npm install` in `client/`. CI uses `npm ci` in client for lockfile fidelity.
- **No Cursor worktree config yet**: [.cursor/](.cursor/) exists but there is no `worktrees.json`.

## 1. Add `.cursor/worktrees.json`

Cursor runs the configured commands in the **worktree directory** (the new checkout). The environment variable for the root worktree path is:

- **Windows**: `%ROOT_WORKTREE_PATH%`
- **Unix**: `$ROOT_WORKTREE_PATH`

**Recommended content:**

- **setup-worktree-windows** (array of commands, or a single script path relative to the file):
  1. Optional: if `.env` exists in `ROOT_WORKTREE_PATH`, copy it into the worktree root so the new worktree has the same env (e.g. `if (Test-Path "$env:ROOT_WORKTREE_PATH\.env") { Copy-Item "$env:ROOT_WORKTREE_PATH\.env" ".env" }`).
  2. Install dependencies: run the same steps as the repo (real installs, not symlinks). Prefer invoking the existing installer so one place defines the steps:
    - **Option A**: `python scripts/install.py` (from worktree root). install.py is worktree-aware and runs uv + npm from project root; in a Cursor-created worktree the “project root” is the worktree root, so this works.
    - **Option B**: inline commands: `uv sync --project server --all-extras --dev`, then `uv run --active pre-commit install -f`, then `cd client && npm install` (or `npm ci` for CI-like).
- **setup-worktree-unix**: same logic with `$ROOT_WORKTREE_PATH` and shell commands (bash).
- **setup-worktree**: fallback for other platforms; can mirror Unix or call a small script.

Use **Option A** (call `python scripts/install.py`) to avoid duplicating logic and to stay aligned with `make install` and worktree-ops.

Example structure (Windows PowerShell-style steps; Cursor allows script path or command list):

```json
{
  "setup-worktree": ["python scripts/install.py"],
  "setup-worktree-windows": [
    "if (Test-Path \"%ROOT_WORKTREE_PATH%\\.env\") { Copy-Item \"%ROOT_WORKTREE_PATH%\\.env\" \".env\" }",
    "python scripts/install.py"
  ],
  "setup-worktree-unix": [
    "[ -f \"$ROOT_WORKTREE_PATH/.env\" ] && cp \"$ROOT_WORKTREE_PATH/.env\" .env",
    "python scripts/install.py"
  ]
}
```

If Cursor expects a single script path instead of an array, use a small wrapper script (e.g. `scripts/setup_worktree.ps1` and `scripts/setup_worktree.sh`) that:

1. Copy `.env` from `ROOT_WORKTREE_PATH` when present.
2. Run `python scripts/install.py` (or `make install`).

Verify against [Cursor worktrees docs](https://docs.cursor.com/context/worktrees) (or Context7) for exact key names and whether entries are arrays of strings or paths to scripts.

## 2. install.py behavior in a Cursor worktree

In a Cursor-created worktree, the working directory is the **worktree root** (the repo root for that branch). [scripts/install.py](scripts/install.py) uses `get_project_root()` which returns the parent directory only when `cwd` contains one of `MythosMUD-server`, `MythosMUD-client`, etc. So when you open a **single** worktree (one folder = whole repo), `get_project_root()` returns `current_dir` and install runs correctly from that root. No change to install.py is required for the “one worktree = one repo root” case.

## 3. Coexistence with worktree-manager.ps1 and worktree-ops.py

- **worktree-manager.ps1**: Predefined named worktrees (main, client, server, docs, testing) with fixed paths. Use it for that layout and for `list` / `switch` / `cleanup`.
- **worktree-ops.py**: Used by Codacy and other scripts; remains the source of truth for “am I in a worktree and where is project root?”
- **Cursor worktrees**: Typically one worktree per branch/folder. `.cursor/worktrees.json` only runs setup when Cursor creates/opens a worktree; it does not replace the PowerShell manager. Document in README or a short `docs/worktrees.md` that:
  - Cursor’s Worktrees UI uses `.cursor/worktrees.json` for setup.
  - For the named worktree layout (E:\…\MythosMUD, MythosMUD-client, etc.), continue using `scripts/worktree-manager.ps1` and `make install` (or install.py) from the chosen worktree.

## 4. Optional: script path vs array of commands

Context7 notes that setup can be “array of shell commands” or “path to a script”. If the copy-.env step is awkward as inline PowerShell/Bash in JSON, add two small scripts and point Cursor at them:

- **scripts/setup_worktree.ps1**: copy .env from `$env:ROOT_WORKTREE_PATH` if present; then `python scripts/install.py`.
- **scripts/setup_worktree.sh**: same for Unix.

Then in `worktrees.json` set e.g. `"setup-worktree-windows": "scripts/setup_worktree.ps1"` (if the schema supports a string path). Otherwise keep the array form and use minimal one-line commands.

## 5. Documentation

- Add a short section in the main README or create **docs/development-worktrees.md** describing:
  - Using Cursor’s Worktrees UI with this repo (and that setup is automatic via `.cursor/worktrees.json`).
  - Optional: using `scripts/worktree-manager.ps1` for the named multi-folder layout.
  - That `make install` / `python scripts/install.py` is worktree-aware and safe to run from any worktree root.

## 6. Quickstart guide: using worktrees to improve development

Add a **quickstart** (e.g. **docs/worktrees-quickstart.md** or a "Quickstart" section in docs/development-worktrees.md) that gives a minimal, copy-paste workflow for developers. Include:

- **Why worktrees**: Isolate feature work (branch = folder), keep main clean; match CI (fresh install per worktree); switch context without stashing.
- **Create a worktree (Git)**:
  - `git worktree add ../MythosMUD-my-feature -b my-feature` (new branch), or `git worktree add ../MythosMUD-hotfix main` (existing branch).
  - Where to put paths (e.g. sibling of main repo).
- **Open in Cursor**: File > Open Folder (or Cursor Worktrees UI if available); Cursor runs `.cursor/worktrees.json` setup (deps + optional .env copy).
- **Daily workflow**: Edit in worktree; run `make test` / `make install` from worktree root; commit and push from that folder; when done, `git worktree remove` or delete the folder and prune.
- **Optional**: One-line reminder that `scripts/worktree-manager.ps1` exists for the predefined (main/client/server/docs/testing) layout.

Keep the quickstart to one short page so it stays scannable.

## Files to add/change


| Action   | File                                                                                                                                                            |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create   | [.cursor/worktrees.json](.cursor/worktrees.json) with setup-worktree, setup-worktree-windows, setup-worktree-unix (and optional scripts if needed).             |
| Optional | [scripts/setup_worktree.ps1](scripts/setup_worktree.ps1) and [scripts/setup_worktree.sh](scripts/setup_worktree.sh) if using script path.                       |
| Optional | [docs/development-worktrees.md](docs/development-worktrees.md) or README section for worktrees + Cursor.                                                        |
| Create   | [docs/worktrees-quickstart.md](docs/worktrees-quickstart.md) (or Quickstart section in development-worktrees.md) – how to use worktrees to improve development. |


## Verification

- Create a new worktree (e.g. `git worktree add ../MythosMUD-feature feature-branch`), open it in Cursor, and confirm Cursor runs the setup (or run the same steps manually and confirm deps install).
- Ensure no duplicate or conflicting logic with install.py and worktree-ops.py.
