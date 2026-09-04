---
name: Cursor-centric AI config
overview: Revise the AI configuration so the canonical rule set is Cursor-native (.cursor/rules/) per Cursor's official guidance; keep CLAUDE.md as a supporting artifact for non-Cursor tools and human reference.
todos: []
isProject: false
---

# Cursor-Centric AI Config (Revised)

## What Cursor's guidance says

From [Cursor Docs > Rules](https://cursor.com/docs/context/rules):

- **Project Rules**: Stored in `.cursor/rules`, version-controlled, scoped to the codebase. This is the **primary** location for project rules.
- **AGENTS.md**: "Simple alternative to .cursor/rules" — plain markdown in project root for straightforward instructions.
- **.cursorrules**: "Legacy... still supported but will be deprecated. We recommend migrating to Project Rules or to AGENTS.md."

**CLAUDE.md is not part of Cursor's rule hierarchy.** Using CLAUDE.md as the canonical rule set is therefore **not** a Cursor best practice. For Cursor as your primary tool, the canonical rule set should be **.cursor/rules/** (which you already use).

---

## Revised direction: .cursor/rules as canonical

- **Canonical rule set**: [.cursor/rules/](.cursor/rules/) (existing `.mdc` files). No change to where Cursor reads rules; this is the source of truth for Cursor.
- **.cursorrules**: Minimal stub only. State "see .cursor/rules/ and AGENTS.md" so Cursor still has a root file until you fully migrate. No long content; Cursor recommends migrating to Project Rules or AGENTS.md.
- **CLAUDE.md**: **Supporting** artifact only — for Claude Code, Agent OS, or human-readable reference. State at the top that the **canonical** rules for Cursor are in `.cursor/rules/`. Keep the rest as a consolidated snapshot for environments that cannot read Cursor rules (see sync strategy below).
- **AGENTS.md**: Add a short `AGENTS.md` in the project root with high-level instructions and a pointer to `.cursor/rules/` for full rules. Cursor then has both structured rules and a simple fallback.
- **.claude/CLAUDE.md**: If Agent OS or other tooling expects `@.claude/CLAUDE.md`, keep it as a **pointer** to where rules live: e.g. "For Cursor: use .cursor/rules/. For a consolidated view see repo root CLAUDE.md."
- **.cursorignore**: Populate with Python/Node/build/logs patterns (unchanged from prior plan).
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)**: Keep as the Copilot-facing slice; add a line that the canonical project rules for Cursor are in `.cursor/rules/` and that CLAUDE.md is a supporting reference.

---

## Summary of file roles


| File / location                     | Role                                                                                          |
| ----------------------------------- | --------------------------------------------------------------------------------------------- |
| **.cursor/rules/*.mdc**             | **Canonical** (Cursor Project Rules). Source of truth for Cursor.                             |
| **.cursorrules**                    | Legacy; minimal stub: "see .cursor/rules/ and AGENTS.md".                                     |
| **CLAUDE.md**                       | Supporting: human / non-Cursor reference; states canonical = .cursor/rules/.                  |
| **AGENTS.md**                       | Cursor simple-alternative; short instructions + link to .cursor/rules/.                       |
| **.claude/CLAUDE.md**               | Pointer for Agent OS: "Cursor uses .cursor/rules/; see root CLAUDE.md for consolidated view." |
| **.github/copilot-instructions.md** | Copilot slice; reference .cursor/rules/ as canonical.                                         |


---

## Concrete steps

1. **.cursorignore**
  Add patterns (e.g. from [.gitignore](.gitignore)) so Cursor does not index build artifacts, venvs, logs, large data dirs.
2. **.cursorrules**
  Replace with a **minimal stub** (few lines) that says: project rules live in **.cursor/rules/** and in **AGENTS.md**; see those for full guidance. No bullet list; keep it as a pointer only until you fully migrate.
3. **CLAUDE.md**
  - Add a short "Canonical rules" section at or near the top: **For Cursor IDE, the canonical project rules are in `.cursor/rules/`. This file is a consolidated reference for other tools and humans.**
  - Keep the rest as-is for now (or trim later) so it remains a useful consolidated view; no need to remove content unless you want to avoid duplication.
4. **.claude/CLAUDE.md** (create if missing)
  Single short file: Cursor uses `.cursor/rules/`; for a full consolidated view see the repo root [CLAUDE.md](CLAUDE.md). Satisfies Agent OS reference to `@.claude/CLAUDE.md` without making CLAUDE.md canonical for Cursor.
5. **.github/copilot-instructions.md**
  Add one sentence: canonical project rules for Cursor are in `.cursor/rules/`; CLAUDE.md is a supporting reference.
6. **AGENTS.md**
  Create a short AGENTS.md in the project root: high-level project instructions and "See .cursor/rules/ for full rules." Cursor then has both structured rules and a simple fallback.
7. **References**
  In [CLAUDE.md](CLAUDE.md) REFERENCES section: change "Primary rules file: .cursorrules" to "Canonical rules (Cursor): .cursor/rules/. Legacy root file: .cursorrules. Consolidated reference: this file (CLAUDE.md)."
  Update any skills/docs that say "primary rules file: CLAUDE.md" or ".cursorrules" to point to `.cursor/rules/` as canonical for Cursor.
8. **Sync policy (Option A)**
  In CLAUDE.md (e.g. in the Canonical rules section or REFERENCES), add a one-line maintenance note: **When you add or change rules in .cursor/rules/ or Cursor agents/skills, update this file and .github/copilot-instructions.md so Claude and Copilot stay in sync.**

---

## Claude and Copilot: they cannot use Cursor rules

**Claude** (outside Cursor — e.g. Claude Code, API, other UIs) does **not** read `.cursor/rules/` or Cursor agents. Those are Cursor IDE–specific. The only way to give Claude project instructions outside Cursor is via CLAUDE.md (or .claude/CLAUDE.md). It will not auto-see Cursor config.

**GitHub Copilot** does **not** read `.cursor/rules/` or Cursor agents. It uses its own mechanism (e.g. `.github/copilot-instructions.md`). Copilot will not see Cursor rules.

**Implication:** We have two surfaces — Cursor (`.cursor/rules/`, agents) vs non-Cursor (CLAUDE.md, copilot-instructions.md).

**Chosen: Option A — Sync when rules change.** When you add or change rules in `.cursor/rules/` (or Cursor agents/skills), update CLAUDE.md and/or .github/copilot-instructions.md so Claude and Copilot stay in sync. Document this in CLAUDE.md (or CONTRIBUTING) so maintainers know to sync after editing Cursor config.

---

## What we are not doing

- We are **not** making CLAUDE.md the canonical rule set for Cursor; Cursor's guidance favors `.cursor/rules/` and AGENTS.md.
- We are **not** expanding .cursorrules with full content; Cursor recommends migrating to Project Rules or AGENTS.md.
- We are **not** removing CLAUDE.md; it stays as a supporting consolidated reference and for non-Cursor tooling.

This keeps your setup aligned with Cursor's best practice while preserving CLAUDE.md and .claude for other tools and readability.
