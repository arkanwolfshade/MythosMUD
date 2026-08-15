---
title: Worktree Task Plan Template
description: Template for per-worktree task plans in MythosMUD
---

## Metadata

- **Branch**: `<kind>/<slug>`
- **Worktree path**: `f:/MythosMUD-worktrees/<kind>-<slug>`
- **GitHub issue**: `#<issue-number-or-link>`
- **Kind**: `feature | bugfix | refactor | spike | chore`
- **Slug**: `<kebab-case-task-name>`

## Context

Briefly describe:

- What problem this worktree is solving.
- Any relevant links (issue, PR, design doc).
- Dependencies on other branches or services.

## Plan / Todos

Use this section as the authoritative checklist for the work done in this
worktree. Keep items small and concrete.

- [ ] Clarify requirements and constraints
- [ ] Add or update tests to capture desired behavior
- [ ] Implement server-side changes
- [ ] Implement client-side changes
- [ ] Implement persistence / database changes (if applicable)
- [ ] Update documentation (docs, OpenAPI, ADRs, rules/skills/commands)
- [ ] Run `make test` and verify coverage expectations
- [ ] Run formatting and linting
- [ ] Prepare commits and open PR
- [ ] Perform local cleanup after merge (worktree removal, branch cleanup)

Feel free to add or remove items based on the specific task.

## Design Notes

Capture key decisions and trade-offs here. This should be just enough to help
future you (or another investigator) understand why certain approaches were
taken.

Examples:

- Why a particular data model was chosen.
- Why a simpler implementation was rejected.
- Any known limitations or follow-up work that was deferred.

## Testing

Document how this work was tested:

- **Unit tests**:
  - Files / modules touched:
  - New or updated tests:
- **Integration / e2e**:
  - Scenarios covered:
  - Manual test steps (if any):
- **Coverage notes**:
  - Any critical paths with special coverage considerations:

## Risks and Edge Cases

List:

- Edge cases that were considered and handled.
- Edge cases that are known but intentionally out of scope.
- Any security, performance, or data migration concerns.

## Cleanup Checklist

After the worktree’s branch has been merged or abandoned:

- [ ] Confirm branch status (merged / abandoned).
- [ ] From `f:/MythosMUD`, run `git worktree list` and identify this worktree.
- [ ] Remove worktree: `git worktree remove f:/MythosMUD-worktrees/<kind>-<slug>`.
- [ ] Optionally delete branch (if merged and no longer needed).
- [ ] Close or update the associated GitHub issue.
- [ ] Leave this plan file in Git history as documentation (preferred).
