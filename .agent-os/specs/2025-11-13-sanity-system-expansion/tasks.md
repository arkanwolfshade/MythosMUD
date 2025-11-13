# Spec Tasks

## Tasks

- [x] 1. Implement sanity data model and persistence
  - [x] 1.1 Write database migration tests for new sanity tables and constraints
  - [x] 1.2 Add SQLAlchemy models for `player_sanity`, `sanity_adjustment_log`, `sanity_exposure_state`, and `sanity_cooldowns`
  - [x] 1.3 Implement repository/service layer for SAN adjustments and liability tracking
  - [x] 1.4 Verify all tests pass

- [ ] 2. Build passive SAN flux scheduler and telemetry
  - [ ] 2.1 Write scheduler unit tests covering passive gain/drain scenarios
  - [ ] 2.2 Extend tick loop to apply environment/time modifiers and adaptive resistance
  - [ ] 2.3 Emit structured logging and metrics for passive SAN changes
  - [ ] 2.4 Verify all tests pass

- [ ] 3. Integrate active SAN loss and recovery hooks
  - [ ] 3.1 Write tests for encounter-driven SAN loss, recovery actions, and liability triggers
  - [ ] 3.2 Wire SAN adjustments into combat, exploration, ritual learning, and death/sanitarium flows
  - [ ] 3.3 Implement recovery endpoints (`pray`, `meditate`, `group solace`, `therapy`, `folk tonic`)
  - [ ] 3.4 Verify all tests pass

- [ ] 4. Deliver client UX for SAN feedback and hallucinations
  - [ ] 4.1 Write frontend tests for SAN indicators, hallucination prompts, and rescue messaging
  - [ ] 4.2 Render hallucinated mobs, command misfires, and distorted chat in the terminal UI
  - [ ] 4.3 Surface rescue progress and sanitarium transitions with accessible cues
  - [ ] 4.4 Verify all tests pass

- [ ] 5. Implement catatonia rescue and sanitarium workflows
  - [ ] 5.1 Write integration tests for `ground` command, catatonia transitions, and sanitarium respawn
  - [ ] 5.2 Add server-side handling for rescue channeling, failure conditions, and liability escalation
  - [ ] 5.3 Ensure sanitarium debrief and therapy limits hook into existing NPC systems
  - [ ] 5.4 Verify all tests pass
