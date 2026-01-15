---
name: Playwright Test Plan for DI Migration Validation
overview: Create a comprehensive Playwright test suite to validate the app.state to dependency injection migration, testing both regression (existing functionality) and new service functionality for combat, magic, NPC, chat, and shutdown services.
todos:
  - id: test-setup
    content: Create test file structure and configuration in client/tests/e2e/di-migration-validation.spec.ts
    status: completed
  - id: test-helpers
    content: Implement helper functions for service verification, API testing, command testing, and game tick testing
    status: completed
  - id: suite1-core-services
    content: "Implement Suite 1: Core Service Functionality Tests (container, combat, magic, NPC, chat, other services)"
    status: completed
  - id: suite2-api-endpoints
    content: "Implement Suite 2: API Endpoint Validation Tests (metrics API and dependency injection verification)"
    status: completed
  - id: suite3-commands
    content: "Implement Suite 3: Command Handler Validation Tests (status, communication, magic, combat, NPC admin, shutdown)"
    status: completed
  - id: suite4-game-tick
    content: "Implement Suite 4: Game Tick and Background Task Tests (tick processing, service access verification)"
    status: completed
  - id: suite5-websocket
    content: "Implement Suite 5: WebSocket and Real-time Communication Tests (connection, broadcasting, request context)"
    status: completed
  - id: suite6-integration
    content: "Implement Suite 6: Integration Tests (service interactions, multi-service workflows, backward compatibility)"
    status: completed
  - id: test-execution
    content: Run test suite and verify all tests pass
    status: pending
  - id: test-documentation
    content: Document test results and any issues found
    status: pending
---

# Playwright Test Plan: Dependency Injection Migration Validation

## Overview

This test plan validates the migration from `app.state` global state access to dependency injection using `ApplicationContainer`. The tests ensure that:

1. **Regression**: All existing functionality continues to work after migration
2. **Service Functionality**: All migrated services (combat, magic, NPC, chat, shutdown) function correctly
3. **API Endpoints**: Migrated API routes work with dependency injection
4. **Game Tick Processing**: Background tasks and game tick processing work correctly
5. **WebSocket Handlers**: Real-time communication works with container-based services

## Test File Structure

**Location**: `client/tests/e2e/di-migration-validation.spec.ts`

The test file will be organized into test suites covering:

- Core service functionality tests
- API endpoint validation tests
- Command handler validation tests
- Game tick and background task tests
- WebSocket and real-time communication tests
- Integration tests for service interactions

## Test Suites

### Suite 1: Core Service Functionality Tests

**Purpose**: Verify that all migrated services are accessible and functional

**Tests**:

1. **Container Initialization Test**

   - Verify `ApplicationContainer` is initialized on server startup
   - Verify all services are available in container
   - Verify services are accessible via dependency injection

2. **Combat Services Test**

   - Test `player_combat_service` via DI
   - Test `player_death_service` via DI
   - Test `player_respawn_service` via DI
   - Test `combat_service` via DI
   - Verify combat state management works

3. **Magic Services Test**

   - Test `magic_service` via DI
   - Test `spell_registry` via DI
   - Test `spell_targeting_service` via DI
   - Test `spell_effects` via DI
   - Test `spell_learning_service` via DI
   - Test `mp_regeneration_service` via DI
   - Verify MP regeneration works (meditate/pray commands)

4. **NPC Services Test**

   - Test `npc_lifecycle_manager` via DI
   - Test `npc_spawning_service` via DI
   - Test `npc_population_controller` via DI
   - Verify NPCs spawn and despawn correctly

5. **Chat Service Test**

   - Test `chat_service` via DI
   - Verify chat messages are broadcast correctly
   - Test local channel functionality
   - Test whisper functionality

6. **Other Services Test**

   - Test `catatonia_registry` via DI
   - Test `passive_lucidity_flux_service` via DI
   - Test `mythos_time_consumer` via DI
   - Test `nats_message_handler` via DI

### Suite 2: API Endpoint Validation Tests

**Purpose**: Verify that migrated API endpoints work with dependency injection

**Tests**:

1. **Metrics API Test** (`/metrics`)

   - Test GET `/metrics` endpoint
   - Test GET `/metrics/summary` endpoint
   - Test GET `/metrics/dlq` endpoint
   - Test POST `/metrics/reset` endpoint
   - Test POST `/metrics/circuit-breaker/reset` endpoint
   - Test POST `/metrics/dlq/{filepath}/replay` endpoint
   - Test DELETE `/metrics/dlq/{filepath}` endpoint
   - Verify `nats_message_handler` is injected correctly

2. **API Endpoint Dependency Injection Test**

   - Verify all API endpoints can access services via DI
   - Test that services are properly injected
   - Verify error handling when services are unavailable

### Suite 3: Command Handler Validation Tests

**Purpose**: Verify that migrated command handlers work with dependency injection

**Tests**:

1. **Status Command Test**

   - Test `status` command
   - Test `whoami` command
   - Verify `combat_service` is accessed via container
   - Verify combat status is displayed correctly

2. **Communication Commands Test**

   - Test `say` command
   - Test `local` command
   - Test `whisper` command
   - Test `system` command (admin)
   - Verify `chat_service` is accessed via container

3. **Magic Commands Test**

   - Test spell casting commands
   - Test `meditate` command (uses `mp_regeneration_service`)
   - Test `pray` command (uses `mp_regeneration_service`)
   - Verify magic services are accessed via container

4. **Combat Commands Test**

   - Test combat initiation
   - Test combat progression
   - Test death handling
   - Test respawn functionality
   - Verify combat services are accessed via container

5. **NPC Admin Commands Test**

   - Test NPC spawning commands (admin)
   - Test NPC management commands
   - Verify NPC services are accessed via container

6. **Shutdown Command Test**

   - Test `/shutdown` command (admin)
   - Test shutdown countdown
   - Test shutdown cancellation
   - Verify `server_shutdown_pending` and `shutdown_data` are stored in container

### Suite 4: Game Tick and Background Task Tests

**Purpose**: Verify that game tick processing and background tasks work with container

**Tests**:

1. **Game Tick Processing Test**

   - Verify game tick loop runs correctly
   - Test status effect processing
   - Test combat tick processing
   - Test casting progress processing
   - Test DP decay and death processing
   - Test MP regeneration processing
   - Test NPC maintenance processing
   - Test corpse cleanup processing
   - Verify all services are accessed via container

2. **Background Task Service Access Test**

   - Verify background tasks can access services via container
   - Test that services are available during background processing
   - Verify no `app.state` direct access in background tasks

### Suite 5: WebSocket and Real-time Communication Tests

**Purpose**: Verify that WebSocket handlers work with container-based services

**Tests**:

1. **WebSocket Connection Test**

   - Test WebSocket connection establishment
   - Verify connection manager is accessed via container
   - Test player connection/disconnection events

2. **Real-time Message Broadcasting Test**

   - Test message broadcasting via WebSocket
   - Test chat message delivery
   - Test movement message delivery
   - Test combat message delivery
   - Verify services are accessed via container

3. **WebSocket Request Context Test**

   - Test `WebSocketRequestContext` creation
   - Verify services are accessible in WebSocket context
   - Test command processing via WebSocket

### Suite 6: Integration Tests

**Purpose**: Verify that services work together correctly after migration

**Tests**:

1. **Service Interaction Test**

   - Test combat service interacting with player service
   - Test magic service interacting with combat service
   - Test chat service interacting with connection manager
   - Test NPC services interacting with room service
   - Verify all interactions use container-based services

2. **Multi-Service Workflow Test**

   - Test complete player workflow (login → move → combat → death → respawn)
   - Test complete magic workflow (learn spell → cast spell → MP regeneration)
   - Test complete NPC workflow (spawn → interact → despawn)
   - Verify all services are accessed via container

3. **Backward Compatibility Test**

   - Verify that `app.state.container` is accessible
   - Test that services are still available via `app.state` (for backward compatibility)
   - Verify deprecation warnings are logged (if applicable)

## Test Implementation Details

### Test Configuration

```typescript
// Test configuration
const BASE_URL = 'http://localhost:5173';
const SERVER_URL = 'http://localhost:54731';
const TEST_USERNAME = 'ArkanWolfshade';
const TEST_PASSWORD = 'Cthulhu1';
const ADMIN_USERNAME = 'ArkanWolfshade'; // Admin account
```

### Helper Functions

1. **Service Access Verification**

   - Function to verify service is accessible via container
   - Function to verify service is not directly accessed via `app.state`
   - Function to verify service is injected correctly

2. **API Endpoint Testing**

   - Function to test API endpoints with dependency injection
   - Function to verify service injection in API routes
   - Function to test error handling when services are unavailable

3. **Command Testing**

   - Function to execute commands via WebSocket
   - Function to verify command responses
   - Function to verify service access in command handlers

4. **Game Tick Testing**

   - Function to wait for game tick
   - Function to verify tick processing
   - Function to verify service access in tick processing

### Test Data Setup

1. **Player Setup**

   - Create test players if needed
   - Set up player state for testing
   - Clean up after tests

2. **Service State Setup**

   - Initialize services for testing
   - Set up test data for services
   - Clean up service state after tests

### Assertions

1. **Service Availability**

   - Assert services are available in container
   - Assert services are not None
   - Assert services are properly initialized

2. **Functionality**

   - Assert commands execute correctly
   - Assert API endpoints return correct responses
   - Assert game tick processing works
   - Assert WebSocket communication works

3. **Dependency Injection**

   - Assert services are accessed via container
   - Assert no direct `app.state` access (except `app.state.container`)
   - Assert dependency injection functions work correctly

## Execution Strategy

### Test Execution Order

1. **Prerequisites**

   - Verify server is running
   - Verify database is accessible
   - Verify client is accessible
   - Clean up any existing test data

2. **Core Service Tests** (Suite 1)

   - Run first to verify basic service functionality
   - These are foundational tests

3. **API Endpoint Tests** (Suite 2)

   - Run after core service tests
   - Verify API endpoints work with DI

4. **Command Handler Tests** (Suite 3)

   - Run after API tests
   - Verify commands work with DI

5. **Game Tick Tests** (Suite 4)

   - Run after command tests
   - Verify background processing works

6. **WebSocket Tests** (Suite 5)

   - Run after game tick tests
   - Verify real-time communication works

7. **Integration Tests** (Suite 6)

   - Run last
   - Verify complete workflows work

### Test Isolation

- Each test should be independent
- Clean up after each test
- Use unique test data
- Avoid test interdependencies

### Error Handling

- Handle service unavailability gracefully
- Log errors for debugging
- Continue testing even if one test fails
- Provide clear error messages

## Success Criteria

### All Tests Must Pass

1. **Service Availability**: All services are available in container
2. **Functionality**: All functionality works as expected
3. **Dependency Injection**: All services are accessed via DI
4. **No Regressions**: Existing functionality is not broken
5. **Performance**: No performance degradation

### Validation Checklist

- [ ] All core services are accessible via container
- [ ] All API endpoints work with dependency injection
- [ ] All command handlers work with dependency injection
- [ ] Game tick processing works with container
- [ ] WebSocket handlers work with container
- [ ] Integration tests pass
- [ ] No direct `app.state` access (except `app.state.container`)
- [ ] Backward compatibility maintained
- [ ] Performance is acceptable

## Test File Location

**File**: `client/tests/e2e/di-migration-validation.spec.ts`

This file will contain all test suites and test cases described above, following the existing Playwright test patterns in the codebase.
