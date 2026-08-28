# ADR-014: Circuit Breaker + Dead Letter Queue for NATS Error Boundaries

**Version 1.1.0** · MythosMUD · 2026-08-28

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
**Context**: CRITICAL-4 NATS Error Boundaries Implementation (recovered from .agent-os)

---

## 2. Context and Problem Statement

**[SPEC]**
The NATS message handler had broad exception catching without recovery mechanisms:

1. **No Retry Logic**: Transient failures caused permanent message loss
2. **No Circuit Breaker**: System continued attempting operations during outages
3. **No Dead Letter Queue**: Failed messages were lost completely
4. **No Metrics**: No visibility into message delivery failures
5. **Cascading Failures**: NATS issues could overwhelm the entire system

**Question**: How should we implement resilient message delivery with failure recovery?

---

## 3. Decision Drivers

**[SPEC]**
**Message Reliability**: Must prevent message loss

**Resilience**: Must handle transient and persistent failures gracefully

**Observability**: Must provide visibility into failure patterns

- **Performance**: Must not significantly impact message delivery performance
- **Simplicity**: Should be understandable and maintainable
- **Infrastructure Requirements**: Must work without additional infrastructure

---

## 4. Considered Options

**[SPEC]**

### Option 1: Circuit Breaker + DLQ + Retry (Custom Implementation)

**Pros**:

- Tailored to our exact needs
- No external dependencies
- Full control over behavior
- File-based DLQ (no additional infrastructure)
- **Cons**:
  - Must implement all patterns ourselves
  - Higher maintenance burden
  - More potential for bugs
- **Complexity**: High
- **Infrastructure**: None required

### Option 2: resilience4j + External Message Queue

**Pros**:

- Battle-tested patterns
- Comprehensive features
- Large community
- **Cons**:
  - JVM-based (not Python native)
  - Requires external message queue (RabbitMQ, etc.)
  - Significant infrastructure overhead
  - Overkill for our needs
- **Complexity**: Very High
- **Infrastructure**: RabbitMQ/Kafka required

### Option 3: Python retry libraries (tenacity, backoff)

**Pros**:

- Simple retry logic
- Exponential backoff built-in
- Mature libraries
- **Cons**:
  - No circuit breaker
  - No DLQ
  - No metrics
  - Would need to add other components separately
- **Complexity**: Low (but incomplete)
- **Infrastructure**: None

---

## 5. Decision Outcome

**[SPEC]**
**Chosen Option**: **Custom Circuit Breaker + DLQ + Retry Implementation**

**Rationale**:

1. **Zero Infrastructure**: File-based DLQ requires no additional services
2. **Tailored Solution**: Exactly fits our needs without unnecessary complexity
3. **Full Control**: Can optimize for our specific use case
4. **Python Native**: Pure Python, async-native implementation
5. **Testability**: circuit breaker, DLQ and retry handler are each covered by unit tests
6. **Observability**: Built-in metrics collection
7. **Integration**: Seamlessly integrates with existing code

**Trade-offs Accepted**:

- Custom implementation maintenance (offset by comprehensive tests)
- No off-the-shelf solution (acceptable - our needs are specific)

---

## 6. Implementation Details

**[NOTE]**

### 1. Retry Handler with Exponential Backoff

```python
class NATSRetryHandler:
    async def retry_with_backoff(self, func, *args, **kwargs):
        for attempt in range(self.config.max_attempts):
            try:
                return True, await func(*args, **kwargs)
            except Exception as e:
                if attempt < self.config.max_attempts - 1:
                    delay = min(
                        self.config.base_delay * (2 ** attempt),
                        self.config.max_delay
                    )
                    await asyncio.sleep(delay)
        return False, last_error
```

**Defaults**: 3 attempts, 1s → 2s → 4s, max 30s

### 2. Circuit Breaker (Three-State FSM)

```python
class CircuitBreaker:
    # States: CLOSED (normal) → OPEN (failing) → HALF_OPEN (testing)
    # Opens after 5 failures
    # Resets after 60s timeout
    # Closes after 2 successful recoveries
```

**Thresholds**: 5 failures → OPEN, 60s timeout, 2 successes → CLOSED

### 3. Dead Letter Queue (File-Based)

```python
class DeadLetterQueue:
    # Stores failed messages as JSON files in logs/dlq/nats/
    # Automatic cleanup after 7 days
    # Statistics by error type
    # Admin API for retrieval/replay
```

**Storage**: `logs/dlq/nats/dlq_YYYYMMDD_HHMMSS_µs.json`

### 4. Metrics Collector (Thread-Safe)

```python
class MetricsCollector:
    # Per-channel message tracking
    # Processing time statistics
    # Circuit breaker state changes
    # Thread-safe concurrent updates
```

### 5. Integration

```python
class NATSMessageHandler:
    async def _handle_nats_message(self, message_data):
        try:
            # Circuit Breaker → Retry Handler → Processing → DLQ
            await self.circuit_breaker.call(
                self._process_message_with_retry, message_data
            )
        except CircuitBreakerOpen:
            # Add to DLQ immediately when circuit open
            await self.dead_letter_queue.enqueue(message_data, ...)
```

---

## 7. Consequences

**[SPEC]**

### Positive

- **Zero Message Loss**: DLQ ensures all messages are preserved
- **Resilient Delivery**: Retry logic handles transient failures
- **Cascade Prevention**: Circuit breaker prevents overwhelming failed services
- **Observability**: Comprehensive metrics for monitoring
- **Admin Control**: `/v1/metrics` endpoints for operational visibility
- **No Infrastructure**: File-based DLQ requires no additional services
- **Performance**: Minimal overhead (only on failures)

### Negative

- **File I/O**: DLQ writes to disk (acceptable - only on failures)
- **Manual Replay**: DLQ messages require manual replay or investigation
- **Disk Space**: DLQ could grow unbounded (mitigated by automatic cleanup)

### Neutral

- **Complexity**: Custom implementation requires maintenance (offset by tests)
- **Monitoring**: Requires monitoring DLQ growth (standard operational practice)

---

## 8. Validation

**[SPEC]**

- Retry handler, Dead Letter Queue, Circuit Breaker, and Metrics Collector each have passing test coverage
- No performance regression
- `/v1/metrics` endpoints functional

---

## 9. Operational Considerations

**[SPEC]**

### Monitoring

Monitor these metrics for health:

- `messages_in_dlq` - Should stay near zero
- `circuit_open_count` - Indicates service degradation
- `success_rate_percent` - Should stay >99%

### Alerting

Alert on:

- DLQ size > 100 messages
- Circuit breaker opens
- Success rate < 95%

### DLQ Management

- Automatic cleanup after 7 days (configurable)
- Admin endpoint: `GET /v1/metrics/dlq` for investigation
- Manual replay: `POST /v1/metrics/dlq/{id}/replay` (future enhancement)

---

## 10. References

**[SPEC]**

- [Martin Fowler - Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html)
- [AWS - Dead Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- Implementation:
  - `server/realtime/nats_retry_handler.py`
  - `server/realtime/dead_letter_queue.py`
  - `server/realtime/circuit_breaker.py`
  - `server/middleware/metrics_collector.py`
  - `server/api/metrics.py`
- Tests: `server/tests/` (retry handler, DLQ, circuit breaker, metrics collector suites)

---

## 11. Related ADRs

**[SPEC]**

- [ADR-011](ADR-011-xstate-frontend-fsm.md): XState for Frontend Connection FSM
- [ADR-012](ADR-012-python-statemachine-backend.md): python-statemachine for Backend Connection FSM
- [ADR-013](ADR-013-pydantic-configuration.md): Pydantic Configuration Management

## 12. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Record provenance; remove hard-coded test counts; correct metrics paths to `/v1/metrics` (#721) |
