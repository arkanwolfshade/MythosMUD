# Test Organization Guide

> *Quick reference for where to put new tests in the reorganized test suite*

## Quick Decision Tree

**When writing a new test, ask:**

1. **What am I testing?** → Choose the appropriate domain directory
2. **What type of test is this?** → Choose unit/integration/e2e/etc.
3. **Does a related test file already exist?** → Add to existing file or create new one

## Test Categories and Locations

### Unit Tests (`unit/`)

> Tests for individual components in isolation, using mocks for dependencies

#### API Layer (`unit/api/`)
- API endpoint handlers
- Request/response validation
- API-specific business logic

**Examples:**
- `test_players.py` - Player API endpoints
- `test_health_endpoints.py` - Health check endpoints

#### Commands (`unit/commands/`)
- Command handlers
- Command validation
- Command parsing
- Rate limiting

**Examples:**
- `test_command_handler.py` - Core command processing
- `test_admin_commands.py` - Admin command handlers
- `test_command_validation.py` - Input validation

#### Chat/Communication (`unit/chat/`)
- Chat services
- Channel implementations
- Emote system
- Message filtering

**Examples:**
- `test_chat_service.py` - Core chat functionality
- `test_whisper_channel.py` - Private messaging
- `test_emote_filtering.py` - Emote and mute filtering

#### Player Management (`unit/player/`)
- Player services
- Character creation/recovery
- Player statistics
- User preferences

**Examples:**
- `test_player_service.py` - Player CRUD operations
- `test_character_creation.py` - Character creation flow
- `test_player_stats.py` - Statistics generation

#### NPC System (`unit/npc/`)
- NPC models
- Behavior system
- Spawning/lifecycle
- Population control

**Examples:**
- `test_npc_models.py` - NPC data models
- `test_npc_behaviors.py` - Behavior AI
- `test_npc_spawning_service.py` - Spawn mechanics

#### World/Rooms (`unit/world/`)
- Room models and services
- World loading
- Movement mechanics
- Room hierarchy

**Examples:**
- `test_room_service.py` - Room CRUD operations
- `test_world_loader.py` - World data loading
- `test_movement_service.py` - Player movement

#### Events (`unit/events/`)
- Event bus
- Event publishers/handlers
- Message factories

**Examples:**
- `test_event_bus.py` - Event bus core
- `test_event_publisher.py` - Event publishing
- `test_message_handler_factory.py` - Handler creation

#### Authentication (`unit/auth/`)
- Authentication logic
- Password hashing
- JWT handling
- Email utilities

**Examples:**
- `test_auth.py` - Core authentication
- `test_jwt_authentication.py` - JWT tokens
- `test_argon2_utils.py` - Password hashing

#### Infrastructure (`unit/infrastructure/`)
- Configuration
- Database core
- App factory
- Persistence layer

**Examples:**
- `test_config.py` - Configuration management
- `test_database.py` - Database connections
- `test_persistence.py` - Data persistence

#### Middleware (`unit/middleware/`)
- Error handling middleware
- Logging middleware
- Security middleware
- CORS configuration

**Examples:**
- `test_error_handling_middleware.py` - Error middleware
- `test_logging_middleware.py` - Request logging
- `test_security_middleware.py` - Security headers

#### Models (`unit/models/`)
- Data models
- Model relationships
- Model validation
- Pydantic models

**Examples:**
- `test_models.py` - Base models
- `test_model_relationships.py` - SQLAlchemy relationships
- `test_profession_models.py` - Profession data

#### Services (`unit/services/`)
- Service layer components
- Business logic services
- Background services

**Examples:**
- `test_health_service.py` - Health check service
- `test_game_tick_service.py` - Game loop service
- `test_metrics_collector.py` - Metrics collection

#### Real-time Communication (`unit/realtime/`)
- WebSocket handlers
- SSE handlers
- NATS messaging
- Connection management

**Examples:**
- `test_websocket_handler.py` - WebSocket core
- `test_sse_handler.py` - Server-Sent Events
- `test_nats_service.py` - NATS messaging

#### Logging (`unit/logging/`)
- Logging utilities
- Audit logging
- Chat logging
- Log analysis

**Examples:**
- `test_audit_logger.py` - Audit trail
- `test_chat_logger.py` - Chat history
- `test_log_analysis_tools.py` - Log parsing

#### Utilities (`unit/utilities/`)
- Security utilities
- Rate limiters
- Circuit breakers
- Validation functions

**Examples:**
- `test_security_utils.py` - Security helpers
- `test_rate_limiter.py` - Rate limiting
- `test_validation_functions.py` - Input validation

---

### Integration Tests (`integration/`)

> Tests for component interactions, may use real dependencies

#### By Domain
- `integration/api/` - API integration tests
- `integration/commands/` - Command integration
- `integration/chat/` - Chat system integration
- `integration/events/` - Event flow tests
- `integration/npc/` - NPC system integration
- `integration/movement/` - Movement integration
- `integration/nats/` - NATS messaging integration
- `integration/comprehensive/` - Cross-domain tests

**Examples:**
- `integration/api/test_api_players_integration.py` - Player API with database
- `integration/chat/test_whisper_integration.py` - End-to-end whisper flow
- `integration/events/test_event_flow_integration.py` - Complete event lifecycle

---

### E2E Tests (`e2e/`)

> Full user workflow tests, testing entire application stack

**Examples:**
- `test_multiplayer_integration.py` - Multi-player scenarios
- `test_logout_integration.py` - Complete logout workflow

---

### Performance Tests (`performance/`)

> Performance benchmarks and load tests

**Examples:**
- `test_dual_connection_performance.py` - Connection performance
- `test_model_performance_benchmarks.py` - Model operation benchmarks

---

### Security Tests (`security/`)

> Security-focused tests and penetration tests

**Examples:**
- `test_security_penetration.py` - Penetration testing
- `test_admin_teleport_security.py` - Admin feature security
- `test_centralized_security_validation.py` - Security validation

---

### Coverage Tests (`coverage/`)

> Tests specifically written to improve code coverage

**Examples:**
- `test_command_handler_coverage.py` - Command handler coverage gaps
- `test_comprehensive_logging_coverage.py` - Logging coverage

---

### Regression Tests (`regression/`)

> Bug fix tests to prevent regressions

**Examples:**
- `test_unknown_room_fix.py` - Unknown room bug fix
- `test_self_message_bug.py` - Self-message bug fix

**Naming:** `test_<issue_description>_fix.py` or `test_<bug_name>.py`

---

### Monitoring Tests (`monitoring/`)

> Tests for monitoring and observability features

**Examples:**
- `test_mute_filtering_monitoring.py` - Mute filter monitoring
- `test_movement_monitor.py` - Movement tracking

---

### Verification Tests (`verification/`)

> Tests verifying patterns and standards compliance

**Examples:**
- `test_async_operations_verification.py` - Async pattern verification
- `test_help_topic_validation.py` - Help content validation

---

## File Naming Conventions

### General Rules
- All test files start with `test_`
- Use descriptive, lowercase names with underscores
- Match the module/component being tested when possible

### Specific Patterns

**Unit Tests:**
```
test_<component>.py              # Basic unit test
test_<component>_<aspect>.py     # Specific aspect test
```

**Integration Tests:**
```
test_<feature>_integration.py    # Integration test
```

**E2E Tests:**
```
test_<workflow>_e2e.py           # End-to-end test
test_<workflow>_integration.py   # Also acceptable
```

**Specialized Tests:**
```
test_<feature>_security.py       # Security test
test_<feature>_performance.py    # Performance test
test_<feature>_coverage.py       # Coverage test
test_<issue>_fix.py              # Regression test
```

## Test Class and Method Naming

### Test Classes
```python
class TestComponentName:           # PascalCase, descriptive
    """Test suite for ComponentName."""
```

### Test Methods
```python
def test_<what>_<condition>_<expected_result>():
    """Test that <what> <condition> <expected_result>."""
```

**Examples:**
```python
def test_login_with_valid_credentials_succeeds():
def test_teleport_without_admin_permission_fails():
def test_npc_spawn_in_full_room_raises_error():
def test_movement_to_adjacent_room_updates_location():
```

## When to Create a New Test File

### Create New File When:
1. **New Component**: Testing a new component/module
2. **Different Domain**: Tests belong to different functional area
3. **Different Type**: Unit vs integration vs e2e
4. **Size Limit**: Existing file exceeds ~500 lines
5. **Clear Separation**: Distinct set of related tests

### Add to Existing File When:
1. **Same Component**: Testing same module/class
2. **Related Functionality**: Closely related features
3. **Shared Setup**: Tests use same fixtures/setup
4. **Reasonable Size**: File stays under ~500 lines

## Fixture Organization

### Global Fixtures (`conftest.py`)
- Application-wide fixtures
- Database setup
- Authentication fixtures
- Connection fixtures

### Domain Fixtures (`fixtures/`)
```
fixtures/
├── player_fixtures.py          # Player-related fixtures
├── room_fixtures.py            # Room/world fixtures
├── npc_fixtures.py             # NPC fixtures
└── connection_fixtures.py      # Connection fixtures
```

### Local Fixtures (in test file)
- Test-specific fixtures
- Simple data factories
- Mock configurations

## Common Patterns

### Unit Test Structure (AAA Pattern)
```python
def test_feature_with_condition_has_expected_result():
    """Test that feature with condition has expected result."""
    # Arrange - Set up test data and conditions
    player = create_test_player(admin=True)
    target_room = "arkham_001"

    # Act - Execute the code being tested
    result = teleport_player(player, target_room)

    # Assert - Verify the expected outcome
    assert result.success
    assert player.current_room_id == target_room
```

### Using Fixtures
```python
@pytest.fixture
def admin_player():
    """Fixture providing an admin player."""
    return create_test_player(admin=True)

def test_admin_command(admin_player):
    """Test admin command with admin player."""
    result = execute_admin_command(admin_player, "teleport")
    assert result.allowed
```

### Async Tests
```python
@pytest.mark.asyncio
async def test_async_operation():
    """Test asynchronous operation."""
    result = await async_function()
    assert result.success
```

## Examples by Use Case

### "I'm adding a new API endpoint"
→ **Location:** `unit/api/test_<resource>.py`
→ **Also consider:** Integration test in `integration/api/`

### "I'm adding a new command"
→ **Location:** `unit/commands/test_<command_type>_commands.py`
→ **Also consider:** Integration test in `integration/commands/`

### "I'm fixing a bug"
→ **Location:** `regression/test_<bug_description>_fix.py`
→ **Reference:** Link to issue/bug report in docstring

### "I'm adding a new NPC behavior"
→ **Location:** `unit/npc/test_npc_behaviors.py`
→ **Also consider:** Integration test in `integration/npc/`

### "I'm testing a complete user workflow"
→ **Location:** `e2e/test_<workflow>_e2e.py`

### "I'm improving test coverage"
→ **Location:** `coverage/test_<component>_coverage.py`
→ **Note:** Consider if tests should be in domain-specific unit tests instead

### "I'm testing security"
→ **Location:** `security/test_<feature>_security.py`

### "I'm testing performance"
→ **Location:** `performance/test_<feature>_performance.py`

## Migration Checklist

When migrating existing tests:

- [ ] Identify test type (unit/integration/e2e/etc.)
- [ ] Determine domain (API/commands/chat/etc.)
- [ ] Check for existing related test file
- [ ] Update imports to match new structure
- [ ] Update conftest.py if needed
- [ ] Verify tests still pass
- [ ] Update test documentation
- [ ] Remove old test file
- [ ] Update migration tracking

## Quick Reference Table

| What You're Testing    | Test Type    | Location                                             |
| ---------------------- | ------------ | ---------------------------------------------------- |
| Single function/class  | Unit         | `unit/<domain>/test_<component>.py`                  |
| Component interaction  | Integration  | `integration/<domain>/test_<feature>_integration.py` |
| Full user workflow     | E2E          | `e2e/test_<workflow>_e2e.py`                         |
| Security vulnerability | Security     | `security/test_<feature>_security.py`                |
| Performance/benchmarks | Performance  | `performance/test_<feature>_performance.py`          |
| Coverage gap           | Coverage     | `coverage/test_<component>_coverage.py`              |
| Bug fix                | Regression   | `regression/test_<issue>_fix.py`                     |
| Monitoring/metrics     | Monitoring   | `monitoring/test_<feature>_monitoring.py`            |
| Standards compliance   | Verification | `verification/test_<pattern>_verification.py`        |

---

**For More Details:**
- See `docs/TEST_SUITE_REFACTORING_PLAN.md` for complete refactoring plan
- See `docs/TEST_MIGRATION_MAPPING.md` for file migration mapping
- See `server/tests/README.md` for test suite documentation

---

*"Proper organization of our test rituals ensures that knowledge is preserved and readily accessible to those who seek it."*
