# Spec Requirements Document

> Spec: Player Position System
> Created: 2025-11-10

## Overview

Introduce a player position system with standing as default and optional sitting or lying postures, affecting
movement and presentation while persisting across sessions.

## User Stories

### Positional Roleplay Foundations

As a player exploring the Miskatonic corridors, I want to sit or lie down using intuitive commands so that I can
roleplay moments of rest or dramatic collapse in a way consistent with Mythos ambiance.

When I type `/sit` or `/lie` (with optional “down”), or invoke character aliases `sit` or `lie`, my avatar’s state
changes. The system confirms the shift, stores it in memory and persistence, and notifies nearby observers with
descriptive flavor text drawn from Pnakotic-inspired messaging.

### Movement Restrictions While Reclining

As a player temporarily resting, I want the system to prevent me from accidentally wandering off while seated or
prone, so that posture changes feel meaningful.

If I attempt to move rooms while not standing, the engine blocks the move, tells me I must stand first, and leaves me
in place with no automatic posture adjustment.

### Character Awareness

As a scholar monitoring my status, I want to see my current position in `/whoami` output and on the Player Information
panel so that I can verify posture without guesswork.

Both representations pull from the persisted position state, ensuring consistency between server truth and client UI.

## Spec Scope

1. **Slash Commands** - Implement `/sit`, `/stand`, and `/lie` (with optional “down”) commands plus default aliases at

   character creation.

2. **State Management** - Track player position in memory and SQLite so reconnects restore posture; ensure standing is

   default on creation/login when no value exists.

3. **Movement Restriction** - Block room transitions while sitting or lying with an explicit “stand first” message and

   no auto-standing.

4. **Observer Notifications** - Broadcast structured descriptive messages to room occupants when a player changes

   position.

5. **Status Display** - Surface current position in `/whoami` output and the Player Information panel using shared data

   sourcing.

## Out of Scope

Combat or skill modifiers tied to position changes.

- Animations or audio cues beyond text messaging.

## Expected Deliverable

1. Demonstrable Playwright scenarios showing players issuing position commands, observers seeing notifications, and

   movement being blocked while seated or prone.

2. `/whoami` command output and Player Information panel updates reflecting persisted position across reconnects.
