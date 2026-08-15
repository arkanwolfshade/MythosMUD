---
name: git-workflow
description: Git branching, commit message, and history-hygiene conventions. Use when creating a branch, writing a commit message, rebasing, or resolving merge conflicts.
---

# Git Workflow

## Branching

Feature-branch workflow off `main` (this repo has no `develop` branch — the vendored version
of this doc that mentioned one was wrong for this repo). Never commit directly to `main`.

Branch naming: `<type>/<short-description>`, e.g. `feat/aggro-radius`, `fix/npc-aggro-reset`,
`refactor/combat-logging`. See the `mythosmud-worktree-workflow` skill for the full worktree +
branch naming convention this repo actually uses (`<kind>/<slug>` where kind is
feature/bugfix/refactor/spike/chore).

## Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
`<type>(<scope>): <description>` — `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`,
`build`, `ci`, `chore`, `revert`. Concise, imperative, present tense. Link issues with `#number`.
See the `mythosmud-commit-messages` skill for repo-specific commit generation.

Each commit should be one logical change — don't bundle an unrelated fix into a feature commit.

## History hygiene

- Rebase feature branches onto `main` before opening a PR; squash WIP commits into logical
  units. Only force-push your own unmerged/unshared branches
  (`git push --force-with-lease`) — never force-push `main`.
- Merge via PR with `--no-ff` (or the platform's merge-commit equivalent) so branch context is
  preserved in history.
- Pull frequently to minimize conflict scope (`git pull --rebase`).
- Resolve conflicts manually and understand each hunk — never blindly `--theirs`/`--ours`.

## Repository hygiene

- Keep `.gitignore` comprehensive: build artifacts, dependencies, IDE files, secrets/env files.
- Never commit large binaries directly — use Git LFS for anything that isn't source.
- Pre-commit hooks in this repo run through `pre-commit` (see `.pre-commit-config.yaml`) with
  Ruff for Python formatting/linting — not Black (see `.claude/rules/black.md` for why).

## Never

- Force-push a shared/merged branch
- Commit secrets, `.env` files, or credentials
- Rewrite history on `main`
