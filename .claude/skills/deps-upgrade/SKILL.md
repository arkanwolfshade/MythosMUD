---
name: deps-upgrade
description: Plan and execute safe, incremental dependency upgrades for MythosMUD (Python via uv, client via npm). Use when the user asks to upgrade dependencies, bump a package version, or address a Dependabot alert.
disable-model-invocation: true
---

# Dependency Upgrade

MythosMUD has two dependency ecosystems: Python (`pyproject.toml`, managed by `uv`) and the
client (`client/package.json`, managed by `npm`). This is a manual-trigger workflow
(`disable-model-invocation: true`) since dependency bumps are side-effecting and can introduce
breaking changes — invoke it explicitly rather than letting it auto-fire.

## Before starting

- Check for an open Dependabot PR first — many routine bumps are already automated (see the
  Dependabot alert comments already present in `pyproject.toml` for prior CVE-driven pins).
- Confirm what's actually outdated:
  - Python: `uv pip list --outdated` (or check `pyproject.toml` version pins against PyPI)
  - Client: `cd client && npm outdated`

## Upgrade procedure

1. **Branch first** — never bump on `main` directly; use the `mythosmud-worktree-workflow`
   skill or a plain feature branch.
2. **One ecosystem, one logical change at a time.** Don't mix an unrelated Python bump with a
   client bump in the same commit unless they're part of the same CVE remediation.
3. **Patch/minor bumps**: apply, then run the full check:
   - `make lint && make mypy && make test` (Python side)
   - `cd client && npm run lint && npm run test:unit` (client side)
4. **Major bumps**: read the package's actual changelog/migration guide before touching code —
   don't guess at breaking changes. Check this repo's own usage of the package
   (`search_symbols`/`find_references` via jCodemunch) to scope the blast radius before editing.
5. **Security-flagged bumps** (Dependabot alert, `npm audit`, or a CVE mentioned in a
   `pyproject.toml` comment): treat as priority — these routinely get pinned inline in this
   repo's `pyproject.toml` with a comment explaining the alert number, follow that existing
   convention for new pins.

## Verify

Run the full pipeline before considering the upgrade done:
`make format && make mypy && make lint && make test` — same bar as any other change
(see the `mythosmud-pre-commit-checklist` skill).

## Rollback

`git checkout -- pyproject.toml uv.lock` (or `client/package.json client/package-lock.json`),
then reinstall (`uv sync` / `npm ci`). If already committed, revert the commit rather than
hand-editing lockfiles back.

## Never

- Bump a major version and assume it "probably still works" without reading what changed
- Silence a new lint/type error introduced by the upgrade instead of fixing it
- Edit `uv.lock`/`package-lock.json` by hand — always regenerate via the package manager
