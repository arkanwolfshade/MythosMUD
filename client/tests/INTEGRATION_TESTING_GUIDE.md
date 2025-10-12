# Integration Testing Guide for MythosMUD

## Overview

This guide provides comprehensive procedures and best practices for integration testing in the MythosMUD project. Integration tests verify that critical user workflows function correctly across the entire application stack.

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Test User Management](#test-user-management)
3. [Critical User Workflows](#critical-user-workflows)
4. [Test Execution](#test-execution)
5. [Best Practices](#best-practices)
6. [Troubleshooting](#troubleshooting)

## Environment Setup

### Prerequisites

- **Server Running**: The MythosMUD server must be running on `http://localhost:54731`
- **Client Running**: The MythosMUD client must be running on `http://localhost:5173`
- **Database**: Production database with test users created
- **Dependencies**: Playwright, Node.js, and all project dependencies installed

### Starting the Development Environment

```powershell
# From project root
./scripts/stop_server.ps1  # Stop any running instances
./scripts/start_dev.ps1    # Start both server and client
```

### Verifying Server Status

```powershell
# Check if servers are running
netstat -an | findstr :54731  # Backend server
netstat -an | findstr :5173   # Frontend client
```

## Test User Management

### Test User Credentials

The following test users are available for integration testing:

| Username         | Password            | Role         | Level | Description                           |
| ---------------- | ------------------- | ------------ | ----- | ------------------------------------- |
| `test1`          | `test_password_123` | Regular User | 1     | Basic test user                       |
| `test2`          | `test_password_123` | Regular User | 2     | Secondary test user                   |
| `ArkanWolfshade` | `test_password_123` | Admin        | 5     | Admin user for testing admin commands |
| `Ithaqua`        | `test_password_123` | Regular User | 3     | User with occult knowledge            |

### Creating Test Users

Test users are created in the production database using the `create_production_test_users.py` script:

```powershell
# From server directory
cd server
python create_production_test_users.py
```

### Test User Characteristics

- **All users use the same password** (`test_password_123`) for simplicity
- **Passwords are properly hashed** using Argon2
- **Users have associated player records** with stats and game data
- **Users are verified and active** by default

## Critical User Workflows

### Workflow 1: User Login and Basic Navigation

**Purpose**: Verify that users can successfully log in and access the game interface.

**Test Steps**:

1. Navigate to the login page
2. Enter valid credentials
3. Submit login form
4. Verify game interface loads
5. Verify all UI components are visible

**Expected Results**:

- Login succeeds without errors
- Game terminal is visible
- Room info panel displays room information
- Chat panel is accessible
- Command panel is functional

### Workflow 2: Basic Command Execution

**Purpose**: Verify that users can execute basic game commands.

**Test Steps**:

1. Log in successfully
2. Wait for command input to be available
3. Execute `help` command
4. Verify command response is displayed

**Expected Results**:

- Command input accepts text
- Commands execute successfully
- Command responses appear in the game terminal
- Help content is displayed correctly

### Workflow 3: Room Movement

**Purpose**: Verify that users can move between rooms and see room information.

**Test Steps**:

1. Log in successfully
2. Execute `look` command
3. Verify room description is displayed
4. Test movement commands (if available)

**Expected Results**:

- Room information is displayed correctly
- Room descriptions are visible
- Movement commands work (if implemented)

### Workflow 4: Chat Communication

**Purpose**: Verify that users can send and receive chat messages.

**Test Steps**:

1. Log in successfully
2. Send a test message
3. Verify message appears in chat
4. Test different chat channels (if available)

**Expected Results**:

- Chat input accepts messages
- Messages are sent successfully
- Messages appear in chat history
- Chat interface is responsive

### Workflow 5: Multiplayer Interaction

**Purpose**: Verify that multiple users can interact in the same environment.

**Test Steps**:

1. Log in two different users
2. Send messages from both users
3. Verify messages are visible to both users
4. Test real-time interaction

**Expected Results**:

- Both users can log in simultaneously
- Messages are broadcast between users
- Real-time communication works
- No conflicts or crashes occur

### Workflow 6: Admin Commands

**Purpose**: Verify that admin users can access admin-specific functionality.

**Test Steps**:

1. Log in as admin user (`ArkanWolfshade`)
2. Execute admin commands (e.g., `who`)
3. Verify admin functionality works
4. Test admin-specific features

**Expected Results**:

- Admin user can log in successfully
- Admin commands execute properly
- Admin functionality is accessible
- No permission errors occur

### Workflow 7: Error Handling

**Purpose**: Verify that the system handles errors gracefully.

**Test Steps**:

1. Log in successfully
2. Execute invalid commands
3. Verify error handling
4. Test edge cases

**Expected Results**:

- Invalid commands don't crash the system
- Error messages are displayed appropriately
- System remains stable
- User can continue using the application

### Workflow 8: Session Persistence

**Purpose**: Verify that user sessions persist across page refreshes.

**Test Steps**:

1. Log in successfully
2. Refresh the page
3. Verify user remains logged in
4. Test session timeout (if applicable)

**Expected Results**:

- User remains logged in after refresh
- Session data is preserved
- No re-authentication required
- Application state is maintained

### Workflow 9: Performance and Responsiveness

**Purpose**: Verify that the system responds quickly to user actions.

**Test Steps**:

1. Measure login time
2. Measure command response time
3. Test under load
4. Verify responsiveness

**Expected Results**:

- Login completes within 15 seconds
- Commands respond within 5 seconds
- System remains responsive
- No performance degradation

### Workflow 10: Cross-Browser Compatibility

**Purpose**: Verify that critical workflows work across different browsers.

**Test Steps**:

1. Test in Chromium
2. Test in Firefox
3. Test in WebKit
4. Compare results

**Expected Results**:

- All browsers support basic functionality
- No browser-specific issues
- Consistent behavior across browsers
- No compatibility problems

## Test Execution

### Running Individual Tests

```powershell
# Run specific test
npx playwright test --grep "Critical Path 1" --reporter=line

# Run all critical workflow tests
npx playwright test --grep "Critical User Workflow" --reporter=line

# Run tests in specific browser
npx playwright test --project=chromium --grep "Critical Path"
```

### Running All Integration Tests

```powershell
# Run all integration tests
npx playwright test tests/ --reporter=line

# Run with verbose output
npx playwright test tests/ --reporter=verbose

# Run with HTML report
npx playwright test tests/ --reporter=html
```

### Test Configuration

Integration tests are configured in `playwright.config.ts`:

```typescript
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:5173',
    trace: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
});
```

## Best Practices

### Test Design

1. **Focus on Critical Paths**: Test only the most important user workflows
2. **Keep Tests Simple**: Each test should verify one specific functionality
3. **Use Real Data**: Test with actual user credentials and data
4. **Test Edge Cases**: Include error handling and boundary condition tests
5. **Maintain Independence**: Tests should not depend on each other

### Test Maintenance

1. **Regular Updates**: Update tests when features change
2. **Documentation**: Keep test documentation current
3. **Version Control**: Commit test changes with feature changes
4. **Review Process**: Review test changes like code changes
5. **Monitoring**: Monitor test results and fix failures quickly

### Performance Considerations

1. **Timeout Management**: Set appropriate timeouts for different operations
2. **Resource Cleanup**: Clean up resources after each test
3. **Parallel Execution**: Run tests in parallel when possible
4. **Efficient Selectors**: Use efficient element selectors
5. **Minimal Waits**: Use minimal wait times for better performance

### Error Handling

1. **Graceful Degradation**: Handle errors gracefully in tests
2. **Clear Messages**: Provide clear error messages for debugging
3. **Retry Logic**: Implement retry logic for flaky tests
4. **Logging**: Include comprehensive logging for debugging
5. **Screenshots**: Take screenshots on test failures

## Troubleshooting

### Common Issues

#### Authentication Failures

**Symptoms**: Login tests fail with "Invalid credentials"

**Solutions**:

1. Verify test users exist in the database
2. Check if server is running
3. Verify database connection
4. Check password hashing

#### Timeout Errors

**Symptoms**: Tests timeout waiting for elements

**Solutions**:

1. Increase timeout values
2. Check if server is responsive
3. Verify element selectors
4. Check for JavaScript errors

#### Element Not Found

**Symptoms**: Tests can't find UI elements

**Solutions**:

1. Verify element selectors
2. Check if elements are visible
3. Wait for elements to load
4. Use more specific selectors

#### Network Errors

**Symptoms**: Tests fail with network errors

**Solutions**:

1. Check server status
2. Verify network connectivity
3. Check firewall settings
4. Verify port availability

### Debugging Tips

1. **Use Screenshots**: Take screenshots to see what the test sees
2. **Check Console**: Look for JavaScript errors in browser console
3. **Verify Network**: Check network requests in browser dev tools
4. **Test Manually**: Manually verify the functionality being tested
5. **Check Logs**: Review server logs for errors

### Getting Help

1. **Check Documentation**: Review this guide and other documentation
2. **Review Test Results**: Look at test output and error messages
3. **Check Issues**: Look for similar issues in the project repository
4. **Ask for Help**: Contact the development team for assistance

## Conclusion

Integration testing is crucial for ensuring that MythosMUD provides a reliable and functional user experience. By following the procedures and best practices outlined in this guide, you can effectively test critical user workflows and maintain high quality standards.

Remember to:

- Keep tests focused on critical paths
- Use real data and credentials
- Maintain test independence
- Handle errors gracefully
- Monitor test performance
- Update tests with feature changes

For additional information, refer to the Playwright documentation and the project's README files.
