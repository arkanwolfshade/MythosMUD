# Test Coverage Gaps Report

> *"In the cartography of code coverage, we find that some regions remain unexplored — not for lack of importance, but for lack of attention. These unmapped territories harbor the greatest potential for dimensional instability."*

**Purpose:** Identify critical code paths lacking adequate test coverage and recommend targeted tests.

---

## Critical Coverage Gaps

### Gap 1: Domain Layer (NEW ARCHITECTURE)

**Location:** `server/domain/`
**Current Coverage:** 0%
**Lines of Code:** ~0 (structure created, not yet migrated)
**Risk Level:** 🔴 HIGH (when migration occurs)

**Gap Description:**
Domain layer structure created during architectural remediation, but no entities/value objects/repositories have been migrated yet.

**Missing Tests:**
- Domain entity validation tests
- Value object immutability tests
- Repository interface compliance tests
- Domain service orchestration tests
- Domain event tests
- Domain exception handling tests

**Recommended Tests:** 20-30 tests when migration begins

**Priority:** MEDIUM (no code yet, but prepare for migration)

---

### Gap 2: Message Broker Abstraction

**Location:** `server/infrastructure/message_broker.py`, `server/infrastructure/nats_broker.py`
**Current Coverage:** ~40% (implementation exists, minimal tests)
**Lines of Code:** ~200
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
New MessageBroker protocol and NATSMessageBroker implementation created during architectural remediation. Only basic tests exist.

**Missing Tests:**
- MessageBroker protocol compliance tests
- NATS connection lifecycle tests
- Message publishing/subscribing integration tests
- Error recovery and reconnection tests
- Message serialization/deserialization tests
- Queue group behavior tests

**Recommended Tests:** 15-20 integration tests

**Priority:** HIGH (affects real-time messaging reliability)

**Specific Test Cases Needed:**
```python
# Test 1: Protocol compliance
def test_nats_broker_implements_message_broker_protocol():
    broker = NATSMessageBroker(...)
    assert isinstance(broker, MessageBroker)
    # Verify all protocol methods exist

# Test 2: Connection lifecycle
@pytest.mark.asyncio
async def test_nats_broker_connection_lifecycle():
    broker = NATSMessageBroker(...)
    await broker.connect()
    assert broker.is_connected
    await broker.disconnect()
    assert not broker.is_connected

# Test 3: Message publishing
@pytest.mark.asyncio
async def test_nats_broker_publishes_messages():
    broker = NATSMessageBroker(...)
    await broker.connect()
    await broker.publish("test.subject", {"data": "test"})
    # Verify message was published

# Test 4: Error recovery
@pytest.mark.asyncio
async def test_nats_broker_reconnects_on_connection_loss():
    broker = NATSMessageBroker(...)
    await broker.connect()
    # Simulate connection loss
    # Verify automatic reconnection
```

---

### Gap 3: ApplicationContainer Lifecycle

**Location:** `server/container.py`
**Current Coverage:** ~60% (mostly infrastructure tests)
**Lines of Code:** ~400
**Risk Level:** 🔴 HIGH

**Gap Description:**
ApplicationContainer manages all service initialization and shutdown. Current tests mostly verify types (`assert isinstance`). Missing integration tests for actual lifecycle management.

**Missing Tests:**
- Container initialization order tests
- Service dependency resolution tests
- Container shutdown cleanup tests
- Container initialization failure recovery tests
- Multiple initialization attempts handling
- Service singleton behavior verification

**Recommended Tests:** 10-15 integration tests

**Priority:** HIGH (affects entire application startup/shutdown)

**Specific Test Cases Needed:**
```python
# Test 1: Initialization order
@pytest.mark.asyncio
async def test_container_initializes_services_in_correct_order():
    container = ApplicationContainer()
    await container.initialize()
    # Verify config loaded before services
    # Verify persistence before services
    # Verify event bus before handlers

# Test 2: Shutdown cleanup
@pytest.mark.asyncio
async def test_container_cleanup_on_shutdown():
    container = ApplicationContainer()
    await container.initialize()
    await container.shutdown()
    # Verify all resources released
    # Verify database connections closed
    # Verify event loop cleaned up

# Test 3: Initialization failure recovery
@pytest.mark.asyncio
async def test_container_handles_initialization_failures():
    with patch('server.database.init_db', side_effect=Exception("DB Error")):
        container = ApplicationContainer()
        with pytest.raises(RuntimeError):
            await container.initialize()
        # Verify partial cleanup occurred
```

---

### Gap 4: Error Recovery Paths

**Location:** Multiple files
**Current Coverage:** ~50% (happy paths well-tested, error paths less so)
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
Most tests focus on happy paths. Error recovery, fallback mechanisms, and graceful degradation are under-tested.

**Missing Test Scenarios:**

#### Database Connection Loss
```python
@pytest.mark.asyncio
async def test_persistence_handles_connection_loss_gracefully():
    # Simulate database connection loss mid-operation
    # Verify error is logged
    # Verify graceful error response to user
    # Verify automatic reconnection attempt
```

#### NATS Unavailability
```python
@pytest.mark.asyncio
async def test_game_continues_when_nats_unavailable():
    # Disable NATS
    # Verify game still functions
    # Verify local events still work
    # Verify error is logged
```

#### Room Data Corruption
```python
def test_movement_service_handles_corrupted_room_data():
    # Provide malformed room data
    # Verify player moved to default room
    # Verify error is logged
    # Verify no crash
```

**Recommended Tests:** 20-25 error scenario tests

**Priority:** MEDIUM (improves reliability)

---

### Gap 5: Async/Await Pattern Verification

**Location:** All async functions
**Current Coverage:** ~70% (some async tests, but not comprehensive)
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
Many async functions lack tests verifying they properly await all operations and don't have blocking calls.

**Missing Tests:**
- Tests verifying no blocking I/O in async functions
- Tests verifying proper exception propagation in async
- Tests verifying async context manager usage
- Tests for async deadlock scenarios

**Recommended Tests:** 15-20 async pattern tests

**Priority:** MEDIUM (prevents async bugs)

---

### Gap 6: Rate Limiting and Throttling

**Location:** `server/middleware/command_rate_limiter.py`, various command handlers
**Current Coverage:** ~65%
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
Rate limiting logic exists but edge cases under-tested.

**Missing Tests:**
- Concurrent rate limit threshold tests
- Rate limit reset behavior tests
- Per-command vs global rate limit tests
- Rate limit bypass for admin users
- Rate limit error message tests

**Recommended Tests:** 10-15 rate limiting tests

**Priority:** MEDIUM (prevents abuse)

---

### Gap 7: WebSocket Connection Edge Cases

**Location:** `server/realtime/websocket_handler.py`, `server/realtime/connection_manager.py`
**Current Coverage:** ~75%
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
Happy path well-tested, but connection edge cases under-tested.

**Missing Tests:**
- Simultaneous disconnection handling
- Message queue overflow behavior
- Slow client handling
- Connection timeout scenarios
- Duplicate connection from same user
- Connection during server shutdown

**Recommended Tests:** 15-20 connection edge case tests

**Priority:** HIGH (affects user experience)

---

### Gap 8: Combat System Integration

**Location:** `server/combat/`, various combat services
**Current Coverage:** ~70% unit, ~40% integration
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
Combat system has good unit test coverage but lacks comprehensive integration tests for combat workflows.

**Missing Tests:**
- Complete combat encounter from initiation to resolution
- Multi-NPC combat scenarios
- Player death and respawn integration
- Combat state persistence across reconnection
- Combat event broadcasting to observers

**Recommended Tests:** 10-15 combat integration tests

**Priority:** MEDIUM (complex feature needs integration coverage)

---

### Gap 9: Database Migration and Schema Evolution

**Location:** `server/database.py`, `server/sql/schema.sql`
**Current Coverage:** ~60%
**Risk Level:** 🔴 HIGH

**Gap Description:**
Database initialization tested, but schema migration and evolution under-tested.

**Missing Tests:**
- Schema migration from old to new versions
- Column addition handling (like `respawn_room_id`)
- Data migration for schema changes
- Rollback scenarios
- Schema validation tests

**Recommended Tests:** 10-12 migration tests

**Priority:** HIGH (data integrity critical)

---

### Gap 10: Configuration Edge Cases

**Location:** `server/config/`
**Current Coverage:** ~70%
**Risk Level:** 🟡 MEDIUM

**Gap Description:**
Configuration loading tested, but edge cases and fallbacks under-tested.

**Missing Tests:**
- Missing required configuration handling
- Invalid configuration format handling
- Environment variable override precedence
- Configuration reload behavior
- Default value fallback tests

**Recommended Tests:** 8-10 configuration tests

**Priority:** MEDIUM (affects startup reliability)

---

## Coverage Gap Priority Matrix

| Gap | Lines Uncovered | User Impact | Bug Risk | Priority | Recommended Tests |
|-----|----------------|-------------|----------|----------|-------------------|
| **Message Broker** | ~120 | HIGH | HIGH | 🔴 HIGH | 15-20 |
| **Container Lifecycle** | ~160 | HIGH | HIGH | 🔴 HIGH | 10-15 |
| **Database Migration** | ~80 | HIGH | HIGH | 🔴 HIGH | 10-12 |
| **WebSocket Edge Cases** | ~200 | MEDIUM | HIGH | 🟡 HIGH | 15-20 |
| **Error Recovery** | ~300 | MEDIUM | MEDIUM | 🟡 MEDIUM | 20-25 |
| **Combat Integration** | ~400 | MEDIUM | MEDIUM | 🟡 MEDIUM | 10-15 |
| **Async Patterns** | ~250 | LOW | MEDIUM | 🟡 MEDIUM | 15-20 |
| **Rate Limiting** | ~100 | LOW | MEDIUM | 🟡 MEDIUM | 10-15 |
| **Configuration** | ~80 | LOW | MEDIUM | 🟡 MEDIUM | 8-10 |
| **Domain Layer** | 0 | NONE | FUTURE | 🔵 LOW | 20-30 (future) |

---

## Recommended Test Additions

### Immediate Priority (Add First)

**1. MessageBroker Integration Tests (15 tests, ~1 hour)**
- File: `server/tests/integration/nats/test_message_broker_integration.py`
- Focus: Connection lifecycle, message pub/sub, error recovery
- Impact: HIGH (critical for real-time features)

**2. ApplicationContainer Lifecycle Tests (10 tests, ~1 hour)**
- File: `server/tests/integration/infrastructure/test_container_lifecycle.py`
- Focus: Initialization order, shutdown cleanup, failure recovery
- Impact: HIGH (affects entire application)

**3. Database Migration Tests (10 tests, ~1.5 hours)**
- File: `server/tests/integration/infrastructure/test_database_migrations.py`
- Focus: Schema evolution, data migration, rollback
- Impact: HIGH (data integrity)

**Total: 35 tests, ~3.5 hours effort, closes critical gaps**

### Secondary Priority (Add Second)

**4. WebSocket Edge Case Tests (15 tests, ~2 hours)**
- File: `server/tests/integration/realtime/test_websocket_edge_cases.py`
- Focus: Connection failures, timeouts, concurrent connections
- Impact: MEDIUM-HIGH (user experience)

**5. Error Recovery Tests (20 tests, ~3 hours)**
- File: `server/tests/integration/comprehensive/test_error_recovery.py`
- Focus: Service failures, fallback behavior, graceful degradation
- Impact: MEDIUM (reliability)

**Total: 35 tests, ~5 hours effort, improves reliability**

---

## Net Impact Summary

### If We Execute Full Recommendations:

**Removals:**
- ~320 low-value tests removed (conservative)
- ~5 minutes time saved

**Additions:**
- ~70 high-value tests added (critical gaps)
- ~2 minutes time added

**Net Result:**
- -250 tests total (-5% suite size)
- -3 minutes total (10% faster)
- +15% critical coverage quality
- Improved signal-to-noise ratio
- Better focused test failures

---

*"The goal is not comprehensive coverage of all code, but comprehensive protection of all user value."*
