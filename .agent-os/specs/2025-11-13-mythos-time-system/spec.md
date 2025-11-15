# Spec Requirements Document

> Spec: Mythos Time System
> Created: 2025-11-13

## Overview

Deliver a unified Mythos time and calendar system that compresses real time at a 1:9.6 ratio, governs all in-game temporal mechanics, and enables scheduled festivals drawn from multiple traditions. This foundation must freeze when the server halts and resume deterministically on restart.

## User Stories

### Timekeeping Arbiter

As a systems engineer, I want a deterministic `MythosChronicle` service that converts between real-world and Mythos time, so that every subsystem can coordinate day/night cycles and event triggers without bespoke math.

The service exposes conversion helpers, hour-level tick notifications, and persists the last-known real/Mythos timestamps for accurate resume after downtime.

### World Event Designer

As a narrative designer, I want to author holiday and schedule definitions in JSON, so that I can add Catholic, Muslim, Jewish, and neo-pagan observances (bounded to the first two Mythos days) without code changes.

The engine ingests validated JSON, generates hourly trigger windows, and rotates full events each time the compressed calendar reaches the configured dates. Mythos-specific cult calendars sourced from `docs/MYTHOS_HOLIDAY_CANDIDATES.md` provide additional faction content.

### Player Explorer

As a player, I want the client UI and command feedback to surface the current Mythos time, upcoming festivals, and contextual room lighting cues, so that the accelerated world feels alive and predictable.

The UI renders a Mythos clock, banner notifications for active holidays, and iconography keyed to day/night and seasonal states provided by the server.

## Spec Scope

1. **MythosChronicle core service** - Implement the authoritative time conversion, persistence, and hourly tick broadcaster.
2. **Scheduler integration** - Wire game systems (NPC routines, lighting, passive effects) to the chronicle via structured hooks.
3. **Holiday and schedule JSON ingestion** - Define schemas, loaders, and validation for designer-authored calendars with fixed lunar alignment.
4. **UI/UX surfacing** - Update client HUD and command responses to show Mythos time, holiday banners, and contextual cues.
5. **Operational controls** - Provide admin tooling/logging to monitor time state, freeze/resume events, and validate upcoming triggers.

## Out of Scope

- Retrofitting legacy timed content that will be rebuilt on top of the new chronicle.
- Implementing real-world time displays or localization for calendar labels.

## Expected Deliverable

1. Hourly-accurate Mythos timekeeping that can be integration-tested by simulating server restarts and verifying resumed schedules.
2. End-to-end demos (Playwright + pytest) proving holiday JSON ingestion, NPC schedule shifts, and client UI time displays under compressed cycles.
3. Curated holiday references and seed data: `docs/MYTHOS_HOLIDAY_CANDIDATES.md` outlining cult observances plus companion entries in `data/calendar/holidays.json` (e.g., Innsmouth Tide Offering, Feast of Yig, Ghoulmarket Convocation) ready for schema validation.
