# ADR-011: XState for Frontend Connection State Machine

**Version 1.1.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Date**: 2025-10-11
**Status**: Accepted
**Provenance:** Recorded by the 2026-08 design/implementation audit. This document states 2025-10-11 but
first appears in this repository on 2026-02-26; its Context line notes it was **recovered from `.agent-os`**,
so the stated date is most likely the original decision date under earlier tooling and the later date is when
the record was transcribed here. Its section structure differs from ADR-001–010, consistent with that
separate origin. Unlike much of this ADR set, this one may well be a genuine contemporaneous decision record.
**Decision Makers**: Prof. Wolfshade, AI Assistant
**Context**: CRITICAL-1 Connection State Machine Implementation (recovered from .agent-os)

---

## 2. Context and Problem Statement

**[SPEC]**
The frontend connection management in `useGameConnection.ts` had grown to 750+ lines with complex manual state tracking using multiple refs and timers. This led to:

1. **Implicit State Bugs**: Impossible states like "connected but also connecting"
2. **Manual Timer Management**: Complex timeout handling prone to memory leaks
3. **Difficult Testing**: No way to verify state transitions systematically
4. **Poor Visibility**: No clear view of current connection state or transition history

**Question**: What state management library should we use for robust frontend connection handling?

---

## 3. Decision Drivers

**[SPEC]**
**Type Safety**: Must provide TypeScript support and type-safe state definitions

**Testability**: Must enable comprehensive unit testing of state transitions

**Visualization**: Should support visual debugging of state machines

- **React Integration**: Must integrate cleanly with React hooks
- **Bundle Size**: Should be reasonable (<100KB added to bundle)
- **Maintainability**: Must be actively maintained with good documentation

---

## 4. Considered Options

**[SPEC]**

### Option 1: XState

**Pros**:

- Industry-standard FSM library (used by Microsoft, Amazon, etc.)
- Excellent TypeScript support
- Visual debugging with XState Inspector
- Comprehensive testing utilities
- Official React integration (`@xstate/react`)
- Extensive documentation and community
- **Cons**:
  - ~50KB bundle size impact
  - Learning curve for team members unfamiliar with FSMs
  - V4 to V5 migration happening (but V5 is stable)
- **Bundle Impact**: ~50KB

### Option 2: Manual State Machine

**Pros**:

- Zero bundle size impact
- Complete control over implementation
- No external dependencies
- **Cons**:
  - Must implement all FSM logic manually
  - No visual debugging tools
  - Higher maintenance burden
  - No type-safe state transitions
  - Requires custom testing utilities
- **Bundle Impact**: 0KB

### Option 3: Robot (State Machine Library)

**Pros**:

- Lightweight (~5KB)
- Simple API
- Functional approach
- **Cons**:
  - Limited TypeScript support
  - No visual debugging
  - Smaller community
  - Less mature than XState
- **Bundle Impact**: ~5KB

---

## 5. Decision Outcome

**[SPEC]**
**Chosen Option**: **XState v5** with @xstate/react integration

**Rationale**:

1. **Type Safety**: XState provides excellent TypeScript support with typed states, events, and context
2. **Testing**: Built-in testing utilities make state transitions easy to verify
3. **Debugging**: XState Inspector provides visual debugging - invaluable for complex connection flows
4. **Maturity**: Industry-proven library with extensive real-world usage
5. **React Integration**: `@xstate/react` provides idiomatic React hooks
6. **Documentation**: Comprehensive documentation and active community
7. **Bundle Size**: 50KB is acceptable given the benefits

**Trade-offs Accepted**:

- 50KB bundle increase (acceptable for improved reliability and developer experience)
- Learning curve for team (offset by better long-term maintainability)

---

## 6. Implementation Details

**[NOTE]**

### State Machine Definition

```typescript
export const connectionMachine = setup({
  types: {
    context: {} as ConnectionContext,
    events: {} as ConnectionEvent,
  },
  // ... actions, guards, delays
}).createMachine({
  id: "connection",
  initial: "disconnected",
  states: {
    disconnected: {
      /* ... */
    },
    connecting_sse: {
      /* ... */
    },
    sse_connected: {
      /* ... */
    },
    connecting_ws: {
      /* ... */
    },
    fully_connected: {
      /* ... */
    },
    reconnecting: {
      /* ... */
    },
    failed: {
      /* ... */
    },
  },
});
```

### React Hook Wrapper

```typescript
export function useConnectionState(options?: {
  maxReconnectAttempts?: number;
  onStateChange?: (state: string) => void;
}): UseConnectionStateResult {
  const [state, send] = useMachine(connectionMachine, {
    context: {
      /* ... */
    },
  });

  // ... returns type-safe state checks and actions
}
```

---

## 7. Consequences

**[SPEC]**

### Positive

- **Eliminated Implicit State Bugs**: Impossible states are now prevented by the FSM
- **Improved Testability**: the state machine is covered by unit tests verifying its transitions
- **Visual Debugging**: XState Inspector provides real-time state visualization
- **Type Safety**: TypeScript catches invalid state transitions at compile time
- **Maintainability**: Clear, explicit state machine logic replaces 750 lines of ad-hoc state management
- **Automatic Recovery**: Built-in reconnection with exponential backoff

### Negative

- **Bundle Size**: +50KB to production bundle (acceptable trade-off)
- **Learning Curve**: Team needs to understand FSM concepts (mitigated by good documentation)
- **Dependency**: Adds external dependency (but mature and well-maintained)

### Neutral

- **Migration Effort**: Requires refactoring `useGameConnection.ts` (planned work)
- **Version 5**: Using XState v5 (latest stable) - may have fewer Stack Overflow answers than v4

---

## 8. Validation

**[SPEC]**

- All 13 frontend state machine tests passing
- No TypeScript compilation errors
- No linting errors
- Bundle size increase within acceptable limits (<100KB)
- React 19 compatibility verified (with --legacy-peer-deps)

---

## 9. References

**[SPEC]**

- [XState Documentation](https://xstate.js.org/)
- [XState Inspector](https://stately.ai/docs/inspector)
- [Martin Fowler on State Machines](https://martinfowler.com/articles/state-machine.html)
- Implementation: `client/src/hooks/useConnectionStateMachine.ts`
- Tests: `client/src/hooks/useConnectionStateMachine.test.ts`

---

## 10. Related ADRs

**[SPEC]**

- [ADR-012](ADR-012-python-statemachine-backend.md): python-statemachine for Backend Connection FSM
- [ADR-013](ADR-013-pydantic-configuration.md): Pydantic Configuration Management
- [ADR-014](ADR-014-nats-error-boundaries.md): Circuit Breaker + Dead Letter Queue for NATS

## 11. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-19 | Provenance note; remove hard-coded test count |
