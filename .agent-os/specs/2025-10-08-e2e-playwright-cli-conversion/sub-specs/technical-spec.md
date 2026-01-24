# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-08-e2e-playwright-cli-conversion/spec.md

## Technical Requirements

### Test Infrastructure

**Test Directory Structure**:

  ```
  client/tests/e2e/runtime/
  ├── fixtures/              # Test fixtures and setup
  │   ├── auth.ts           # Authentication helpers (loginAsPlayer, logout)
  │   ├── player.ts         # Player creation/management utilities
  │   ├── database.ts       # Database seeding and cleanup utilities
  │   └── test-data.ts      # Test data constants and generators
  ├── error-handling/        # Error scenario tests
  │   ├── local-channel-errors.spec.ts
  │   ├── whisper-errors.spec.ts
  │   ├── whisper-rate-limiting.spec.ts
  │   └── logout-errors.spec.ts
  ├── accessibility/         # Accessibility tests
  │   └── logout-accessibility.spec.ts
  ├── admin/                 # Admin functionality tests
  │   └── whisper-logging.spec.ts
  └── integration/           # Integration tests (partial)
      ├── who-command.spec.ts
      ├── logout-button.spec.ts
      ├── local-channel-integration.spec.ts
      └── whisper-integration.spec.ts
  ```

**Playwright Runtime Configuration**:

- Create `client/tests/e2e/playwright.runtime.config.ts`
- Configure 30-second default timeout for test operations
- Set base URL to `http://localhost:5173`
- Enable trace collection on first retry for debugging
- Configure Chromium as primary test browser
- Set up web server auto-start for local development
- Disable web server auto-start in CI (handled by GitHub Actions)

**Test Fixtures**:
  **Authentication Fixture**: `loginAsPlayer(page, username, password)` - handles login flow, MOTD screen, and game entry

**Database Seeding Fixture**: `seedTestDatabase()` - populates `data/players/unit_test_players.db` with known test players

**Database Cleanup Fixture**: `cleanupTestDatabase()` - resets database to known state after tests
- **Player Creation Fixture**: `createTestPlayer(username, stats)` - creates test player with specific attributes
- **Room Setup Fixture**: `setupTestRooms()` - ensures test rooms exist in `data/rooms/` structure

### Category A: Full Conversion Scenarios

#### Scenario 11: Local Channel Errors (`client/tests/e2e/runtime/error-handling/local-channel-errors.spec.ts`)

**Test Cases**:

- Empty local message rejection with error message verification
- Invalid command syntax error handling
- Long message (>500 chars) rejection
- Special characters support (!@#$%^&*())
- Unicode characters support (你好世界 🌍)
- Whitespace-only message rejection
- Valid message functionality after error conditions
- System stability verification after errors

**Technical Implementation**:

- Use `page.fill()` and `page.press()` for command input
- Use `expect(page.locator('.message')).toContainText()` for message verification
- Use `page.locator('.error-message')` for error detection
- Implement error recovery verification between test cases

#### Scenario 14: Whisper Errors (`client/tests/e2e/runtime/error-handling/whisper-errors.spec.ts`)

**Test Cases**:

- Non-existent player error ("Player 'X' not found")
- Empty whisper message rejection
- Invalid command syntax (missing player or message)
- Long whisper message rejection
- Self-whisper rejection ("You cannot whisper to yourself")
- Special characters and Unicode support
- Whitespace-only message rejection
- Valid whisper after error conditions

**Technical Implementation**:

- Mock second player presence for error condition testing
- Verify error message format and content
- Test both single-player and multi-player error scenarios
- Ensure error messages are user-friendly and actionable

#### Scenario 15: Whisper Rate Limiting (`client/tests/e2e/runtime/error-handling/whisper-rate-limiting.spec.ts`)

**Test Cases**:

- Normal whisper rate (1-3 messages/minute) success
- Per-recipient rate limit (3 whispers/minute to same player)
- Global rate limit (5 whispers/minute total)
- Rate limit reset after 60 seconds
- Error message clarity and information
- System stability under rate limiting

**Technical Implementation**:

- Use `page.waitForTimeout()` for time-based testing
- Implement counter verification for rate limit enforcement
- Test rate limit reset behavior with 60-second wait
- Verify both per-recipient and global rate limiting independently

#### Scenario 18: Whisper Logging (`client/tests/e2e/runtime/admin/whisper-logging.spec.ts`)

**Test Cases**:

- Admin log access with `admin whisper logs` command
- Non-admin log access denial
- Log content verification (sender, recipient, message)
- Multiple whisper logging
- Privacy verification (logs not visible to non-admins)

**Technical Implementation**:

- Use admin test account with `is_admin=1` database flag
- Mock whisper messages for log verification
- Verify log format and content structure
- Test permission-based access control

#### Scenario 20: Logout Errors (`client/tests/e2e/runtime/error-handling/logout-errors.spec.ts`)

**Test Cases**:

- Network error during logout (simulated offline)
- Server error during logout (simulated fetch failure)
- Session expiry during logout
- Multiple logout attempt handling
- Concurrent logout attempt handling
- System stability after error conditions

**Technical Implementation**:

- Use `page.evaluate()` to simulate network offline: `window.navigator.onLine = false`
- Mock fetch failures for server error testing
- Simulate session expiry by clearing localStorage/sessionStorage
- Test error recovery and fallback mechanisms

#### Scenario 21: Logout Accessibility (`client/tests/e2e/runtime/accessibility/logout-accessibility.spec.ts`)

**Test Cases**:

- ARIA attributes verification (aria-label, role, tabindex)
- Keyboard navigation (Tab to focus, Enter to activate)
- Screen reader compatibility (text content + ARIA labels)
- Focus management (focusable, visible, enabled states)
- Color contrast verification (background vs text)
- Touch target size (minimum 44px)
- Button state changes (disabled, aria-disabled, loading)
- Error and success state accessibility

**Technical Implementation**:

- Use `page.locator().getAttribute()` for ARIA verification
- Use `page.keyboard.press('Tab')` for keyboard navigation testing
- Use `page.evaluate()` for computed style verification
- Use `page.locator().boundingBox()` for size verification
- Test with keyboard-only navigation (no mouse)

### Category B: Partial Conversion Scenarios

#### Scenario 7: Who Command (Partial)

**Automated Portion** (`client/tests/e2e/runtime/integration/who-command.spec.ts`):

- Command output format verification
- Location information display
- Single player visibility
- Response time testing

**MCP Portion** (remains in `e2e-tests/scenarios/scenario-07-who-command.md`):

- Multiple online players visibility
- Real-time player list updates
- Player location synchronization

#### Scenario 19: Logout Button (Partial)

**Automated Portion** (`client/tests/e2e/runtime/integration/logout-button.spec.ts`):

- Button visibility and accessibility
- Click functionality and UI state changes
- Logout confirmation message
- Redirect to login page
- Re-login functionality

**MCP Portion** (remains in `e2e-tests/scenarios/scenario-19-logout-button.md`):

- Logout message broadcasting to other players
- Multi-player session termination verification

#### Scenario 12: Local Channel Integration (Partial)

**Automated Portion** (`client/tests/e2e/runtime/integration/local-channel-integration.spec.ts`):

- Integration with player management (player lookup, validation)
- Integration with location tracking (current room verification)
- Integration with error handling (error message delivery)
- Integration with logging (message logging verification)

**MCP Portion** (remains in `e2e-tests/scenarios/scenario-12-local-channel-integration.md`):

- Message broadcasting to multiple players
- Real-time message delivery verification

#### Scenario 17: Whisper Integration (Partial)

**Automated Portion** (`client/tests/e2e/runtime/integration/whisper-integration.spec.ts`):

- Integration with player management
- Integration with authentication (token validation)
- Integration with rate limiting
- Integration with error handling
- Integration with logging

**MCP Portion** (remains in `e2e-tests/scenarios/scenario-17-whisper-integration.md`):

- Cross-player message delivery
- Real-time whisper notification

### Test Data Management

**Test Database Location**: `data/players/unit_test_players.db` (separate from development database)

**Test NPC Database**: `data/npcs/test_npcs.db` (for NPC interaction tests)

**Test Rooms**: Use existing `data/rooms/` structure with test-specific room configurations
- **Seeding Strategy**:
  - Create known test players with predictable credentials
  - Use existing `DualConnectionTestData` pattern from `server/tests/data/dual_connection_test_data.py`
  - Implement TypeScript equivalent for client-side test data generation
- **Cleanup Strategy**:
  - Run `beforeEach()` hook to seed fresh test data
  - Run `afterEach()` hook to cleanup test-specific data
  - Preserve baseline test data structure between test runs

### Database Cleanup Mechanisms

**Before Test Suite**:

- Backup existing `unit_test_players.db` if present
- Create fresh test database with schema
- Seed with baseline test players (ArkanWolfshade, Ithaqua, TestAdmin)

**Between Tests**:

- Reset player positions to default rooms
- Clear session data and authentication tokens
- Reset player stats to baseline values
- Clear temporary test messages/whispers

**After Test Suite**:

- Optional: Restore original test database backup
- Optional: Preserve test database for debugging
- Clean up temporary files and logs

### GitHub Actions Integration

**Workflow File**: `.github/workflows/e2e-tests.yml` (update existing or create new)

**Trigger Events**:

  - Pull request creation and updates
  - Push to main branch
  - Manual workflow dispatch

**Job Structure**:

  ```yaml
  jobs:
    e2e-automated:
      runs-on: ubuntu-latest
      steps:
        - Checkout code
        - Setup Node.js (v18)
        - Setup Python (v3.11)
        - Install dependencies (npm, uv)
        - Start development server in background
        - Wait for server health check
        - Run Playwright CLI tests
        - Upload test artifacts (screenshots, videos, traces)
        - Report test results to PR
        - Fail job if tests fail
  ```

**Test Reporting**:

- Use Playwright HTML reporter for detailed results
- Upload test artifacts to GitHub Actions artifacts
- Comment on PR with test summary
- Annotate PR files with test failures

### Makefile Target Updates

```makefile
# New targets for runtime E2E tests

.PHONY: test-client-runtime test-server-runtime test-runtime

test-client-runtime:
 @echo "Running client runtime E2E tests..."
 cd client && npm run test:e2e:runtime

test-server-runtime:
 @echo "Starting server and running runtime E2E tests..."
 ./scripts/start_local.ps1
 sleep 10
 cd client && npm run test:e2e:runtime
 ./scripts/stop_server.ps1

test-runtime: test-client-runtime
 @echo "All runtime E2E tests complete"

# Update existing test target to include runtime tests

test: test-server test-client test-runtime
 @echo "All tests complete"
```

### Package.json Script Updates

```json
{
  "scripts": {
    "test:e2e:runtime": "playwright test --config=tests/e2e/playwright.runtime.config.ts",
    "test:e2e:runtime:headed": "playwright test --config=tests/e2e/playwright.runtime.config.ts --headed",
    "test:e2e:runtime:debug": "playwright test --config=tests/e2e/playwright.runtime.config.ts --debug",
    "test:e2e:runtime:ui": "playwright test --config=tests/e2e/playwright.runtime.config.ts --ui"
  }
}
```

### MCP Scenario Refactoring

**Scenarios Remaining in MCP** (11 total):

1. Scenario 1: Basic Connection/Disconnection - Multi-player message broadcasting
2. Scenario 2: Clean Game State - Multi-player state isolation
3. Scenario 3: Movement Between Rooms - Room transition broadcasting
4. Scenario 4: Muting System/Emotes - Cross-player muting verification
5. Scenario 5: Chat Messages - Bidirectional chat
6. Scenario 6: Admin Teleportation - Multi-player teleport effects
7. Scenario 8: Local Channel Basic - Same sub-zone messaging
8. Scenario 9: Local Channel Isolation - Different sub-zone isolation
9. Scenario 10: Local Channel Movement - Movement-based routing
10. Scenario 13: Whisper Basic - Private messaging between players
11. Scenario 16: Whisper Movement - Cross-location whispers

**Refactoring Updates**:

- Add clear "REQUIRES MULTI-PLAYER" markers in scenario titles
- Simplify execution steps where possible
- Remove redundant verification steps
- Improve execution guards to prevent infinite loops
- Add time estimates for each scenario
- Create scenario dependency maps for efficient execution order

### Performance Considerations

**Test Execution Time**: Aim for <5 minutes total runtime for automated tests

**Parallel Execution**: Configure Playwright to run tests in parallel where possible

**Selective Test Running**: Support test filtering by tag/category for faster iteration
- **Server Startup Optimization**: Reuse server instance across test suites when possible
- **Database Optimization**: Use in-memory SQLite for faster test data operations

### Error Handling & Debugging

**Screenshot on Failure**: Automatically capture screenshots when tests fail

**Video Recording**: Record video of test execution (on failure in CI, always in debug mode)

**Trace Collection**: Collect Playwright traces on first retry for detailed debugging
- **Console Log Capture**: Capture browser console logs and errors
- **Network Request Logging**: Log failed network requests for debugging
- **Test Retry Strategy**: Retry failed tests once to handle transient failures

### Security Considerations

**Test Credentials**: Use dedicated test accounts separate from development/production

**Database Isolation**: Test database must be completely separate from development database

**No Secrets in Code**: All credentials via environment variables
- **CI Secret Management**: Use GitHub Actions secrets for sensitive configuration
- **Network Isolation**: Tests run against local server only, no external API calls
- **Data Privacy**: Test data contains no real user information

### Documentation Requirements

**README Updates**: Update main README with new test commands

**Testing Guide**: Create comprehensive testing guide explaining automated vs MCP tests

**Scenario Conversion Guide**: Document which scenarios were converted and why
- **Adding New Tests Guide**: Provide template and guidelines for adding new automated tests
- **Troubleshooting Guide**: Common test failures and resolution steps
- **CI/CD Documentation**: Explain GitHub Actions workflow and test reporting

## External Dependencies

None. All required dependencies already exist in the project:

- Playwright (already installed in client/package.json)
- TypeScript (already configured)
- SQLite database utilities (already in server/tests/)
- GitHub Actions (already configured for project)
