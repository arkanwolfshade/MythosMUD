# Spec Tasks

## Tasks

- [x] 1. Build MythosChronicle core service
  - [x] 1.1 Write unit tests for time conversion, persistence, and freeze/resume behavior
  - [x] 1.2 Implement singleton `MythosChronicle` with conversion helpers and persistence layer
  - [x] 1.3 Integrate Prometheus metrics and structured logging for chronicle operations
  - [x] 1.4 Verify all tests pass

- [x] 2. Implement hourly tick engine and scheduler integration
  - [x] 2.1 Write integration tests for hourly tick emissions and event payloads
  - [x] 2.2 Wire chronicle into task registry and EventBus for `mythos.hour.tick`
  - [x] 2.3 Provide helper APIs (e.g., witching hour checks) for dependent modules
  - [x] 2.4 Verify all tests pass

- [x] 3. Create calendar schemas and JSON ingestion pipeline
  - [x] 3.1 Write validation tests covering holiday JSON and CLI validator behavior
  - [x] 3.2 Define schema files and Pydantic models for holidays and schedules
  - [x] 3.3 Build JSON loaders plus CLI validator referencing `docs/MYTHOS_HOLIDAY_CANDIDATES.md`
  - [x] 3.4 Verify all tests pass

- [x] 4. Integrate system consumers (NPCs, environment, holiday service, admin tooling)
  - [x] 4.1 Write tests for NPC schedule shifts, lighting changes, and `/admin/time`
  - [x] 4.2 Implement holiday service managing active bonuses and 48-hour limits
  - [x] 4.3 Update NPC, room, and admin modules to subscribe to chronicle events
  - [x] 4.4 Verify all tests pass

- [ ] 5. Update client UI/UX and end-to-end coverage
  - [ ] 5.1 Write UI/unit and Playwright tests for Mythos clock, banners, and commands
  - [ ] 5.2 Implement HUD updates, notification hooks, and command outputs
  - [ ] 5.3 Extend docs, runbooks, and CI (lint/test) to cover new assets
  - [ ] 5.4 Verify all tests pass
