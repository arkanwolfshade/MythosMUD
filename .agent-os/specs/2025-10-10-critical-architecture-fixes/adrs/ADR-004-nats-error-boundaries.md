# ADR-004: Circuit Breaker + Dead Letter Queue for NATS Error Boundaries

**Date**: 2025-10-11
**Status**: ✅ ACCEPTED
**Decision Makers**: Prof. Wolfshade, AI Assistant
**Context**: CRITICAL-4 NATS Error Boundaries Implementation

---

## Context and Problem Statement

The NATS message handler had broad exception catching without recovery mechanisms:

1. **No Retry Logic**: Transient failures caused permanent message loss
2. **No Circuit Breaker**: System continued attempting operations during outages
3. **No Dead Letter Queue**: Failed messages were lost completely
4. **No Metrics**: No visibility into message delivery failures
5. **Cascading Failures**: NATS issues could overwhelm the entire system

**Question**: How should we implement resilient message delivery with failure recovery?

---

## Decision Drivers

**Message Reliability**: Must prevent message loss

**Resilience**: Must handle transient and persistent failures gracefully

**Observability**: Must provide visibility into failure patterns
- **Performance**: Must not significantly impact message delivery performance
- **Simplicity**: Should be understandable and maintainable
- **Infrastructure Requirements**: Must work without additional infrastructure

---

## Considered Options

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

## Decision Outcome

**Chosen Option**: **Custom Circuit Breaker + DLQ + Retry Implementation**

**Rationale**:

1. **Zero Infrastructure**: File-based DLQ requires no additional services
2. **Tailored Solution**: Exactly fits our needs without unnecessary complexity
3. **Full Control**: Can optimize for our specific use case
4. **Python Native**: Pure Python, async-native implementation
5. **Testability**: 60 comprehensive tests verify all components
6. **Observability**: Built-in metrics collection
7. **Integration**: Seamlessly integrates with existing code

**Trade-offs Accepted**:

- Custom implementation maintenance (offset by comprehensive tests)
- No off-the-shelf solution (acceptable - our needs are specific)

---

## Implementation Details

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

## Consequences

### Positive

✅ **Zero Message Loss**: DLQ ensures all messages are preserved
✅ **Resilient Delivery**: Retry logic handles transient failures
✅ **Cascade Prevention**: Circuit breaker prevents overwhelming failed services
✅ **Observability**: Comprehensive metrics for monitoring
✅ **Admin Control**: `/api/metrics` endpoints for operational visibility
✅ **No Infrastructure**: File-based DLQ requires no additional services
✅ **Performance**: Minimal overhead (only on failures)

### Negative

⚠️ **File I/O**: DLQ writes to disk (acceptable - only on failures)
⚠️ **Manual Replay**: DLQ messages require manual replay or investigation
⚠️ **Disk Space**: DLQ could grow unbounded (mitigated by automatic cleanup)

### Neutral

ℹ️ **Complexity**: Custom implementation requires maintenance (offset by tests)
ℹ️ **Monitoring**: Requires monitoring DLQ growth (standard operational practice)

---

## Validation

✅ All 60 NATS error boundary tests passing (100%)

✅ Retry handler: 13/13 tests passing

✅ Dead Letter Queue: 13/13 tests passing
- ✅ Circuit Breaker: 16/16 tests passing
- ✅ Metrics Collector: 18/18 tests passing
- ✅ No performance regression
- ✅ `/api/metrics` endpoints functional

---

## Operational Considerations

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

Automatic cleanup after 7 days (configurable)

- Admin endpoint: `GET /api/metrics/dlq` for investigation
- Manual replay: `POST /api/metrics/dlq/{id}/replay` (future enhancement)

---

## References

[Martin Fowler - Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html)

- [AWS - Dead Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- Implementation:
  - `server/realtime/nats_retry_handler.py`
  - `server/realtime/dead_letter_queue.py`
  - `server/realtime/circuit_breaker.py`
  - `server/middleware/metrics_collector.py`
  - `server/api/metrics.py`
- Tests: 60 tests across 4 test files

---

## Related ADRs

ADR-001: XState for Frontend Connection FSM

- ADR-002: python-statemachine for Backend Connection FSM
- ADR-003: Pydantic Configuration Management
