# Claude / non-Cursor agent routing (MythosMUD)

**Authoritative consolidated instructions for AI agents:** see the repo root
[`AGENTS.md`](AGENTS.md).

- **Cursor IDE:** `.cursor/rules/` remains the granular, canonical project rule set loaded by Cursor.
- **Sync:** When you add or change rules in `.cursor/rules/` or Cursor agents/skills, update
  [`AGENTS.md`](AGENTS.md). Keep [`.github/copilot-instructions.md`](.github/copilot-instructions.md) and this file as
  routers to `AGENTS.md` (no second copy of the rules).

This file intentionally stays small so Claude Code and other tools can delegate to `AGENTS.md` without duplicating
guidance.
