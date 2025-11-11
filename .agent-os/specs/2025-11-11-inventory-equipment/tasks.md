# Spec Tasks

## Tasks

- [ ] 1. Baseline inventory persistence tests
  - [ ] 1.1 Author pytest fixtures covering empty, partial, and full inventories
  - [ ] 1.2 Draft round-trip serialization/deserialization tests against JSON schema
  - [ ] 1.3 Verify all tests pass

- [ ] 2. Implement persistence migration
  - [ ] 2.1 Write tests validating migration idempotence and row creation per player
  - [ ] 2.2 Create SQLite migration script establishing `player_inventories`
  - [ ] 2.3 Update verification script to enforce table presence before startup
  - [ ] 2.4 Update seeded databases (`unit_test`, `local`, `e2e_test`) to include the new table and default rows
  - [ ] 2.5 Verify all tests pass

- [ ] 3. Integrate JSON schema validation runtime
  - [ ] 3.1 Write tests asserting invalid payloads are rejected with diagnostics
  - [ ] 3.2 Implement schema loader/cache and validation hooks in persistence layer
  - [ ] 3.3 Add structured logging for schema validation failures
  - [ ] 3.4 Verify all tests pass

- [ ] 4. Construct inventory service stacking logic
  - [ ] 4.1 Write tests for stacking, splitting, and capacity enforcement
  - [ ] 4.2 Implement stacking algorithms with slot management helpers
  - [ ] 4.3 Verify thread-safety or atomic mutation assumptions with docstrings/tests
  - [ ] 4.4 Verify all tests pass

- [ ] 5. Implement dupe protection and concurrency guards
  - [ ] 5.1 Write tests simulating double-execution and race conditions
  - [ ] 5.2 Add atomic command guards and idempotent execution pathways
  - [ ] 5.3 Log anomaly detections with moderation-friendly metadata
  - [ ] 5.4 Verify all tests pass

- [ ] 6. Build equip/unequip service helpers
  - [ ] 6.1 Write tests for slot validation, auto-swaps, and overflow handling
  - [ ] 6.2 Implement equip/unequip helpers consuming stacking services
  - [ ] 6.3 Ensure metadata propagation for equipped items
  - [ ] 6.4 Verify all tests pass

- [ ] 7. Implement player command handlers
  - [ ] 7.1 Write tests for `inventory`, `pickup`, `drop`, `equip`, and `unequip` commands
  - [ ] 7.2 Integrate command handlers with services and validation
  - [ ] 7.3 Confirm rate limiting and argument validation paths
  - [ ] 7.4 Verify all tests pass

- [ ] 8. Update room rendering for dropped items
  - [ ] 8.1 Write tests for room description formatting and client rendering
  - [ ] 8.2 Implement room state updates and description augmentation
  - [ ] 8.3 Confirm narrative flavor text adheres to Mythos tone
  - [ ] 8.4 Verify all tests pass

- [ ] 9. Logging, monitoring, and moderation audit
  - [ ] 9.1 Write tests or assertions for logging payload structure
  - [ ] 9.2 Verify enhanced logging includes required context fields
  - [ ] 9.3 Integrate alerts/metrics for dupe anomaly detection
  - [ ] 9.4 Verify all tests pass

- [ ] 10. Final integration and regression sweep
  - [ ] 10.1 Execute end-to-end tests covering lifecycle scenarios
  - [ ] 10.2 Run `make format`, `make my`, `make lint`, `make test`, and review coverage thresholds
  - [ ] 10.3 Update documentation and TASKS.local.md with outcomes
  - [ ] 10.4 Verify all tests pass
