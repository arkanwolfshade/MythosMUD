---
name: gh-stack
description: >-
  Manage stacked MythosMUD branches and PRs with gh stack (init, add, submit,
  sync, rebase, merge, view). Use automatically when opening PRs, syncing after
  merges, splitting reviewable layers, navigating stacks, or when the user
  mentions stack, stacked PR, gh-stack, or /gh-stack.
---

# gh-stack (MythosMUD)

Authoritative command reference for agents:
[`.agents/skills/gh-stack/SKILL.md`](../../../.agents/skills/gh-stack/SKILL.md)

This file is the **project trigger surface**. Follow the full skill for flags,
exit codes, and conflict recovery. Defaults below are Mythos-specific.

## Mythos defaults

| Item         | Default                                                                    |
| ------------ | -------------------------------------------------------------------------- |
| Trunk        | `main` (`gh stack init --base main ...` when not on default trunk)         |
| Remote       | `origin` (pass `--remote origin` if a command requires an explicit remote) |
| New PRs      | Drafts via `gh stack submit --auto`; add `--open` when requesting review   |
| Merge        | `gh stack merge --yes` (optional `--squash` / `--rebase` / `--merge`)      |
| Commit style | `mythosmud-commit-messages` skill, then stack for push/PR                  |

Do not write `git config` unless the user asks. Prefer CLI flags over config.

## Automatic decision tree

1. **Need stack status?** → `gh stack view --json`
2. **Not in a stack, multi-layer or user wants stack?** →
   `gh stack init <branch> [layer2 ...]` (names verbatim; adopt existing branches)
3. **Next layer / concern?** → commit current layer, then `gh stack add <branch>`
4. **Push + create/update PRs?** → `gh stack submit --auto` (`--open` if ready)
5. **Trunk moved / PR squash-merged?** → `gh stack sync` (`--prune` optional)
6. **Edit lower layer while upstack?** → go down, commit, `gh stack rebase --upstack`
7. **Merge?** → `gh stack merge --yes` (not bare `gh pr merge` for stacks)

## Forbidden (hangs non-interactive agents)

- `gh stack view` without `--json`
- `gh stack submit` without `--auto`
- `init` / `add` / `checkout` without positional arguments

## Integration with other skills

| Skill / intent                 | Stack behavior                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| Opening a PR / new branch + PR | Prefer stack submit when branched is/part of a stack or layered                                  |
| review-and-ship                | After review/fixes: `submit --auto` or `push` if PRs exist                                       |
| make-pr-easy-to-review         | Prefer one concern per stack layer                                                               |
| loop-on-ci / fix-ci            | Stay on stack branch; use stack navigation; do not rewrite bases ad hoc                          |
| worktree workflow              | One worktree per **task/stack story**; stack branches share that worktree unless user opens more |

## One-liner status check (PowerShell)

```powershell
gh stack view --json
```

If stderr says the branch is not part of a stack, either stay single-PR or
`gh stack init` with the current branch name.

## Full skill body

For workflows, mid-stack fixes, conflict recovery, and the complete command set,
**read** [`.agents/skills/gh-stack/SKILL.md`](../../../.agents/skills/gh-stack/SKILL.md)
and execute those steps non-interactively.
