# ADR-024: Server-Authoritative Perceived Reality for Hallucinations

**Version 1.0.0** · MythosMUD · 2026-09-08

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-09-08

Written to close `#714`, which began as a narrow question ("should ui-v2 rebuild the deleted
`HallucinationTicker`?") and was reframed via investigation into a larger one: the server was
generating hallucination content — fake NPC tells, room text overlays — that reached no ui-v2
client, and the two prior hallucination features (`#625` phantom hostiles, `#626` exit
hallucination) had chosen **opposite architectures** for where the fiction lives. This ADR states
the rule going forward: **the server decides per-viewer reality and ships it already-lied-to; the
client renders what it is told and holds zero hallucination logic.** It also **explicitly reverses
`#626`'s documented client-side placement** for exit hallucination.

## 2. Context

**[NOTE]**
`lucidity_event_dispatcher.send_hallucination_event()` emitted a `hallucination` event from the
tick loop at a real cadence (Fractured 25%/30s, Deranged 45%/20s, per
`hallucination_frequency_service.py`). ui-v2 had no handler for it in `eventHandlers/index.ts` or
the projector's `PROJECTED_EVENT_TYPES` allowlist — every fake NPC tell and room overlay was
logged as "Unknown event type, ignoring" and discarded. The product decision behind this ADR
(reached via Socratic interview during planning) was that hallucinations must be an **integrated**
experience — phantom voices in the Chat widget, phantom mobs in the Occupants widget, hallucinated
exits in the Room widget and `/look` — not a labelled, separately-styled feed. This is not a new
invention: it was already the written spec in `docs/archive/lucidity-system.md` §5.1 and
`docs/archive/phantom-hostile-requirements.md` FR-3.2, both still marked "Not Yet Implemented" in
three of four Phase-3 items.

The two prior features exposed the incoherence this ADR resolves:

| Surface | Server (before) | ui-v2 client (before) | Result |
| --- | --- | --- | --- |
| Phantom in `/look` "Also here:" | injects (`#625`) | renders text | works |
| Phantom in Occupants panel | `room_occupants` was a broadcast, not per-viewer | nothing | truth leaks |
| Hallucinated exits in Location panel | truthful | `getHallucinatedExits` (`#626`) | lies |
| Hallucinated exits in `/look` | truthful | renders text | truth leaks |
| Fake NPC tell / room text overlay | emits `hallucination` event | dropped (no handler) | invisible |
| Uneasy-tier hallucinations | `check_room_entry_hallucination` had zero production callers | — | never fire |

`#625` put its fiction server-side because combat integration forced it (a phantom needs a
resolvable combat target). `#626` put its fiction client-side and explicitly left `/look`
truthful (its own FR-3.3 called that "optional"). Neither prior ADR reconciled the two models;
this one does, in the server's favor — the argument in §4.2 below.

## 3. Decision

**[SPEC]**

**Per-viewer room payload.** `game_state` is already per-player
(`realtime/integration/game_state_provider.py`, delivered via `send_personal_message`). The
`room_update` and `room_occupants` broadcasts (`realtime/websocket_room_updates.py`,
`realtime/event_handler.py`) are converted to per-viewer fan-out (`realtime/room_viewer_fanout.py`,
`send_personalized_room_events` / `send_personalized_occupants_update`): each connected player in
the room gets a payload built for their own perceived reality. A fast-path gate
(`services/phantom_visibility.py`'s `room_has_hallucinating_viewer`, later broadened to also check
`lucidity_tier_cache.is_deranged`) falls back to the original single `broadcast_to_room` whenever
no one in the room is hallucination-eligible, so the common case pays no extra per-broadcast cost.

**Phantoms in the room payload.** `look_room.py`'s already-correct, already-tested
`_get_viewer_phantom_names(viewer_player_id, room_id)` was promoted to a shared
`services/phantom_visibility.py` and reused by the per-viewer `room_update`/`room_occupants`
builders and by `game_state_provider.py`'s `npc_names_list` construction. No client change:
`OccupantsPanel.tsx` already renders `room.npcs` verbatim.

**Server-side exit hallucination.** `#626`'s determinism (`seedFrom(roomId, playerId)` +
`mulberry32`, `client/src/utils/directionHallucination.ts`) was bit-for-bit ported to Python as
`services/exit_hallucination.py`, verified against the real JS output via `node` before any test
was written. Eligible viewers (cached-deranged, via `lucidity_tier_cache`) get the seeded lie
applied to the per-viewer `room_update` payload, `game_state`'s `room_data`, and `/look`'s exit
line (`look_room.py`'s `_handle_room_look`). Movement stays truthful: `go <direction>` always
resolves against real exits — the hallucination is a display lie, never a mechanical one.

**Retirement of the player-facing `hallucination` event.** `send_hallucination_event` is now a
structured-logging-only call (`logger.debug`), never dispatched to a client.
`passive_lucidity_flux/hallucinations.py`'s handlers deliver real content instead: fake NPC tells
go out as an ordinary whisper (`chat_npc_system.deliver_fake_npc_whisper`, byte-identical on the
wire to a real NPC whisper); room text overlays and the phantom-spawn narration go out as an
ambient system line (`deliver_personal_system`) — not persisted, not re-shown on a later `look`.

**In-fiction command interactions.** `services/fake_sender_registry.py` tracks each player's most
recent fake NPC sender (mirroring `#625`'s `phantom_hostile_service` registry pattern, including
tier-change/disconnect cleanup via `lucidity_service.py`). `reply` checks it before the real
whisper tracker and returns in-fiction prose ("Your words dissolve into the dark; no answer
comes.") instead of the truth-leaking "player... no longer available."

**Uneasy tier wired up.** `hallucination_frequency_service.py`'s `"room_entry"` trigger — spec'd
since `lucidity-system.md` §5.1 but never called in production — now fires from
`MovementService._maybe_trigger_room_entry_hallucination`, a post-success hook on `move_player`
that reads the cached tier (`lucidity_tier_cache`, no DB session needed for the room-entry trigger
type) and delivers the ambient-overlay half of Uneasy's palette
(`handle_uneasy_room_entry_hallucination`). See §5 for the palette gap this leaves.

**Verification affordances.** `admin hallucinate <target> <fake_tell|overlay|phantom>`
(`commands/admin_hallucinate_command.py`) forces a specific hallucination bypassing the chance
roll and cooldown, for manual QA. `GameConfig.hallucination_rng_seed`
(`GAME_HALLUCINATION_RNG_SEED`) seeds a shared `random.Random` (`services/hallucination_rng.py`)
used by every hallucination-related `random.*` call site, so integration tests can exercise the
real trigger path deterministically instead of calling services directly.

**Explicit reversal of `#626`.** `LocationPanel.tsx` no longer imports or calls
`getHallucinatedExits`; it renders `room.exits` exactly as the server sends it, because the server
now sends the lie itself when appropriate. `ChatHistoryPanel.tsx`'s
`TAG_MESSAGE_CLASSES.hallucination` was deleted — under server-authority, a distinct color for a
hallucinated message is itself a truth leak, and nothing in the client ever populated
`message.tags` to feed it anyway. `directionHallucination.ts` is **kept**, but scoped to a single
remaining caller: the `/map` page's `AsciiNoise` distortion. That page is an out-of-world
meta/editing tool (`RoomDetailsPanel.tsx`'s `isAdmin`/`onEditRoom` mode) fed by a REST endpoint,
not the per-viewer realtime payload — lying in an admin editing surface would be actively harmful,
so it stays client-side and outside this ADR's server-authority rule.

## 4. Alternatives Considered

**[SPEC]**

1. **Rebuild `HallucinationTicker` as a labelled feed** — Rejected: a player-facing event type
   named `hallucination`, or a UI element styled differently for hallucinated content, is itself
   the truth leak this epic exists to close. The product decision (§2) was integrated, in-fiction
   delivery, not a separate labelled surface.
2. **Keep `#626`'s client-side exit model, patch only the fake-tell/overlay delivery gap** —
   Rejected: leaves the `/look`-vs-Location-panel incoherence table in §2 unresolved, and any
   client on a raw socket (or a future non-ui-v2 client) would see the truth regardless of what
   the graphical panel shows. A MUD is fundamentally a text protocol; client-side fiction cannot
   survive that.
3. **Per-viewer fan-out unconditionally, no fast path** — Rejected: pays a per-recipient payload
   build on every `room_update`/`room_occupants` broadcast even in the overwhelming common case of
   an all-lucid room. The fast-path gate (`room_has_hallucinating_viewer`) keeps that cost at
   effectively the original single-broadcast cost when nobody in the room is eligible.
4. **Leave the Uneasy tier silent** — Rejected: `lucidity-system.md` §5.1 has promised Uneasy's
   "ambient whispers, fleeting shadows, misleading exit highlight" since before this epic; leaving
   `check_room_entry_hallucination` permanently uncalled contradicts standing written spec rather
   than deferring it.

## 5. Consequences

**[SPEC]**

- **Positive**: `/look`, the Occupants panel, the Room/Location panel, and the Chat widget are now
  consistent for every hallucination type a player can encounter — the incoherence table in §2 no
  longer has a "truth leaks" row. Verification no longer waits on chance rolls: `admin hallucinate`
  plus the seeded-RNG config make the real trigger path scriptable.
- **Negative**: per-viewer fan-out adds a per-room-update branch (the fast-path check) that did
  not exist before; the hallucination-eligibility caches (`lucidity_tier_cache`, the phantom and
  fake-sender registries) are additional in-memory state that must stay synchronized with
  `LucidityService`'s tier transitions — a missed cleanup path there would leak stale
  hallucination-eligibility rather than stale hallucination content, a narrower but still real
  failure mode.
- **Neutral**: `/map`'s client-side `directionHallucination.ts` usage is deliberately **not**
  reversed by this ADR (§3, final paragraph) — it is an out-of-world admin/editing surface, not an
  in-world one. If that boundary line is judged wrong on review, `directionHallucination.ts`'s
  narrowed single-caller role is the file to revisit.
- **Deferred**: Uneasy's spec'd "misleading exit highlight" (`lucidity-system.md` §5.1) was **not**
  built — no existing UI mechanic supports a highlight distinct from Deranged's whole-exit-list
  swap, and building one is new feature work rather than wiring up a dead call site. Uneasy
  currently delivers only the ambient-overlay half of its written palette.

## 6. Related ADRs

**[SPEC]**

- [ADR-022](ADR-022-ui-v2-client-transition.md) — records `#714` (among `#713`/`#715`) as a
  decide-then-port issue after `HallucinationTicker`'s deletion found its feed pipeline dead
  end-to-end; its `[NOTE]` on `#714` is updated alongside this ADR's publication to record that the
  ticker was **not** rebuilt, and why.

## 7. Related docs

**[SPEC]**

- [`docs/subsystems/SUBSYSTEM_LUCIDITY_DESIGN.md`](../../subsystems/SUBSYSTEM_LUCIDITY_DESIGN.md)
  — new hallucination phenomenology/delivery section, cross-referencing this ADR for the *why*.
- [`docs/archive/lucidity-system.md`](../../archive/lucidity-system.md) §5.1 — the original
  hallucination phenomenology spec this ADR implements delivery for.
- [`docs/archive/phantom-hostile-requirements.md`](../../archive/phantom-hostile-requirements.md)
  — marked superseded alongside this ADR; its Phase-3 gaps are closed here.
- [`docs/archive/reversed-compass-directions-requirements.md`](../../archive/reversed-compass-directions-requirements.md)
  — marked superseded alongside this ADR; its client-side placement is reversed here.

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-09-08 | Initial version, closes `#714`: server-authoritative per-viewer hallucination delivery; explicit reversal of `#626`'s client-side exit-hallucination placement |
