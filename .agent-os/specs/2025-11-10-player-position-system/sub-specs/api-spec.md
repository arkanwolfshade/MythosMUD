# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-11-10-player-position-system/spec.md

## Endpoints

### GET /api/player/whoami

**Purpose:** Expose player identity and status, now including posture.
**Parameters:** None (authenticated session required).
**Response:** Extend JSON payload with `position` field (`"standing" | "sitting" | "lying"`). Maintain backwards
compatibility by ensuring clients ignoring the field remain unaffected.
**Errors:** Existing authentication errors only.

### GET /api/player/state

**Purpose:** Provide full player state for the Player Information panel.
**Parameters:** None (authenticated session required).
**Response:** Include `position` field mirroring `/api/player/whoami` to keep client displays consistent.
**Errors:** Existing authentication/authorization errors only.

### POST /api/commands/execute

**Purpose:** Handle slash command submissions including `/sit`, `/stand`, `/lie`.
**Parameters:** Request body already conveys command text; ensure validation allows the new commands.
**Response:** Return structured success payload including updated `position` value so clients can update immediately.
**Errors:** Validation errors for unsupported commands, movement constraint responses remain 200 with message payload.

## Controllers

- Update command execution controller to route new slash commands to posture-handling service functions.
- Ensure movement controller checks `position` before room transitions and returns structured denial payload when not
  standing.

## Purpose

- Provide consistent API exposure of posture for UI elements.
- Maintain real-time synchronization between command execution, server state, and client displays.
