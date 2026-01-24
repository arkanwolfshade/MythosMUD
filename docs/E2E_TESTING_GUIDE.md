# E2E Testing Guide

## Overview

MythosMUD uses two approaches for E2E testing:

1. **Automated Playwright CLI Tests** - Single-player scenarios testing error handling, accessibility, and integration

   points

2. **Playwright MCP Scenarios** - Multi-player scenarios requiring real-time coordination and message broadcasting

This guide explains when to use each approach, how to run tests locally, and how to add new test scenarios.

## Quick Start

### Running Automated E2E Tests Locally

```bash
# Run all automated E2E runtime tests

make test-client-runtime

# Or directly with npm

cd client
npm run test:e2e:runtime

# Run in headed mode (see browser)

npm run test:e2e:runtime:headed

# Run in debug mode

npm run test:e2e:runtime:debug

# Run with UI mode (interactive)

npm run test:e2e:runtime:ui
```

### Running Multiplayer MCP Scenarios

For multiplayer scenarios that require AI Agent coordination:

```bash
# See e2e-tests/MULTIPLAYER_TEST_RULES.md for complete instructions
# These scenarios require Playwright MCP and AI Agent execution

```

## Test Categories

### Automated Playwright CLI Tests (10 Scenarios)

**Location**: `client/tests/e2e/runtime/`

#### Category A: Full Conversion (6 Scenarios)

1. **Local Channel Errors** - `error-handling/local-channel-errors.spec.ts`

   - Tests: 8 tests covering error conditions and edge cases
   - Runtime: ~1 minute

2. **Whisper Errors** - `error-handling/whisper-errors.spec.ts`

   - Tests: 10 tests covering validation and error handling
   - Runtime: ~1 minute

3. **Whisper Rate Limiting** - `error-handling/whisper-rate-limiting.spec.ts`

   - Tests: 9 tests including 60-second reset test
   - Runtime: ~2 minutes (includes slow test)

4. **Whisper Logging** - `admin/whisper-logging.spec.ts`

   - Tests: 9 tests covering admin access and privacy
   - Runtime: ~1 minute

5. **Logout Errors** - `error-handling/logout-errors.spec.ts`

   - Tests: 9 tests covering error conditions and recovery
   - Runtime: ~1 minute

6. **Logout Accessibility** - `accessibility/logout-accessibility.spec.ts`

   - Tests: 25 tests covering WCAG compliance
   - Runtime: ~2 minutes

#### Category B: Partial Conversion (4 Scenarios)

1. **Who Command** - `integration/who-command.spec.ts`

   - Automated: 10 tests for single-player functionality
   - MCP: Multi-player visibility (see `e2e-tests/scenarios/scenario-07-who-command.md`)
   - Runtime: ~1 minute

2. **Logout Button** - `integration/logout-button.spec.ts`

   - Automated: 13 tests for UI functionality and state
   - MCP: Logout broadcasting (see `e2e-tests/scenarios/scenario-19-logout-button.md`)
   - Runtime: ~1 minute

3. **Local Channel Integration** - `integration/local-channel-integration.spec.ts`

   - Automated: 11 tests for system integration points
   - MCP: Message broadcasting (see `e2e-tests/scenarios/scenario-12-local-channel-integration.md`)
   - Runtime: ~1 minute

4. **Whisper Integration** - `integration/whisper-integration.spec.ts`

    - Automated: 12 tests for system integration
    - MCP: Cross-player delivery (see `e2e-tests/scenarios/scenario-17-whisper-integration.md`)
    - Runtime: ~1 minute

5. **Map Viewer** - `integration/map-viewer.spec.ts`

    - Automated: 9 tests for map viewer functionality
    - Tests: Opening map, displaying rooms, room details, filtering, navigation
    - Runtime: ~2 minutes

6. **Map Admin Edit** - `integration/map-admin-edit.spec.ts`

    - Automated: 8 tests for admin edit mode
    - Tests: Node repositioning, edge creation/deletion, room editing, undo/redo
    - Runtime: ~2 minutes

7. **Map Performance** - `performance/map-performance.spec.ts`

    - Automated: 6 tests for performance benchmarks
    - Tests: Large room sets (500+), FPS monitoring, viewport optimization, memory usage
    - Runtime: ~3 minutes

**Total Automated Tests**: 137 tests in 13 files
**Total Runtime**: ~12 minutes (excluding 60-second rate limit test)

### Playwright MCP Scenarios (11 Scenarios)

**Location**: `e2e-tests/scenarios/`

These scenarios require multi-player coordination via Playwright MCP and AI Agent:

1. Scenario 1: Basic Connection/Disconnection
2. Scenario 2: Clean Game State
3. Scenario 3: Movement Between Rooms
4. Scenario 4: Muting System/Emotes
5. Scenario 5: Chat Messages
6. Scenario 6: Admin Teleportation
7. Scenario 8: Local Channel Basic
8. Scenario 9: Local Channel Isolation
9. Scenario 10: Local Channel Movement
10. Scenario 13: Whisper Basic
11. Scenario 16: Whisper Movement

**See**: `e2e-tests/MULTIPLAYER_TEST_RULES.md` for execution instructions

## When to Use Automated vs MCP Tests

### Use Automated Playwright CLI Tests When

✅ Testing **single-player functionality**
✅ Testing **error conditions** (invalid input, missing data)
✅ Testing **accessibility features** (ARIA, keyboard navigation)
✅ Testing **system integration points** (auth, rate limiting, logging)
✅ Testing **UI state changes** (button states, visibility)
✅ Tests can run **without real-time multi-player coordination**

### Use Playwright MCP Scenarios When

🎭 Testing **message broadcasting** to multiple players
🎭 Testing **real-time synchronization** between players
🎭 Testing **multi-player state isolation** (what each player sees)
🎭 Testing **cross-player interactions** (whispers, muting, teleportation)
🎭 Testing **room-based message routing** (local channel, movement)
🎭 Tests require **simultaneous multi-tab coordination**

## Test Database Management

### Test Database Location

Automated tests use a separate test database:

**Location**: `data/players/unit_test_players.db`

**Structure**: Matches production database schema

**Isolation**: Completely separate from development and production databases

### Baseline Test Players

The test database is seeded with three baseline players. **MULTI-CHARACTER**: Each player can have multiple characters
(up to 3 active characters per user).

1. **ArkanWolfshade** (Admin)

   - Username: `ArkanWolfshade`
   - Password: `Cthulhu1`
   - Admin: Yes
   - Characters: Each user can have up to 3 active characters
   - Starting Room: Main Foyer (per character)

2. **Ithaqua** (Regular Player)

   - Username: `Ithaqua`
   - Password: `Cthulhu1`
   - Admin: No
   - Characters: Each user can have up to 3 active characters
   - Starting Room: Main Foyer (per character)

3. **TestAdmin** (Superuser)

   - Username: `TestAdmin`
   - Password: `Cthulhu1`
   - Admin: Yes, Superuser: Yes
   - Characters: Each user can have up to 3 active characters
   - Starting Room: Main Foyer (per character)

**Note**: Character names are case-insensitive unique among active characters. Deleted character names can be reused.

### Database Lifecycle

1. **Global Setup** (before all tests):

   - Backs up existing `unit_test_players.db` if present
   - Creates fresh database with schema
   - Seeds baseline test players (each with their initial character)

2. **Between Tests**:

   - Player positions reset to starting rooms (per character)
   - Test-created data cleaned up
   - Baseline players and their characters preserved
   - Soft-deleted characters remain in database but are hidden

3. **Global Teardown** (after all tests):

   - Final cleanup performed
   - Test database remains for debugging
   - All characters (active and deleted) are preserved for analysis

### Manual Database Management

```bash
# Reset test database manually

cd client
npx ts-node tests/e2e/runtime/fixtures/database.ts

# Remove test database completely

rm data/players/unit_test_players.db
```

## Multi-Character Testing

**MULTI-CHARACTER SUPPORT**: The system now supports multiple characters per user (up to 3 active characters).

### Character Selection Flow

When logging in:

1. If user has characters → Character Selection Screen appears
2. If user has no characters → Character Creation Flow appears
3. User selects character → Game connects with selected character

**Single Character Login**: Users can only be logged in with one character at a time. If a user selects a different
character while already logged in with another character, the existing connection will be automatically disconnected
before the new character connects.

### Testing Multi-Character Scenarios

**Character Selection**: Test that users with multiple characters see the selection screen

**Character Creation**: Test creating up to 3 characters per user

**Character Limit**: Test that 4th character creation is rejected

**Character Deletion**: Test soft deletion and name reuse

**Case-Insensitive Names**: Test that "Ithaqua" and "ithaqua" are mutually exclusive

- **Character Switching**: Test selecting different characters in the same session

See `e2e-tests/scenarios/scenario-XX-character-selection.md` and related multi-character scenarios for detailed test
procedures.

## Adding New Automated Tests

### Step 1: Determine Test Category

Choose the appropriate directory based on what you're testing:

- `error-handling/` - Error conditions, validation, edge cases
- `accessibility/` - WCAG compliance, keyboard navigation, ARIA
- `admin/` - Admin-only functionality
- `integration/` - System integration points
- `performance/` - Performance benchmarks and large dataset testing

### Step 2: Create Test File

Create a new `.spec.ts` file in the appropriate directory:

```typescript
// client/tests/e2e/runtime/error-handling/my-feature-errors.spec.ts

import { test, expect } from '@playwright/test';
import { loginAsPlayer } from '../fixtures/auth';
import { sendCommand, waitForMessage, getMessages } from '../fixtures/player';
import { TEST_PLAYERS, ERROR_MESSAGES } from '../fixtures/test-data';

test.describe('My Feature Error Handling', () => {
  test.beforeEach(async ({ page }) => {
    await loginAsPlayer(
      page,
      TEST_PLAYERS.ARKAN_WOLFSHADE.username,
      TEST_PLAYERS.ARKAN_WOLFSHADE.password
    );
  });

  test('should reject invalid input', async ({ page }) => {
    // Send invalid command
    await sendCommand(page, 'mycommand invalid');

    // Verify error message
    await waitForMessage(page, 'Expected error message');

    // Additional assertions
    const messages = await getMessages(page);
    expect(messages).toContain('Expected error message');
  });
});
```

### Step 3: Use Test Fixtures

Available fixtures:

- `loginAsPlayer(page, username, password, characterName?)` - Complete login flow with optional character selection
  - **MULTI-CHARACTER**: If user has multiple characters, `characterName` parameter selects which character to use
  - If `characterName` is not provided and user has multiple characters, selects the first available character
  - If user has no characters, navigates to character creation flow
- `logout(page)` - Logout flow
- `sendCommand(page, command)` - Send game command
- `waitForMessage(page, text, timeout?)` - Wait for specific message
- `getMessages(page)` - Get all chat messages
- `hasMessage(page, text)` - Check if message exists
- `getPlayerLocation(page)` - Get current room
- `clearMessages(page)` - Clear chat history
- `selectCharacter(page, characterName)` - Select a character from character selection screen (MULTI-CHARACTER)
- `createCharacter(page, characterName, professionId, stats)` - Create a new character (MULTI-CHARACTER)
- `deleteCharacter(page, characterName)` - Soft delete a character (MULTI-CHARACTER)

### Step 4: Run Your Tests

```bash
cd client

# Run your specific test file

npx playwright test tests/e2e/runtime/error-handling/my-feature-errors.spec.ts

# Run in headed mode to see what's happening

npx playwright test tests/e2e/runtime/error-handling/my-feature-errors.spec.ts --headed

# Run in debug mode

npx playwright test tests/e2e/runtime/error-handling/my-feature-errors.spec.ts --debug
```

### Step 5: Verify Tests Pass

```bash
# Run all runtime tests to ensure no regressions

npm run test:e2e:runtime
```

## Troubleshooting

### Common Issues

#### Issue: "Test database not found"

**Solution**: The global setup should create the database automatically. If it doesn't:

```bash
cd client
npm run test:e2e:runtime
```

The global setup will run and create the database.

#### Issue: "Cannot find module" or dependency errors

**Solution**: Install dependencies:

```bash
cd client
npm install
```

#### Issue: "Login failed - username field not found"

**Solution**: Server might not be running. Start the development server:

```bash
./scripts/start_local.ps1
```

Then wait 10 seconds for it to initialize before running tests.

#### Issue: "Timeout waiting for message"

**Possible Causes**:

1. Server not running or not responding
2. Command syntax incorrect
3. Feature not implemented or broken

**Solution**:

1. Verify server is running: `curl http://localhost:54731/health`
2. Check server logs in `logs/development/`
3. Run test in headed mode to see what's happening: `npm run test:e2e:runtime:headed`

#### Issue: "Tests fail in CI but pass locally"

**Possible Causes**:

1. Server not starting properly in CI
2. Different timing/performance in CI environment
3. Port conflicts in CI

**Solution**:

1. Check GitHub Actions workflow logs
2. Increase timeouts for CI environment
3. Ensure server health check passes before tests run

### Debug Mode Usage

```bash
cd client

# Run specific test in debug mode

npx playwright test tests/e2e/runtime/error-handling/local-channel-errors.spec.ts --debug

# Run with Playwright Inspector

PWDEBUG=1 npm run test:e2e:runtime
```

### Viewing Test Reports

After tests run, view the HTML report:

```bash
cd client
npx playwright show-report playwright-report/runtime/
```

## CI/CD Integration

### GitHub Actions

Automated E2E tests run automatically on:

- Pull request creation and updates
- Push to main branch
- Manual workflow dispatch

**Workflow File**: `.github/workflows/e2e-runtime-tests.yml`

### Test Artifacts

On test failure, the following artifacts are uploaded:

- Screenshots of failures
- Videos of test execution
- Playwright traces for debugging
- HTML test report

**Access artifacts**: Go to the GitHub Actions run and download from the "Artifacts" section.

## Best Practices

### Writing Tests

1. **One assertion per test** - Makes failures easier to debug
2. **Use descriptive test names** - "should reject empty local messages" not "test1"
3. **Test isolation** - Tests should not depend on each other
4. **Clean state** - Use `beforeEach` to ensure clean state
5. **Meaningful waits** - Use `waitForMessage()` not `waitForTimeout()`
6. **Test error recovery** - Verify system works after errors

### Test Organization

1. **Group related tests** - Use `test.describe()` for logical grouping
2. **Share setup** - Use `beforeEach()` for common setup
3. **Keep tests focused** - Each test should test one specific behavior
4. **Document test purpose** - Add comments explaining what you're testing

### Performance

1. **Avoid unnecessary waits** - Don't use fixed `waitForTimeout()` unless necessary
2. **Run tests in parallel** - Playwright runs tests in parallel by default
3. **Mark slow tests** - Use `test.slow()` for tests that take >30 seconds
4. **Skip slow tests in development** - Use `--grep-invert @slow` to skip slow tests

## Test Data Management

### Using Test Constants

```typescript
import { TEST_PLAYERS, ERROR_MESSAGES, SUCCESS_MESSAGES } from '../fixtures/test-data';

// Login as test player
// MULTI-CHARACTER: Login with optional character selection
await loginAsPlayer(
  page,
  TEST_PLAYERS.ARKAN_WOLFSHADE.username,
  TEST_PLAYERS.ARKAN_WOLFSHADE.password,
  'CharacterName' // Optional: specify character name if user has multiple characters
);

// Verify error message
await waitForMessage(page, ERROR_MESSAGES.LOCAL_EMPTY_MESSAGE);

// Verify success message
const expectedMessage = SUCCESS_MESSAGES.LOCAL_MESSAGE_SENT('Hello');
await waitForMessage(page, expectedMessage);
```

### Adding New Test Constants

Edit `client/tests/e2e/runtime/fixtures/test-data.ts`:

```typescript
export const ERROR_MESSAGES = {
  // ... existing messages
  MY_NEW_ERROR: 'My new error message',
} as const;
```

## FAQ

### Q: Should I write an automated test or an MCP scenario?

**A**: Ask yourself: "Does this test require real-time verification of message broadcasting to multiple players?"

**Yes** → Use MCP scenario

**No** → Use automated test

### Q: Why are some tests marked as `test.slow()`?

**A**: Tests that take longer than 30 seconds (like the 60-second rate limit reset test) are marked as slow. You can
exclude them during development:

```bash
npx playwright test --grep-invert @slow
```

### Q: Can I run automated tests without the server running?

**A**: No, the automated tests require the development server to be running. The test configuration can auto-start the
server for you in local development, but in CI it's started separately.

### Q: How do I debug a failing test?

**A**:

1. Run in headed mode: `npm run test:e2e:runtime:headed`
2. Run in debug mode: `npm run test:e2e:runtime:debug`
3. Check the HTML report: `npx playwright show-report playwright-report/runtime/`
4. Check server logs in `logs/development/`

### Q: What if the test database gets corrupted?

**A**: Remove it and let global setup recreate it:

```bash
rm data/players/unit_test_players.db
npm run test:e2e:runtime
```

### Q: How do I test features that require multiple players?

**A**: Either:

1. Write an MCP scenario in `e2e-tests/scenarios/`
2. Mock the second player in automated tests if you're only testing integration points

## Enhanced Logging in E2E Tests

### **CRITICAL: Enhanced Logging Requirements**

All E2E tests MUST use the enhanced logging system for proper observability and debugging.

#### **Required Import Pattern**

```typescript
// ✅ CORRECT - Enhanced logging import (MANDATORY)
import { getLogger } from 'server/logging/enhanced_logging_config';
const logger = getLogger(__name__);
```

#### **Forbidden Patterns**

```typescript
// ❌ FORBIDDEN - Will cause import failures and system crashes
import { logging } from 'logging';
const logger = logging.getLogger(__name__);

// ❌ FORBIDDEN - Deprecated context parameter (causes TypeError)
logger.info("Test started", context={"test_name": "example"});

// ❌ FORBIDDEN - String formatting breaks structured logging
logger.info(`Test ${testName} started`);
```

#### **Correct Logging Patterns in Tests**

```typescript
// ✅ CORRECT - Test setup logging
logger.info("E2E test started", test_name="local-channel-errors", test_file="error-handling/local-channel-errors.spec.ts");

// ✅ CORRECT - Test step logging
logger.debug("Test step executed", step="navigate_to_chat", url="/chat", expected_element="chat-panel");

// ✅ CORRECT - Error logging in tests
logger.error("Test assertion failed", assertion="chat_message_visible", expected=true, actual=false, test_step="verify_message_display");

// ✅ CORRECT - Performance logging
logger.info("Test performance metrics", test_duration_ms=1500, steps_completed=8, assertions_passed=10);
```

#### **Test Logging Best Practices**

**Structured Logging**: Always use key-value pairs for log data

**Test Context**: Include test name, file, and step information

**Error Context**: Log sufficient context for debugging test failures

**Performance Tracking**: Log test execution times and metrics

**Security**: Never log sensitive test data (passwords, tokens)

#### **Logging Validation in Tests**

```typescript
// ✅ CORRECT - Validate logging behavior in tests
test('should log user actions correctly', async () => {
  // Mock the logger to capture log calls
  const mockLogger = jest.fn();
  jest.spyOn(enhancedLogging, 'getLogger').mockReturnValue({
    info: mockLogger,
    error: mockLogger,
    debug: mockLogger
  });

  // Perform test action
  await page.click('[data-testid="send-message"]');

  // Verify logging occurred
  expect(mockLogger).toHaveBeenCalledWith(
    "User action completed",
    expect.objectContaining({
      action: "send_message",
      user_id: expect.any(String),
      success: true
    })
  );
});
```

#### **Documentation References**

**Complete Guide**: [LOGGING_BEST_PRACTICES.md](LOGGING_BEST_PRACTICES.md)

**Quick Reference**: [LOGGING_QUICK_REFERENCE.md](LOGGING_QUICK_REFERENCE.md)

**Testing Examples**: [docs/examples/logging/testing_examples.py](examples/logging/testing_examples.py)

## Additional Resources

[Playwright Documentation](https://playwright.dev/docs/intro)

- [MCP Scenario Documentation](../e2e-tests/MULTIPLAYER_TEST_RULES.md)
- [Scenario Conversion Guide](./SCENARIO_CONVERSION_GUIDE.md)
- [Test Data Constants](../client/tests/e2e/runtime/fixtures/test-data.ts)
