# Chat Effect Accessibility Floor Design

**Version 1.1.0** · MythosMUD · 2026-09-10

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Planned. A constraints specification, not a feature — it bounds the atmosphere effects
this decomposition of `#145` describes elsewhere, rather than adding a new one.

`#145` asks for "options to adjust effect intensity" and "effects don't make chat unusable." Every
chat-degrading effect in scope — text garbling
(`server/services/lucidity_communication_dampening.py`), corruption's perceptual filter
(`SUBSYSTEM_CORRUPTION_DESIGN.md`), hallucinations, entity contact, and dream messages — is **server
game state under [ADR-024](../architecture/decisions/ADR-024-server-authoritative-perceived-reality.md)**.
A client-side opt-out that weakened or disabled them would let a player render identical game state
more legibly than an opponent, which is a combat advantage and directly contradicts `#145`'s own
"Fairness" balance criterion. This document specifies hard, server-side guarantees instead of a
settings surface.

## 2. Why (almost) no settings panel

**[SPEC]**

As of `#804`'s client PR, `ThemeProvider` **is mounted** (`client/src/AppRouter.tsx`, wrapping the
whole app) and a settings panel **does exist**
(`client/src/components/ui-v2/panels/SettingsPanel.tsx`). This section originally argued against
building either; §1.1.0 narrows that argument rather than discarding it — the reasoning below still
holds for every *server-side* effect, and still explains why the panel that got built is
deliberately small.

- **Server-side effects still can't be tuned client-side without a fairness problem.** Garbling,
  shout blocking, and hallucination content are decided server-side per ADR-024; a client toggle
  over them would either do nothing (the client can't undo a decision it never made) or require the
  server to send an *undistorted* copy alongside the distorted one and let the client choose — which
  defeats the entire point of the effects (an opponent with the toggle off reads clean text while
  yours is garbled). `SettingsPanel.tsx` exposes **no control over any of these**, and never should.
- **Corruption's grain overlay is the one exception, because it's presentation-only** (per
  [ADR-025](../architecture/decisions/ADR-025-corruption-perceptual-filter.md)): the `chatGrain`
  preference toggles a decorative texture derived from the viewer's own already-delivered corruption
  value, touching no game state and creating no fairness gap between players. That is the single
  toggle `SettingsPanel.tsx` ships for chat effects; the text-color filter itself
  (`--corruption-intensity`, `SUBSYSTEM_CORRUPTION_DESIGN.md` §5) has no toggle, since a player
  darkening their own text tint would still be reading identical characters — there is nothing there
  to gain an advantage from hiding.
- **The panel also surfaces unrelated, already-built preferences** (`animations`, `compactMode`,
  `highContrast`, `reducedMotion`, `showDebugInfo`) that had storage and hooks
  (`useThemeContext.ts`) but no control surface until now. Their inclusion piggybacks on `chatGrain`
  needing a panel to exist at all; it does not expand this document's scope, since none of them
  touch a server-side effect either.

## 3. The floor — server-side hard guarantees

**[SPEC]**

Every effect that mutates message text or blocks it must satisfy these unconditionally, with no
per-player configuration:

1. **Bounded garbling proportion.** `_maybe_scramble_deranged_message`
   (`lucidity_communication_dampening.py:59`) already caps its word-swap count at
   `min(len(words) // 4, 3)` — never more than a quarter of the message, capped at 3 swaps
   regardless of length. Any new distortion effect (corruption's future non-visual effects, if any
   ever touch message text) must hold to an equivalent or tighter bound: **never garble more than
   25% of a message's content.**
2. **Names and numbers are never corrupted.** No effect may alter a player name, item name, room
   name, or numeric value (damage, currency, coordinates) appearing in a message. This is a new
   constraint — `_maybe_muffle_fractured_message`'s punctuation-strip
   (`lucidity_communication_dampening.py:50`) and the word-scramble already satisfy it incidentally
   (they don't target specific tokens), but any future effect must preserve it explicitly, since a
   corrupted number or name is a correctness bug dressed as atmosphere.
3. **Blocking always returns a legible refusal.** `_apply_sender_effects`'s shout-block
   (`lucidity_communication_dampening.py:43`) already sets `result["message"] = ""` and a `blocked`
   flag rather than sending garbled text — the caller is responsible for surfacing a plain-language
   refusal (e.g. "your throat won't obey you"), never silence with no feedback and never a garbled
   attempt.
4. **Contrast floor on the corruption filter.** Whatever CSS the corruption filter
   (`SUBSYSTEM_CORRUPTION_DESIGN.md` §5) applies, text must remain readable at the *maximum*
   corruption value (100) against the theme's background — verified against WCAG AA contrast ratios
   in both light and dark themes, the same bar `ThemeContext.tsx`'s `highContrast` mode implies for
   the rest of the UI even though nothing currently reads that flag in production.

## 4. `prefers-reduced-motion`

**[SPEC]**

Any effect with a motion/animation component (an animated corruption overlay, a flicker on message
arrival) must honor `prefers-reduced-motion`, using the pattern already proven in this codebase:
`client/src/components/map/AsciiNoise.tsx:23-24,42`'s `prefersReducedMotion()` via
`window.matchMedia`, which halts noise churn without removing the effect's static presence. A static
corruption filter (no animation) is exempt — this guarantee is about *motion*, not intensity.

## 5. What this document does not do

**[SPEC]**

- It does not add, and never will add, a settings control over any server-side effect (garbling,
  shout blocking, hallucination content) — `chatGrain` (§2) is deliberately the only chat-effect
  toggle in `SettingsPanel.tsx`, and it governs presentation only.
- It does not weaken any server-side effect's actual intensity — it bounds what future effects may
  do, and audits that the existing dampening effects already comply (they do, per §3.1 and §3.3).
- It does not specify `SettingsPanel.tsx`'s design beyond the one row this document is responsible
  for; the panel's other rows (`animations`, `compactMode`, etc.) are `ThemeContext.tsx`'s existing
  preferences getting a control surface, not new accessibility guarantees this document makes.

## 6. Related docs

**[SPEC]**

- [ADR-024](../architecture/decisions/ADR-024-server-authoritative-perceived-reality.md) — why
  server-side effects can't be safely client-toggled.
- [ADR-025](../architecture/decisions/ADR-025-corruption-perceptual-filter.md) — the one effect in
  this decomposition that is presentation-only and therefore the right future home for any
  intensity control, if one is ever built.
- [SUBSYSTEM_CORRUPTION_DESIGN.md](SUBSYSTEM_CORRUPTION_DESIGN.md) — the filter this floor bounds.

## 7. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-09-09 | Initial version, filed to close part of `#145`: server-side accessibility guarantees in place of a client intensity slider |
| 1.1.0 | 2026-09-10 | `#804`'s client PR mounted `ThemeProvider` and built `SettingsPanel.tsx`, taken up in this document's §2 carve-out for corruption's presentation-only filter (`chatGrain`); §5 updated to match. No change to the §3 server-side floor or §4 motion guarantee. |
