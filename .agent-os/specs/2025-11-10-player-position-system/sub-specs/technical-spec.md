# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-10-player-position-system/spec.md

## Technical Requirements

- **Data Model**: Persist the `position` value inside the existing player stats JSON blob (e.g., `stats.position`),
  storing enum-like values (`standing`, `sitting`, `lying`). Default to `standing`. Ensure migration updates existing
  stats records and server-side models use a shared constant set to avoid typos.
- **In-Memory Representation**: Augment the player session object/state machine with a `position` attribute initialized
  from persistence on login and updated after command handling. Guarantee thread-safe updates if player objects are
  shared across asyncio tasks.
- **Command Handling**: Implement slash command handlers for `/sit`, `/stand`, `/lie` (optional “down”). Back them with
  reusable service functions so aliases (`sit`, `stand`, `lie`) resolve client-side into the corresponding slash command
  before submission. Validate current state (no-op if already in requested posture) and emit confirmation messages to
  the invoking player.
- **Movement Guard**: Extend the existing combat movement restriction logic to also deny room transitions when position
  is not `standing`. Reuse/augment current guardrails so the same pipeline blocks movement, logs an info-level message,
  and sends the curated “cannot move while seated/prone; stand first” response with no parallel system.
- **Observer Broadcasts**: Use existing room messaging infrastructure to send descriptive notifications when a player
  changes position. Messages should include player display name and posture, e.g., “Professor Wolfshade settles into a
  seated position,” with Mythos-flavored text.
- **Client Integration**: Update `/whoami` server response payload to include current position, and ensure the Player
  Information panel consumes that field. Add localized text or iconography if needed while keeping accessibility
  compliance (ARIA labels, etc.).
- **Aliases at Creation**: During character creation (and retrofit for existing characters), seed default aliases so
  `sit`, `stand`, and `lie` map to the corresponding slash commands. Provide idempotent logic to avoid duplicate alias
  entries.
- **Testing**: Add pytest coverage verifying command behavior, persistence, movement restriction, and emitted events.
  Add Playwright tests covering multi-client observation and UI updates. Ensure tests remain serial for database usage.

## External Dependencies (Conditional)

None.
