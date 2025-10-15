# ADR-002: python-statemachine for Backend Connection FSM

**Date**: 2025-10-11
**Status**: ✅ ACCEPTED
**Decision Makers**: Prof. Wolfshade, AI Assistant
**Context**: CRITICAL-1 Connection State Machine Implementation

---

## Context and Problem Statement

The backend NATS service had manual connection retry logic with implicit state tracking. This led to:

1. **Race Conditions**: Multiple reconnection attempts could run simultaneously
2. **Unclear State**: No explicit tracking of connection states (connecting, connected, degraded)
3. **No Circuit Breaker Integration**: Manual retry logic didn't integrate with circuit breaker pattern
4. **Difficult Testing**: No way to verify connection state transitions

**Question**: What state machine library should we use for backend NATS connection management?

---

## Decision Drivers

- **Python Native**: Must work well with Python's async/await
- **Async Support**: Must support asynchronous state transitions
- **Simplicity**: Should be easy to understand and maintain
- **Testing**: Must be testable with pytest
- **Documentation**: Should have clear documentation
- **Active Maintenance**: Should be actively maintained

---

## Considered Options

### Option 1: python-statemachine
- **Pros**:
  - Clean, Pythonic API
  - Built-in async support
  - Decorators for state transitions
  - Good documentation
  - Active maintenance (last release recent)
  - pytest compatible
- **Cons**:
  - Smaller community than transitions
  - Fewer Stack Overflow answers
- **Complexity**: Low to Medium

### Option 2: transitions
- **Pros**:
  - Larger community
  - More Stack Overflow answers
  - Extensive features (nested states, conditional transitions)
  - Well-established
- **Cons**:
  - Async support is addon/plugin
  - More complex API
  - Overkill for our use case
- **Complexity**: Medium to High

### Option 3: Manual Implementation
- **Pros**:
  - Zero dependencies
  - Complete control
- **Cons**:
  - Must implement all FSM logic
  - Error-prone
  - Higher maintenance burden
  - Reinventing the wheel
- **Complexity**: High

---

## Decision Outcome

**Chosen Option**: **python-statemachine v2.5.0**

**Rationale**:

1. **Clean API**: Declarative state definitions using class attributes
2. **Async Support**: Native async/await support without plugins
3. **Simplicity**: Straightforward API matches our needs perfectly
4. **Testing**: Works seamlessly with pytest
5. **Pythonic**: Feels natural to Python developers
6. **Sufficient Features**: Has everything we need without complexity overhead

**Trade-offs Accepted**:
- Smaller community than transitions (acceptable - library is stable and well-documented)
- Fewer examples available (offset by excellent official documentation)

---

## Implementation Details

### State Machine Definition

```python
class NATSConnectionStateMachine(StateMachine):
    # Define states
    disconnected = State("Disconnected", initial=True)
    connecting = State("Connecting")
    connected = State("Connected")
    reconnecting = State("Reconnecting")
    circuit_open = State("Circuit Open")
    degraded = State("Degraded")

    # Define transitions
    connect = disconnected.to(connecting)
    connected_successfully = connecting.to(connected) | reconnecting.to(connected)
    connection_failed = connecting.to(disconnected) | reconnecting.to(disconnected)
    # ... etc
```

### Integration with NATS Service

```python
class NATSService:
    def __init__(self, config):
        self.state_machine = NATSConnectionStateMachine(
            connection_id="nats-primary",
            max_reconnect_attempts=5
        )

    async def connect(self):
        if not self.state_machine.can_attempt_connection():
            return False

        self.state_machine.connect()
        # ... actual connection logic
        self.state_machine.connected_successfully()
```

---

## Consequences

### Positive

✅ **Explicit State Tracking**: All connection states are explicit and tracked
✅ **Prevents Race Conditions**: FSM ensures only one connection attempt at a time
✅ **Circuit Breaker Integration**: State machine provides hooks for circuit breaker
✅ **Testability**: 24 comprehensive tests verify all state transitions
✅ **Type Safety**: Python type hints ensure correct state usage
✅ **Monitoring**: `get_stats()` method provides connection metrics

### Negative

⚠️ **Dependency**: Adds external dependency (but lightweight and stable)
⚠️ **Learning Curve**: Team needs to understand FSM concepts

### Neutral

ℹ️ **Async Overhead**: Minimal async overhead for state transitions (negligible)
ℹ️ **Documentation**: Requires documenting state machine for team

---

## Validation

- ✅ All 24 backend state machine tests passing
- ✅ No import errors
- ✅ No linting errors
- ✅ Successfully integrated with NATS service
- ✅ State transitions logged for debugging
- ✅ Circuit breaker integration working

---

## References

- [python-statemachine Documentation](https://python-statemachine.readthedocs.io/)
- [python-statemachine GitHub](https://github.com/fgmacedo/python-statemachine)
- Implementation: `server/realtime/connection_state_machine.py`
- Integration: `server/services/nats_service.py`
- Tests: `server/tests/test_connection_state_machine.py`

---

## Related ADRs

- ADR-001: XState for Frontend Connection FSM
- ADR-003: Pydantic Configuration Management
- ADR-004: Circuit Breaker + Dead Letter Queue for NATS
