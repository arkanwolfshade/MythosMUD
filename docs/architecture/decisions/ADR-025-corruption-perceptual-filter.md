# ADR-025: Corruption as a Global Perceptual Filter, Not Per-Message Styling

**Version 1.0.0** · MythosMUD · 2026-09-09

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-09-09

Written while decomposing `#145` ("Add Lovecraftian atmosphere effects to chat system") into
implementable design documents. `#145` asks for corruption-driven "visual corruption", "color
shifts", and an acceptance criterion that "corruption effects are visually distinct." Taken
literally, that criterion **contradicts [ADR-024](ADR-024-server-authoritative-perceived-reality.md)**
§3, which deleted `ChatHistoryPanel.tsx`'s `TAG_MESSAGE_CLASSES.hallucination` on the explicit
ground that "a distinct color for a hallucinated message is itself a truth leak." This ADR
reconciles the two: it draws the line between styling that reveals a *message's* nature (forbidden)
and styling that reflects a *viewer's* condition (permitted), and states which of #145's visuals
fall on which side.

## 2. Context

**[NOTE]**
ADR-024's rule exists because the server lies to a viewer on purpose (hallucinations, exit
hallucination, phantom occupants), and any client-visible difference between a lied-to message and
a truthful one hands the player a tell that defeats the lie. That argument is airtight for
**per-message** styling — a hallucinated whisper rendered in a different color is distinguishable
from a real one by definition.

Corruption is a different shape of problem. `server/models/game.py:174` —
`corruption: int = Field(default=0, description="Taint from dark forces")` — is a per-*player*
value, not a per-*message* one. It has exactly one consumer today, `is_corrupted() -> bool`
(`server/models/game.py:322`, threshold `>= 50`), and no chat code reads it at all. Nothing about
corruption requires comparing one message against another; the entire chat pane belongs to one
viewer with one corruption value.

## 3. Decision

**[SPEC]**

**A global, viewer-scoped perceptual filter is not a truth leak. Per-message marking still is.**

Corruption-driven visuals apply uniformly to the reader's **entire chat pane** — every message,
from every sender, hallucinated or real, styled identically by one CSS custom property derived
from the reader's own corruption value (see
[SUBSYSTEM_CORRUPTION_DESIGN.md](../../subsystems/SUBSYSTEM_CORRUPTION_DESIGN.md) for the
filter's shape). Because no message is ever styled *relative to another message the same viewer
sees*, there is nothing for the filter to reveal: a hallucinated message and a real one degrade
identically, exactly as ADR-024 requires.

This is narrower than it sounds. It does **not** reopen ADR-024 §3's decision:

- `TAG_MESSAGE_CLASSES` stays free of any hallucination/effect entry. Per-message tag-driven
  styling (`ChatHistoryPanel.tsx`'s `classFromTags`) remains prohibited for anything that could
  distinguish message provenance.
- The dampening tags emitted by `lucidity_communication_dampening.py` (`strained`, `muffled`,
  `scrambled`) stay unstyled on the client. The fact that the client currently drops
  `_event.data.tags` entirely (`messageHandlers.ts:127` never reads it) needs no repair — there is
  still nothing for it to feed.
- A corruption filter reads **one number the reader already possesses about themselves**. It never
  reads or reacts to any property of an individual message.

## 4. Alternatives Considered

**[SPEC]**

1. **Per-message corruption styling ("corruption is known, hallucination is not")** — Rejected.
   The argument that a player already knows their own corruption level and so per-message styling
   leaks nothing was considered, but it does not survive contact with hallucinated messages: any
   per-message divergence between how a real message and a hallucinated one render — even if both
   are "corruption-styled" — becomes a tell the moment their styling differs by anything other than
   the reader's own state. The failure mode is exactly the one ADR-024 closed.
2. **No corruption visuals at all** — Rejected as unnecessarily strict. It would satisfy ADR-024
   trivially but abandon #145's "color shifts" and "visual corruption" bullets entirely, when a
   viewer-scoped filter satisfies both constraints at once.
3. **Global filter plus a narrow per-message exception list** (e.g. never darken the player's own
   echoed messages) — Rejected for this round. Expressively richer, but an exception list is a
   second thing that must stay correct forever, or it quietly becomes the leak this ADR exists to
   prevent. Revisit only if a concrete accessibility need requires it.

## 5. Consequences

**[SPEC]**

- **Positive**: #145's corruption-visuals bullets become buildable without amending ADR-024's
  substance. The corruption subsystem doc's filter is a single derived value per viewer, not a
  per-message pipeline — the smallest correct implementation, not a compromise.
- **Positive**: No client wiring for `tags` needs to be repaired. The filter reads corruption
  directly (already delivered to the client via `player_update`/`game_state`, not a new channel),
  independent of the chat message stream entirely.
- **Neutral**: This ADR does not authorize a client-side intensity control over the filter — see
  [SUBSYSTEM_CHAT_EFFECT_ACCESSIBILITY_DESIGN.md](../../subsystems/SUBSYSTEM_CHAT_EFFECT_ACCESSIBILITY_DESIGN.md)
  for why the accessibility answer is a server-side floor rather than a client-side slider.
- **Deferred**: If corruption later needs a per-message effect (not merely a pane-wide filter), that
  is a **new** decision requiring its own alternatives analysis — this ADR's reasoning does not
  extend to it automatically.

## 6. Related ADRs

**[SPEC]**

- [ADR-024](ADR-024-server-authoritative-perceived-reality.md) — establishes the per-message
  truth-leak rule this ADR narrows to per-message scope specifically, leaving it otherwise intact.

## 7. Related docs

**[SPEC]**

- [`docs/subsystems/SUBSYSTEM_CORRUPTION_DESIGN.md`](../../subsystems/SUBSYSTEM_CORRUPTION_DESIGN.md)
  — the corruption subsystem this ADR licenses the visual filter for.
- [`docs/subsystems/SUBSYSTEM_CHAT_EFFECT_ACCESSIBILITY_DESIGN.md`](../../subsystems/SUBSYSTEM_CHAT_EFFECT_ACCESSIBILITY_DESIGN.md)
  — the accessibility floor that bounds the filter server-side.

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-09-09 | Initial version: reconciles #145's corruption-visuals ask with ADR-024's per-message truth-leak rule via a global, viewer-scoped filter |
