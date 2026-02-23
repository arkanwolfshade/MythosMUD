# Dead Code Definition and Tooling

This document describes how MythosMUD defines and manages dead code, and where allowlists live.

## Definition

- **Truly dead**: Code unreachable from application entry points and not referenced by tests or
  tooling. Safe to remove.
- **Unused exports / optional dead**: Symbols exported but never imported (including from tests).
  Treat separately; remove only after confirming they are not public API or reserved for future use.

Code used only by tests is **not** considered truly dead; list it separately and do not remove by
default.

## Entry Points

- **Server:** `server/main.py` → `server/app/factory.py` `create_app` and registered routers/lifespan.
- **Client:** `client/src/main.tsx` → AppRouter → App (and lazy Map/Skills).

## Tooling

- **Server (Python):** [vulture](https://github.com/jendrikseipp/vulture). Config and paths in
  `pyproject.toml` under `[tool.vulture]`. Allowlist file: **`vulture_allowlist.py`** at repo root
  (valid Python that references intentional "unused" names).
- **Client (TypeScript):** [knip](https://github.com/webpro/knip). Run with `npm run knip` in
  `client/`. Config: **`client/knip.json`** (entry, project, ignoreDependencies).

## Allowlist / Do Not Remove

- **Server:** Side-effect imports (e.g. router registration, `server/models` re-exports), reserved
  stubs (`combat_service`, `command_parser`), FastAPI `_request` convention. See
  `vulture_allowlist.py` and `pyproject.toml` `[tool.vulture]`.
- **Client:** Test utilities and components only used in tests; `_`-prefixed args/vars. Exclude or
  allowlist in `client/knip.json` as needed.

## Reports

- **Server:** `dead-code-server.txt` (from `uv run vulture`).
- **Client:** `dead-code-client.txt` (from `npm run knip` in client).

## Plan Reference

Full workflow and phases: `.cursor/plans/dead_code_analysis_and_removal_746bc5c1.plan.md`.
