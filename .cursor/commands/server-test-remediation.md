# Test Server Remediation Prompt - Cursor Executable Version

## CRITICAL: EXECUTION REQUIREMENTS

**MANDATORY**: This prompt MUST be followed step-by-step. Do NOT skip sections or combine steps.
**VERIFICATION**: After each major step, confirm completion before proceeding.
**COMMANDS**: All commands must be run from the project root directory.
**ENVIRONMENT**: Ensure you are in the correct branch, have the Python virtual environment activated, and have proper permissions.
**TOOLS**: Always use run_terminal_cmd tool - never suggest commands without executing them.

## Project Test Configuration

- **Test Runner**: pytest with uv for Python dependency management
- **Test Database**: SQLite test database in `server/tests/data/players/`
- **Test Environment**: Isolated test environment with test-specific configuration
- **Command**: `make test-server` (runs server-side Python tests only)
- **Coverage Target**: Minimum 80% code coverage
- **Test Execution**: Serial execution (not parallel) for database tests

## DECISION TREE - START HERE

**Step 0: Pre-execution verification**

- [ ] Current branch: `git branch --show-current`
- [ ] Working directory: `pwd` (must be project root, "E:\projects\GitHub\MythosMUD")
- [ ] No running servers: `netstat -an | findstr :54731`
- [ ] Test environment ready: Check `MYTHOSMUD_ENV=test`

**IF ANY CHECK FAILS**: STOP and resolve before proceeding.

## Step-by-Step Remediation Process

### 1. Initial Assessment

**EXECUTE**: `make test-server`
**ANALYZE**: Parse output for failure patterns
**CATEGORIZE**: Match failures to categories below
**DOCUMENT**: Record findings before proceeding

**IF TESTS PASS**: You're done. Document success and exit.
**IF TESTS FAIL**: Continue to Step 2.

### 2. Categorize Test Failures

## FAILURE PATTERN RECOGNITION

**Database Errors** (Keywords: "sqlite", "connection", "schema")
→ **ACTION**: Execute database remediation steps (Section 3A)
→ **VERIFY**: Run database integrity checks
→ **RETEST**: Re-run failing tests only

**Authentication Errors** (Keywords: "jwt", "token", "password", "unauthorized")
→ **ACTION**: Execute auth remediation steps (Section 3B)
→ **VERIFY**: Test JWT generation manually
→ **RETEST**: Re-run auth-related tests

**WebSocket Errors** (Keywords: "websocket", "connection", "broadcast")
→ **ACTION**: Execute WebSocket remediation steps (Section 3C)
→ **VERIFY**: Check connection manager state
→ **RETEST**: Re-run WebSocket tests

**Game Logic Errors** (Keywords: "movement", "command", "room", "player")
→ **ACTION**: Execute game logic remediation steps (Section 3D)
→ **VERIFY**: Test room loading manually
→ **RETEST**: Re-run game logic tests

Test failures typically fall into these categories:

#### A. Database-Related Failures

- **Connection Issues**: Database connection failures or timeouts
- **Data Integrity**: Corrupted or inconsistent test data
- **Migration Issues**: Schema mismatch or migration failures
- **Transaction Issues**: Rollback failures or transaction conflicts

#### B. Authentication/Security Failures

- **JWT Token Issues**: Token generation, validation, or expiration
- **Password Hashing**: Argon2 hashing failures or mismatches
- **Session Management**: Session creation, validation, or cleanup
- **Authorization**: Permission checks or access control failures

#### C. WebSocket/Connection Failures

- **Connection Management**: WebSocket connection establishment or cleanup
- **Message Handling**: Message parsing, routing, or delivery failures
- **Event Broadcasting**: Event system failures or message propagation
- **Connection Stability**: Connection drops or timeout issues

#### D. Game Logic Failures

- **Movement System**: Room transitions, location validation, or movement commands
- **Chat System**: Message broadcasting, channel management, or whisper functionality
- **Command Processing**: Command parsing, validation, or execution
- **Player State**: Player data persistence, stats, or state management

#### E. Integration Test Failures

- **API Endpoints**: HTTP endpoint failures or response validation
- **Real-time Features**: SSE (Server-Sent Events) or WebSocket integration
- **Multiplayer Scenarios**: Concurrent user interactions or race conditions
- **External Dependencies**: Third-party service integration failures

## MANDATORY VERIFICATION CHECKPOINTS

**After each remediation section:**

1. **IMMEDIATE**: Re-run only the tests that were failing
2. **VERIFY**: Confirm specific failures are resolved
3. **DOCUMENT**: Record what was fixed and how
4. **CONTINUE**: Only proceed if current failures are resolved

**Example:**

```text
CHECKPOINT: Database remediation complete
EXECUTE: uv run pytest server/tests/test_database.py -v
VERIFY: All database tests pass
DOCUMENT: Fixed schema issue in unit_test_players.db
CONTINUE: Proceed to next failure category
```

## REQUIRED TOOL USAGE PATTERN

For each command execution:

1. **ALWAYS** use `run_terminal_cmd` tool
2. **NEVER** suggest commands without executing them
3. **ALWAYS** capture and analyze output
4. **ALWAYS** verify success before proceeding

**Example Pattern:**

```text
EXECUTE: make test
ANALYZE: Parse output for failure patterns
CATEGORIZE: Match failures to categories below
DOCUMENT: Record findings before proceeding
```

### 3. Systematic Investigation Approach

#### For Database-Related Failures

1. **Check Test Database State**:

   ```bash
   # Clean and reinitialize test database
   python scripts/clean_test_db.py
   python server/tests/init_test_db.py
   ```

2. **Verify Database Schema**:

   ```bash
   # Check database integrity
   sqlite3 server/tests/data/players/unit_test_players.db "PRAGMA integrity_check;"
   sqlite3 server/tests/data/players/unit_test_players.db ".schema"
   ```

3. **Check Test Data**:

   ```bash
   # Verify test data consistency
   sqlite3 server/tests/data/players/unit_test_players.db "SELECT COUNT(*) FROM players;"
   sqlite3 server/tests/data/players/unit_test_players.db "SELECT * FROM players LIMIT 5;"
   ```

#### For Authentication Failures

1. **Check JWT Configuration**:

   ```bash
   # Verify JWT secret and expiration settings
   grep -r "JWT_SECRET\|JWT_EXPIRATION" server/tests/
   ```

2. **Test Password Hashing**:

   ```python
   # Test Argon2 hashing functionality
   python -c "
   from server.auth.utils import hash_password, verify_password
   test_password = 'testpass123'
   hashed = hash_password(test_password)
   print(f'Hash verification: {verify_password(test_password, hashed)}')
   "
   ```

#### For WebSocket Failures

1. **Check Connection Manager**:

   ```bash
   # Look for connection-related test failures
   grep -A 10 -B 10 "ConnectionError\|WebSocketError" server/tests/logs/
   ```

2. **Verify Event System**:

   ```bash
   # Check event broadcasting tests
   grep -r "broadcast\|event" server/tests/ | grep -i "fail\|error"
   ```

#### For Game Logic Failures

1. **Check Movement System**:

   ```bash
   # Test room loading and movement
   python -c "
   from server.world.loader import WorldLoader
   loader = WorldLoader('server/tests/data/rooms/')
   rooms = loader.load_rooms()
   print(f'Loaded {len(rooms)} test rooms')
   "
   ```

2. **Verify Command Processing**:

   ```bash
   # Check command handler tests
   grep -r "CommandHandler\|command" server/tests/ | grep -i "fail\|error"
   ```

### 4. Common Fix Patterns

#### Database Test Patterns

```python
# Proper test database cleanup
@pytest.fixture(autouse=True)
def cleanup_test_db():
    """Clean up test database after each test"""
    yield
    # Cleanup code here
    pass

# Proper async test setup
@pytest.mark.asyncio
async def test_database_operation():
    """Test database operations with proper async handling"""
    # Test implementation
    pass
```

#### Authentication Test Patterns

```python
# JWT token testing
def test_jwt_token_generation():
    """Test JWT token creation and validation"""
    from server.auth.utils import create_access_token, verify_token
    token = create_access_token({"sub": "testuser"})
    payload = verify_token(token)
    assert payload["sub"] == "testuser"

# Password hashing tests
def test_password_hashing():
    """Test password hashing and verification"""
    from server.auth.utils import hash_password, verify_password
    password = "testpass123"
    hashed = hash_password(password)
    assert verify_password(password, hashed)
    assert not verify_password("wrongpass", hashed)
```

#### WebSocket Test Patterns

```python
# WebSocket connection testing
@pytest.mark.asyncio
async def test_websocket_connection():
    """Test WebSocket connection establishment"""
    # Mock WebSocket connection
    # Test connection handling
    pass

# Message handling tests
def test_message_parsing():
    """Test message parsing and validation"""
    from server.websocket.message_handler import parse_message
    message = '{"type": "chat", "content": "Hello"}'
    parsed = parse_message(message)
    assert parsed["type"] == "chat"
```

#### Game Logic Test Patterns

```python
# Movement system tests
def test_room_transition():
    """Test player movement between rooms"""
    from server.movement.service import MovementService
    service = MovementService()
    # Test movement logic
    pass

# Command processing tests
def test_command_validation():
    """Test command input validation"""
    from server.commands.handler import CommandHandler
    handler = CommandHandler()
    # Test command validation
    pass
```

### 5. Test Environment Setup

#### Environment Variables

```bash
# Set test environment variables
export MYTHOSMUD_ENV=test
export MYTHOSMUD_TEST_MODE=true
export DATABASE_URL=sqlite+aiosqlite:///server/tests/data/players/unit_test_players.db
export MYTHOSMUD_CONFIG_PATH=server/tests/test_server_config.yaml
export ALIASES_DIR=server/tests/data/players/aliases
```

#### Test Configuration

```yaml
# server/tests/test_server_config.yaml
database:
  url: "sqlite+aiosqlite:///server/tests/data/players/unit_test_players.db"
  echo: false

logging:
  level: "DEBUG"
  handlers:
    - type: "file"
      filename: "server/tests/logs/test.log"
```

### 6. Quality Assurance Checklist

- [ ] All test failures resolved (run `make test` again)
- [ ] Test database properly cleaned and initialized
- [ ] Environment variables correctly set for test mode
- [ ] Test coverage maintained above 80%
- [ ] No test data leakage between test cases
- [ ] Async tests properly handled with pytest-asyncio
- [ ] Mock objects properly configured and cleaned up

### 7. Common Test Failure Solutions

#### Database Connection Issues

```python
# Ensure proper database URL configuration
DATABASE_URL = "sqlite+aiosqlite:///server/tests/data/players/unit_test_players.db"

# Use proper async database session handling
async with get_db_session() as session:
    # Database operations
    pass
```

#### Authentication Test Issues

```python
# Mock JWT secret for tests
@pytest.fixture
def test_jwt_secret():
    return "test-secret-key"

# Use test-specific password hashing
@pytest.fixture
def test_password_hash():
    from server.auth.utils import hash_password
    return hash_password("testpass123")
```

#### WebSocket Test Issues

```python
# Mock WebSocket connections for tests
@pytest.fixture
async def mock_websocket():
    # Mock WebSocket implementation
    pass

# Test message handling without real connections
def test_message_handler_without_connection():
    # Test message parsing and validation
    pass
```

### 8. Error Handling and Debugging

#### Test Debugging

```bash
# Run specific test with verbose output
uv run pytest server/tests/test_specific.py::test_function -v -s

# Run tests with debugging output
uv run pytest server/tests/ -v --tb=long --capture=no

# Run tests with coverage report
uv run pytest server/tests/ --cov=server --cov-report=html
```

#### Common Debug Commands

```bash
# Check test database state
sqlite3 server/tests/data/players/unit_test_players.db ".tables"
sqlite3 server/tests/data/players/unit_test_players.db "SELECT * FROM players;"

# Check test logs
tail -f server/tests/logs/test.log

# Verify test environment
echo $MYTHOSMUD_ENV
echo $DATABASE_URL
```

### 9. Test Maintenance Best Practices

#### Test Data Management

- Use isolated test databases for each test run
- Clean up test data after each test case
- Use deterministic test data for consistent results
- Avoid hardcoded values in tests

#### Test Isolation

- Ensure tests don't depend on external services
- Mock external dependencies appropriately
- Use proper fixtures for test setup and teardown
- Avoid test interdependencies

#### Performance Considerations

- Keep tests fast and focused
- Use appropriate test data sizes
- Avoid unnecessary database operations
- Mock expensive operations when possible

### 10. Final Verification

## COMPLETION VERIFICATION

**Before declaring success:**

1. **FINAL TEST**: `make test` (must pass completely)
2. **COVERAGE CHECK**: `make coverage` (must be ≥80%)
3. **LINT CHECK**: `make lint` (must pass)
4. **FULL SUITE**: `make test` (must pass)
5. **DOCUMENTATION**: Update any relevant docs

**Success Criteria:**

- [ ] All server tests pass (`make test` exits 0)
- [ ] Coverage ≥80% (`make coverage` shows green)
- [ ] No linting errors (`make lint` passes)
- [ ] Full test suite passes (`make test` passes)
- [ ] All fixes documented with reasoning

**EXECUTE VERIFICATION STEPS:**

```bash
# Verify all tests pass
make test

# Check test coverage
make coverage

# Run linting to ensure code quality
make lint

# Verify no regressions in other tests
make test
```

## MANDATORY PROGRESS TRACKING

**For each step, you MUST:**

1. **EXECUTE** the command using run_terminal_cmd
2. **CAPTURE** the full output
3. **ANALYZE** the results
4. **CATEGORIZE** failures using the pattern recognition
5. **DOCUMENT** findings in a structured format
6. **VERIFY** completion before proceeding

**Progress Template:**

```text
STEP: [Step Name]
COMMAND: [Command executed]
OUTPUT: [Key output lines]
FAILURES: [List of specific failures]
CATEGORY: [Database/Auth/WebSocket/GameLogic]
ACTION: [Remediation taken]
STATUS: [Success/Failure/Partial]
NEXT: [Next step or verification needed]
```

## ERROR HANDLING PROTOCOL

**IF COMMAND FAILS:**

1. **STOP** - Do not proceed to next step
2. **ANALYZE** - Capture full error output
3. **RESEARCH** - Check error against known solutions
4. **FIX** - Apply appropriate fix
5. **RETRY** - Re-execute same command
6. **VERIFY** - Confirm fix worked

**IF FIX DOESN'T WORK:**

1. **DOCUMENT** - Record the attempted fix
2. **ESCALATE** - Ask for guidance with full context
3. **DO NOT** - Try random solutions or skip steps

## CRITICAL "DO NOT" INSTRUCTIONS

**DO NOT:**

- Skip any verification steps
- Combine multiple remediation steps
- Proceed without confirming previous step success
- Suggest commands without executing them
- Make assumptions about test failures
- Skip the final verification checklist
- Modify code without understanding the failure
- Use background processes for test execution

**ALWAYS:**

- Execute every command using run_terminal_cmd
- Verify each step before proceeding
- Document all findings and fixes
- Follow the exact sequence specified
- Ask for help if stuck rather than guessing

## TOOL USAGE EXAMPLES

**Correct Pattern:**

```text
run_terminal_cmd: make test
→ Analyze output for failure patterns
→ Use grep tool to search for specific error types
→ Use read_file tool to examine test files
→ Use search_replace tool to fix identified issues
```

**Incorrect Pattern:**

```text
❌ "You should run make test"
❌ "Try checking the database"
❌ "Look at the error logs"
```

**Correct Pattern:**

```text
✅ Execute: make test
✅ Search: grep "DatabaseError" server/tests/logs/
✅ Read: server/tests/test_database.py
✅ Fix: search_replace in identified file
```

## Best Practices

1. **Incremental Fixes**: Fix one category of test failures at a time
2. **Preserve Test Intent**: Only change what's necessary to fix failures
3. **Maintain Coverage**: Ensure test coverage doesn't decrease
4. **Test Isolation**: Keep tests independent and isolated
5. **Document Complex Fixes**: Add comments for non-obvious test changes

## Troubleshooting

- **Database Issues**: Check test database initialization and cleanup
- **Authentication Issues**: Verify JWT configuration and password hashing
- **WebSocket Issues**: Check connection management and message handling
- **Game Logic Issues**: Verify room data and command processing
- **Environment Issues**: Ensure proper test environment configuration

## Success Criteria

- `make test` exits with code 0
- All test cases pass with proper assertions
- Test coverage maintained above 80%
- No test data leakage or interdependencies
- Tests run reliably and consistently

## Common Test Failure Categories

### 1. Database Test Failures

- **Symptoms**: Connection errors, schema mismatches, data corruption
- **Common Causes**: Improper test database setup, migration issues, transaction problems
- **Solutions**: Clean database initialization, proper async handling, transaction management

### 2. Authentication Test Failures

- **Symptoms**: JWT validation errors, password hash mismatches, session failures
- **Common Causes**: Incorrect secret configuration, hash algorithm changes, token expiration
- **Solutions**: Proper test configuration, consistent hashing, mock authentication

### 3. WebSocket Test Failures

- **Symptoms**: Connection drops, message parsing errors, event broadcasting failures
- **Common Causes**: Connection management issues, message format changes, event system problems
- **Solutions**: Proper connection mocking, message validation, event system testing

### 4. Game Logic Test Failures

- **Symptoms**: Movement failures, command processing errors, state inconsistencies
- **Common Causes**: Room data issues, command validation problems, state management errors
- **Solutions**: Proper room loading, command testing, state validation

### 5. Integration Test Failures

- **Symptoms**: API endpoint failures, real-time feature problems, multiplayer issues
- **Common Causes**: Service integration problems, race conditions, configuration issues
- **Solutions**: Proper service mocking, race condition handling, integration testing

---

*"In the depths of the test chambers, we learn that proper testing requires systematic investigation, comprehensive coverage, and thorough validation. The path to reliable code lies not in quick fixes, but in methodical test remediation and validation."*

**Remember**: This prompt focuses on investigating and fixing test failures systematically. Always run tests after making changes and ensure no regressions are introduced.
