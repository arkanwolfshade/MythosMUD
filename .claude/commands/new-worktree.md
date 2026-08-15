---
description: Create a new Git branch and worktree for MythosMUD using the canonical layout and naming conventions.
argument-hint: <kind: feature|bugfix|refactor|spike|chore> <slug> [base_branch=main]
---

### Purpose

Create a new Git branch and worktree for MythosMUD under the canonical
directory layout:

- Canonical repo: `C:/projects/MythosMUD` *(confirm this still matches your setup — the original Cursor version of this command pointed at `f:/MythosMUD`)*
- Worktrees root: `C:/projects/MythosMUD-worktrees/`
- Worktree path: `C:/projects/MythosMUD-worktrees/<kind>-<slug>`
- Branch name: `<kind>/<slug>`

This command is a thin, focused automation layer around the workflow defined in
the `mythosmud-worktree-workflow` skill.

### Arguments

$ARGUMENTS should contain, in order:

- `kind`: one of `feature`, `bugfix`, `refactor`, `spike`, `chore` (required)
- `slug`: short, kebab-case identifier for the task, e.g. `npc-aggro`, `client-message-desync` (required)
- `base_branch`: branch to base the new worktree branch on (optional, defaults to `main`)

### Behavior

The command will:

1. **Derive names and paths**
   - Branch: `<kind>/<slug>`
   - Worktree path: `<worktrees-root>/<kind>-<slug>`

2. **Ensure canonical repo context**
   - Run from the canonical repo root.
   - Optionally show: `git status`, `git worktree list`

3. **Verify base branch**
   - Default `base_branch` to `main` if not provided.
   - Run: `git show-ref --verify --quiet refs/heads/<base_branch>`
   - If that fails, check: `git show-ref --verify --quiet refs/remotes/origin/<base_branch>`
   - If the base branch does not exist, stop and report the error instead of guessing.

4. **Create worktrees root if needed**
   - If the worktrees root does not exist, create it.

5. **Create the worktree**
   - From the canonical repo root, run:

     ```powershell
     git worktree add <worktrees-root>/<kind>-<slug> -b <kind>/<slug> <base_branch>
     ```

   - This creates both the new branch and the new worktree.

6. **Report results and next steps**
   - Print or summarize the new branch name and worktree path.
   - Remind the caller to:
     - Open the new worktree path in a new editor window.
     - Create a plan file for the new worktree using the standard plan template once it exists.

### Usage Notes for Agents

- **PowerShell only**: All shell commands must be valid in PowerShell on this project. Do not chain commands with
  `&&`; use separate tool calls.
- **No nested worktrees**: Always operate from the canonical repo root as the Git root when running `git worktree`
  commands.
- **Server rules still apply**:
  - Creating a new worktree does **not** start the server.
  - When later starting the MythosMUD server for this worktree, follow the server-management rules:
    - Run `./scripts/stop_server.ps1` first.
    - Start the server only once and only from the active worktree.

---

*Ported from `.cursor/commands/new-worktree.md`.*
