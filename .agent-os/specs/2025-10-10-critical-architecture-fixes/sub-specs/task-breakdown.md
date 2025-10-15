# Task Breakdown

This is the task breakdown for the spec detailed in @.agent-os/specs/2025-10-10-critical-architecture-fixes/spec.md

## Sprint 1: Backend Critical Fixes (Week 1)

### Day 1-2: CRITICAL-2 Configuration Refactoring

**Tasks:**

1. **Create Pydantic Configuration Models** (4 hours)
   - Create `server/config/models.py` with all configuration classes
   - Define validators for port ranges, environment values, file paths
   - Add type hints and docstrings
   - **Acceptance:** All configuration fields have Pydantic models with validation

2. **Create Configuration Module** (2 hours)
   - Create `server/config/__init__.py` with `get_config()` singleton
   - Use `@lru_cache()` for configuration caching
   - **Acceptance:** Configuration accessible via `get_config()` function

3. **Update Environment Files** (2 hours)
   - Update `.env.local.example` with all required fields
   - Update `.env.unit_test.example`
   - Update `.env.e2e_test.example`
   - Create `.env.production.example` template
   - **Acceptance:** All environment files have required configuration fields

4. **Update Import References** (3 hours)
   - Find all imports of `server.config_loader`
   - Replace with `server.config`
   - Update configuration access patterns (e.g., `config["host"]` → `config.server.host`)
   - **Acceptance:** All configuration access uses new models

5. **Write Configuration Tests** (3 hours)
   - Unit tests for each configuration model validator
   - Negative tests for invalid values
   - Integration test for configuration loading
   - Test environment-specific configuration
   - **Acceptance:** Tests achieve ≥80% coverage, all passing

6. **Remove Legacy Configuration** (1 hour)
   - Delete `server/config_loader.py`
   - Delete YAML config files (if any)
   - Update `.gitignore` for new `.env` pattern
   - **Acceptance:** Legacy configuration removed, git clean

7. **Update Deployment Documentation** (1 hour)
   - Document new `.env` requirements
   - Create deployment checklist
   - Document configuration validation errors
   - **Acceptance:** Deployment docs updated

**Day 1-2 Deliverables:**

- ✅ Configuration refactoring complete
- ✅ Tests passing with ≥80% coverage
- ✅ Documentation updated

---

### Day 2-3: CRITICAL-3 Command Security Hardening

**Tasks:**

1. **Implement Alias Graph** (4 hours)
   - Create `server/utils/alias_graph.py`
   - Implement graph construction from aliases
   - Implement cycle detection using networkx DFS
   - Add method to identify cycle path
   - **Acceptance:** Alias graph detects circular dependencies

2. **Implement Command Rate Limiter** (3 hours)
   - Create `server/middleware/rate_limiter.py`
   - Implement sliding window algorithm
   - Add per-player tracking
   - Add cleanup for old timestamps
   - **Acceptance:** Rate limiter enforces 10 commands/second limit

3. **Implement Command Validator** (2 hours)
   - Create `server/validators/command_validator.py`
   - Add dangerous pattern detection
   - Add null byte checking
   - Add length validation
   - **Acceptance:** Validator blocks dangerous patterns

4. **Implement Audit Logger** (2 hours)
   - Create `server/utils/audit_logger.py`
   - Add structured logging for security commands
   - Create audit log file handler
   - Add IP address tracking
   - **Acceptance:** Security-sensitive commands logged to audit.log

5. **Integrate with Command Handler** (3 hours)
   - Update `server/command_handler_unified.py`
   - Add rate limit check at entry point
   - Add alias cycle detection before expansion
   - Add command validation before execution
   - Add audit logging for admin commands
   - **Acceptance:** All security checks integrated

6. **Write Security Tests** (4 hours)
   - Unit tests for alias cycle detection (10+ test cases)
   - Unit tests for rate limiter edge cases
   - Unit tests for command validator patterns
   - Integration tests for command rejection
   - Security tests for bypass attempts
   - **Acceptance:** Tests achieve ≥90% coverage, all passing

7. **Security Audit** (2 hours)
   - Manual testing of alias bomb scenarios
   - Attempt command injection patterns
   - Verify audit log entries
   - Review error messages for information leakage
   - **Acceptance:** Security audit passed

**Day 2-3 Deliverables:**

- ✅ Command security hardening complete
- ✅ Security tests passing with ≥90% coverage
- ✅ Security audit passed

---

### Day 3-5: CRITICAL-4 NATS Error Boundaries

**Tasks:**

1. **Implement Retry Handler** (3 hours)
   - Create `server/realtime/nats_retry_handler.py`
   - Implement exponential backoff algorithm
   - Add configurable retry limits
   - Add async support
   - **Acceptance:** Retry handler works with async functions

2. **Implement Dead Letter Queue** (3 hours)
   - Create `server/realtime/dead_letter_queue.py`
   - Implement file-based storage
   - Add metadata tracking (timestamp, error, retry_count)
   - Add DLQ count method
   - Create DLQ directory structure
   - **Acceptance:** Failed messages stored in DLQ with metadata

3. **Implement Circuit Breaker** (4 hours)
   - Create `server/realtime/circuit_breaker.py`
   - Implement three states (CLOSED, OPEN, HALF_OPEN)
   - Add failure threshold tracking
   - Add timeout-based reset logic
   - Add success threshold for recovery
   - **Acceptance:** Circuit breaker transitions correctly

4. **Implement Metrics Collector** (2 hours)
   - Create `server/middleware/metrics_middleware.py`
   - Add counters for messages processed, failed, DLQ
   - Add circuit breaker state tracking
   - **Acceptance:** Metrics collector tracks all events

5. **Integrate with NATS Handler** (4 hours)
   - Update `server/realtime/nats_message_handler.py`
   - Add retry logic to message processing
   - Add circuit breaker wrapping
   - Add DLQ for failed messages
   - Update metrics on each event
   - **Acceptance:** NATS handler uses all error boundaries

6. **Add Metrics Endpoint** (2 hours)
   - Add `/api/metrics` endpoint to FastAPI
   - Return JSON metrics data
   - Add basic authentication (admin only)
   - **Acceptance:** Metrics endpoint returns current statistics

7. **Write Error Boundary Tests** (4 hours)
   - Unit tests for retry handler (3 retries, backoff timing)
   - Unit tests for DLQ operations
   - Unit tests for circuit breaker state transitions
   - Integration tests for end-to-end message delivery
   - Chaos tests for NATS failures
   - **Acceptance:** Tests achieve ≥80% coverage, all passing

8. **Integration Testing** (3 hours)
   - Test message delivery under network failures
   - Test DLQ accumulation and monitoring
   - Test circuit breaker recovery
   - Test metrics accuracy
   - **Acceptance:** All integration scenarios passing

**Day 3-5 Deliverables:**

- ✅ NATS error boundaries complete
- ✅ Tests passing with ≥80% coverage
- ✅ Metrics endpoint functional

---

### Sprint 1 Final Tasks

**Day 5: Sprint 1 Integration & Deployment** (8 hours)

1. **Run Full Test Suite** (1 hour)
   - Run `make test` from project root
   - Verify all tests pass
   - Verify coverage ≥80%
   - Fix any regressions

2. **Code Quality** (1 hour)
   - Run `make lint`
   - Fix all linting errors
   - Run formatting checks

3. **Update Documentation** (2 hours)
   - Write 4 ADRs (one per critical finding)
   - Update deployment documentation
   - Update developer documentation

4. **Staging Deployment** (2 hours)
   - Deploy to staging environment
   - Verify configuration validation
   - Test security hardening
   - Monitor NATS metrics

5. **Production Deployment** (2 hours)
   - Deploy backend to production
   - Monitor error rates
   - Verify metrics endpoint
   - Create rollback plan document

**Sprint 1 Exit Criteria:**

- All Sprint 1 tests passing
- ≥80% code coverage achieved
- Staging deployment successful
- Production deployment successful (backend only)
- Zero critical bugs detected
- Documentation complete

---

## Sprint 2: Frontend Connection FSM (Week 2)

### Day 1-2: XState Integration

**Tasks:**

1. **Install XState Dependencies** (0.5 hours)
   - `npm install xstate@^4.38.0 @xstate/react@^3.2.0`
   - Update `package.json`
   - **Acceptance:** Dependencies installed

2. **Create Connection State Machine** (4 hours)
   - Create `client/src/hooks/useConnectionStateMachine.ts`
   - Define connection states (disconnected, connecting_sse, sse_connected, connecting_ws, fully_connected, reconnecting, failed)
   - Define state transitions with guards
   - Define timeout transitions (30s connection, 5s reconnect)
   - Add XState context for metadata
   - **Acceptance:** State machine definition complete with TypeScript types

3. **Extract WebSocket Logic** (3 hours)
   - Create `client/src/hooks/useWebSocketConnection.ts`
   - Move WebSocket-specific logic from `useGameConnection.ts`
   - Integrate with state machine
   - **Acceptance:** WebSocket logic extracted and functional

4. **Extract SSE Logic** (3 hours)
   - Create `client/src/hooks/useSSEConnection.ts`
   - Move SSE-specific logic from `useGameConnection.ts`
   - Integrate with state machine
   - **Acceptance:** SSE logic extracted and functional

5. **Extract Health Monitoring** (2 hours)
   - Create `client/src/hooks/useConnectionHealth.ts`
   - Move health check logic
   - Integrate with state machine
   - **Acceptance:** Health monitoring extracted and functional

6. **Extract Session Management** (2 hours)
   - Create `client/src/hooks/useSessionManagement.ts`
   - Move session ID logic
   - Integrate with state machine
   - **Acceptance:** Session management extracted and functional

7. **Refactor Main Hook** (3 hours)
   - Update `client/src/hooks/useGameConnection.ts` to orchestrate sub-hooks
   - Replace reducer with XState machine
   - Replace refs with XState context
   - Remove manual timer management
   - **Acceptance:** Main hook simplified to <200 lines

**Day 1-2 Deliverables:**

- ✅ XState integration complete
- ✅ Hooks refactored and modular
- ✅ State machine functional

---

### Day 3-4: Connection UI & Testing

**Tasks:**

1. **Add Connection Status Indicators** (2 hours)
   - Create visual indicator component for connection states
   - Show "Connecting...", "Connected", "Reconnecting...", "Failed" states
   - Add color coding (green/yellow/red)
   - **Acceptance:** Visual indicators match state machine states

2. **Configure XState Inspector** (1 hour)
   - Add `@xstate/inspect` for development
   - Configure to run only in dev mode
   - Add documentation for debugging with inspector
   - **Acceptance:** Inspector functional in development

3. **Write Frontend Unit Tests** (6 hours)
   - Unit tests for state machine transitions (all states)
   - Unit tests for each extracted hook
   - Unit tests for timeout guards
   - Unit tests for error handling
   - Mock WebSocket and EventSource
   - **Acceptance:** Tests achieve ≥85% coverage, all passing

4. **Write Integration Tests** (4 hours)
   - Integration tests for connection establishment
   - Integration tests for connection recovery
   - Integration tests for session management
   - Integration tests for health monitoring
   - **Acceptance:** Integration tests passing

5. **Write E2E Connection Tests** (3 hours)
   - E2E test for initial connection
   - E2E test for network interruption recovery
   - E2E test for WebSocket fallback to SSE
   - E2E test for session persistence
   - **Acceptance:** E2E tests passing in Playwright

**Day 3-4 Deliverables:**

- ✅ Connection UI complete
- ✅ Frontend tests passing with ≥85% coverage
- ✅ E2E tests passing

---

### Day 4-5: Backend State Machine Integration

**Tasks:**

1. **Install python-statemachine** (0.5 hours)
   - Add to `pyproject.toml` dependencies
   - Run `uv pip install python-statemachine==2.1.*`
   - **Acceptance:** Dependency installed

2. **Create NATS Connection FSM** (3 hours)
   - Create `server/realtime/connection_state_machine.py`
   - Define states for NATS connection
   - Add async transition handlers
   - Integrate with NATS service
   - **Acceptance:** NATS connection managed by FSM

3. **Integrate Circuit Breaker with FSM** (2 hours)
   - Update `server/realtime/circuit_breaker.py` to use FSM
   - Map circuit states to FSM states
   - **Acceptance:** Circuit breaker states managed by FSM

4. **Write Backend State Machine Tests** (3 hours)
   - Unit tests for FSM state transitions
   - Unit tests for NATS connection lifecycle
   - Integration tests with NATS service
   - **Acceptance:** Tests achieve ≥80% coverage, all passing

**Day 4-5 Deliverables:**

- ✅ Backend state machine complete
- ✅ Tests passing with ≥80% coverage

---

### Sprint 2 Final Tasks

**Day 5: Sprint 2 Integration & Deployment** (8 hours)

1. **Run Full Test Suite** (1 hour)
   - Run backend tests: `make test-server`
   - Run frontend tests: `cd client && npm test`
   - Run E2E tests
   - Verify all tests pass
   - Verify coverage ≥80%

2. **Code Quality** (1 hour)
   - Run `make lint`
   - Fix all linting errors
   - Run frontend ESLint

3. **Cross-Browser Testing** (2 hours)
   - Test in Chrome, Firefox, Safari
   - Test connection recovery in each browser
   - Verify state machine transitions

4. **Write ADRs** (2 hours)
   - ADR-001: XState Selection for Frontend FSM
   - ADR-002: python-statemachine Selection for Backend
   - ADR-003: Connection State Design
   - ADR-004: Error Boundary Strategy

5. **Final Documentation** (1 hour)
   - Update developer documentation
   - Create XState debugging guide
   - Document state machine visualization

6. **Staging Deployment** (0.5 hours)
   - Deploy full stack to staging
   - Run smoke tests
   - Verify metrics

7. **Production Deployment** (0.5 hours)
   - Deploy to production
   - Monitor connection metrics
   - Monitor error rates
   - Verify no critical issues

**Sprint 2 Exit Criteria:**

- All tests passing (unit + integration + E2E)
- ≥80% code coverage for all new code
- Linting passes with no errors
- Production deployment successful
- Zero critical bugs in production
- All documentation complete
- ADRs written and committed

---

## Effort Estimates

### Sprint 1 (Backend Focus)

| Task Category             | Estimated Hours | Priority |
| ------------------------- | --------------- | -------- |
| Configuration Refactoring | 16              | P0       |
| Command Security          | 18              | P0       |
| NATS Error Boundaries     | 25              | P0       |
| Integration & Deployment  | 8               | P0       |
| **Total Sprint 1**        | **67 hours**    |          |

**Note:** 67 hours over 5 business days = ~13.5 hours/day (aggressive for solo developer)

**Adjustment Recommendation:** Focus on completing CRITICAL-2 and CRITICAL-3 fully, with CRITICAL-4 carried over if time runs short.

### Sprint 2 (Frontend Focus)

| Task Category            | Estimated Hours | Priority |
| ------------------------ | --------------- | -------- |
| XState Integration       | 17.5            | P0       |
| Connection UI & Testing  | 16              | P0       |
| Backend State Machine    | 8.5             | P1       |
| Integration & Deployment | 8               | P0       |
| **Total Sprint 2**       | **50 hours**    |          |

**Note:** 50 hours over 5 business days = ~10 hours/day (more sustainable)

---

## Risk Mitigation

### High-Risk Areas

1. **Risk:** XState learning curve delays frontend work
   - **Mitigation:** Complete XState tutorial before Sprint 2, allocate buffer time
   - **Contingency:** Simplify state machine to essential states only

2. **Risk:** Breaking changes cause widespread test failures
   - **Mitigation:** Update tests incrementally, run regression suite frequently
   - **Contingency:** Feature flag new configuration system during transition

3. **Risk:** Solo developer burnout with aggressive timeline
   - **Mitigation:** Prioritize CRITICAL-3 (security) and CRITICAL-1 (UX), defer CRITICAL-4 if needed
   - **Contingency:** Extend to 3-sprint timeline

4. **Risk:** Production issues after deployment
   - **Mitigation:** Incremental deployment, extensive staging testing, rollback plan ready
   - **Contingency:** Immediate rollback to previous version

---

## Testing Strategy

### Test Pyramid

**Unit Tests (60%):**

- Configuration model validation
- Alias cycle detection
- Rate limiter logic
- Command validator patterns
- Circuit breaker state transitions
- Retry logic
- State machine transitions

**Integration Tests (30%):**

- Configuration loading from environment
- Command processing with security checks
- Message delivery with retries
- Connection lifecycle with state machine
- End-to-end alias expansion

**E2E Tests (10%):**

- Full connection recovery scenarios
- Multi-player connection scenarios
- Real-time message delivery
- Security rejection scenarios

### Test Execution

**Per Commit:**

- Run unit tests for changed files
- Run linting

**Pre-Merge:**

- Run full test suite
- Verify coverage targets
- Run security tests

**Pre-Deployment:**

- Run full test suite
- Run E2E tests
- Run load tests
- Manual security audit

---

## Deployment Strategy

### Incremental Deployment Phases

**Phase 1: Configuration (Day 2-3)**

- Deploy configuration refactoring to staging
- Validate all environments load correctly
- If stable, deploy to production backend
- Monitor for configuration errors

**Phase 2: Command Security (Day 3-4)**

- Deploy command security hardening to staging
- Test alias bomb protection
- If stable, deploy to production backend
- Monitor audit logs and error rates

**Phase 3: NATS Error Boundaries (Day 4-5)**

- Deploy NATS improvements to staging
- Monitor message delivery metrics
- If stable, deploy to production backend
- Monitor DLQ and circuit breaker states

**Phase 4: Frontend FSM (Day 8-9)**

- Deploy frontend changes to staging
- Test connection recovery
- If stable, deploy to production
- Monitor connection metrics

**Phase 5: Backend FSM (Day 9-10)**

- Deploy backend state machine to staging
- Verify integration with frontend
- If stable, deploy to production
- Monitor full system metrics

### Rollback Procedures

Each phase has independent rollback:

- Git revert commits for specific phase
- Redeploy previous version
- No data migrations to reverse

---

## Success Criteria Summary

### Sprint 1 Success Criteria

✅ **Functionality:**

- Configuration loads from `.env` with validation
- Command injection attempts blocked
- Alias bombs detected and rejected
- Rate limiting enforces 10 cmd/sec limit
- NATS messages retry on transient failures
- Failed messages stored in DLQ
- Circuit breaker protects against NATS outages
- Metrics endpoint exposes delivery stats

✅ **Quality:**

- All backend tests passing
- Code coverage ≥80% (≥90% for security code)
- Linting passes
- No regression failures

✅ **Deployment:**

- Staging deployment successful
- Production backend deployment successful
- No critical bugs in production

### Sprint 2 Success Criteria

✅ **Functionality:**

- Connection state visualized in UI
- Connection recovery automatic (<5s)
- State machine prevents infinite loops
- Health monitoring accurate
- Session management persistent
- Frontend + backend state synchronized

✅ **Quality:**

- All frontend tests passing
- Code coverage ≥80% (≥85% for FSM)
- Linting passes (ESLint + Prettier)
- No regression failures
- E2E tests passing

✅ **Deployment:**

- Staging deployment successful
- Production full-stack deployment successful
- Connection metrics improved
- No critical bugs in production
- Zero infinite reconnection loops observed

✅ **Documentation:**

- 4 ADRs written
- Deployment docs updated
- Developer docs updated
- XState debugging guide created
