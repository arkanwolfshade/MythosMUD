# Architecture Decision Records Template

This template should be used for creating the 4 required ADRs during implementation of @.agent-os/specs/2025-10-10-critical-architecture-fixes/spec.md

## ADR Template Format

Each ADR should be created in `docs/architecture/decisions/` with the naming pattern: `ADR-XXX-title.md`

---

## ADR-001: XState Selection for Frontend Connection FSM

**Status:** Proposed

**Context:**

The frontend connection management in `useGameConnection.ts` has grown to 750+ lines with complex state management using multiple refs, manual timer management, and potential race conditions. We need a robust solution for managing connection states, transitions, timeouts, and reconnection logic.

**Decision:**

Adopt XState 4.x as the state machine library for frontend connection management.

**Considered Alternatives:**

1. **XState** (Selected)
   - Pros: Industry standard, TypeScript support, visualization tools, testing utilities
   - Cons: 50KB bundle size, learning curve

2. **Robot**
   - Pros: Lightweight (2KB), simple API
   - Cons: Limited features, no visualization, smaller community

3. **Custom FSM**
   - Pros: No dependencies, full control
   - Cons: Maintenance burden, no tooling, reinventing the wheel

4. **Enhanced useReducer**
   - Pros: No new dependencies, familiar pattern
   - Cons: Still manual timer management, no visualization, prone to bugs

**Rationale:**

- Bundle size (50KB) is acceptable for reliability gains
- TypeScript support prevents state machine bugs
- Visualization tools (@xstate/inspect) enable rapid debugging
- Testing utilities make connection scenarios testable
- Industry adoption means good documentation and community support

**Consequences:**

- Positive: Eliminates race conditions, provides clear state visualization, simplifies testing
- Negative: Team must learn XState patterns, slight bundle size increase
- Neutral: Requires refactoring existing connection logic

**Implementation Notes:**

- Use XState context for connection metadata (session_id, attempt counts)
- Use delayed transitions for timeouts instead of manual timers
- Use guards for connection availability checks
- Enable XState inspector in development mode only

---

## ADR-002: python-statemachine Selection for Backend FSM

**Status:** Proposed

**Context:**

Backend connection management (NATS, WebSocket health, circuit breakers) requires state tracking with async support. Need a Python state machine library compatible with FastAPI async patterns.

**Decision:**

Adopt python-statemachine 2.x for backend state management.

**Considered Alternatives:**

1. **python-statemachine** (Selected)
   - Pros: Native async/await, excellent type hints, Pythonic API, clean syntax
   - Cons: Smaller community than transitions

2. **transitions**
   - Pros: More mature, larger community, better visualization
   - Cons: More verbose API, less type-safe, async support as addon

**Rationale:**

- Native async/await aligns with FastAPI patterns
- Type hints integrate well with existing Pydantic models
- Cleaner, more maintainable code
- Easier to test with pytest
- Better fit for modern Python codebase

**Consequences:**

- Positive: Clean async state management, better type safety
- Negative: Smaller community means fewer examples
- Neutral: New dependency to maintain

---

## ADR-003: Pydantic BaseSettings for Configuration Management

**Status:** Proposed

**Context:**

Current configuration system (`config_loader.py`) has 395 lines with hardcoded defaults, mixed YAML/environment loading, and no validation. This creates security risks, deployment issues, and testing challenges.

**Decision:**

Refactor configuration to use Pydantic BaseSettings with explicit validation and no security-sensitive defaults.

**Considered Alternatives:**

1. **Pydantic BaseSettings** (Selected)
   - Pros: Type-safe, validation built-in, environment variable support, no hardcoded secrets
   - Cons: Breaking change, requires all configs to be explicit

2. **dynaconf**
   - Pros: Supports multiple config sources, validation, secrets management
   - Cons: Another dependency, more complex than needed

3. **Refactor existing config_loader**
   - Pros: No breaking changes
   - Cons: Doesn't solve validation or security issues

**Rationale:**

- Pydantic already used throughout project for validation
- Type safety catches configuration errors at startup
- Explicit validation with clear error messages
- No security-sensitive defaults prevents accidental exposure
- Environment-specific configs prevent drift

**Consequences:**

- **Breaking Change:** YAML configs no longer supported, must use `.env` files
- Positive: Configuration errors caught at startup, type-safe config access
- Negative: Deployment scripts must be updated
- Neutral: All environments must have explicit configuration

**Migration Strategy:**

1. Create new `server/config/` module with Pydantic models
2. Update all import references
3. Create `.env` templates for each environment
4. Remove `config_loader.py` after validation
5. Update deployment documentation

---

## ADR-004: Circuit Breaker + Dead Letter Queue for NATS

**Status:** Proposed

**Context:**

NATS message handler currently catches all exceptions but only logs them, leading to silent message loss. No retry mechanism, no visibility into failures, no protection against cascading failures.

**Decision:**

Implement three-layer error boundary: Retry with exponential backoff → Circuit Breaker → Dead Letter Queue.

**Considered Alternatives:**

1. **Circuit Breaker + DLQ + Retry** (Selected)
   - Pros: Comprehensive error handling, prevents cascading failures, preserves failed messages
   - Cons: Added complexity, requires monitoring

2. **Retry Only**
   - Pros: Simple, handles transient failures
   - Cons: No protection against persistent failures, can overwhelm failing systems

3. **Circuit Breaker Only**
   - Pros: Protects against cascading failures
   - Cons: No message preservation, no retry for transient failures

4. **Logging Only** (Current)
   - Pros: Simple
   - Cons: Silent message loss, no recovery

**Rationale:**

- **Retry Logic:** Handles transient network issues (80% of failures)
- **Circuit Breaker:** Protects server from cascading NATS failures
- **Dead Letter Queue:** Preserves messages for forensics and manual recovery
- **Three layers** provide defense in depth

**Implementation Details:**

```
Message Flow:
  1. Process message through circuit breaker
  2. If circuit CLOSED or HALF_OPEN:
     a. Attempt processing with retry (max 3 attempts, exponential backoff)
     b. On success: record success, continue
     c. On all retries failed: add to DLQ, record failure
  3. If circuit OPEN:
     a. Reject immediately
     b. Add to DLQ
     c. Log circuit open state
```

**Circuit Breaker Thresholds:**

- Failure threshold: 5 consecutive failures → OPEN
- Timeout: 60 seconds in OPEN before attempting HALF_OPEN
- Success threshold: 2 consecutive successes in HALF_OPEN → CLOSED

**Retry Configuration:**

- Max attempts: 3
- Base delay: 1 second
- Max delay: 30 seconds
- Exponential base: 2.0

**Consequences:**

- Positive: No message loss, visibility into failures, protection against cascading failures
- Negative: Added latency (~10-20ms per message), DLQ requires monitoring
- Neutral: Requires metrics endpoint for observability

**Monitoring:**

- Track messages in DLQ (alert if >100)
- Track circuit breaker state changes (alert if OPEN >5 minutes)
- Track retry success rate
- Track average processing latency

---

## ADR Template for Future Use

```markdown
# ADR-XXX: [Title]

**Status:** [Proposed | Accepted | Deprecated | Superseded]

**Date:** YYYY-MM-DD

**Context:**

[Describe the problem and context requiring a decision]

**Decision:**

[State the architectural decision that was made]

**Considered Alternatives:**

1. **Option A** (Selected/Not Selected)
   - Pros: [list]
   - Cons: [list]

2. **Option B**
   - Pros: [list]
   - Cons: [list]

**Rationale:**

[Explain why this decision was made, including trade-offs considered]

**Consequences:**

- Positive: [beneficial outcomes]
- Negative: [drawbacks or costs]
- Neutral: [impacts that are neither positive nor negative]

**Implementation Notes:**

[Key implementation details, if applicable]

**Related ADRs:**

- [Links to related decisions]
```

---

## ADR Placement

All ADRs should be created in: `docs/architecture/decisions/`

Create the directory if it doesn't exist:

```bash
mkdir -p docs/architecture/decisions
```

**Naming Convention:**

- `ADR-001-xstate-frontend-fsm.md`
- `ADR-002-python-statemachine-backend.md`
- `ADR-003-pydantic-configuration.md`
- `ADR-004-circuit-breaker-dlq-nats.md`

**Index File:**

Create `docs/architecture/decisions/README.md` listing all ADRs chronologically with status and date.
