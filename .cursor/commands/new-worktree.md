---
name: new-worktree
description: >
  Create a new Git branch and worktree for MythosMUD using the canonical
  layout and naming conventions.
arguments:
  kind:
    description: >
      Type of work. One of: feature, bugfix, refactor, spike, chore.
    required: true
  slug:
    description: >
      Short kebab-case identifier for the task (e.g. npc-aggro, client-message-desync).
    required: true
  base_branch:
    description: >
      Name of the branch to base the new worktree branch on. Defaults to main.
    required: false
---

### Purpose

Create a new Git branch and worktree for MythosMUD under the canonical
directory layout:

- Canonical repo: `f:/MythosMUD`
- Worktrees root: `f:/MythosMUD-worktrees/`
- Worktree path: `f:/MythosMUD-worktrees/<kind>-<slug>`
- Branch name: `<kind>/<slug>`

This command is a thin, focused automation layer around the workflow defined in
`.cursor/rules/worktrees.mdc` and the `mythosmud-worktree-workflow` skill.

### Behavior

Given:

- `kind`: one of `feature`, `bugfix`, `refactor`, `spike`, `chore`
- `slug`: short, kebab-case description
- `base_branch` (optional, default `main`)

The command will:

1. **Derive names and paths**
   - Branch: `<kind>/<slug>`
   - Worktree path: `f:/MythosMUD-worktrees/<kind>-<slug>`

2. **Ensure canonical repo context**
   - Use the Shell tool with `working_directory: "f:/MythosMUD"`.
   - Optionally show:
     - `git status`
     - `git worktree list`

3. **Verify base branch**
   - Default `base_branch` to `main` if not provided.
   - Run:
     - `git show-ref --verify --quiet refs/heads/<base_branch>`
   - If that fails, check:
     - `git show-ref --verify --quiet refs/remotes/origin/<base_branch>`
   - If the base branch does not exist, stop and report the error instead of
     guessing.

4. **Create worktrees root if needed**
   - If `f:/MythosMUD-worktrees/` does not exist, create it using the Shell
     tool (PowerShell semantics).

5. **Create the worktree**
   - From `f:/MythosMUD`, run:

     ```powershell
     git worktree add f:/MythosMUD-worktrees/<kind>-<slug> -b <kind>/<slug> <base_branch>
     ```

   - This creates both:
     - The new branch `<kind>/<slug>` based on `<base_branch>`.
     - The new worktree at `f:/MythosMUD-worktrees/<kind>-<slug>`.

6. **Report results and next steps**
   - Print or summarize:
     - The new branch name.
     - The new worktree path.
   - Remind the caller:
     - Open `f:/MythosMUD-worktrees/<kind>-<slug>` in a new Cursor window.
     - Create a `.cursor/plans/` plan file in the new worktree using the
       standard worktree plan template once it exists.

### Usage Notes for Agents

- **PowerShell only**: All Shell commands must be valid in PowerShell. Do not
  chain commands with `&&`; use separate tool calls.
- **No nested worktrees**: Always operate from `f:/MythosMUD` as the Git root
  when running `git worktree` commands.
- **Server rules still apply**:
  - Creating a new worktree does **not** start the server.
  - When later starting the MythosMUD server for this worktree, follow the
    server management rules:
    - Run `./scripts/stop_server.ps1` first.
    - Start the server only once and only from the active worktree.
