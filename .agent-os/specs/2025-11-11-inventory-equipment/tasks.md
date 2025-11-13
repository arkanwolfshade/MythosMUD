# Spec Tasks

## Tasks

- [x] 1. Baseline inventory persistence tests
  - [x] 1.1 Author pytest fixtures covering empty, partial, and full inventories
  - [x] 1.2 Draft round-trip serialization/deserialization tests against JSON schema
  - [x] 1.3 Verify all tests pass

- [x] 2. Implement persistence migration
  - [x] 2.1 Write tests validating migration idempotence and row creation per player
  - [x] 2.2 Create SQLite migration script establishing `player_inventories`
  - [x] 2.3 Update verification script to enforce table presence before startup
  - [x] 2.4 Update seeded databases (`unit_test`, `local`, `e2e_test`) to include the new table and default rows
  - [x] 2.5 Verify all tests pass

- [x] 3. Integrate JSON schema validation runtime
  - [x] 3.1 Write tests asserting invalid payloads are rejected with diagnostics
  - [x] 3.2 Implement schema loader/cache and validation hooks in persistence layer
  - [x] 3.3 Add structured logging for schema validation failures
  - [x] 3.4 Verify all tests pass

- [x] 4. Construct inventory service stacking logic
  - [x] 4.1 Write tests for stacking, splitting, and capacity enforcement
  - [x] 4.2 Implement stacking algorithms with slot management helpers
  - [x] 4.3 Verify thread-safety or atomic mutation assumptions with docstrings/tests
  - [x] 4.4 Verify all tests pass

- [x] 5. Implement dupe protection and concurrency guards
  - [x] 5.1 Write tests simulating double-execution and race conditions
  - [x] 5.2 Add atomic command guards and idempotent execution pathways
  - [x] 5.3 Log anomaly detections with moderation-friendly metadata
  - [x] 5.4 Verify all tests pass

- [x] 6. Build equip/unequip service helpers
  - [x] 6.1 Write tests for slot validation, auto-swaps, and overflow handling
  - [x] 6.2 Implement equip/unequip helpers consuming stacking services
  - [x] 6.3 Ensure metadata propagation for equipped items
  - [x] 6.4 Verify all tests pass

- [x] 7. Implement player command handlers
  - [x] 7.1 Write tests for `inventory`, `pickup`, `drop`, `equip`, and `unequip` commands
  - [x] 7.2 Integrate command handlers with services and validation
  - [x] 7.3 Confirm rate limiting and argument validation paths
  - [x] 7.4 Verify all tests pass

- [x] 8. Update room rendering for dropped items
  - [x] 8.1 Write tests for room description formatting and client rendering
  - [x] 8.2 Implement room state updates and description augmentation
  - [x] 8.3 Confirm narrative flavor text adheres to Mythos tone
  - [x] 8.4 Verify all tests pass

- [x] 9. Logging, monitoring, and moderation audit
  - [x] 9.1 Write tests or assertions for logging payload structure
  - [x] 9.2 Verify enhanced logging includes required context fields
  - [x] 9.3 Integrate alerts/metrics for dupe anomaly detection
  - [x] 9.4 Verify all tests pass

- [x] 10. Final integration and regression sweep
  - [x] 10.1 Execute end-to-end tests covering lifecycle scenarios
  - [x] 10.2 Run `make format`, `make my`, `make lint`, `make test`, and review coverage thresholds
  - [x] 10.3 Update documentation and TASKS.local.md with outcomes
