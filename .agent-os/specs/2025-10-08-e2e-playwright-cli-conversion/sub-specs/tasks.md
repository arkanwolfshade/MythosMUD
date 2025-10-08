# Implementation Tasks

This is the task breakdown for implementing the spec detailed in @.agent-os/specs/2025-10-08-e2e-playwright-cli-conversion/spec.md

## Task Organization

Tasks are organized into 5 phases with estimated effort and dependencies clearly marked.

---

## Phase 1: Infrastructure Setup (Week 1, Day 1-2)

### Task 1.1: Create Playwright Runtime Configuration
**Estimated Effort**: 2 hours
**Dependencies**: None
**Files to Create**:
- `client/tests/e2e/playwright.runtime.config.ts`

**Requirements**:
- Configure 30-second default timeout
- Set base URL to `http://localhost:5173`
- Enable trace collection on first retry
- Configure Chromium browser
- Set up web server auto-start with port 5173
- Disable web server in CI environment
- Configure test output directory: `test-results/runtime/`
- Configure HTML reporter output: `playwright-report/runtime/`

**Acceptance Criteria**:
- [ ] Configuration file created and properly typed
- [ ] Can run `npx playwright test --config=tests/e2e/playwright.runtime.config.ts` successfully
- [ ] Server auto-starts for local development
- [ ] Server doesn't auto-start in CI environment

---

### Task 1.2: Create Test Fixtures - Database Utilities
**Estimated Effort**: 4 hours
**Dependencies**: Task 1.1
**Files to Create**:
- `client/tests/e2e/runtime/fixtures/database.ts`
- `client/tests/e2e/runtime/global-setup.ts`
- `client/tests/e2e/runtime/global-teardown.ts`

**Requirements**:
- Implement `seedTestDatabase()` function
- Implement `cleanupTestDatabase()` function
- Implement `createDatabaseSchema()` function
- Create baseline test players (ArkanWolfshade, Ithaqua, TestAdmin)
- Implement Argon2 password hashing for test credentials
- Implement database backup mechanism
- Configure global setup/teardown hooks

**Acceptance Criteria**:
- [ ] Database seeding creates all baseline test players
- [ ] Password hashing matches production Argon2 configuration
- [ ] Cleanup resets player positions and stats
- [ ] Backup mechanism preserves previous test database
- [ ] Global setup runs before test suite
- [ ] Global teardown runs after test suite

---

### Task 1.3: Create Test Fixtures - Authentication Helpers
**Estimated Effort**: 3 hours
**Dependencies**: Task 1.2
**Files to Create**:
- `client/tests/e2e/runtime/fixtures/auth.ts`

**Requirements**:
- Implement `loginAsPlayer(page, username, password)` function
  - Navigate to login page
  - Fill username and password fields
  - Click login button
  - Wait for MOTD screen
  - Click Continue button
  - Wait for game interface load
  - Verify successful login
- Implement `logout(page)` function
  - Click logout button
  - Wait for logout confirmation
  - Verify redirect to login page
- Implement `isLoggedIn(page)` helper
- Handle login failures gracefully

**Acceptance Criteria**:
- [ ] `loginAsPlayer()` successfully logs in test players
- [ ] Login function handles MOTD screen transition
- [ ] Login function verifies game interface loaded
- [ ] `logout()` successfully logs out players
- [ ] `isLoggedIn()` correctly detects authentication state

---

### Task 1.4: Create Test Fixtures - Player Utilities
**Estimated Effort**: 2 hours
**Dependencies**: Task 1.2
**Files to Create**:
- `client/tests/e2e/runtime/fixtures/player.ts`

**Requirements**:
- Implement `getPlayerLocation(page)` function
- Implement `sendCommand(page, command)` function
- Implement `waitForMessage(page, messageText, timeout)` function
- Implement `getMessages(page)` function to extract all chat messages
- Implement `clearMessages(page)` function
- Implement message filtering utilities

**Acceptance Criteria**:
- [ ] Can retrieve player location from UI
- [ ] Can send commands via command input
- [ ] Can wait for specific messages with timeout
- [ ] Can extract all chat messages from DOM
- [ ] Message utilities work with all message types

---

### Task 1.5: Create Test Fixtures - Test Data Constants
**Estimated Effort**: 1 hour
**Dependencies**: None
**Files to Create**:
- `client/tests/e2e/runtime/fixtures/test-data.ts`

**Requirements**:
- Export test player credentials
- Export test room IDs
- Export test message templates
- Export error message constants
- Export timeout configurations

**Acceptance Criteria**:
- [ ] All test constants defined and exported
- [ ] Constants match values used in scenarios
- [ ] TypeScript types defined for all constants

---

### Task 1.6: Update package.json Scripts
**Estimated Effort**: 30 minutes
**Dependencies**: Task 1.1
**Files to Modify**:
- `client/package.json`

**Requirements**:
- Add `test:e2e:runtime` script
- Add `test:e2e:runtime:headed` script
- Add `test:e2e:runtime:debug` script
- Add `test:e2e:runtime:ui` script
- Add `test:e2e:runtime:server` script with server tag filtering

**Acceptance Criteria**:
- [ ] All npm scripts execute successfully
- [ ] Scripts use correct config file path
- [ ] Debug and UI modes work for local testing

---

## Phase 2: Category A - Full Conversion (Week 1, Day 3-5)

### Task 2.1: Convert Scenario 11 - Local Channel Errors
**Estimated Effort**: 4 hours
**Dependencies**: Phase 1 complete
**Files to Create**:
- `client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`

**Test Cases to Implement**:
1. Empty local message rejection
2. Invalid command syntax error
3. Long message (>500 chars) rejection
4. Special characters support
5. Unicode characters support
6. Whitespace-only message rejection
7. Valid message after errors
8. System stability after errors

**Acceptance Criteria**:
- [ ] All 8 test cases pass successfully
- [ ] Error messages match expected text
- [ ] Tests complete in <2 minutes total
- [ ] Tests are isolated and don't affect each other

---

### Task 2.2: Convert Scenario 14 - Whisper Errors
**Estimated Effort**: 4 hours
**Dependencies**: Task 2.1 (reuse patterns)
**Files to Create**:
- `client/tests/e2e/runtime/error-handling/whisper-errors.spec.ts`

**Test Cases to Implement**:
1. Non-existent player error
2. Empty whisper message rejection
3. Invalid command syntax
4. Long whisper message rejection
5. Self-whisper rejection
6. Special characters support
7. Unicode characters support
8. Whitespace-only rejection
9. Valid whisper after errors
10. System stability verification

**Acceptance Criteria**:
- [ ] All 10 test cases pass successfully
- [ ] Error messages are clear and informative
- [ ] Tests complete in <2 minutes total

---

### Task 2.3: Convert Scenario 15 - Whisper Rate Limiting
**Estimated Effort**: 5 hours
**Dependencies**: Task 2.2
**Files to Create**:
- `client/tests/e2e/runtime/error-handling/whisper-rate-limiting.spec.ts`

**Test Cases to Implement**:
1. Normal whisper rate (1-3 messages) success
2. Per-recipient rate limit (3 whispers/min to same player)
3. Global rate limit (5 whispers/min total)
4. Rate limit error message verification
5. Rate limit reset after 60 seconds (with timeout)
6. System stability under rate limiting

**Acceptance Criteria**:
- [ ] All 6 test cases pass successfully
- [ ] Rate limit enforcement is accurate
- [ ] 60-second reset test completes successfully
- [ ] Both rate limit types are tested (per-recipient and global)

---

### Task 2.4: Convert Scenario 18 - Whisper Logging
**Estimated Effort**: 4 hours
**Dependencies**: Task 2.2
**Files to Create**:
- `client/tests/e2e/runtime/admin/whisper-logging.spec.ts`

**Test Cases to Implement**:
1. Admin log access with `admin whisper logs`
2. Non-admin log access denial
3. Log content verification
4. Multiple whisper logging
5. Privacy verification (logs not visible to non-admins)
6. Log format and structure verification

**Acceptance Criteria**:
- [ ] All 6 test cases pass successfully
- [ ] Admin permission checks work correctly
- [ ] Log content matches expected format
- [ ] Privacy is maintained for non-admin players

---

### Task 2.5: Convert Scenario 20 - Logout Errors
**Estimated Effort**: 5 hours
**Dependencies**: Task 2.1 (reuse error patterns)
**Files to Create**:
- `client/tests/e2e/runtime/error-handling/logout-errors.spec.ts`

**Test Cases to Implement**:
1. Network error during logout (simulated offline)
2. Server error during logout (fetch failure)
3. Session expiry during logout
4. Error recovery after network restoration
5. Error recovery after session restoration
6. Multiple logout attempts handling
7. Concurrent logout attempts
8. System stability after errors

**Acceptance Criteria**:
- [ ] All 8 test cases pass successfully
- [ ] Network simulation works correctly
- [ ] Error recovery is properly tested
- [ ] System remains stable under error conditions

---

### Task 2.6: Convert Scenario 21 - Logout Accessibility
**Estimated Effort**: 6 hours
**Dependencies**: Task 1.3
**Files to Create**:
- `client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts`

**Test Cases to Implement**:
1. ARIA attributes verification (aria-label, role, tabindex)
2. Keyboard navigation (Tab to focus)
3. Keyboard activation (Enter to activate)
4. Screen reader compatibility (text content + ARIA)
5. Focus management (focusable, visible, enabled)
6. Color contrast verification
7. Touch target size (minimum 44px)
8. Button state changes (disabled, loading, success)
9. Error state accessibility
10. Accessibility summary verification

**Acceptance Criteria**:
- [ ] All 10 test cases pass successfully
- [ ] ARIA attributes meet WCAG 2.1 AA standards
- [ ] Keyboard navigation works without mouse
- [ ] Touch target meets minimum size requirements
- [ ] Color contrast meets WCAG requirements

---

## Phase 3: Category B - Partial Conversion (Week 2, Day 1-3)

### Task 3.1: Convert Scenario 7 - Who Command (Automated Portion)
**Estimated Effort**: 3 hours
**Dependencies**: Phase 2 complete
**Files to Create**:
- `client/tests/e2e/runtime/integration/who-command.spec.ts`

**Automated Test Cases**:
1. Command output format verification
2. Location information display
3. Single player visibility (self in list)
4. Proper formatting with zone + room info
5. Response time <2 seconds

**MCP Portion Remains**:
- Multiple online players visibility
- Real-time player list updates

**Acceptance Criteria**:
- [ ] Automated tests cover single-player functionality
- [ ] Output format matches expected structure
- [ ] MCP scenario updated to focus on multi-player aspects only

---

### Task 3.2: Convert Scenario 19 - Logout Button (Automated Portion)
**Estimated Effort**: 3 hours
**Dependencies**: Task 2.5
**Files to Create**:
- `client/tests/e2e/runtime/integration/logout-button.spec.ts`

**Automated Test Cases**:
1. Button visibility and accessibility
2. Click functionality
3. Logout confirmation message
4. Redirect to login page verification
5. Re-login functionality after logout
6. Button styling verification

**MCP Portion Remains**:
- Logout message broadcasting to other players
- Multi-player session termination

**Acceptance Criteria**:
- [ ] Automated tests cover single-player logout flow
- [ ] Button UI state changes are tested
- [ ] MCP scenario simplified to focus on broadcasting only

---

### Task 3.3: Convert Scenario 12 - Local Channel Integration (Automated Portion)
**Estimated Effort**: 4 hours
**Dependencies**: Task 2.1
**Files to Create**:
- `client/tests/e2e/runtime/integration/local-channel-integration.spec.ts`

**Automated Test Cases**:
1. Player management integration (player lookup works)
2. Location tracking integration (current room verified)
3. Error handling integration (errors properly displayed)
4. Logging integration (messages logged)
5. Authentication integration (token validated)

**MCP Portion Remains**:
- Message broadcasting verification
- Real-time delivery to multiple players

**Acceptance Criteria**:
- [ ] Integration points tested independently
- [ ] System stability verified
- [ ] MCP scenario focuses on message delivery only

---

### Task 3.4: Convert Scenario 17 - Whisper Integration (Automated Portion)
**Estimated Effort**: 4 hours
**Dependencies**: Task 2.2
**Files to Create**:
- `client/tests/e2e/runtime/integration/whisper-integration.spec.ts`

**Automated Test Cases**:
1. Player management integration
2. Authentication integration
3. Rate limiting integration
4. Error handling integration
5. Logging integration
6. Performance integration (multiple messages)

**MCP Portion Remains**:
- Cross-player message delivery
- Real-time whisper notifications

**Acceptance Criteria**:
- [ ] Integration points verified independently
- [ ] Rate limiting works correctly in integration
- [ ] MCP scenario simplified for message delivery only

---

## Phase 4: MCP Scenario Refactoring (Week 2, Day 4-5)

### Task 4.1: Refactor MCP Scenarios for Focused Execution
**Estimated Effort**: 6 hours
**Dependencies**: Phase 3 complete
**Files to Modify**:
- `e2e-tests/scenarios/scenario-01-basic-connection.md`
- `e2e-tests/scenarios/scenario-02-clean-game-state.md`
- `e2e-tests/scenarios/scenario-03-movement-between-rooms.md`
- `e2e-tests/scenarios/scenario-04-muting-system-emotes.md`
- `e2e-tests/scenarios/scenario-05-chat-messages.md`
- `e2e-tests/scenarios/scenario-06-admin-teleportation.md`
- `e2e-tests/scenarios/scenario-08-local-channel-basic.md`
- `e2e-tests/scenarios/scenario-09-local-channel-isolation.md`
- `e2e-tests/scenarios/scenario-10-local-channel-movement.md`
- `e2e-tests/scenarios/scenario-13-whisper-basic.md`
- `e2e-tests/scenarios/scenario-16-whisper-movement.md`

**Requirements**:
- Add "REQUIRES MULTI-PLAYER" marker to scenario titles
- Remove redundant verification steps covered by automated tests
- Simplify execution guards
- Update time estimates
- Improve completion logic
- Add cross-references to automated tests where applicable

**Acceptance Criteria**:
- [ ] All 11 scenarios clearly marked as multi-player required
- [ ] Redundant steps removed
- [ ] Time estimates updated
- [ ] Documentation improved

---

### Task 4.2: Update MCP Playbook Documentation
**Estimated Effort**: 2 hours
**Dependencies**: Task 4.1
**Files to Modify**:
- `e2e-tests/MULTIPLAYER_TEST_RULES.md`
- `e2e-tests/CLEANUP.md`
- `e2e-tests/TESTING_APPROACH.md`

**Requirements**:
- Update scenario count (21 -> 11 MCP scenarios)
- Add reference to automated Playwright CLI tests
- Update execution time estimates
- Add decision tree for when to use automated vs MCP tests
- Update cleanup procedures for new test structure

**Acceptance Criteria**:
- [ ] Documentation accurately reflects new structure
- [ ] Clear guidance on automated vs MCP tests
- [ ] Execution time estimates updated

---

## Phase 5: CI/CD Integration (Week 3, Day 1-2)

### Task 5.1: Create GitHub Actions Workflow for E2E Tests
**Estimated Effort**: 4 hours
**Dependencies**: Phase 2 complete
**Files to Create**:
- `.github/workflows/e2e-runtime-tests.yml`

**Requirements**:
- Configure workflow to run on PR creation and updates
- Set up Node.js v18 and Python 3.11
- Install dependencies (npm, uv)
- Start development server in background
- Wait for server health check on port 54731
- Run Playwright CLI tests
- Upload test artifacts (screenshots, videos, traces)
- Report test results to PR as comment
- Fail workflow if tests fail

**Acceptance Criteria**:
- [ ] Workflow runs successfully on PR creation
- [ ] Server starts and health check passes
- [ ] Tests execute and results are reported
- [ ] Test artifacts uploaded on failure
- [ ] PR comment contains test summary

---

### Task 5.2: Update Existing CI Workflows
**Estimated Effort**: 2 hours
**Dependencies**: Task 5.1
**Files to Modify**:
- `.github/workflows/ci.yml` (if exists)
- `.github/workflows/test.yml` (if exists)

**Requirements**:
- Add E2E runtime tests to existing CI pipeline
- Ensure proper job dependencies
- Configure caching for Playwright browsers
- Set up parallel execution where possible

**Acceptance Criteria**:
- [ ] E2E tests integrated into existing CI
- [ ] Job dependencies configured correctly
- [ ] Browser caching works (faster CI runs)

---

### Task 5.3: Update Makefile Targets
**Estimated Effort**: 1 hour
**Dependencies**: Phase 2 complete
**Files to Modify**:
- `Makefile`

**Requirements**:
- Add `test-client-runtime` target
- Add `test-server-runtime` target
- Add `test-runtime` target
- Update `test` target to include runtime tests
- Add target documentation

**Acceptance Criteria**:
- [ ] `make test-client-runtime` runs successfully
- [ ] `make test-server-runtime` starts server and runs tests
- [ ] `make test-runtime` runs all runtime tests
- [ ] `make test` includes runtime tests

---

## Phase 6: Documentation & Validation (Week 3, Day 3-5)

### Task 6.1: Create Testing Guide Documentation
**Estimated Effort**: 4 hours
**Dependencies**: Phase 5 complete
**Files to Create**:
- `docs/E2E_TESTING_GUIDE.md`

**Requirements**:
- Explain automated vs MCP testing decision criteria
- Provide commands for running tests locally
- Document test data seeding and cleanup
- Explain how to add new automated tests
- Provide troubleshooting guide for common failures
- Document CI/CD integration and test reporting

**Acceptance Criteria**:
- [ ] Documentation is comprehensive and clear
- [ ] Examples provided for common tasks
- [ ] Troubleshooting guide covers major issues

---

### Task 6.2: Create Scenario Conversion Migration Guide
**Estimated Effort**: 2 hours
**Dependencies**: Phase 4 complete
**Files to Create**:
- `docs/SCENARIO_CONVERSION_GUIDE.md`

**Requirements**:
- Document which scenarios were converted and why
- Explain conversion criteria (Category A, B, C)
- Provide before/after comparisons
- List benefits of conversion
- Document MCP scenarios that remain

**Acceptance Criteria**:
- [ ] Clear explanation of conversion decisions
- [ ] Benefits quantified (time, cost, reliability)
- [ ] Easy reference for future conversions

---

### Task 6.3: Update Main README
**Estimated Effort**: 1 hour
**Dependencies**: Task 6.1
**Files to Modify**:
- `README.md`
- `client/README.md`

**Requirements**:
- Add section on E2E testing
- Document new test commands
- Reference testing guide
- Update testing badge (if applicable)

**Acceptance Criteria**:
- [ ] README includes E2E testing information
- [ ] Commands documented clearly
- [ ] Links to detailed guides provided

---

### Task 6.4: Validate Full Test Suite
**Estimated Effort**: 4 hours
**Dependencies**: All previous tasks
**Testing Activities**:
- Run full automated test suite locally
- Run full automated test suite in CI
- Run remaining MCP scenarios manually
- Verify test isolation (no cross-test contamination)
- Verify database cleanup works correctly
- Test failure scenarios (intentionally break features)
- Verify test reporting in GitHub Actions
- Performance validation (total runtime <5 minutes)

**Acceptance Criteria**:
- [ ] All automated tests pass consistently (3+ runs)
- [ ] CI integration works without manual intervention
- [ ] MCP scenarios still execute correctly
- [ ] Test data seeding/cleanup is reliable
- [ ] Performance targets met

---

## Task Summary

| Phase                          | Tasks        | Total Effort   | Dependencies |
| ------------------------------ | ------------ | -------------- | ------------ |
| Phase 1: Infrastructure        | 6 tasks      | 12.5 hours     | None         |
| Phase 2: Category A Conversion | 6 tasks      | 27 hours       | Phase 1      |
| Phase 3: Category B Conversion | 4 tasks      | 14 hours       | Phase 2      |
| Phase 4: MCP Refactoring       | 2 tasks      | 8 hours        | Phase 3      |
| Phase 5: CI/CD Integration     | 3 tasks      | 7 hours        | Phase 2      |
| Phase 6: Documentation         | 4 tasks      | 11 hours       | Phase 5      |
| **Total**                      | **25 tasks** | **79.5 hours** | Sequential   |

## Estimated Timeline

- **Week 1**: Phase 1 + Phase 2 (Infrastructure + Category A) = 39.5 hours
- **Week 2**: Phase 3 + Phase 4 (Category B + MCP Refactoring) = 22 hours
- **Week 3**: Phase 5 + Phase 6 (CI/CD + Documentation) = 18 hours

**Total Calendar Time**: ~3 weeks (assuming 40 hours/week development capacity)

## Risk Factors

1. **Database Seeding Complexity** - Test data seeding may require more effort than estimated if schema is complex
   - *Mitigation*: Reuse existing `dual_connection_test_data.py` patterns

2. **Rate Limiting Tests** - 60-second wait times may make tests slow
   - *Mitigation*: Configure lower rate limits for testing environment

3. **CI/CD Integration** - GitHub Actions may have environment differences
   - *Mitigation*: Test CI workflow early and iterate

4. **Test Flakiness** - Timing-dependent tests may be unreliable
   - *Mitigation*: Use proper waits, retries, and increased timeouts

## Success Metrics

- **Test Coverage**: 47% of scenarios automated (10 of 21)
- **Execution Time**: <5 minutes for automated tests vs 100+ minutes for all MCP scenarios
- **CI Integration**: 100% automated tests run in CI/CD
- **Reliability**: >95% test pass rate on repeated runs
- **Cost Reduction**: ~50% reduction in AI Agent execution time
