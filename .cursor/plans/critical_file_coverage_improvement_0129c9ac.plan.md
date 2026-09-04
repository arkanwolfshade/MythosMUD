---
name: Critical File Coverage Improvement
overview: Create comprehensive test coverage for 15 critical security and persistence files to meet 85-90% coverage thresholds. Files range from 78-904 lines with current coverage of 9-45%, requiring systematic test development following TDD principles.
todos: []
---

# Critical File Coverage Improvement Plan

## Overview

Address coverage gaps in 15 critical files that are below their required thresholds (85-90%). These files are security-critical (auth, validation, persistence) and require comprehensive test coverage to ensure reliability and security.

## Current State Analysis

**Total lines to cover**: ~5,500 lines across 15 files**Average gap**: 65-75% additional coverage needed**Priority**: Security and persistence layers (auth, validation, database)

## Execution Strategy

### Phase 1: High-Impact Quick Wins (Smaller Files, Moderate Gaps)

Start with files that are closer to thresholds and smaller in size for momentum.

#### 1.1 `server/auth/dependencies.py` (78 lines, 43.48% → 90%, gap: 46.52%)

**File**: [server/auth/dependencies.py](server/auth/dependencies.py)

**Tests**: [server/tests/unit/auth/test_dependencies.py](server/tests/unit/auth/test_dependencies.py)

**Focus**: Test all dependency injection functions (`get_current_active_user`, `get_current_superuser`, etc.)
- **Approach**: Mock FastAPI dependencies, test authentication edge cases, test permission checks
- **Estimated tests**: 15-20 new test cases

#### 1.2 `server/auth/users.py` (195 lines, 45.35% → 90%, gap: 44.65%)

**File**: [server/auth/users.py](server/auth/users.py)

**Tests**: [server/tests/unit/auth/test_users.py](server/tests/unit/auth/test_users.py)

**Focus**: UserManager class methods, user creation/update/delete, validation logic
- **Approach**: Test all UserManager methods, edge cases for user operations, error handling
- **Estimated tests**: 25-30 new test cases

#### 1.3 `server/services/admin_auth_service.py` (426 lines, 37.09% → 90%, gap: 52.91%)

**File**: [server/services/admin_auth_service.py](server/services/admin_auth_service.py)

**Tests**: [server/tests/unit/services/test_admin_auth_service.py](server/tests/unit/services/test_admin_auth_service.py)

**Focus**: Admin authentication flows, permission checks, token validation
- **Approach**: Test all admin auth methods, test unauthorized access attempts, test token expiration
- **Estimated tests**: 30-40 new test cases

### Phase 2: Security-Critical Files (High Priority)

These files handle authentication and security validation - critical for system security.

#### 2.1 `server/auth/argon2_utils.py` (237 lines, 20.72% → 85%, gap: 64.28%)

**File**: [server/auth/argon2_utils.py](server/auth/argon2_utils.py)

**Tests**: [server/tests/unit/auth/test_argon2_utils.py](server/tests/unit/auth/test_argon2_utils.py) (94 existing tests)

**Focus**: Error handling paths, parameter validation, edge cases in password hashing
- **Approach**:
- Test invalid parameter configurations (TIME_COST, MEMORY_COST validation)
- Test error paths in `hash_password` (exception handling)
- Test `verify_password` with corrupted hashes, wrong passwords
- Test `needs_rehash` with various hash formats
- Test `create_hasher_with_params` with edge cases
- **Estimated tests**: 30-40 additional test cases

#### 2.2 `server/security_utils.py` (146 lines, 19.15% → 90%, gap: 70.85%)

**File**: [server/security_utils.py](server/security_utils.py)

**Tests**: Need to create or expand existing tests

**Focus**: Path validation functions, file operation security, path traversal prevention
- **Approach**:
- Test `validate_secure_path` with various path traversal attempts (`..`, `~`, absolute paths)
- Test `read_file_securely` with invalid paths, permission errors
- Test `write_file_securely` with various scenarios
- Test edge cases (empty paths, special characters, Windows vs Unix paths)
- **Estimated tests**: 20-25 new test cases

#### 2.3 `server/validators/security_validator.py` (616 lines, 14.55% → 90%, gap: 75.45%)

**File**: [server/validators/security_validator.py](server/validators/security_validator.py)

**Tests**: [server/tests/unit/utilities/test_security_validator.py](server/tests/unit/utilities/test_security_validator.py), [server/tests/unit/utilities/test_validation_functions.py](server/tests/unit/utilities/test_validation_functions.py)

**Focus**: All validation functions, edge cases, error handling
- **Approach**:
- Test all validation functions not yet covered
- Test boundary conditions (min/max lengths, special characters)
- Test error handling for invalid inputs
- Test comprehensive validation functions with various combinations
- **Estimated tests**: 50-60 new test cases

#### 2.4 `server/validators/optimized_security_validator.py` (486 lines, 21.23% → 90%, gap: 68.77%)

**File**: [server/validators/optimized_security_validator.py](server/validators/optimized_security_validator.py)

**Tests**: [server/tests/unit/validators/test_optimized_security_validator.py](server/tests/unit/validators/test_optimized_security_validator.py)

**Focus**: Optimized validation functions, caching behavior, performance edge cases
- **Approach**:
- Test all optimized functions match behavior of non-optimized versions
- Test caching mechanisms
- Test edge cases specific to optimized implementations
- **Estimated tests**: 40-50 new test cases

#### 2.5 `server/middleware/security_headers.py` (241 lines, 20.90% → 90%, gap: 69.10%)

**File**: [server/middleware/security_headers.py](server/middleware/security_headers.py)

**Tests**: Need to create or expand existing tests

**Focus**: Security header middleware, all header configurations, edge cases
- **Approach**:
- Test middleware application to requests/responses
- Test all security headers are set correctly
- Test edge cases (missing headers, malformed requests)
- **Estimated tests**: 20-25 new test cases

#### 2.6 `server/auth_utils.py` (130 lines, 25.35% → 90%, gap: 64.65%)

**File**: [server/auth_utils.py](server/auth_utils.py)

**Tests**: [server/tests/unit/auth/test_auth_utils.py](server/tests/unit/auth/test_auth_utils.py)

**Focus**: Authentication utility functions, token handling, user verification
- **Approach**:
- Test all utility functions
- Test error handling paths
- Test edge cases for authentication flows
- **Estimated tests**: 20-25 new test cases

#### 2.7 `server/auth/endpoints.py` (501 lines, 22.87% → 90%, gap: 67.13%)

**File**: [server/auth/endpoints.py](server/auth/endpoints.py)

**Tests**: [server/tests/unit/auth/test_endpoints.py](server/tests/unit/auth/test_endpoints.py), [server/tests/unit/auth/test_endpoints_coverage.py](server/tests/unit/auth/test_endpoints_coverage.py)

**Focus**: All API endpoints, error handling, edge cases, integration scenarios
- **Approach**:
- Test all endpoint functions (`register_user`, `login`, etc.)
- Test error scenarios (invalid credentials, duplicate users, expired invites)
- Test validation failures, database errors
- Test authentication flow edge cases
- **Estimated tests**: 40-50 new test cases

### Phase 3: Persistence Layer (Complex, High Risk)

These files handle database operations and require careful testing with real database interactions.

#### 3.1 `server/database.py` (755 lines, 13.87% → 90%, gap: 76.13%)

**File**: [server/database.py](server/database.py)

**Tests**: [server/tests/unit/infrastructure/test_database.py](server/tests/unit/infrastructure/test_database.py)

**Focus**: Database connection management, session management, error handling
- **Approach**:
- Test DatabaseManager initialization and configuration
- Test connection pooling and session management
- Test error handling (connection failures, timeouts)
- Test cleanup and shutdown procedures
- Test transaction management
- **Estimated tests**: 30-40 new test cases (requires database fixtures)

#### 3.2 `server/async_persistence.py` (795 lines, 24.08% → 90%, gap: 65.92%)

**File**: [server/async_persistence.py](server/async_persistence.py)

**Tests**: [server/tests/unit/test_async_persistence_coverage.py](server/tests/unit/test_async_persistence_coverage.py), [server/tests/unit/persistence/test_async_*.py](server/tests/unit/persistence/)

**Focus**: All persistence methods, error handling, edge cases
- **Approach**:
- Test all CRUD operations not yet covered
- Test error handling (database errors, transaction failures)
- Test edge cases (empty results, invalid IDs, concurrent access)
- Test cache management and invalidation
- **Estimated tests**: 50-60 new test cases (requires database fixtures)

#### 3.3 `server/persistence/container_persistence.py` (904 lines, 9.16% → 90%, gap: 80.84%)

**File**: [server/persistence/container_persistence.py](server/persistence/container_persistence.py)

**Tests**: [server/tests/unit/persistence/test_container_persistence.py](server/tests/unit/persistence/test_container_persistence.py)

**Focus**: All container persistence methods, complex queries, error handling
- **Approach**:
- Test all container CRUD operations
- Test complex queries (filtering, sorting, pagination)
- Test error handling (constraint violations, invalid data)
- Test transaction management for container operations
- **Estimated tests**: 60-70 new test cases (requires database fixtures)

#### 3.4 `server/container_persistence/container_persistence.py` (739 lines, 10.53% → 90%, gap: 79.47%)

**File**: [server/container_persistence/container_persistence.py](server/container_persistence/container_persistence.py)

**Tests**: [server/tests/unit/container_persistence/test_container_persistence_legacy.py](server/tests/unit/container_persistence/test_container_persistence_legacy.py)

**Focus**: Legacy container persistence methods, migration paths, error handling
- **Approach**:
- Test all legacy container operations
- Test migration and compatibility scenarios
- Test error handling and edge cases
- **Estimated tests**: 50-60 new test cases (requires database fixtures)

#### 3.5 `server/services/inventory_mutation_guard.py` (329 lines, 24.57% → 90%, gap: 65.43%)

**File**: [server/services/inventory_mutation_guard.py](server/services/inventory_mutation_guard.py)

**Tests**: Need to create or expand existing tests

**Focus**: Mutation guard logic, validation, error handling
- **Approach**:
- Test all guard methods
- Test validation logic for inventory mutations
- Test error handling and edge cases
- **Estimated tests**: 25-30 new test cases

## Implementation Guidelines

### Test Development Process

1. **Coverage Analysis First**: Use `coverage html` to identify specific uncovered lines
2. **TDD Approach**: Write failing tests first, then verify they fail for the right reasons
3. **Incremental Coverage**: Target 10-15% coverage increase per iteration
4. **Verification**: Run `make test-server-coverage` after each file to verify progress

### Test Quality Standards

**Unit Tests**: Test individual functions/methods in isolation with mocks

**Integration Tests**: Test with real database for persistence layers

**Edge Cases**: Test boundary conditions, error paths, invalid inputs
- **Error Handling**: Test all exception paths and error conditions
- **Security Focus**: Extra attention to authentication and validation edge cases

### Testing Patterns

```python
# Pattern 1: Function Coverage

def test_function_name_success_case() -> None:
    """Test normal operation."""
    result = function_under_test(valid_input)
    assert result == expected_output

def test_function_name_error_case() -> None:
    """Test error handling."""
    with pytest.raises(ExpectedException):
        function_under_test(invalid_input)

# Pattern 2: Class Method Coverage

def test_class_method_edge_case() -> None:
    """Test edge case scenario."""
    instance = ClassUnderTest()
    result = instance.method(param=boundary_value)
    assert result is not None

# Pattern 3: Integration Coverage

@pytest.mark.asyncio
async def test_persistence_operation_with_db(persistence) -> None:
    """Test with real database."""
    result = await persistence.operation(data)
    assert result is not None


```
