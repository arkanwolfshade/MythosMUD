# Spec Tasks

## Tasks

- [ ] 1. Implement position persistence and data plumbing
  - [ ] 1.1 Write tests covering `stats.position` persistence across login/logout cycles
  - [ ] 1.2 Update player stats JSON schema/defaults to include `position`
  - [ ] 1.3 Load and store in-memory position from persisted stats on login/logout
  - [ ] 1.4 Verify all tests pass

- [ ] 2. Add position command handling and alias wiring
  - [ ] 2.1 Write command handler tests for `/sit`, `/stand`, `/lie` including alias resolution
  - [ ] 2.2 Implement slash command handlers and shared service logic for posture changes
  - [ ] 2.3 Ensure client-side alias system maps `sit`/`stand`/`lie` to slash commands
  - [ ] 2.4 Verify all tests pass

- [ ] 3. Enforce movement restrictions and room notifications
  - [ ] 3.1 Write movement guard tests covering seated/prone scenarios using existing combat restriction harness
  - [ ] 3.2 Extend combat movement restriction pipeline to block non-standing movement with structured logging
  - [ ] 3.3 Trigger descriptive room notifications on position change
  - [ ] 3.4 Verify all tests pass

- [ ] 4. Expose position in player status APIs and UI
  - [ ] 4.1 Write API/UI integration tests ensuring `/whoami` and player info panel show position
  - [ ] 4.2 Update API responses and client components to display posture
  - [ ] 4.3 Verify all tests pass
