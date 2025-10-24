# 🐙 MythosMUD Command Testing Guide

*"In the realm of eldritch coding, the only truth is that which can be tested and verified."* - Dr. Francis Wayland Thurston, Miskatonic University

---

## Table of Contents

1. [Overview](#overview)
2. [Testing Philosophy](#testing-philosophy)
3. [Test Structure](#test-structure)
4. [Unit Testing](#unit-testing)
5. [Integration Testing](#integration-testing)
6. [Mocking Strategies](#mocking-strategies)
7. [Test Data Management](#test-data-management)
8. [Security Testing](#security-testing)
9. [Performance Testing](#performance-testing)
10. [Test Coverage](#test-coverage)
11. [Best Practices](#best-practices)
12. [Common Testing Patterns](#common-testing-patterns)

---

## Overview

Testing is crucial for maintaining the reliability and security of MythosMUD commands. This guide provides comprehensive strategies for testing command handlers, models, and integration points.

### Testing Goals

- **Reliability**: Ensure commands work correctly under all conditions
- **Security**: Verify commands handle malicious input safely
- **Performance**: Confirm commands meet performance requirements
- **Maintainability**: Make tests easy to understand and modify
- **Coverage**: Test all code paths and edge cases

### Testing Pyramid

```
        /\
       /  \     E2E Tests (Few)
      /____\
     /      \   Integration Tests (Some)
    /________\
   /          \ Unit Tests (Many)
  /____________\
```

---

## Testing Philosophy

### Test-Driven Development (TDD)

1. **Write Tests First**: Define expected behavior before implementation
2. **Red-Green-Refactor**: Write failing tests, implement, then improve
3. **Small Increments**: Test and implement in small, manageable chunks
4. **Continuous Feedback**: Use tests to guide development decisions

### Testing Principles

- **Fast**: Tests should run quickly for immediate feedback
- **Isolated**: Tests should not depend on each other
- **Repeatable**: Tests should produce the same results every time
- **Self-Validating**: Tests should clearly pass or fail
- **Timely**: Write tests as you write code, not after

---

## Test Structure

### File Organization

```
server/tests/
├── test_command_handler.py      # Main command handler tests
├── test_command_models.py       # Pydantic model tests
├── test_command_validation.py   # Validation logic tests
├── test_command_integration.py  # Integration tests
├── test_command_security.py     # Security-focused tests
└── conftest.py                  # Shared fixtures and configuration
```

### Test Class Structure

```python
class TestCommandName:
    """Test the command_name command functionality."""

    @pytest.mark.asyncio
    async def test_command_success(self):
        """Test successful command execution."""
        # Arrange
        # Act
        # Assert

    @pytest.mark.asyncio
    async def test_command_missing_parameter(self):
        """Test command with missing required parameter."""
        # Arrange
        # Act
        # Assert

    @pytest.mark.asyncio
    async def test_command_invalid_input(self):
        """Test command with invalid input."""
        # Arrange
        # Act
        # Assert

    @pytest.mark.asyncio
    async def test_command_unauthorized(self):
        """Test command with unauthorized user."""
        # Arrange
        # Act
        # Assert
```

---

## Unit Testing

### Command Handler Testing

#### Basic Handler Test

```python
@pytest.mark.asyncio
async def test_handle_simple_command():
    """Test basic command handler functionality."""

    # Arrange
    mock_request = Mock()
    mock_app = Mock()
    mock_persistence = Mock()
    mock_player = Mock()
    mock_alias_storage = Mock()

    # Setup mocks
    mock_request.app = mock_app
    mock_app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.return_value = mock_player

    # Test data
    command_data = {"command_type": "simple", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data, current_user, mock_request, mock_alias_storage, "testuser"
    )

    # Assert
    assert "result" in result
    assert "success" in result["result"]
    mock_persistence.get_player_by_name.assert_called_once_with("testuser")
```

#### Error Handling Test

```python
@pytest.mark.asyncio
async def test_handle_command_persistence_error():
    """Test command handler when persistence layer is unavailable."""

    # Arrange
    mock_request = Mock()
    mock_app = Mock()
    mock_alias_storage = Mock()

    # Setup mocks for error condition
    mock_request.app = mock_app
    mock_app.state.persistence = None  # Simulate missing persistence

    # Test data
    command_data = {"command_type": "simple"}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data, current_user, mock_request, mock_alias_storage, "testuser"
    )

    # Assert
    assert "result" in result
    assert "can't perform" in result["result"]
```

#### Parameter Validation Test

```python
@pytest.mark.asyncio
async def test_handle_command_missing_parameter():
    """Test command handler with missing required parameter."""

    # Arrange
    mock_request = Mock()
    mock_app = Mock()
    mock_persistence = Mock()
    mock_player = Mock()
    mock_alias_storage = Mock()

    # Setup mocks
    mock_request.app = mock_app
    mock_app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.return_value = mock_player

    # Test data with missing parameter
    command_data = {"command_type": "simple"}  # Missing param1
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data, current_user, mock_request, mock_alias_storage, "testuser"
    )

    # Assert
    assert "result" in result
    assert "Missing required parameter" in result["result"]
```

### Command Model Testing

#### Model Validation Test

```python
def test_command_model_validation():
    """Test command model validation rules."""

    # Test valid command
    valid_cmd = SimpleCommand(param1="valid", param2="optional")
    assert valid_cmd.param1 == "valid"
    assert valid_cmd.param2 == "optional"

    # Test missing required parameter
    with pytest.raises(ValidationError):
        SimpleCommand(param2="optional")  # Missing param1

    # Test invalid parameter type
    with pytest.raises(ValidationError):
        SimpleCommand(param1=123, param2="optional")  # param1 should be string

    # Test parameter length limits
    with pytest.raises(ValidationError):
        SimpleCommand(param1="a" * 101, param2="optional")  # Too long
```

#### Field Validation Test

```python
def test_command_model_field_validation():
    """Test specific field validation rules."""

    # Test empty string validation
    with pytest.raises(ValidationError, match="cannot be empty"):
        SimpleCommand(param1="", param2="optional")

    # Test whitespace-only validation
    with pytest.raises(ValidationError, match="cannot be empty"):
        SimpleCommand(param1="   ", param2="optional")

    # Test special character validation
    with pytest.raises(ValidationError, match="contains invalid characters"):
        SimpleCommand(param1="test<script>", param2="optional")

    # Test valid input
    valid_cmd = SimpleCommand(param1="valid_input", param2="optional")
    assert valid_cmd.param1 == "valid_input"
```

### Command Parser Testing

#### Parser Functionality Test

```python
def test_command_parser_basic():
    """Test basic command parsing functionality."""

    # Test valid command
    result = parse_command("simple value1 value2")
    assert result.command_type == "simple"
    assert result.param1 == "value1"
    assert result.param2 == "value2"

    # Test command with slash prefix
    result = parse_command("/simple value1")
    assert result.command_type == "simple"
    assert result.param1 == "value1"

    # Test empty command
    with pytest.raises(ValueError, match="Empty command"):
        parse_command("")

    # Test unknown command
    with pytest.raises(ValueError, match="Unknown command"):
        parse_command("unknown_command")
```

---

## Integration Testing

### End-to-End Command Testing

```python
@pytest.mark.asyncio
async def test_command_end_to_end():
    """Test complete command execution flow."""

    # Arrange
    app = create_test_app()
    client = TestClient(app)

    # Create test data
    test_player = create_test_player("testuser")
    test_room = create_test_room("test_room_001")

    # Setup test environment
    await setup_test_environment(app, test_player, test_room)

    # Act
    response = await client.post(
        "/command",
        json={"command": "simple value1"},
        headers={"Authorization": f"Bearer {create_test_token('testuser')}"}
    )

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "result" in result
    assert "success" in result["result"]
```

### Database Integration Testing

```python
@pytest.mark.asyncio
async def test_command_database_integration():
    """Test command interaction with database."""

    # Arrange
    async with get_test_database() as db:
        # Create test data
        player = await create_test_player_in_db(db, "testuser")
        room = await create_test_room_in_db(db, "test_room_001")

        # Setup command handler with real database
        handler = CommandHandler(db)

        # Act
        result = await handler.handle_command(
            "simple value1", player, room
        )

        # Assert
        assert result["success"] is True

        # Verify database state
        updated_player = await db.get_player("testuser")
        assert updated_player.last_command == "simple"
```

### Event System Integration Testing

```python
@pytest.mark.asyncio
async def test_command_event_integration():
    """Test command interaction with event system."""

    # Arrange
    event_bus = MockEventBus()
    persistence = MockPersistence(event_bus)

    # Create test player and room
    player = create_test_player("testuser")
    room = create_test_room("test_room_001")

    # Act
    result = await handle_event_command(
        {"command_type": "event", "action": "test_action"},
        {"username": "testuser"},
        create_mock_request(persistence),
        MockAliasStorage(),
        "testuser"
    )

    # Assert
    assert result["result"] == "Event triggered"

    # Verify event was published
    published_events = event_bus.get_published_events()
    assert len(published_events) == 1
    assert published_events[0].event_type == "PLAYER_ACTION"
    assert published_events[0].data["action"] == "test_action"
```

---

## Mocking Strategies

### Mock Setup Patterns

#### Standard Mock Setup

```python
def setup_standard_mocks():
    """Setup standard mocks for command testing."""

    # Create mocks
    mock_request = Mock()
    mock_app = Mock()
    mock_persistence = Mock()
    mock_player = Mock()
    mock_alias_storage = Mock()

    # Configure mocks
    mock_request.app = mock_app
    mock_app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.return_value = mock_player

    # Configure player mock
    mock_player.username = "testuser"
    mock_player.current_room_id = "test_room_001"
    mock_player.is_admin = False

    return {
        "request": mock_request,
        "app": mock_app,
        "persistence": mock_persistence,
        "player": mock_player,
        "alias_storage": mock_alias_storage
    }
```

#### Fixture-Based Mocking

```python
@pytest.fixture
def mock_command_environment():
    """Fixture for command testing environment."""

    mocks = setup_standard_mocks()

    # Additional setup
    mocks["persistence"].get_room.return_value = create_mock_room()
    mocks["persistence"].get_players_in_room.return_value = []

    yield mocks

    # Cleanup (if needed)
    pass

@pytest.mark.asyncio
async def test_command_with_fixture(mock_command_environment):
    """Test command using fixture-based mocking."""

    # Arrange
    command_data = {"command_type": "simple", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data,
        current_user,
        mock_command_environment["request"],
        mock_command_environment["alias_storage"],
        "testuser"
    )

    # Assert
    assert "result" in result
    assert "success" in result["result"]
```

### Mock Verification

```python
@pytest.mark.asyncio
async def test_command_mock_verification():
    """Test that mocks are called correctly."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "simple", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Act
    await handle_simple_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert - verify mocks were called correctly
    mocks["persistence"].get_player_by_name.assert_called_once_with("testuser")
    mocks["persistence"].get_room.assert_called_once_with("test_room_001")

    # Verify no unexpected calls
    mocks["persistence"].get_players_in_room.assert_not_called()
```

---

## Test Data Management

### Test Data Factories

```python
class TestDataFactory:
    """Factory for creating test data."""

    @staticmethod
    def create_test_player(username: str = "testuser", **kwargs) -> Mock:
        """Create a mock player for testing."""
        player = Mock()
        player.username = username
        player.current_room_id = kwargs.get("room_id", "test_room_001")
        player.is_admin = kwargs.get("is_admin", False)
        player.is_muted = kwargs.get("is_muted", False)
        return player

    @staticmethod
    def create_test_room(room_id: str = "test_room_001", **kwargs) -> Mock:
        """Create a mock room for testing."""
        room = Mock()
        room.room_id = room_id
        room.name = kwargs.get("name", "Test Room")
        room.description = kwargs.get("description", "A test room")
        room.exits = kwargs.get("exits", {"north": "test_room_002"})
        return room

    @staticmethod
    def create_test_command_data(command_type: str, **kwargs) -> dict:
        """Create test command data."""
        return {
            "command_type": command_type,
            **kwargs
        }
```

### Test Data Utilities

```python
def create_mock_request(persistence=None):
    """Create a mock request object for testing."""
    mock_request = Mock()
    mock_app = Mock()
    mock_request.app = mock_app
    mock_app.state.persistence = persistence or Mock()
    return mock_request

def create_mock_user(username="testuser", is_admin=False):
    """Create a mock user object for testing."""
    return {
        "username": username,
        "is_admin": is_admin,
        "is_muted": False
    }

def create_test_command_string(command, *args):
    """Create a test command string."""
    return f"{command} {' '.join(args)}".strip()
```

---

## Security Testing

### Input Validation Testing

```python
@pytest.mark.asyncio
async def test_command_sql_injection_prevention():
    """Test that commands prevent SQL injection."""

    # Arrange
    mocks = setup_standard_mocks()
    malicious_input = "'; DROP TABLE players; --"

    command_data = {"command_type": "simple", "param1": malicious_input}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert
    assert "result" in result
    assert "invalid" in result["result"].lower()

    # Verify no database calls were made with malicious input
    mocks["persistence"].execute_raw_sql.assert_not_called()

@pytest.mark.asyncio
async def test_command_xss_prevention():
    """Test that commands prevent XSS attacks."""

    # Arrange
    mocks = setup_standard_mocks()
    malicious_input = "<script>alert('xss')</script>"

    command_data = {"command_type": "simple", "param1": malicious_input}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert
    assert "result" in result
    assert "<script>" not in result["result"]
```

### Authorization Testing

```python
@pytest.mark.asyncio
async def test_command_admin_authorization():
    """Test admin-only command authorization."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "admin", "action": "test"}

    # Test non-admin user
    current_user = {"username": "testuser", "is_admin": False}

    # Act
    result = await handle_admin_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert
    assert "result" in result
    assert "permission" in result["result"].lower()

    # Test admin user
    current_user = {"username": "admin", "is_admin": True}

    # Act
    result = await handle_admin_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "admin"
    )

    # Assert
    assert "result" in result
    assert "success" in result["result"].lower()
```

### Rate Limiting Testing

```python
@pytest.mark.asyncio
async def test_command_rate_limiting():
    """Test command rate limiting functionality."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "rate_limited"}
    current_user = {"username": "testuser"}

    # Act - first call should succeed
    result1 = await handle_rate_limited_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert - first call successful
    assert "result" in result1
    assert "completed" in result1["result"]

    # Act - second call should be rate limited
    result2 = await handle_rate_limited_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert - second call rate limited
    assert "result" in result2
    assert "too frequently" in result2["result"]
```

---

## Performance Testing

### Response Time Testing

```python
@pytest.mark.asyncio
async def test_command_response_time():
    """Test that commands respond within acceptable time limits."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "simple", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Act
    start_time = time.time()
    result = await handle_simple_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )
    end_time = time.time()

    # Assert
    response_time = end_time - start_time
    assert response_time < 0.1  # Should respond within 100ms
    assert "result" in result
```

### Memory Usage Testing

```python
@pytest.mark.asyncio
async def test_command_memory_usage():
    """Test that commands don't cause memory leaks."""

    import psutil
    import os

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "simple", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Get initial memory usage
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss

    # Act - run command multiple times
    for _ in range(100):
        result = await handle_simple_command(
            command_data,
            current_user,
            mocks["request"],
            mocks["alias_storage"],
            "testuser"
        )
        assert "result" in result

    # Get final memory usage
    final_memory = process.memory_info().rss
    memory_increase = final_memory - initial_memory

    # Assert - memory increase should be minimal
    assert memory_increase < 1024 * 1024  # Less than 1MB increase
```

---

## Test Coverage

### Coverage Requirements

```python
# pytest.ini configuration
[tool:pytest]
minversion = 6.0
addopts =
    --strict-markers
    --strict-config
    --verbose
    --tb=short
    --cov=server
    --cov-report=term-missing
    --cov-report=html
    --cov-fail-under=80
testpaths = server/tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    unit: Unit tests
    integration: Integration tests
    security: Security tests
    performance: Performance tests
```

### Coverage Analysis

```python
def test_command_coverage():
    """Ensure all command code paths are tested."""

    # This test ensures we have coverage for:
    # - All command handlers
    # - All validation logic
    # - All error conditions
    # - All success paths

    # The actual coverage is measured by pytest-cov
    # This test serves as a reminder to maintain coverage
    assert True  # Placeholder for coverage requirements
```

---

## Best Practices

### 1. Test Organization

```python
# Good - organized test structure
class TestWhisperCommand:
    """Test the whisper command functionality."""

    @pytest.mark.asyncio
    async def test_whisper_success(self):
        """Test successful whisper to valid player."""
        # Test implementation

    @pytest.mark.asyncio
    async def test_whisper_invalid_target(self):
        """Test whisper to non-existent player."""
        # Test implementation

    @pytest.mark.asyncio
    async def test_whisper_empty_message(self):
        """Test whisper with empty message."""
        # Test implementation

# Bad - disorganized tests
def test_whisper_1():
    # Mixed test scenarios
    pass

def test_whisper_2():
    # Unclear what this tests
    pass
```

### 2. Descriptive Test Names

```python
# Good - descriptive test names
async def test_whisper_command_sends_message_only_to_target_player():
    """Test that whisper messages are only sent to the target player."""
    pass

async def test_whisper_command_returns_error_for_non_existent_player():
    """Test that whisper returns error when target player doesn't exist."""
    pass

# Bad - unclear test names
async def test_whisper_1():
    pass

async def test_whisper_error():
    pass
```

### 3. Comprehensive Assertions

```python
# Good - comprehensive assertions
async def test_whisper_command_comprehensive():
    """Test whisper command with comprehensive assertions."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "whisper", "target": "targetuser", "message": "Hello"}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_whisper_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert - comprehensive checks
    assert "result" in result
    assert "Hello" in result["result"]
    assert "targetuser" in result["result"]

    # Verify mocks were called correctly
    mocks["persistence"].get_player_by_name.assert_called()
    mocks["persistence"].get_players_in_room.assert_called()

# Bad - minimal assertions
async def test_whisper_command_minimal():
    result = await handle_whisper_command(...)
    assert result is not None  # Too vague
```

### 4. Test Isolation

```python
# Good - isolated tests
@pytest.mark.asyncio
async def test_whisper_command_isolated():
    """Test whisper command in isolation."""

    # Each test creates its own mocks
    mocks = setup_standard_mocks()

    # Test implementation
    result = await handle_whisper_command(...)

    # Verify only expected calls were made
    mocks["persistence"].get_player_by_name.assert_called_once()
    mocks["persistence"].get_players_in_room.assert_called_once()

# Bad - shared state
shared_mocks = setup_standard_mocks()  # Shared between tests

async def test_whisper_1():
    # Uses shared mocks - can affect other tests
    pass

async def test_whisper_2():
    # Uses same shared mocks - state from test_whisper_1 affects this
    pass
```

---

## Common Testing Patterns

### 1. Parameterized Testing

```python
@pytest.mark.parametrize("input_data,expected_result", [
    ({"param1": "valid"}, "success"),
    ({"param1": ""}, "error"),
    ({"param1": "a" * 101}, "error"),
    ({"param1": "<script>"}, "error"),
])
@pytest.mark.asyncio
async def test_command_parameterized(input_data, expected_result):
    """Test command with various input parameters."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "simple", **input_data}
    current_user = {"username": "testuser"}

    # Act
    result = await handle_simple_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert
    assert expected_result in result["result"]
```

### 2. Error Testing Pattern

```python
@pytest.mark.asyncio
async def test_command_error_conditions():
    """Test command error handling."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "simple"}
    current_user = {"username": "testuser"}

    # Test persistence layer unavailable
    mocks["app"].state.persistence = None
    result = await handle_simple_command(
        command_data, current_user, mocks["request"], mocks["alias_storage"], "testuser"
    )
    assert "can't perform" in result["result"]

    # Test player not found
    mocks["app"].state.persistence = mocks["persistence"]
    mocks["persistence"].get_player_by_name.return_value = None
    result = await handle_simple_command(
        command_data, current_user, mocks["request"], mocks["alias_storage"], "testuser"
    )
    assert "can't perform" in result["result"]

    # Test room not found
    mocks["persistence"].get_player_by_name.return_value = mocks["player"]
    mocks["persistence"].get_room.return_value = None
    result = await handle_simple_command(
        command_data, current_user, mocks["request"], mocks["alias_storage"], "testuser"
    )
    assert "can't perform" in result["result"]
```

### 3. Async Testing Pattern

```python
@pytest.mark.asyncio
async def test_command_async_operations():
    """Test command with async operations."""

    # Arrange
    mocks = setup_standard_mocks()
    command_data = {"command_type": "async", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Mock async operations
    mocks["persistence"].async_operation = AsyncMock(return_value="result")

    # Act
    result = await handle_async_command(
        command_data,
        current_user,
        mocks["request"],
        mocks["alias_storage"],
        "testuser"
    )

    # Assert
    assert "result" in result
    mocks["persistence"].async_operation.assert_awaited_once()
```

---

## Enhanced Logging in Command Tests

### **CRITICAL: Enhanced Logging Requirements**
All command tests MUST use the enhanced logging system for proper observability and debugging.

#### **Required Import Pattern**
```python
# ✅ CORRECT - Enhanced logging import (MANDATORY)
from server.logging.enhanced_logging_config import get_logger
logger = get_logger(__name__)
```

#### **Forbidden Patterns**
```python
# ❌ FORBIDDEN - Will cause import failures and system crashes
import logging
logger = logging.getLogger(__name__)

# ❌ FORBIDDEN - Deprecated context parameter (causes TypeError)
logger.info("Test started", context={"test_name": "example"})

# ❌ FORBIDDEN - String formatting breaks structured logging
logger.info(f"Test {test_name} started")
```

#### **Correct Logging Patterns in Tests**
```python
# ✅ CORRECT - Test setup logging
logger.info("Command test started", test_name="test_whisper_command", command="whisper", test_file="test_communication_commands.py")

# ✅ CORRECT - Test step logging
logger.debug("Test step executed", step="setup_mock_data", command="whisper", target_user="testuser")

# ✅ CORRECT - Error logging in tests
logger.error("Test assertion failed", assertion="command_success", expected=True, actual=False, test_step="verify_command_execution")

# ✅ CORRECT - Performance logging
logger.info("Test performance metrics", test_duration_ms=250, command="whisper", assertions_passed=5)
```

#### **Test Logging Best Practices**
- **Structured Logging**: Always use key-value pairs for log data
- **Test Context**: Include test name, command, and step information
- **Error Context**: Log sufficient context for debugging test failures
- **Performance Tracking**: Log test execution times and metrics
- **Security**: Never log sensitive test data (passwords, tokens)

#### **Logging Validation in Tests**
```python
# ✅ CORRECT - Validate logging behavior in tests
def test_command_logging():
    """Test that commands log correctly."""
    with patch.object(enhanced_logging, 'get_logger') as mock_logger:
        # Setup mock logger
        mock_logger.return_value.info = MagicMock()
        
        # Execute command
        result = await handle_whisper_command(command_data, current_user, request, alias_storage, "testuser")
        
        # Verify logging occurred
        mock_logger.return_value.info.assert_called_with(
            "Command executed",
            command="whisper",
            user_id=current_user["id"],
            success=True
        )
```

#### **Documentation References**
- **Complete Guide**: [LOGGING_BEST_PRACTICES.md](LOGGING_BEST_PRACTICES.md)
- **Quick Reference**: [LOGGING_QUICK_REFERENCE.md](LOGGING_QUICK_REFERENCE.md)
- **Testing Examples**: [docs/examples/logging/testing_examples.py](examples/logging/testing_examples.py)

## Conclusion

Comprehensive testing is essential for maintaining the reliability and security of MythosMUD commands. By following these patterns and best practices, you can ensure that:

- Commands work correctly under all conditions
- Security vulnerabilities are caught early
- Performance issues are identified
- Code changes don't break existing functionality
- Documentation stays accurate and up-to-date

Remember to:
- Write tests before implementing features (TDD)
- Maintain high test coverage
- Test both success and error paths
- Use descriptive test names and documentation
- Keep tests fast, isolated, and maintainable

---

*This guide should be updated as testing practices evolve and new patterns emerge.*
