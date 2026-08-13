# Dialogue Content Tools (Content Creators)

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified - treat with lower confidence.

---

## 1. Overview

**[SPEC]**
Admins author NPC dialogue trees in Postgres JSONB via **Content Tools — Dialogue**.
Players use classic MUD `talk` / `talk <n>` in-game. This runbook covers the editor
workflow for content creators (#583).

---

## 2. Open the editor

**[SPEC]**

1. Log in as an admin account (game client).
2. Press **Esc** for Main Menu.
3. Choose **Content Tools — Dialogue (New Tab)**, or open `/admin/content/dialogue`.
4. Auth uses the same bearer token as the game session (localStorage). Non-admins
   receive API errors when listing or saving.

---

## 3. Tree shape (nav-only)

**[SPEC]**
Each definition is JSON:

```json
{
  "start": "greeting",
  "nodes": {
    "greeting": {
      "text": "NPC line shown to the player.",
      "options": [
        { "label": "Ask about the library", "next": "library" },
        { "label": "Farewell", "next": null }
      ]
    },
    "library": {
      "text": "Follow-up NPC line.",
      "options": [{ "label": "Thank you", "next": null }]
    }
  }
}
```

Rules enforced on save (server + client):

- `start` must name a key in `nodes`.
- `nodes` must be non-empty.
- Each option needs a non-empty `label`.
- `next` must be a known node id, or `null` / omitted to **end** the conversation.

**[NOTE]**
Option effects (`start_quest`, items, reputation), React Flow graphs, and file-based
authoring are deferred. Keep trees navigation-only.

---

## 4. Editor workflow

**[SPEC]**

| Action   | Steps                                                                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| List     | Left panel lists dialogue ids from the admin API.                                                                                               |
| New      | Click **New**, set **Dialogue id**, optional **NPC definition id**, edit JSON.                                                                  |
| Link NPC | Set **NPC definition id** to the numeric `npc_definitions.id` (e.g. Armitage `53`). One tree per NPC (unique). Leave empty for unlinked drafts. |
| Save     | **Save** calls `PUT /v1/admin/dialogue/definitions/{id}`. Invalid trees return an error.                                                        |
| Delete   | Select a listed tree, then **Delete**.                                                                                                          |

**[NOTE]**
Dialogue id is a stable string key (e.g. `armitage_greeting`). Prefer snake_case.

---

## 5. Player verification

**[SPEC]**

1. Ensure the linked NPC is in the same room (`npc spawn <definition_id>` as admin if needed).
2. `talk <npc name>` — personal system message with NPC text and numbered options.
3. `talk <number>` — advance; farewell / `next: null` ends and clears the session cursor.
4. `help talk` — in-game help for players.
5. Leaving the room clears the conversation cursor.

---

## 6. Seed and API reference

**[SPEC]**

- Seed example: `armitage_greeting` → NPC definition id `53` (migration
  `data/db/migrations/20260730_seed_dialogue_armitage_*.sql`).
- Apply: `.\scripts\apply_dialogue_migration.ps1 -TargetDbs mythos_dev` (and
  `apply_procedures.ps1` for `db/procedures/dialogues.sql`).
- Admin routes: `/v1/admin/dialogue/definitions` (list, get, create, upsert, delete).
- OpenAPI: `docs/openapi/openapi.json`.

---

## 7. Related docs

**[NOTE]**

- Player quest commands remain separate: `quest ask` / `quest turnin` /
  `docs/QUEST_SYSTEM_FEATURES.md`.
- In-game help is part of feature definition of done (see `AGENTS.md`).
