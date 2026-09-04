---
title: E2E testing harness overhaul
description: Worktree plan for refactor/e2e-harness
---

## Metadata

- **Branch**: `refactor/e2e-harness`
- **Worktree path**: `c:\projects\MythosMUD-worktrees\refactor-e2e-harness`
- **GitHub issue**: `#<issue-number-or-link>`
- **Kind**: `refactor`
- **Slug**: `e2e-harness`

## Context

Overhaul the MythosMUD end-to-end testing harness: structure, fixtures, startup/teardown,
CI integration, and developer ergonomics while keeping server authority and existing test
data rules intact.

## Plan / Todos

- [ ] Inventory current E2E entry points (Playwright, scripts, Makefile, CI jobs)
- [ ] Clarify target harness shape (config, env, parallel runs, reporting)
- [ ] Add or update tests that lock in harness contracts before large moves
- [ ] Refactor harness implementation (shared helpers, timeouts, stability)
- [ ] Align documentation (runbook, CONTRIBUTING or test docs if present)
- [ ] Run `make test` / targeted E2E commands from project root as applicable
- [ ] Run formatting and linting for touched stacks
- [ ] Prepare commits and open PR toward `main`
- [ ] After merge: remove worktree per cleanup checklist

## Design Notes

(To be filled as decisions land: e.g. single vs multi-worker, artifact layout, flake retries.)

## Testing

- **Harness smoke**: Document minimal command proving harness boots app stack correctly
- **Regression**: List scenarios that must stay green after refactor

## Risks and Edge Cases

- Port conflicts and duplicate servers (enforce stop before start in docs/scripts)
- Flaky timing: prefer explicit readiness over fixed sleeps where possible

## Cleanup Checklist

- [ ] From `c:\projects\MythosMUD`, run `git worktree list`
- [ ] Remove: `git worktree remove c:\projects\MythosMUD-worktrees\refactor-e2e-harness`
- [ ] Optionally delete branch after merge
