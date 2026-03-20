---
name: mythosmud-worktree-workflow
description: >
  Create and manage Git worktrees for MythosMUD using the canonical layout and
  naming conventions. Use this when starting a new feature/bugfix/refactor
  branch or cleaning up after a task is done.
---

# MythosMUD Worktree Workflow

> "We do not perform our experiments on the original Necronomicon, Prof.
> Wolfshade. We work from carefully labeled copies, stored in separate
> cabinets."

This skill guides the agent through creating, using, and cleaning up Git
worktrees for MythosMUD according to the `worktrees.mdc` rule.

## When to Use

Use this skill when:

- The user asks to:
  - Start a new feature/bugfix/refactor/spike/chore branch.
  - "Spin up a worktree" or "create a new working copy" for MythosMUD.
  - Work on a specific GitHub issue in isolation.
  - Remove or clean up completed/stale worktrees.
- You want to avoid editing multiple tasks in the same working copy.

## Canonical Layout (Summary)

Follow `.cursor/rules/worktrees.mdc`:

- Canonical repo: `f:/MythosMUD`
- Worktrees root: `f:/MythosMUD-worktrees/`
- Worktree path pattern: `f:/MythosMUD-worktrees/<kind>-<slug>`
- Branch name pattern: `<kind>/<slug>`
- `<kind>`: one of `feature`, `bugfix`, `refactor`, `spike`, `chore`
- `<slug>`: short, kebab-case description (e.g. `npc-aggro`, `client-message-desync`)

## Preconditions and Safety

- You are working on Windows with PowerShell; **do not** chain commands with
  `&&`. Run each command separately via the Shell tool.
- **Never** create a worktree inside `.git/` or nested inside another
  worktree. Only use:
  - `f:/MythosMUD` (canonical)
  - `f:/MythosMUD-worktrees/` (additional worktrees)
- Respect the **ONE SERVER ONLY RULE**:
  - Do not start multiple MythosMUD servers, even across worktrees.
  - Always run `./scripts/stop_server.ps1` before switching the active task
    worktree that owns the server.

## Skill: Create a New Worktree for a Task

This procedure assumes the Git repository root is `f:/MythosMUD` and that the
worktrees root `f:/MythosMUD-worktrees/` exists (or can be created).

### Step 1 — Gather Task Metadata

Ask (or infer from the conversation) the following:

1. `kind`:
   - One of: `feature`, `bugfix`, `refactor`, `spike`, `chore`.
   - If ambiguous, prefer:
     - `bugfix` for defect work.
     - `feature` for new behavior.
     - `refactor` for structural/cleanup work.
2. `slug`:
   - Short, kebab-case summary of the task, usually from the issue title.
   - Examples: `npc-aggro`, `client-message-desync`, `combat-logging`.
3. Optional `base_branch`:
   - Default to `main` (or whatever the project standard indicates if
     documented elsewhere).
   - Use an explicit base if the user requests one (e.g. `feature/aggro`).

### Step 2 — Derive Names and Paths

Compute:

- Branch name: `<kind>/<slug>`
- Worktree path: `f:/MythosMUD-worktrees/<kind>-<slug>`

Record these in your reasoning and, when appropriate, surface them to the user
for confirmation.

### Step 3 — Ensure Canonical Repo Context

Use the Shell tool to:

1. Change directory to the canonical repo:
   - `cd f:/MythosMUD`
2. Optionally, show current worktrees and branches for context:
   - `git status`
   - `git worktree list`

Do **not** rely on relative paths; always use the explicit `working_directory`
argument when invoking Shell commands.

### Step 4 — Fetch and Validate Base Branch

From `f:/MythosMUD`:

1. Update remote refs:
   - `git fetch`
2. Verify the base branch exists:
   - `git show-ref --verify --quiet refs/heads/<base_branch>`
   - If it does not exist locally, try:
     - `git show-ref --verify --quiet refs/remotes/origin/<base_branch>`
     - If only remote exists, you may need to create a local tracking branch
       if you intend to base new work on it.

If the base branch truly does not exist, stop and ask the user which branch to
base from instead.

### Step 5 — Create the Worktree

From `f:/MythosMUD`:

- For a **new** branch:
  - `git worktree add f:/MythosMUD-worktrees/<kind>-<slug> -b <kind>/<slug> <base_branch>`
- For an **existing** branch:
  - `git worktree add f:/MythosMUD-worktrees/<kind>-<slug> <kind>/<slug>`

Use Shell commands that are valid PowerShell invocations, one per tool call
if necessary.

After the command succeeds, optionally:

- `git worktree list`

to show the new entry.

### Step 6 — Open the Worktree in Cursor

Instruct the user to open the new worktree path in a fresh Cursor window:

- `f:/MythosMUD-worktrees/<kind>-<slug>`

Each worktree should have its own dedicated Cursor window and `.cursor/`
directory. Do not mix worktrees in a single window.

### Step 7 — Create a Task Plan in the New Worktree

In the new worktree:

1. Ensure `.cursor/plans/` exists.
2. Create a new plan file whose name matches the MythosMUD plan naming
   convention:
   - `<kind>-<slug>_<hash>.plan.md`
     - `<hash>` can be a short, stable identifier (e.g. derived from an issue
       number or a generated token).
3. Seed the plan content using the standard worktree plan template:
   - `.cursor/templates/worktree-plan-template.md`
   - Copy the template into the new plan and fill in:
     - Branch name.
     - Worktree path.
     - Short description and goals derived from the user’s request.

Use the Cursor ApplyPatch tool to create the file; do **not** directly edit in
the terminal.

## Skill: Clean Up a Completed or Stale Worktree

When a branch has been merged or a task has been abandoned:

1. Confirm status:
   - From `f:/MythosMUD`, run:
     - `git worktree list`
   - Identify the worktree path and branch you intend to remove.
   - Optionally, check branch merge status:
     - `git branch --contains <branch_name>`

2. From `f:/MythosMUD`, remove the worktree:
   - `git worktree remove f:/MythosMUD-worktrees/<kind>-<slug>`
   - If Git reports that the worktree is still in use or has uncommitted
     changes, surface this to the user and stop. Do not force-clean without
     explicit permission.

3. If the directory remains:
   - Verify with the Shell tool that:
     - `f:/MythosMUD-worktrees/<kind>-<slug>` is empty or no longer tracked.
   - Ask the user before deleting any non-empty directory outside of Git’s
     control.

4. Optionally clean up the branch:
   - Only if:
     - The branch has been merged and
     - The user has explicitly agreed to branch deletion.
   - `git branch -d <kind>/<slug>`

5. Update documentation:
   - If there is a plan file under `.cursor/plans/` that was specific to this
     worktree, you may:
     - Leave it as historical documentation (preferred), or
     - Add a note that the work is complete and the worktree/branch have been
       removed.

## Weekly Maintenance Pattern

When asked to review or clean up local worktrees:

1. From `f:/MythosMUD`:
   - `git worktree list`
2. For each non-canonical entry under `f:/MythosMUD-worktrees/`:
   - Check whether the corresponding branch is merged or abandoned.
   - Propose cleanup for the ones no longer needed.
3. For each worktree the user agrees to remove:
   - Follow the cleanup steps above.
4. Optionally record an overview in `TASKS.local.md` summarizing:
   - Active worktrees for the current week.
   - Recently cleaned-up worktrees.
