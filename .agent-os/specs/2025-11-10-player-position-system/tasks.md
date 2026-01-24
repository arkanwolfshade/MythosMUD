# Spec Tasks

## Tasks

[x] 1. Implement position persistence and data plumbing

- [x] 1.1 Write tests covering `stats.position` persistence across login/logout cycles
- [x] 1.2 Update player stats JSON schema/defaults to include `position`
- [x] 1.3 Load and store in-memory position from persisted stats on login/logout
- [x] 1.4 Verify all tests pass

- [x] 2. Add position command handling and alias wiring
  - [x] 2.1 Write command handler tests for `/sit`, `/stand`, `/lie` including alias resolution
  - [x] 2.2 Implement slash command handlers and shared service logic for posture changes
  - [x] 2.3 Ensure client-side alias system maps `sit`/`stand`/`lie` to slash commands
  - [x] 2.4 Verify all tests pass

- [x] 3. Enforce movement restrictions and room notifications
  - [x] 3.1 Write movement guard tests covering seated/prone scenarios using existing combat restriction harness
  - [x] 3.2 Extend combat movement restriction pipeline to block non-standing movement with structured logging
  - [x] 3.3 Trigger descriptive room notifications on position change
  - [x] 3.4 Verify all tests pass

- [ ] 4. Expose position in player status APIs and UI
- [x] 4.1 Write API/UI integration tests ensuring `/whoami` and player info panel show position
- [x] 4.2 Update API responses and client components to display posture
  - [ ] 4.3 Verify all tests pass
