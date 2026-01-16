---
name: Convert All E2E Scenarios to Playwright CLI
overview: Convert all 33 e2e test scenarios from MCP format to runnable Playwright CLI tests, using Playwright's multi-context feature for multiplayer scenarios. This will create a comprehensive automated test suite that can run without AI agent coordination.
todos:
  - id: verify-infrastructure
    content: Verify existing test infrastructure files exist (playwright.runtime.config.ts, fixtures, global-setup/teardown)
    status: pending
  - id: create-missing-infrastructure
    content: Create any missing infrastructure files (playwright.runtime.config.ts, global-setup.ts, global-teardown.ts, fixtures)
    status: pending
  - id: create-multiplayer-fixture
    content: Create multiplayer.ts fixture with multi-context helper functions (createMultiPlayerContext, waitForCrossPlayerMessage, cleanupMultiPlayerContexts)
    status: pending
  - id: update-playwright-config
    content: Update playwright.runtime.config.ts to support multi-context testing with proper timeout configuration
    status: pending
  - id: verify-test-database
    content: Verify test database setup works correctly with proper seeding and isolation
    status: pending
  - id: verify-existing-error-tests
    content: Verify existing error-handling tests exist and are working (scenarios 11, 14, 15, 20)
    status: pending
  - id: verify-existing-accessibility-tests
    content: Verify existing accessibility tests exist and are working (scenario 21)
    status: pending
  - id: verify-existing-integration-tests
    content: Verify existing integration tests exist (scenarios 07, 12, 17, 18, 19) and determine if migration needed
    status: pending
  - id: convert-scenario-01
    content: Convert scenario-01-basic-connection.md to connection/basic-connection.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-02
    content: Convert scenario-02-clean-game-state.md to connection/clean-game-state.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-03
    content: Convert scenario-03-movement-between-rooms.md to movement/movement-between-rooms.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-04
    content: Convert scenario-04-muting-system-emotes.md to muting/muting-system-emotes.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-05
    content: Convert scenario-05-chat-messages.md to communication/chat-messages.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-06
    content: Convert scenario-06-admin-teleportation.md to admin/admin-teleportation.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-07
    content: Convert scenario-07-who-command.md to commands/who-command.spec.ts (verify/migrate if exists)
    status: pending
  - id: convert-scenario-08
    content: Convert scenario-08-local-channel-basic.md to communication/local-channel-basic.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-09
    content: Convert scenario-09-local-channel-isolation.md to communication/local-channel-isolation.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-10
    content: Convert scenario-10-local-channel-movement.md to movement/local-channel-movement.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-12
    content: Convert scenario-12-local-channel-integration.md to communication/local-channel-integration.spec.ts (verify/migrate if exists)
    status: pending
  - id: convert-scenario-13
    content: Convert scenario-13-whisper-basic.md to communication/whisper-basic.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-16
    content: Convert scenario-16-whisper-movement.md to communication/whisper-movement.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-17
    content: Convert scenario-17-whisper-integration.md to communication/whisper-integration.spec.ts (verify/migrate if exists)
    status: pending
  - id: convert-scenario-18
    content: Convert scenario-18-whisper-logging.md to admin/whisper-logging.spec.ts (verify/migrate if exists)
    status: pending
  - id: convert-scenario-22
    content: Convert scenario-22-summon-command.md to admin/summon-command.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-23
    content: Convert scenario-23-container-multi-user-looting.md to containers/container-multi-user-looting.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-24
    content: Convert scenario-24-container-environmental-interactions.md to containers/container-environmental-interactions.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-25
    content: Convert scenario-25-container-wearable-management.md to containers/container-wearable-management.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-26
    content: Convert scenario-26-container-corpse-looting.md to containers/container-corpse-looting.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-27
    content: Convert scenario-27-character-selection.md to character/character-selection.spec.ts (single-player)
    status: pending
  - id: convert-scenario-28
    content: Convert scenario-28-multi-character-creation.md to character/multi-character-creation.spec.ts (single-player)
    status: pending
  - id: convert-scenario-29
    content: Convert scenario-29-character-deletion.md to character/character-deletion.spec.ts (single-player)
    status: pending
  - id: convert-scenario-30
    content: Convert scenario-30-character-name-uniqueness.md to character/character-name-uniqueness.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-31
    content: Convert scenario-31-admin-set-stat-command.md to admin/admin-set-stat-command.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-32
    content: Convert scenario-32-disconnect-grace-period.md to commands/disconnect-grace-period.spec.ts (multi-context)
    status: pending
  - id: convert-scenario-33
    content: Convert scenario-33-rest-command.md to commands/rest-command.spec.ts (multi-context)
    status: pending
  - id: convert-lucidity-01
    content: Convert lucidity-system-expansion/scenario-01-catatonia-grounding.md to lucidity/catatonia-grounding.spec.ts (multi-context)
    status: pending
  - id: convert-lucidity-02
    content: Convert lucidity-system-expansion/scenario-02-sanitarium-failover.md to lucidity/sanitarium-failover.spec.ts (multi-context)
    status: pending
  - id: run-full-test-suite
    content: Run full test suite to identify failures and timing issues
    status: pending
  - id: fix-test-failures
    content: Fix any test execution failures, timing issues, and race conditions
    status: pending
  - id: update-makefile
    content: Update Makefile with test-client-runtime target if needed
    status: pending
  - id: update-package-json
    content: Update package.json scripts for test:e2e:runtime if needed
    status: pending
  - id: document-limitations
    content: Document any scenarios that couldn't be fully automated or require manual verification steps
    status: pending
  - id: verify-test-organization
    content: Verify all test files are properly organized in logical directories
    status: pending
  - id: final-test-execution
    content: Execute final test run to ensure all 33 scenarios are converted and passing
    status: pending
---

# Convert All E2E Scenarios to Playwright CLI Tests

## Overview

Convert all 33 scenarios in `e2e-tests/scenarios/` to automated Playwright CLI tests in `client/tests/e2e/runtime/`. Use Playwright's multi-context feature to handle multiplayer scenarios that require multiple players.

## Current State

- **Total Scenarios**: 33 scenarios in `e2e-tests/scenarios/`
- **Multiplayer Scenarios**: 29 marked as `[REQUIRES MULTI-PLAYER]`
- **Single-Player Scenarios**: 4 scenarios (scenarios 11, 14, 18, 20, 21)
- **Existing Infrastructure**: Documentation references exist but test files may need to be created/verified

## Infrastructure Setup

### 1. Verify/Create Test Infrastructure

**Files to verify/create**:

- `client/tests/e2e/playwright.runtime.config.ts` - Playwright configuration
- `client/tests/e2e/runtime/global-setup.ts` - Database seeding
- `client/tests/e2e/runtime/global-teardown.ts` - Database cleanup
- `client/tests/e2e/runtime/fixtures/auth.ts` - Authentication helpers
- `client/tests/e2e/runtime/fixtures/player.ts` - Player utilities
- `client/tests/e2e/runtime/fixtures/database.ts` - Database utilities
- `client/tests/e2e/runtime/fixtures/test-data.ts` - Test constants

**Key Features**:

- Multi-context support for multiplayer scenarios
- Shared authentication state management
- Test database isolation
- Proper timeout configuration (30s default)

### 2. Create Multi-Context Helper

**New File**: `client/tests/e2e/runtime/fixtures/multiplayer.ts`

Helper functions for managing multiple browser contexts:

- `createMultiPlayerContext(browser, players[])` - Creates multiple authenticated contexts
- `switchContext(context, page)` - Helper for context switching
- `waitForCrossPlayerMessage(contexts, expectedText)` - Wait for messages across contexts
- `cleanupMultiPlayerContexts(contexts)` - Cleanup helper

## Test Organization

### Directory Structure

```
client/tests/e2e/runtime/
├── fixtures/
│   ├── auth.ts              # Authentication (existing/verify)
│   ├── player.ts            # Player utilities (existing/verify)
│   ├── database.ts          # Database utilities (existing/verify)
│   ├── test-data.ts         # Test constants (existing/verify)
│   └── multiplayer.ts       # NEW: Multi-context helpers
├── connection/              # NEW: Connection scenarios
│   ├── basic-connection.spec.ts
│   └── clean-game-state.spec.ts
├── movement/                 # NEW: Movement scenarios
│   ├── movement-between-rooms.spec.ts
│   └── local-channel-movement.spec.ts
├── communication/            # NEW: Communication scenarios
│   ├── chat-messages.spec.ts
│   ├── local-channel-basic.spec.ts
│   ├── local-channel-isolation.spec.ts
│   ├── local-channel-integration.spec.ts
│   ├── whisper-basic.spec.ts
│   ├── whisper-movement.spec.ts
│   └── whisper-integration.spec.ts
├── admin/                   # Existing + new
│   ├── whisper-logging.spec.ts (existing)
│   ├── admin-teleportation.spec.ts
│   ├── summon-command.spec.ts
│   └── admin-set-stat-command.spec.ts
├── character/               # NEW: Character management
│   ├── character-selection.spec.ts
│   ├── multi-character-creation.spec.ts
│   ├── character-deletion.spec.ts
│   └── character-name-uniqueness.spec.ts
├── containers/              # NEW: Container scenarios
│   ├── container-multi-user-looting.spec.ts
│   ├── container-environmental-interactions.spec.ts
│   ├── container-wearable-management.spec.ts
│   └── container-corpse-looting.spec.ts
├── commands/                # NEW: Command scenarios
│   ├── who-command.spec.ts (may exist in integration/)
│   ├── rest-command.spec.ts
│   └── disconnect-grace-period.spec.ts
├── muting/                  # NEW: Muting scenarios
│   └── muting-system-emotes.spec.ts
├── error-handling/          # Existing + new
│   ├── local-channel-errors.spec.ts (existing)
│   ├── whisper-errors.spec.ts (existing)
│   ├── whisper-rate-limiting.spec.ts (existing)
│   ├── logout-errors.spec.ts (existing)
│   └── whisper-errors-extended.spec.ts (if needed)
├── accessibility/           # Existing
│   └── logout-accessibility.spec.ts (existing)
├── integration/             # Existing + new
│   ├── who-command.spec.ts (existing)
│   ├── logout-button.spec.ts (existing)
│   ├── local-channel-integration.spec.ts (existing)
│   └── whisper-integration.spec.ts (existing)
└── lucidity/                # NEW: Lucidity system
    ├── catatonia-grounding.spec.ts
    └── sanitarium-failover.spec.ts
```

## Conversion Strategy

### Pattern for Single-Player Scenarios

1. Read scenario markdown file
2. Extract test steps and expected results
3. Convert MCP commands to Playwright API calls
4. Use existing fixtures for authentication
5. Create focused test cases

### Pattern for Multi-Player Scenarios

1. Create multiple browser contexts (one per player)
2. Authenticate each context separately
3. Use context switching to simulate multi-tab behavior
4. Wait for cross-context message delivery
5. Verify state synchronization

### Example Conversion Pattern

**MCP Command**:

```javascript
await mcp_playwright_browser_tab_select({index: 0});
await mcp_playwright_browser_type({element: "Command input", ref: "command-input", text: "say Hello"});
```

**Playwright Equivalent**:

```typescript
const page1 = contexts[0].pages()[0]; // AW's context
await page1.locator('[data-testid="command-input"]').fill('say Hello');
await page1.locator('[data-testid="command-input"]').press('Enter');
```

## Scenario Mapping

### Connection Scenarios (2)

- **scenario-01-basic-connection.md** → `connection/basic-connection.spec.ts`
- **scenario-02-clean-game-state.md** → `connection/clean-game-state.spec.ts`

### Movement Scenarios (2)

- **scenario-03-movement-between-rooms.md** → `movement/movement-between-rooms.spec.ts`
- **scenario-10-local-channel-movement.md** → `movement/local-channel-movement.spec.ts`

### Communication Scenarios (7)

- **scenario-05-chat-messages.md** → `communication/chat-messages.spec.ts`
- **scenario-08-local-channel-basic.md** → `communication/local-channel-basic.spec.ts`
- **scenario-09-local-channel-isolation.md** → `communication/local-channel-isolation.spec.ts`
- **scenario-12-local-channel-integration.md** → `communication/local-channel-integration.spec.ts` (may exist)
- **scenario-13-whisper-basic.md** → `communication/whisper-basic.spec.ts`
- **scenario-16-whisper-movement.md** → `communication/whisper-movement.spec.ts`
- **scenario-17-whisper-integration.md** → `communication/whisper-integration.spec.ts` (may exist)

### Admin Scenarios (4)

- **scenario-06-admin-teleportation.md** → `admin/admin-teleportation.spec.ts`
- **scenario-22-summon-command.md** → `admin/summon-command.spec.ts`
- **scenario-31-admin-set-stat-command.md** → `admin/admin-set-stat-command.spec.ts`
- **scenario-18-whisper-logging.md** → `admin/whisper-logging.spec.ts` (may exist)

### Character Scenarios (4)

- **scenario-27-character-selection.md** → `character/character-selection.spec.ts`
- **scenario-28-multi-character-creation.md** → `character/multi-character-creation.spec.ts`
- **scenario-29-character-deletion.md** → `character/character-deletion.spec.ts`
- **scenario-30-character-name-uniqueness.md** → `character/character-name-uniqueness.spec.ts`

### Container Scenarios (4)

- **scenario-23-container-multi-user-looting.md** → `containers/container-multi-user-looting.spec.ts`
- **scenario-24-container-environmental-interactions.md** → `containers/container-environmental-interactions.spec.ts`
- **scenario-25-container-wearable-management.md** → `containers/container-wearable-management.spec.ts`
- **scenario-26-container-corpse-looting.md** → `containers/container-corpse-looting.spec.ts`

### Command Scenarios (3)

- **scenario-07-who-command.md** → `commands/who-command.spec.ts` (may exist in integration/)
- **scenario-32-disconnect-grace-period.md** → `commands/disconnect-grace-period.spec.ts`
- **scenario-33-rest-command.md** → `commands/rest-command.spec.ts`

### Muting Scenarios (1)

- **scenario-04-muting-system-emotes.md** → `muting/muting-system-emotes.spec.ts`

### Lucidity Scenarios (2)

- **scenario-01-catatonia-grounding.md** → `lucidity/catatonia-grounding.spec.ts`
- **scenario-02-sanitarium-failover.md** → `lucidity/sanitarium-failover.spec.ts`

### Error Handling (Already Converted - 4)

- **scenario-11-local-channel-errors.md** → `error-handling/local-channel-errors.spec.ts` (exists)
- **scenario-14-whisper-errors.md** → `error-handling/whisper-errors.spec.ts` (exists)
- **scenario-15-whisper-rate-limiting.md** → `error-handling/whisper-rate-limiting.spec.ts` (exists)
- **scenario-20-logout-errors.md** → `error-handling/logout-errors.spec.ts` (exists)

### Accessibility (Already Converted - 1)

- **scenario-21-logout-accessibility.md** → `accessibility/logout-accessibility.spec.ts` (exists)

## Implementation Steps

### Phase 1: Infrastructure Verification (1-2 hours)

1. Verify existing test infrastructure files exist
2. Create missing infrastructure files if needed
3. Create `multiplayer.ts` fixture with multi-context helpers
4. Update `playwright.runtime.config.ts` to support multi-context testing
5. Verify test database setup works correctly

### Phase 2: Single-Player Scenarios (2-3 hours)

1. Convert scenario-11 (local-channel-errors) - verify exists
2. Convert scenario-14 (whisper-errors) - verify exists
3. Convert scenario-15 (whisper-rate-limiting) - verify exists
4. Convert scenario-20 (logout-errors) - verify exists
5. Convert scenario-21 (logout-accessibility) - verify exists

### Phase 3: Connection & Movement (3-4 hours)

1. Convert scenario-01 (basic-connection) - multi-context
2. Convert scenario-02 (clean-game-state) - multi-context
3. Convert scenario-03 (movement-between-rooms) - multi-context
4. Convert scenario-10 (local-channel-movement) - multi-context

### Phase 4: Communication Scenarios (4-5 hours)

1. Convert scenario-05 (chat-messages) - multi-context
2. Convert scenario-08 (local-channel-basic) - multi-context
3. Convert scenario-09 (local-channel-isolation) - multi-context
4. Convert scenario-12 (local-channel-integration) - verify/migrate
5. Convert scenario-13 (whisper-basic) - multi-context
6. Convert scenario-16 (whisper-movement) - multi-context
7. Convert scenario-17 (whisper-integration) - verify/migrate

### Phase 5: Admin Scenarios (3-4 hours)

1. Convert scenario-06 (admin-teleportation) - multi-context
2. Convert scenario-18 (whisper-logging) - verify/migrate
3. Convert scenario-22 (summon-command) - multi-context
4. Convert scenario-31 (admin-set-stat-command) - multi-context

### Phase 6: Character Management (3-4 hours)

1. Convert scenario-27 (character-selection) - single-player
2. Convert scenario-28 (multi-character-creation) - single-player
3. Convert scenario-29 (character-deletion) - single-player
4. Convert scenario-30 (character-name-uniqueness) - multi-context

### Phase 7: Container Scenarios (4-5 hours)

1. Convert scenario-23 (container-multi-user-looting) - multi-context
2. Convert scenario-24 (container-environmental-interactions) - multi-context
3. Convert scenario-25 (container-wearable-management) - multi-context
4. Convert scenario-26 (container-corpse-looting) - multi-context

### Phase 8: Commands & Muting (2-3 hours)

1. Convert scenario-07 (who-command) - verify/migrate
2. Convert scenario-32 (disconnect-grace-period) - multi-context
3. Convert scenario-33 (rest-command) - multi-context
4. Convert scenario-04 (muting-system-emotes) - multi-context

### Phase 9: Lucidity System (2-3 hours)

1. Convert scenario-01-catatonia-grounding (lucidity) - multi-context
2. Convert scenario-02-sanitarium-failover (lucidity) - multi-context

### Phase 10: Integration & Testing (2-3 hours)

1. Run all tests to identify failures
2. Fix any issues with test execution
3. Update Makefile with `test-client-runtime` target if needed
4. Update package.json scripts if needed
5. Document any scenarios that couldn't be fully automated

## Key Technical Decisions

### Multi-Context Pattern

Use Playwright's `browser.newContext()` to create separate browser contexts for each player:

```typescript
test('multiplayer scenario', async ({ browser }) => {
  // Create contexts for each player
  const awContext = await browser.newContext();
  const ithaquaContext = await browser.newContext();

  // Authenticate each context
  const awPage = await loginAsPlayer(awContext, 'ArkanWolfshade', 'Cthulhu1');
  const ithaquaPage = await loginAsPlayer(ithaquaContext, 'Ithaqua', 'Cthulhu1');

  // Perform actions across contexts
  await awPage.locator('[data-testid="command-input"]').fill('say Hello');
  await awPage.locator('[data-testid="command-input"]').press('Enter');

  // Wait for message in other context
  await expect(ithaquaPage.locator('[data-message-text*="Hello"]')).toBeVisible();

  // Cleanup
  await awContext.close();
  await ithaquaContext.close();
});
```

### Message Verification

For cross-context message verification, use Playwright's `expect` with appropriate selectors:

- Game log messages: `[data-message-text]` attribute
- Chat messages: `.message` class or specific test IDs
- Room updates: Room description or occupants panel

### Test Data Management

- Use existing `TEST_PLAYERS` constants from `test-data.ts`
- Ensure test database is properly seeded before tests
- Reset player positions between tests if needed

## Success Criteria

- All 33 scenarios converted to Playwright CLI tests
- Tests can run without AI agent coordination
- Multiplayer scenarios use multi-context feature
- All tests pass consistently
- Test execution time < 30 minutes for full suite
- Tests are properly organized in logical directories
- Makefile target `test-client-runtime` works correctly

## Estimated Timeline

- **Total Estimated Time**: 25-35 hours
- **Infrastructure Setup**: 1-2 hours
- **Test Conversion**: 20-28 hours
- **Integration & Testing**: 2-3 hours
- **Documentation**: 1-2 hours

## Dependencies

- Existing Playwright infrastructure (verify/create)
- Test database setup working
- Server running on port 54731
- Client accessible on port 5173
- Proper test IDs on UI elements

## Notes

- Some scenarios may already be converted (verify first)
- Multi-context tests may be slower than single-context tests
- Some scenarios may need simplification for automation
- Document any limitations or manual verification steps needed
