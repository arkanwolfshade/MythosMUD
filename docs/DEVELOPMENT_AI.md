# MythosMUD — AI Agent On-Ramp

**Version 2.0.0** · MythosMUD · 2026-09-08

---

## AI READING INSTRUCTION

Read `[SPEC]` blocks for authoritative pointers.
This file is a **router**, not the rule body.

---

## 1. Overview

**[NOTE]**

_"In the vast archives of Miskatonic University, even the most advanced artificial intelligences must learn to navigate
the forbidden knowledge with care and precision."_

On-ramp for AI agents (Cursor, Claude Code, GitHub Copilot, and similar) working on MythosMUD. Project character lives
here; behavioral persona and hard rules live in `AGENTS.md`; human environment setup lives in `DEVELOPMENT.md`.

---

## 2. Project character

**[SPEC]**

### Theme and setting

**Theme**: Cthulhu Mythos-themed MUD (Multi-User Dungeon)

**Tone**: Academic/scholarly with Mythos flavor

**Setting**: Miskatonic University and surrounding Arkham area

**Atmosphere**: Gothic horror, forbidden knowledge, eldritch mysteries

**Target users**: Professor Wolfshade and teenage son (COPPA compliance critical)

### Agent voice (pointer)

How to speak and behave is defined in [`AGENTS.md`](../AGENTS.md) (Character and hierarchy) and
`.cursor/rules/character-tone.mdc`: untenured professor of Occult Studies; address the user as Professor Wolfshade;
scholarly Mythos flavor with pragmatic implementation. Break character when technical clarity requires it.

---

## 3. Where to read next

**[SPEC]**

| Need                                                                                         | Document                                                 |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Authoritative agent rules** (security, COPPA, server, DB, testing, logging, git, coverage) | [`AGENTS.md`](../AGENTS.md)                              |
| **Human setup** (uv, env templates, PostgreSQL, start/stop, Make targets)                    | [`DEVELOPMENT.md`](DEVELOPMENT.md)                       |
| **Testing details**                                                                          | [`TESTING.md`](TESTING.md) (canonical under `docs/`)     |
| **Claude / non-Cursor router**                                                               | [`CLAUDE.md`](../CLAUDE.md) (also points at `AGENTS.md`) |

Do **not** treat this file as a second copy of standards. If anything here disagrees with `AGENTS.md`, follow
`AGENTS.md`.

---

## 4. Changelog

**[SPEC]**

| Version | Date       | Change                                                            |
| ------- | ---------- | ----------------------------------------------------------------- |
| 2.0.0   | 2026-09-08 | Thin to router + retain project character; SoT rules in AGENTS.md |
| 1.2.0   | 2026-08-28 | Prior full guidelines body (superseded)                           |
| 1.0.0   | 2026-07-30 | Initial HADS structural conversion                                |
