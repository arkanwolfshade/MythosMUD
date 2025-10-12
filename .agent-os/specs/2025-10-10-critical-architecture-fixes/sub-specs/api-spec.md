# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-10-10-critical-architecture-fixes/spec.md

## New Endpoints

### GET /api/metrics

**Purpose:** Expose internal system metrics for monitoring message delivery, circuit breaker states, and connection health.

**Authentication:** Requires admin authentication (Bearer token with admin role)

**Parameters:** None

**Response Format:**

```json
{
  "nats": {
    "messages_processed": {
      "global": 1523,
      "local": 8234,
      "whisper": 432,
      "say": 2341
    },
    "messages_failed": {
      "global": 3,
      "local": 12,
      "whisper": 1
    },
    "messages_dlq": {
      "global": 1,
      "local": 2
    },
    "circuit_breaker_state": "closed"
  },
  "timestamp": "2025-10-10T12:34:56.789Z"
}
```

**Response Codes:**

- `200 OK` - Metrics returned successfully
- `401 Unauthorized` - Missing or invalid authentication token
- `403 Forbidden` - User does not have admin role
- `500 Internal Server Error` - Error collecting metrics

**Rate Limiting:** Not rate-limited (admin-only endpoint)

**Example Usage:**

```bash
# Get current system metrics
curl -H "Authorization: Bearer <admin_token>" http://localhost:54731/api/metrics
```

**Monitoring Use Cases:**

- Track NATS message delivery success rate
- Monitor dead letter queue accumulation
- Alert on circuit breaker state changes
- Track message volume by channel

---

## Modified Endpoints

### POST /command

**Modifications:** Enhanced security validation and rate limiting

**New Behavior:**

1. **Rate Limiting Check** (Before processing)
   - Validates player has not exceeded 10 commands/second
   - Returns error with wait time if rate limit exceeded

2. **Alias Cycle Detection** (Before expansion)
   - Checks for circular alias dependencies
   - Returns error with cycle path if detected

3. **Command Validation** (Before execution)
   - Validates expanded command content for dangerous patterns
   - Blocks commands with shell injection patterns
   - Enforces maximum expanded command length (10,000 chars)

4. **Audit Logging** (For admin commands)
   - Logs all admin/system commands to `logs/audit.log`
   - Includes timestamp, player, IP address, success status

**New Error Responses:**

```json
{
  "result": "Rate limit exceeded. Please wait 0.8 seconds."
}
```

```json
{
  "result": "Alias 'attack' contains circular dependency: attack → strike → attack"
}
```

```json
{
  "result": "Command contains potentially dangerous pattern"
}
```

**Performance Impact:**

- Added latency: +5-10ms per alias command (cycle detection)
- Added latency: +1-2ms per command (rate limit check)
- No impact on non-alias commands

---

## WebSocket Message Protocol

### Modified Message Types

#### game_command (Enhanced)

**Client → Server:**

```json
{
  "type": "game_command",
  "data": {
    "command": "attack goblin",
    "args": ["goblin"],
    "csrf_token": "abc123..."
  }
}
```

**Server → Client (Error Cases):**

```json
{
  "event_type": "error",
  "data": {
    "error_type": "rate_limit_exceeded",
    "message": "Rate limit exceeded. Please wait 0.8 seconds.",
    "retry_after": 0.8
  }
}
```

```json
{
  "event_type": "error",
  "data": {
    "error_type": "alias_cycle_detected",
    "message": "Alias 'loop' contains circular dependency: loop → recurse → loop",
    "cycle_path": ["loop", "recurse", "loop"]
  }
}
```

---

## Configuration API Changes

### Environment Variable Requirements

**New Required Variables:**

```bash
# Server Configuration
SERVER_PORT=54731  # Previously had default, now required

# Database Configuration
DATABASE_URL=sqlite:///data/local/players.db  # Previously could be undefined
NPC_DATABASE_URL=sqlite:///data/local/npcs.db  # Previously could be undefined

# Security Configuration
MYTHOSMUD_ADMIN_PASSWORD=<secure_password>  # Previously had weak default

# Logging Configuration
LOGGING_ENVIRONMENT=local  # Required: local|unit_test|e2e_test|production
```

**Validation Rules:**

- `SERVER_PORT`: Integer between 1024-65535
- `LOGGING_ENVIRONMENT`: Must be one of: `local`, `unit_test`, `e2e_test`, `production`
- `DATABASE_URL`: Must be valid SQLite or PostgreSQL URL
- `MYTHOSMUD_ADMIN_PASSWORD`: Minimum 12 characters (in production)

**Error Messages:**

If configuration is invalid, server will fail to start with clear error:

```
ValidationError: 1 validation error for ServerConfig
port
  Port must be between 1024 and 65535 (type=value_error)
```

**Breaking Changes:**

- **No YAML config files** - Must use `.env` or environment variables
- **No default passwords** - Must provide explicit admin password
- **No fallback configs** - Missing required fields cause startup failure

---

## Integration Points

### Modified Components

**Backend:**

1. `server/config_loader.py` → `server/config/models.py` + `server/config/__init__.py`
2. `server/command_handler_unified.py` - Add security checks
3. `server/realtime/nats_message_handler.py` - Add error boundaries
4. `server/app/factory.py` - Add metrics endpoint

**Frontend:**

1. `client/src/hooks/useGameConnection.ts` - Refactor to use XState
2. New hooks: `useConnectionStateMachine.ts`, `useWebSocketConnection.ts`, `useSSEConnection.ts`, etc.
3. New component: Connection status indicator

**New Modules:**

- `server/config/` - Configuration models
- `server/utils/alias_graph.py` - Cycle detection
- `server/middleware/rate_limiter.py` - Rate limiting
- `server/validators/command_validator.py` - Command validation
- `server/utils/audit_logger.py` - Audit logging
- `server/realtime/nats_retry_handler.py` - Retry logic
- `server/realtime/dead_letter_queue.py` - Failed message storage
- `server/realtime/circuit_breaker.py` - Circuit breaker
- `server/middleware/metrics_middleware.py` - Metrics collection
- `server/realtime/connection_state_machine.py` - Backend FSM
- `client/src/hooks/useConnectionStateMachine.ts` - Frontend FSM

---

## Backward Compatibility Notes

### Breaking Changes Summary

**Configuration:**

- YAML config files no longer supported
- Must migrate to `.env` files
- Required fields must be explicitly set
- No default admin password

**Commands:**

- Circular aliases will be rejected
- Commands exceeding rate limits will be rejected
- Dangerous command patterns will be blocked
- Expanded commands have length limits

**Deployment:**

- Must provide all required environment variables
- Server will not start with invalid configuration
- Must update deployment scripts

### Migration Guide

**For Developers:**

1. Copy `.env.local.example` to `.env.local`
2. Fill in all required fields
3. Set `LOGGING_ENVIRONMENT=local`
4. Provide explicit `DATABASE_URL` and `NPC_DATABASE_URL`
5. Set `MYTHOSMUD_ADMIN_PASSWORD`

**For Production:**

1. Create `.env.production` from template
2. Set all required variables in deployment environment
3. Use secrets manager for `MYTHOSMUD_ADMIN_PASSWORD`
4. Validate configuration before deployment
5. Test with `python -c "from server.config import get_config; get_config()"`

**For Existing Players:**

- **Aliases:** Existing aliases will be validated on first use
- **Circular aliases will be flagged** and must be fixed manually
- **No data loss** - Only validation added

---

## Monitoring & Observability

### Metrics to Monitor

**Connection Metrics:**

- Connection success rate (target: ≥98%)
- Connection recovery time (target: <5s)
- Infinite loop incidents (target: 0)

**Message Metrics:**

- NATS message delivery rate (target: ≥99.9%)
- Messages in DLQ (target: <10 per day)
- Circuit breaker open events (target: <1 per day)

**Security Metrics:**

- Command rate limit violations (monitor for patterns)
- Alias cycle detection events (monitor for intentional abuse)
- Dangerous command pattern blocks (monitor for attack attempts)
- Admin command audit log volume

**System Metrics:**

- API response times (P50, P95, P99)
- Error rates by endpoint
- Configuration validation failures

### Alerting Thresholds

- **Critical:** Circuit breaker open >5 minutes
- **Critical:** DLQ messages >100
- **Warning:** Connection success rate <95%
- **Warning:** Message delivery rate <99%
- **Info:** Admin command executed

---

## Dependencies Between Tasks

### Critical Path

```
Sprint 1:
  Day 1: Config Models → Config Module → Update Imports → Tests
  Day 2: Alias Graph → Rate Limiter → Command Validator
  Day 3: Security Integration → Security Tests → Audit
  Day 4: Retry Handler → DLQ → Circuit Breaker
  Day 5: NATS Integration → Metrics → Deployment

Sprint 2:
  Day 1: Install XState → State Machine Definition
  Day 2: Extract Hooks → Refactor Main Hook
  Day 3: Connection UI → Unit Tests
  Day 4: Integration Tests → Backend FSM
  Day 5: E2E Tests → Full Deployment
```

### Parallel Work Opportunities

- Configuration tests can be written while updating imports
- Frontend XState work can begin while backend NATS work continues
- Documentation can be written throughout both sprints

---

## Post-Implementation Verification

### Week 3: Monitoring & Validation

**Activities:**

1. Monitor production metrics daily
2. Review DLQ for patterns
3. Analyze audit logs for security incidents
4. Collect player feedback on connection stability
5. Measure support ticket reduction

**Success Indicators:**

- Zero alias bomb incidents
- Zero infinite reconnection loops
- Connection-related support tickets reduced by ≥50%
- Message delivery rate ≥99.9%
- Configuration deployment errors: 0

**Iteration Points:**

- Adjust rate limits based on real usage patterns
- Fine-tune retry timeouts based on observed failures
- Optimize circuit breaker thresholds
- Add additional dangerous command patterns if discovered
