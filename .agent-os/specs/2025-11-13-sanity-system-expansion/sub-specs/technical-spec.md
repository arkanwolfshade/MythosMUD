# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-13-sanity-system-expansion/spec.md

## Technical Requirements

- **Sanity Data Model**
  - Introduce `player_sanity` table storing current SAN, tier, liability state, and timestamps.
  - Add `sanity_exposure_log` table documenting passive/active adjustments with reason codes, correlation IDs, and Mythos exposure flags.
  - Persist hallucination cooldowns and command misfire weights via JSON field or auxiliary table to survive reconnects.
- **Server Processing**
  - Extend scheduled tick service to apply passive SAN flux (environment, lighting, companions) every in-game minute.
  - Embed SAN adjustment hooks inside combat resolution, encounter discovery, ritual learning, NPC ability handlers, and death flows.
  - Implement liability engine that evaluates threshold crossings and assigns/removes liabilities with quest hooks.
  - Add catatonia watchdog to block command processing, queue rescue eligibility, and auto-trigger sanitarium transfer at −100 SAN.
- **API & Protocol**
  - Update player state payloads (WebSocket/SSE) to include SAN value, tier, active liabilities, and hallucination cues.
  - Add REST/command endpoints for recovery actions (`pray`, `meditate`, `group solace`, `therapy session`, `folk tonic`) with validation and cooldown responses.
  - Provide structured hallucination events (phantom mobs, message alterations) tagged for client rendering, including toxicity-safe text variants.
- **Client UX**
  - Surface SAN changes via terminal overlays, HUD badges, and log messages following accessibility guidelines (color contrast, text alternatives).
  - Render hallucination prompts, phantom mob encounters, and command misfire feedback without breaking command history.
  - Display rescue prompts and progress meters for `ground` interactions, including failure/success outcomes.
- **Telemetry & Logging**
  - Instrument `get_logger` calls for every SAN change with fields: `player_id`, `san_change`, `reason`, `tier_before`, `tier_after`, `location_id`.
  - Emit metrics counters/timers for hallucination frequency, liability assignments, catatonia rescues, and sanitarium respawns.
  - Ensure logs redact sensitive data and comply with COPPA by excluding player-identifying details.

## External Dependencies (Conditional)

None anticipated; reuse existing FastAPI, SQLAlchemy, and client infrastructure.
