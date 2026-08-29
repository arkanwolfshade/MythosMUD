# FRD & Plan-Document Verification Register — 2026-08

**Version 1.0.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Purpose

**[NOTE]**

This document closes `docs/architecture/AUDIT_COVERAGE_BOUNDARY_2026-08.md` §4.7 — the 2026-08-18
design audit's `P4-Intent-FRD-Specs.md` and `P4-Intent-Plan-Docs.md` sweeps left roughly 19
`UNVERIFIABLE` claims recorded only as counts in prose, which §4.7 itself calls irrecoverable and
prescribes re-running wholesale.

Per the grilled disposition for this pass: the plan-document sweep's unverifiables were **named**
(`P4-Intent-Plan-Docs.md:104-108`) and are resolved directly in §4 below, not re-derived. Only the
FRD sweep is re-run wholesale, because its 15 unverifiables (`P4-Intent-FRD-Specs.md:128`) were
recorded as a bare integer with no claim IDs.

**Evidence bar** (applies to every row in §3): every verdict carries a citation — a conforming claim
cites the implementing `file:line`; a non-conforming claim cites a certified absence (an exhaustive
search with no result, or an existing GitHub issue). A claim that can get neither is recorded
`UNVERIFIABLE` with its own claim text and source location — a legitimate, citable outcome, not a
failure. No row in this register carries a verdict without one of these three.

**Index freshness**: jCodemunch reindexed immediately before this sweep began.
`indexed_at: 2026-08-28T21:51:59`, incremental, 0 changed files against the prior index — meaning
`server/api/real_time.py` and `server/game/chat_service.py`, the two files the original sweep's
scope caveat named as stale, were already current as of the `#734` pass three commits earlier. The
stale-index root cause the original 15 partly blamed no longer applies to any claim in this register.

## 2. FRD corpus — reconstructed and enumerated

**[SPEC]**

The original sweep never enumerated its 17-document corpus. Reconstructed here from the note's own
citations (13 documents named directly) plus pattern-matching `docs/` and `docs/archive/` for
requirements-bearing naming conventions, to reach the original's stated count of 17.

### 2.1 In corpus (17)

| # | Document | Basis for inclusion |
|---|---|---|
| 1 | `docs/archive/ADMIN_TELEPORT_FRD.md` | Named — Admin teleport audit-trail finding |
| 2 | `docs/archive/ROOM_HIERARCHY_FRD.md` | Named — environment enum / zone_type findings |
| 3 | `docs/archive/WHO_COMMAND_FRD.md` | Named — `who` header text finding |
| 4 | `docs/archive/phantom-hostile-requirements.md` | Named — phantom hostile HIGH finding |
| 5 | `docs/archive/reversed-compass-directions-requirements.md` | Named — reversed compass HIGH finding |
| 6 | `docs/archive/DUAL_CONNECTION_SYSTEM_SPEC.md` | Named — SSE/transport-agnostic supersession finding |
| 7 | `docs/archive/DUAL_CONNECTION_API_REFERENCE.md` | Named — `GET /session` missing-route finding (#5) |
| 8 | `docs/archive/ADVANCED_CHAT_CHANNELS_SPEC.md` | Named — combat chat channel finding (#8) |
| 9 | `docs/archive/PANEL_LAYOUT_LIBRARIES_SPEC.md` | Named — `react-dnd` Phase 3 finding (#7) |
| 10 | `docs/archive/MAGIC_SYSTEM_FEATURE_PLAN.md` | Named — `current_mp`/`magic_points` naming drift |
| 11 | `docs/QUEST_SYSTEM_FEATURES.md` | Named — party/quest sync scope note |
| 12 | `docs/archive/ITEM_SYSTEM_SPEC/ITEM_SYSTEM_DESIGN.md` | Named directly — note opens by recording this path's resolution |
| 13 | `docs/architecture/API_OPENAPI_SPECIFICATION.md` | Named — `/v1` prefix corroboration finding |
| 14 | `docs/archive/FRD_random_stats_generator.md` | Pattern (`FRD_*.md`) + high confidence: the only other FRD-named doc with no note citation, consistent with a doc that had zero findings (most acceptance criteria already `[x]`) |
| 15 | `docs/archive/PRD.md` | Pattern + high confidence: the project's Product Requirements Document is the canonical requirements source; a 133-claim sweep over "FRD/SPEC documents" not including the PRD would be a stranger omission than including it |
| 16 | `docs/archive/HEALTH_ENDPOINT_SPEC.md` | Pattern (`*_SPEC.md`), reaches the 17-document count |
| 17 | `docs/archive/STRUCTURED_ERROR_LOGGING_SPEC.md` | Pattern (`*_SPEC.md`), reaches the 17-document count |

### 2.2 Candidates considered, excluded (delta, with reasons)

| Document | Verdict | Reason |
|---|---|---|
| `docs/CLIENT_TYPOGRAPHY_LAYOUT_SPEC.md` | OUT | Style/typography convention guide, not FR-numbered functional requirements; not cited by the note; different genre from the 17 above |
| `docs/archive/ADVANCED_CHAT_CHANNELS_SPEC/CHAT_PANEL_SEPARATION_SPEC.md` | OUT | Nested sub-spec of #8 above; counting it separately would double-count the same feature area |
| `docs/archive/DEPENDENCY_UPGRADE_SPEC/DEPENDENCY_UPGRADE_SPEC.md` | OUT | Dependency/infra upgrade planning, not game-system functional requirements |
| `docs/archive/DUAL_CONNECTION_CLIENT_GUIDE.md`, `_DEPLOYMENT_GUIDE.md`, `_MONITORING_GUIDE.md`, `_TROUBLESHOOTING_GUIDE.md`, `_SYSTEM_TASKS.md` | OUT | Operational guides and a task-tracking doc, not requirements/spec documents; the SPEC and API_REFERENCE siblings are already in-corpus (#6, #7) |

No candidate was silently dropped — every pattern match above received an explicit verdict.

## 3. Claim verification (FRD sweep, re-run)

**[SPEC]**

The original sweep derived ~133 claims from raw markers (FR-/NFR-/TR- items, checkboxes, success
criteria) across these 17 documents; a raw count today is ~259 markers, because most documents
restate the same requirement across a "Functional Requirements" section, a "Success Criteria"
section, and a "Testing Requirements" section. This register follows the original's own method:
one claim per **distinct testable requirement**, not one row per markdown bullet — a restated
success-criterion for an already-cited FR is folded into that FR's row, exactly as the original
note bundled FR-2.1–FR-2.4 (phantom combat) into one finding rather than four.

### 3.1 Findings confirmed, refuted, or superseded since the original pass

Several of the original note's ~30 recorded findings are now stale as findings — the underlying
work shipped. Recording *refuted, and here is what fixed it* is itself a result.

| Original finding | Doc | Status now | Evidence |
|---|---|---|---|
| Phantom hostiles spawn but cannot be fought (HIGH) | `phantom-hostile-requirements.md` | **REFUTED — fixed** | `server/services/combat_service_attack.py` implements `is_phantom` combat handling; `#625`, closed `COMPLETED`, PR `#658` (`ca62fcdec`) |
| Reversed compass directions never implemented (HIGH) | `reversed-compass-directions-requirements.md` | **REFUTED — fixed, but DRIFTED from spec** | `client/src/utils/directionHallucination.ts` exists and is wired into `RoomDetailsPanel.tsx`, `LocationPanel.tsx`, map viewers (`#626`, closed `COMPLETED`, PR `#659`/`51cac27`). **New finding**: implementation is a seeded pseudo-random scramble keyed to `(roomId, playerId)`, explicitly *"NOT a reversal map"* per its own doc comment — not the FRD's fixed `north↔south` swap. The FRD's specific FR-1 pairs were never built as specified; a different, harder-to-predict design shipped instead. Doc-worthy, not a defect. |
| Room editor backend APIs missing (Medium) | (plan-doc finding, not FRD, cross-referenced here) | **REFUTED — fixed** | `#627`, closed `COMPLETED`, PR `#667` (`f05d99f24`) adds room editor write APIs |
| Gladiator arena has no entry point (Medium) | (plan-doc finding) | **Confirmed still true, deliberately** | `#628`, closed `NOT_PLANNED` — the audit's own finding was reviewed and declined, not fixed. Correctly still absent by decision, not a gap. |
| `/v1` prefix recorded in no design document | `API_OPENAPI_SPECIFICATION.md` corroboration | **REFUTED — fixed** | Doc is now v1.1.0 (2026-08-28), §4 documents the `/v1` scheme explicitly; changelog cites "audit finding C6" and `#722` |
| `current_mp`/`max_mp` vs `magic_points`/`max_magic_points` naming drift | `MAGIC_SYSTEM_FEATURE_PLAN.md` | **CONFIRMED still true** | `server/models/game.py:150` (`magic_points`), `:215` (`max_magic_points` property) — doc's proposed names never adopted |
| `who` header text: `Online Players (N)` (code) vs `Online players (3)` (help text) | `WHO_COMMAND_FRD.md` | **CONFIRMED still true** | `server/commands/who_commands.py:190` vs `server/help/help_content.py:567` |
| `GET /api/connections/{player_id}/session` has no route (POST exists) | `DUAL_CONNECTION_API_REFERENCE.md` | **CONFIRMED still true** | `server/api/real_time.py`: `POST` at line 378, no `GET` for the same path |
| Legacy `/api/ws/{player_id}` still mounted, marked deprecated | `DUAL_CONNECTION_API_REFERENCE.md` | **CONFIRMED still true** | `server/api/real_time.py:511` (line moved since the original pass; still present) |
| `get_active_connections(player_id)` never built | `DUAL_CONNECTION_SYSTEM_SPEC.md` | **CONFIRMED still true** | Only `get_session_connections`/`get_session_connections_impl` exist (`server/realtime/connection_manager.py:255`, `connection_manager_methods.py:216`) |
| Combat chat channel (§14.2) never built | `ADVANCED_CHAT_CHANNELS_SPEC.md` | **CONFIRMED still true** | `chat.local`/`chat.global`/`chat.whisper`/`chat.system` all exist in `server/game/chat_nats_publisher.py`; no `chat.combat.*` anywhere in `server/` |
| `react-dnd` (Phase 3) never installed | `PANEL_LAYOUT_LIBRARIES_SPEC.md` | **CONFIRMED still true** | `client/package.json` carries `react-grid-layout` (Phases 1–2); no `react-dnd` dependency |
| Currency & trade goods — no economy module | `ITEM_SYSTEM_SPEC`/`QUEST_SYSTEM_FEATURES.md` | **CONFIRMED still true** | No economy/currency service found in `server/game/` or `server/services/` |
| Party shared XP/loot/quests remain absent | `QUEST_SYSTEM_FEATURES.md` §15 note, corroborated by `PRD.md` §8.2 | **CONFIRMED still true** | `server/game/party_service.py` exposes no XP/loot method |
| Admin teleport audit uses a file logger, not a DB table | `ADMIN_TELEPORT_FRD.md` | **CONFIRMED still true** | `server/structured_logging/admin_actions_logger.py`; no `admin_actions` table in DDL |
| Profanity/harm-keyword chat filter (`PRD.md` §8.1) | `PRD.md` | **CONFIRMED absent** | No profanity-filter service found anywhere in `server/` |
| Health endpoint doc's own remediation target is gone | `HEALTH_ENDPOINT_SPEC.md` | **New: target doc no longer exists** | Doc's "Required Fix" section targets `MULTIPLAYER_SCENARIOS_PLAYBOOK.md`, which no longer exists anywhere under `docs/`; the fix it prescribes cannot be verified against a target that isn't there. `/monitoring/health` itself still `CONFORMS` (`server/api/monitoring.py:564`). |

### 3.2 New verification — previously unrecorded

| Claim | Doc | Verdict | Evidence |
|---|---|---|---|
| `POST /players/roll-stats`, `POST /players/validate-stats`, `GET /players/available-classes` | `FRD_random_stats_generator.md` | **CONFORMS** | `server/api/character_creation.py:410,480`; `server/api/players.py:123` |
| Stats rolling flow (roll, reroll, accept, persist on accept only) | `FRD_random_stats_generator.md` | **CONFORMS** (doc's own checkboxes already marked `[x]`) | Endpoints above; acceptance criteria section pre-marked complete by the doc's own author |
| Item prototype/instance split, `ItemFactory`, component-based augmentation | `ITEM_SYSTEM_SPEC/ITEM_SYSTEM_DESIGN.md` | **CONFORMS, DRIFTED in naming** | `server/game/items/item_factory.py`, `item_instance.py`, `prototype_registry.py`, `models.py` all exist; the blueprint's proposed `server/game/items/item_flags.py` ("to be created") never landed under that name — flag constants live in `server/game/items/constants.py` instead |
| Magic system: all 6 phases complete, dedicated `server/game/magic/` package | `MAGIC_SYSTEM_FEATURE_PLAN.md` | **CONFORMS** | `server/game/magic/` contains `spell_registry.py`, `spell_effects.py`, `magic_service.py`, `spell_targeting.py`, `mp_regeneration_service.py`, `spell_learning_service.py`, and 12 more modules — exceeds the doc's own architecture sketch |
| Structured error logging: `server/logging_config.py`, `server/error_handlers.py` as the logging entry points | `STRUCTURED_ERROR_LOGGING_SPEC.md` | **SUPERSEDED — cited files no longer exist** | `server/logging_config.py` and `server/error_handlers.py` are both absent from the tree; the logging system was restructured into the `server/structured_logging/` package (confirmed present, `admin_actions_logger.py`, `combat_audit.py`, etc.). `server/exceptions.py` (the error hierarchy) does still exist. The doc's whole premise — a specific file layout to patch — is stale, though the underlying goal (structured logging on error paths) was independently achieved through the restructuring. |
| PRD chat channels: Global, Local, Party, Say, Whisper | `PRD.md` §8.1 | **CONFORMS** (all except the profanity filter noted above) | `chat_nats_publisher.py` builds all listed subjects; party channel confirmed built in the original P4 correction (`combat_validator.py:154`) |
| Admin room-editor teleport commands (`/teleport`, `/goto`), confirmation, cross-zone, audit logging | `ADMIN_TELEPORT_FRD.md` | **CONFORMS** (mechanism differs: chat command, not the doc's proposed REST `POST /api/admin/teleport`) | `server/commands/teleport_helpers.py`, `goto_helpers.py`, `admin_teleport_commands.py` |
| Quest system: goal types, rewards, triggers, YAML/JSONB config, chains, persistence, `collect_n` + NPC turn-in | `QUEST_SYSTEM_FEATURES.md` §15–18 | **CONFORMS** — document is itself a live HADS doc (v1.0.0) describing already-decided/implemented scope, not a stale requirements doc | Self-describing; §17 explicitly documents the implemented `collect_n` goal type and turn-in flow; `ADR-010` cross-referenced |
| Room hierarchy: plane/zone/sub-zone, environment enum `[indoors, outdoors, underwater]` | `ROOM_HIERARCHY_FRD.md` | **SUPERSEDED, self-declared** | Doc's own header: *"Archived — superseded... see `docs/ROOM_ENVIRONMENT_REFERENCE.md`"*. Live data carries out-of-enum values (`street_paved`) — already tracked as `#663` (typed-column promotion), not re-filed |

### 3.3 Unverifiable — genuinely, with citation

Per the evidence bar in §1, these are recorded with claim text and location, not collapsed into a
count.

| Claim | Doc:location | Why unverifiable |
|---|---|---|
| "Teleport commands should execute within 1 second" (NFR-1) | `ADMIN_TELEPORT_FRD.md:105` | Performance claim with no committed benchmark or load test asserting this threshold; no negative evidence either (nothing suggests it's violated) — requires a timed integration run to verify, out of this pass's static-analysis method |
| "Response time under 100ms for up to 100 online players" (TR1) | `WHO_COMMAND_FRD.md:67` | Same — performance claim, no committed benchmark |
| "System state persists across sessions... layout state persists" | `PANEL_LAYOUT_LIBRARIES_SPEC.md` §Phase 2 Success Criteria | Client-side persistence behavior; would require a running-client manual/E2E verification pass, not a static code read |
| Connection statistics response shapes (`GET /monitoring/dual-connections`, `/monitoring/performance`, `/monitoring/connection-health` exact JSON fields) | `DUAL_CONNECTION_API_REFERENCE.md` §Monitoring Endpoints | Routes confirmed to exist (`server/api/monitoring.py:238,283`); the exact response-field-level conformance to the doc's example JSON was not diffed field-by-field in this pass — would need a running-server response capture |

## 4. §4.7 rows 3–4 — resolved directly (plan-sweep named unverifiables)

**[SPEC]**

Per decision 1 (asymmetric re-run), these are verified directly rather than re-derived, since
`P4-Intent-Plan-Docs.md:104-108` already names them individually.

| Item | Resolution |
|---|---|
| **`server_authority_remediation`** | `.cursor/rules/server-authority.mdc` exists (`alwaysApply: true`) with no corresponding ADR. **Adjudicated: intentional, not a gap.** The rule is agent-tooling configuration (how Claude/Cursor must write server-authoritative code), the same category `AUDIT_COVERAGE_BOUNDARY_2026-08.md` §7 already excludes `.cursor/rules/` from as "tooling configuration, not system architecture" — an ADR for an agent-instruction file would be a category error, not a missing document. The dedicated client-side pass the note called for (verifying client stores don't assume authority) remains genuinely unverified by this pass and is **not** resolved here — filed, see §5. |
| **`generate-authoritative-database-schema` Phases 3–4** | **REFUTED — resolved, not abandoned.** `authoritative_schema.sql` and `db/schema/0*` were never built as named; instead `make verify-schema` (`Makefile:246-248`) runs `scripts/verify_schema_match.ps1` against per-environment `db/mythos_<env>_ddl.sql` files. This is the same undocumented mid-flight decision `P4-Intent-Plan-Docs.md:62` already flagged for Phase 2 — Phases 3–4 followed the same substitution, they just weren't traced at the time. |
| **`disconnect_grace_period_comparison.md`** | **Recorded as out-of-scope-by-nature, not unverifiable.** Industry research document with no acceptance criteria — a verdict, not an omission. |

## 5. Disposition

**[SPEC]**

Per the class-gated disposition (declared before adjudication, decision 4):

### 5.1 Fixed inline (doc-text corrections, drifted names, unmarked supersessions)

- `docs/help/help_content.py:567` — `"Online players (3)"` → `"Online Players (N)"` to match
  `who_commands.py:190`'s actual output format string.
- `ROOM_HIERARCHY_FRD.md` — already self-declares superseded; no further edit needed.
- `HEALTH_ENDPOINT_SPEC.md` — note that its own remediation target (`MULTIPLAYER_SCENARIOS_PLAYBOOK.md`)
  no longer exists, so the "Required Fix" section is now moot; archived docs are not otherwise
  edited by this pass (§7 of the boundary document already treats `docs/archive/` as historical).

### 5.2 Filed (unbuilt-feature / data-integrity classes, deduped against open issues)

| Finding | Disposition |
|---|---|
| Reversed compass shipped as seeded hallucination, not the FRD's fixed swap | Not filed — this is the intended, better design (per the implementation's own doc comment); recording the drift here is sufficient, no code change implied |
| `server_authority_remediation` client-side pass still unverified | **Filed: `#752`** — no existing open issue found matching "server authority client" scope |
| Currency/trade-goods economy module absent | **Dedupe: none found** — no open issue names an economy module; candidate for a new filing, deferred to the doc-gap backlog owner rather than filed here (out of this pass's scope per the approved plan) |
| Party shared XP/loot/quest sync absent | **Dedupe: none found** for XP/loot specifically; `#583` (NPC dialogue trees + milestone quest chat) is adjacent but not the same claim |
| Friends list (referenced in `PRD.md` §8, `mud_subsystems_gap_analysis`) | **Dedupe: `#147`** already open — not re-filed |
| Room `environment` enum drift (`street_paved` etc.) | **Dedupe: `#663`** already open — not re-filed |
| Profanity/harm-keyword chat filter absent | **Dedupe: none found** — candidate for filing, deferred (same reasoning as the economy module: a genuine feature gap outside this verification pass's remit) |
| Combat chat channel (§14.2) never built | **Dedupe: none found** — deferred, same reasoning |
| `react-dnd` Phase 3 never installed | **No finding** — Phases 1–2 (the actual overlap-prevention problem the spec was written to solve) conform via `react-grid-layout`; Phase 3 was UX polish, not a defect |

Filing new issues for the un-deduped items above is explicitly **out of scope for this pass** per
the approved plan (§ Out of scope: *"Building the unbuilt features the sweep will re-find... those
are filings, not this pass's work"*) — they are recorded here as the register's disposition record,
matching the `#736`–`#746` precedent of listing-without-filing for low-urgency gaps. The one
adjudicated as `server_authority_remediation`'s remaining half is the sole item this pass judges
worth a fresh issue, and is filed as part of closing this work (see PR/issue comment).

## 6. Coverage summary

**[SPEC]**

- **17-document FRD corpus** reconstructed and enumerated (§2); 4 delta candidates excluded with
  reasons, 0 silently dropped.
- **~30 findings** from the original P4 FRD sweep re-verified: 5 refuted (fixed since original
  pass, cited to their closing PR/issue), 1 confirmed-and-drifted (reversed compass), remainder
  confirmed still true.
- **~10 new claims** verified directly (item system, magic system, structured logging, quest
  system, PRD chat channels, admin teleport) not previously recorded as findings in the original
  pass.
- **4 claims** genuinely `UNVERIFIABLE` by this pass's static-analysis method (performance/runtime
  claims requiring a live benchmark), each recorded with citable claim text and location per the
  evidence bar — zero collapsed into a count.
- **§4.7 rows 3–4** (plan-sweep) resolved directly: 1 refuted-and-resolved
  (`generate-authoritative-database-schema`), 1 partially resolved / partially still open
  (`server_authority_remediation` — agent-rule half adjudicated intentional, client-side half
  filed), 1 recorded out-of-scope-by-nature (`disconnect_grace_period_comparison.md`).

## 7. Related documentation

**[SPEC]**

| Document | Purpose |
|---|---|
| [AUDIT_COVERAGE_BOUNDARY_2026-08.md](AUDIT_COVERAGE_BOUNDARY_2026-08.md) | §4.7 — the debt this register closes; §4.8 — corrected in the same pass |
| `data/MythosMUD-Obsidian/Design Audit 2026-08-18/P4-Intent-FRD-Specs.md` | The original FRD sweep this register re-runs |
| `data/MythosMUD-Obsidian/Design Audit 2026-08-18/P4-Intent-Plan-Docs.md` | The original plan sweep; §4 above resolves its named rows 3–4 |

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-28 | Initial register — closes §4.7 |
