# ADR-021: Character Display Name Validation

**Version 1.1.0** · MythosMUD · 2026-08-27

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-08-23

Character display names (the `name` field on player records) must match the same
rules enforced at runtime by `validate_player_name` in
`server/validators/security_validator.py`. Creation, API schemas, client UX,
chat search, alias file paths, and command targets all share one charset and
length policy. Closes [#671](https://github.com/arkanwolfshade/MythosMUD/issues/671)
and [#670](https://github.com/arkanwolfshade/MythosMUD/issues/670).

## 2. Context

**[NOTE]**
Character creation allowed spaced names (e.g. `Arkan Lovecraft`) while alias
storage, command parsing, and admin/moderation paths called `validate_player_name`,
which rejects spaces. Players could finish creation then crash on normal commands
such as `go down` during alias expansion.

**[BUG]**
**Symptom:** `go down` raised `ValueError` from `alias_storage.get_alias_file_path` when the
display name contained spaces ([#670](https://github.com/arkanwolfshade/MythosMUD/issues/670)).
**Fix:** enforce `validate_player_name`'s charset/length policy at character creation too, not
just at runtime — closing the gap between what creation allowed and what alias/command
paths required.

## 3. Decision

**[SPEC]**

- **Option A (chosen):** Disallow spaces at creation. One display name string
  used everywhere (commands, alias files, chat targets, occupant lists).
- **Charset:** `^[a-zA-Z][a-zA-Z0-9_-]*$` — must start with a letter; only
  letters, digits, underscores, and hyphens.
- **Length:** minimum 3, maximum 20 characters (after trim).
- **Canonical validator:** `validate_player_name` in `security_validator.py`
  (and parallel `optimized_validate_player_name` for the optimized path).
  Module constants: `PLAYER_NAME_MIN_LENGTH = 3`, `PLAYER_NAME_MAX_LENGTH = 20`.
- **API:** `CreateCharacterRequest.name` uses `Field(min_length=3, max_length=20)`
  and delegates format checks to `validate_player_name` after strip.
- **Client:** `client/src/utils/playerNameValidation.ts` mirrors server rules;
  `CharacterNameScreen` shows inline hints and disables Create until valid.
- **Search:** `player_search_service.validate_player_name` defers format to
  `validate_player_name`; keeps player-existence check only.
- **Legacy spaced names:** Manual cleanup in dev/prod; no automated migration.
  Document known cases in this ADR or issue comments as they are found.

## 4. Alternatives Considered

**[SPEC]**

1. **Option B — spaced display names + separate slug/key** — Rejected: requires
   auditing every `validate_player_name` call site, safe filesystem key derivation,
   and command quoting for multi-word targets.
2. **Max length 50 at creation** — Rejected: `player_search_service` already
   capped at 20; align creation with runtime.
3. **Min length 2** — Rejected: min 3 avoids junk one- and two-letter names and
   matches product preference from [#671](https://github.com/arkanwolfshade/MythosMUD/issues/671).
4. **Automated DB migration for legacy spaced names** — Rejected: low volume;
   manual rename/delete is safer for `mythos_dev`.
5. **Separate ops runbook** — Rejected for this change; policy lives in this ADR.

## 5. Consequences

**[SPEC]**

- Positive: creation and runtime behavior are consistent; alias expansion and
  movement no longer crash on valid new characters; one regex/length source of truth.
- Negative: players cannot use spaces or punctuation in names; legacy spaced names
  still crash until manually cleaned up.
- Neutral: NPC names are out of scope; `player_id` remains UUID.

## 6. Legacy cleanup (manual)

**[NOTE]**
To find invalid display names in PostgreSQL (dev only, with explicit approval):

```sql
SELECT player_id, name
FROM players
WHERE name !~ '^[a-zA-Z][a-zA-Z0-9_-]*$'
   OR length(trim(name)) < 3
   OR length(trim(name)) > 20;
```

Rename or delete affected rows by hand. Do not run bulk updates against
`mythos_dev` without explicit owner approval.

## 7. Changelog

**[SPEC]**

| Version | Date | Change |
| ------- | ---------- | ------ |
| 1.0.0 | 2026-08-23 | Initial decision closing #670 and #671. |
| 1.1.0 | 2026-08-27 | Restructure the `[BUG]` block into HADS-required Symptom/Fix fields (audit deferred register, #648). |
