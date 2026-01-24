# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-10-critical-architecture-fixes/spec.md

## Technical Requirements

### CRITICAL-1: Connection State Machine Implementation

**Frontend (React/TypeScript):**

**State Machine Library:** XState 4.x (adds ~50KB to bundle)

**Implementation Location:** `client/src/hooks/useGameConnection.ts` (refactor)

**State Definition:** Create explicit FSM with states:

  ```typescript
  type ConnectionState =
    | 'disconnected'
    | 'connecting_sse'
    | 'sse_connected'
    | 'connecting_ws'
    | 'fully_connected'
    | 'reconnecting'
    | 'failed'
  ```

**Transition Guards:** Implement timeout guards (30s connection timeout, 5s reconnection timeout)

**State Persistence:** Use XState context for connection metadata (attempts, session_id, last_error)

**Visualization:** Enable XState inspector for debugging (dev mode only)
- **Error Handling:** Map all connection errors to state transitions

**Backend (Python/FastAPI):**

**State Machine Library:** python-statemachine 2.x

**Implementation Location:** New module `server/realtime/connection_state_machine.py`

**Use Cases:**
  - NATS connection lifecycle
  - WebSocket health tracking
  - Circuit breaker state management
- **States:** Define NATS connection states (disconnected, connecting, connected, reconnecting, circuit_open)
- **Async Support:** Use async transitions for all I/O operations
- **Logging:** Log all state transitions with structured logging

**Refactoring Strategy:**

1. Extract connection logic from 750-line `useGameConnection.ts` into:

   - `useConnectionStateMachine.ts` - XState machine definition
   - `useWebSocketConnection.ts` - WebSocket-specific logic
   - `useSSEConnection.ts` - SSE-specific logic
   - `useConnectionHealth.ts` - Health check monitoring
   - `useSessionManagement.ts` - Session ID tracking

2. Replace multiple refs with XState context
3. Replace manual timer management with XState delayed transitions
4. Add comprehensive unit tests for state transitions

**Testing Requirements:**

- Unit tests for all state transitions (happy path + error paths)
- Integration tests for connection recovery scenarios
- Chaos testing for network interruptions
- Test coverage: ≥85% for state machine logic

---

### CRITICAL-2: Configuration Management Refactoring

**Current State Issues:**

- 395-line `server/config_loader.py` with hardcoded defaults
- Mixed YAML + environment variable loading
- No validation schema
- Security-sensitive defaults

**Target Architecture:**

**Core Configuration Models:**

```python
# server/config/models.py

from pydantic import BaseSettings, Field, validator

class ServerConfig(BaseSettings):
    """Server network configuration."""
    host: str = Field("127.0.0.1", env="SERVER_HOST")
    port: int = Field(..., env="SERVER_PORT")  # Required, no default

    @validator('port')
    def validate_port(cls, v):
        if not 1024 <= v <= 65535:
            raise ValueError('Port must be between 1024 and 65535')
        return v

    class Config:
        env_file = '.env'
        case_sensitive = False

class DatabaseConfig(BaseSettings):
    """Database configuration."""
    url: str = Field(..., env="DATABASE_URL")  # Required
    npc_url: str = Field(..., env="NPC_DATABASE_URL")  # Required

    class Config:
        env_file = '.env'

class NATSConfig(BaseSettings):
    """NATS messaging configuration."""
    enabled: bool = Field(True, env="NATS_ENABLED")
    url: str = Field("nats://localhost:4222", env="NATS_URL")
    max_payload: int = Field(1048576, env="NATS_MAX_PAYLOAD")
    reconnect_time_wait: int = Field(1, env="NATS_RECONNECT_WAIT")
    max_reconnect_attempts: int = Field(5, env="NATS_MAX_RECONNECT_ATTEMPTS")
    connect_timeout: int = Field(5, env="NATS_CONNECT_TIMEOUT")

    class Config:
        env_file = '.env'

class SecurityConfig(BaseSettings):
    """Security-sensitive configuration."""
    admin_password: str = Field(..., env="MYTHOSMUD_ADMIN_PASSWORD")  # Required
    invite_codes_file: str = Field("invites.json", env="INVITE_CODES_FILE")

    class Config:
        env_file = '.env'

class LoggingConfig(BaseSettings):
    """Logging configuration."""
    environment: str = Field(..., env="LOGGING_ENVIRONMENT")  # Required: local, unit_test, e2e_test, production
    level: str = Field("INFO", env="LOG_LEVEL")
    format: str = Field("colored", env="LOG_FORMAT")
    log_base: str = Field("logs", env="LOG_BASE_DIR")

    @validator('environment')
    def validate_environment(cls, v):
        valid = ['local', 'unit_test', 'e2e_test', 'production']
        if v not in valid:
            raise ValueError(f'Environment must be one of {valid}')
        return v

    class Config:
        env_file = '.env'

class AppConfig(BaseSettings):
    """Composite application configuration."""
    server: ServerConfig = Field(default_factory=ServerConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    nats: NATSConfig = Field(default_factory=NATSConfig)
    security: SecurityConfig = Field(default_factory=SecurityConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)

    class Config:
        env_file = '.env'
```

**Configuration Loading:**

```python
# server/config/__init__.py

from functools import lru_cache
from .models import AppConfig

@lru_cache()
def get_config() -> AppConfig:
    """
    Get application configuration (singleton).
    Raises ValidationError if configuration is invalid.
    """
    return AppConfig()

# Export for compatibility

__all__ = ['get_config', 'AppConfig']
```

**Migration Strategy:**

1. Create new `server/config/` module with Pydantic models
2. Update all imports from `server.config_loader` to `server.config`
3. Update `.env.local.example`, `.env.unit_test.example`, `.env.e2e_test.example`, `.env.production.example`
4. Remove `server/config_loader.py` after validation
5. Update deployment scripts to require explicit environment configuration

**Environment Files Required:**

- `.env.local` - Local development configuration
- `.env.unit_test` - Unit test configuration
- `.env.e2e_test` - E2E test configuration
- `.env.production` - Production configuration (template only, actual values in deployment)

**Breaking Changes:**

**YAML config files no longer supported** - Must use `.env` files

**No hardcoded defaults for security fields** - Must provide `MYTHOSMUD_ADMIN_PASSWORD`, `DATABASE_URL`, etc.

**Environment must be explicit** - Must set `LOGGING_ENVIRONMENT`

**Testing Requirements:**

- Unit tests for each configuration model validation
- Integration tests for configuration loading from different environments
- Negative tests for invalid configuration values
- Test coverage: ≥80%

---

### CRITICAL-3: Command Security Hardening

**Security Vulnerabilities Identified:**

1. **Alias Bombs:** Recursive alias expansion without circular dependency detection
2. **Command Injection:** Insufficient validation of expanded commands
3. **Denial of Service:** No rate limiting on command processing
4. **Audit Gap:** No logging of security-sensitive commands

**Implementation Requirements:**

**1. Circular Dependency Detection:**

```python
# server/utils/alias_graph.py

from typing import Dict, Set, List
import networkx as nx

class AliasGraph:
    """
    Graph-based circular dependency detection for alias expansion.
    Uses depth-first search to detect cycles before expansion.
    """

    def __init__(self, alias_storage: AliasStorage):
        self.alias_storage = alias_storage
        self.graph = nx.DiGraph()

    def build_graph(self, player_name: str) -> None:
        """Build dependency graph for player's aliases."""
        aliases = self.alias_storage.get_all_aliases(player_name)
        for alias in aliases:
            self.graph.add_node(alias.name)
            # Parse alias command to find referenced aliases

            referenced = self._extract_alias_references(alias.command)
            for ref in referenced:
                self.graph.add_edge(alias.name, ref)

    def detect_cycle(self, alias_name: str) -> List[str] | None:
        """
        Detect if expanding this alias would create a cycle.
        Returns the cycle path if found, None otherwise.
        """
        try:
            cycle = nx.find_cycle(self.graph, source=alias_name)
            return [edge[0] for edge in cycle]
        except nx.NetworkXNoCycle:
            return None

    def is_safe_to_expand(self, alias_name: str) -> bool:
        """Check if alias can be safely expanded."""
        return self.detect_cycle(alias_name) is None
```

**Integration with Command Handler:**

```python
# server/command_handler_unified.py (modifications)

async def process_command_unified(
    command_line: str,
    current_user: dict,
    request: Request,
    alias_storage: AliasStorage | None = None,
    player_name: str | None = None,
) -> dict[str, Any]:
    """Modified to include alias safety checks."""

    # ... existing code ...

    # Step 6: Check for alias expansion with safety validation

    if alias_storage:
        alias = alias_storage.get_alias(player_name, cmd)
        if alias:
            # NEW: Check for circular dependencies

            alias_graph = AliasGraph(alias_storage)
            alias_graph.build_graph(player_name)

            if not alias_graph.is_safe_to_expand(alias.name):
                cycle = alias_graph.detect_cycle(alias.name)
                logger.warning(
                    "Circular alias dependency detected",
                    player=player_name,
                    alias=alias.name,
                    cycle=cycle
                )
                return {
                    "result": f"Alias '{alias.name}' contains circular dependency: {' → '.join(cycle)}"
                }

            # NEW: Validate expanded command length

            expanded_command = alias.get_expanded_command(args)
            if len(expanded_command) > MAX_EXPANDED_COMMAND_LENGTH:
                logger.warning(
                    "Expanded command exceeds length limit",
                    player=player_name,
                    alias=alias.name,
                    length=len(expanded_command)
                )
                return {
                    "result": f"Expanded command too long ({len(expanded_command)} chars, max {MAX_EXPANDED_COMMAND_LENGTH})"
                }

            # Proceed with expansion

            result = await handle_expanded_command(...)
            return result
```

**2. Command Rate Limiting:**

```python
# server/middleware/rate_limiter.py

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict

class CommandRateLimiter:
    """
    Per-player command rate limiting.
    Uses sliding window algorithm for accurate rate limiting.
    """

    def __init__(self, max_commands: int = 10, window_seconds: int = 1):
        self.max_commands = max_commands
        self.window = timedelta(seconds=window_seconds)
        self.player_timestamps: Dict[str, List[datetime]] = defaultdict(list)

    def is_allowed(self, player_name: str) -> bool:
        """Check if player can execute command."""
        now = datetime.now()
        cutoff = now - self.window

        # Remove old timestamps

        self.player_timestamps[player_name] = [
            ts for ts in self.player_timestamps[player_name]
            if ts > cutoff
        ]

        # Check limit

        if len(self.player_timestamps[player_name]) >= self.max_commands:
            return False

        # Record new command

        self.player_timestamps[player_name].append(now)
        return True

    def get_wait_time(self, player_name: str) -> float:
        """Get seconds until rate limit resets."""
        if not self.player_timestamps[player_name]:
            return 0.0
        oldest = min(self.player_timestamps[player_name])
        reset_time = oldest + self.window
        wait = (reset_time - datetime.now()).total_seconds()
        return max(0.0, wait)

# Global rate limiter instance

command_rate_limiter = CommandRateLimiter(max_commands=10, window_seconds=1)
```

**Integration:**

```python
# server/command_handler_unified.py (add at start of process_command_unified)

# Check rate limit

if not command_rate_limiter.is_allowed(player_name):
    wait_time = command_rate_limiter.get_wait_time(player_name)
    logger.warning("Command rate limit exceeded", player=player_name, wait_time=wait_time)
    return {
        "result": f"Rate limit exceeded. Please wait {wait_time:.1f} seconds."
    }
```

**3. Command Validation:**

```python
# server/validators/command_validator.py

import re
from typing import Set

class CommandValidator:
    """Validate commands for security threats."""

    DANGEROUS_PATTERNS = [
        r';\s*rm\s+-rf',  # Shell injection
        r'\$\(',  # Command substitution
        r'`',  # Backtick execution
        r'\|\s*sh',  # Pipe to shell
        r'>\s*/dev',  # Device redirection
    ]

    SYSTEM_COMMANDS = {
        'admin', 'teleport', 'spawn', 'delete', 'grant', 'revoke'
    }

    @classmethod
    def validate_command_content(cls, command: str) -> tuple[bool, str | None]:
        """
        Validate command for security threats.
        Returns (is_valid, error_message).
        """
        # Check for dangerous patterns

        for pattern in cls.DANGEROUS_PATTERNS:
            if re.search(pattern, command, re.IGNORECASE):
                return False, f"Command contains potentially dangerous pattern: {pattern}"

        # Check for null bytes

        if '\x00' in command:
            return False, "Command contains null bytes"

        # Check for excessive length

        if len(command) > 10000:
            return False, "Command exceeds maximum length"

        return True, None

    @classmethod
    def is_security_sensitive(cls, command: str) -> bool:
        """Check if command requires audit logging."""
        cmd_parts = command.split()
        if not cmd_parts:
            return False
        return cmd_parts[0].lower() in cls.SYSTEM_COMMANDS
```

**4. Audit Logging:**

```python
# server/utils/audit_logger.py

from datetime import datetime
import json

class AuditLogger:
    """Audit logging for security-sensitive commands."""

    def __init__(self, log_file: str = "logs/audit.log"):
        self.log_file = log_file

    def log_command(
        self,
        player_name: str,
        command: str,
        success: bool,
        ip_address: str | None = None,
        metadata: dict | None = None
    ) -> None:
        """Log security-sensitive command execution."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "player": player_name,
            "command": command,
            "success": success,
            "ip_address": ip_address,
            "metadata": metadata or {}
        }

        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

audit_logger = AuditLogger()
```

**Testing Requirements:**

- Unit tests for alias cycle detection (various cycle configurations)
- Unit tests for rate limiter (sliding window edge cases)
- Unit tests for command validation (all dangerous patterns)
- Integration tests for command rejection scenarios
- Load testing for rate limiter performance
- Security testing for bypass attempts
- Test coverage: ≥90% (security-critical code)

---

### CRITICAL-4: NATS Error Boundaries

**Current Issues:**

- Broad exception catching without recovery
- No retry logic for transient failures
- No dead letter queue for persistent failures
- No metrics for failure tracking

**Implementation Requirements:**

**1. Message Retry Logic:**

```python
# server/realtime/nats_retry_handler.py

from typing import Callable, Any
import asyncio
from functools import wraps

class RetryConfig:
    """Configuration for retry behavior."""
    max_attempts: int = 3
    base_delay: float = 1.0  # seconds
    max_delay: float = 30.0  # seconds
    exponential_base: float = 2.0

class NATSRetryHandler:
    """Handle message retries with exponential backoff."""

    def __init__(self, config: RetryConfig = RetryConfig()):
        self.config = config

    async def retry_with_backoff(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> tuple[bool, Any]:
        """
        Retry function with exponential backoff.
        Returns (success, result_or_error).
        """
        last_error = None

        for attempt in range(self.config.max_attempts):
            try:
                result = await func(*args, **kwargs)
                return True, result
            except Exception as e:
                last_error = e
                if attempt < self.config.max_attempts - 1:
                    delay = min(
                        self.config.base_delay * (self.config.exponential_base ** attempt),
                        self.config.max_delay
                    )
                    logger.warning(
                        "NATS operation failed, retrying",
                        attempt=attempt + 1,
                        max_attempts=self.config.max_attempts,
                        delay=delay,
                        error=str(e)
                    )
                    await asyncio.sleep(delay)

        return False, last_error
```

**2. Dead Letter Queue:**

```python
# server/realtime/dead_letter_queue.py

from datetime import datetime
from typing import Any, Dict
import json
from pathlib import Path

class DeadLetterQueue:
    """Store messages that fail after all retries."""

    def __init__(self, storage_path: str = "logs/dlq"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    async def enqueue(
        self,
        message_data: Dict[str, Any],
        error: Exception,
        retry_count: int
    ) -> None:
        """Add failed message to dead letter queue."""
        dlq_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": message_data,
            "error": str(error),
            "error_type": type(error).__name__,
            "retry_count": retry_count,
        }

        filename = f"dlq_{datetime.utcnow().strftime('%Y%m%d_%H%M%S_%f')}.json"
        filepath = self.storage_path / filename

        with open(filepath, 'w') as f:
            json.dump(dlq_entry, f, indent=2)

        logger.error(
            "Message added to dead letter queue",
            filepath=str(filepath),
            message_id=message_data.get('message_id'),
            error=str(error)
        )

    async def get_pending_count(self) -> int:
        """Get count of messages in DLQ."""
        return len(list(self.storage_path.glob("dlq_*.json")))
```

**3. Circuit Breaker Pattern:**

```python
# server/realtime/circuit_breaker.py

from enum import Enum
from datetime import datetime, timedelta
from typing import Callable, Any
import asyncio

class CircuitState(Enum):
    CLOSED = "closed"  # Normal operation
    OPEN = "open"  # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if recovered

class CircuitBreaker:
    """Circuit breaker for NATS message processing."""

    def __init__(
        self,
        failure_threshold: int = 5,
        timeout: timedelta = timedelta(seconds=60),
        success_threshold: int = 2
    ):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: datetime | None = None

    async def call(self, func: Callable, *args, **kwargs) -> Any:
        """Execute function through circuit breaker."""
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitState.HALF_OPEN
                logger.info("Circuit breaker entering HALF_OPEN state")
            else:
                raise CircuitBreakerOpen("Circuit breaker is OPEN")

        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self) -> None:
        """Handle successful call."""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
                self.success_count = 0
                logger.info("Circuit breaker reset to CLOSED state")
        else:
            self.failure_count = 0

    def _on_failure(self) -> None:
        """Handle failed call."""
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        self.success_count = 0

        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
            logger.error(
                "Circuit breaker opened due to failures",
                failure_count=self.failure_count,
                threshold=self.failure_threshold
            )

    def _should_attempt_reset(self) -> bool:
        """Check if enough time has passed to attempt reset."""
        if self.last_failure_time is None:
            return True
        return datetime.now() - self.last_failure_time >= self.timeout

class CircuitBreakerOpen(Exception):
    """Exception raised when circuit breaker is open."""
    pass
```

**4. Integration with NATS Message Handler:**

```python
# server/realtime/nats_message_handler.py (modifications)

class NATSMessageHandler:
    """Enhanced with error boundaries."""

    def __init__(self, nats_service):
        self.nats_service = nats_service
        self.retry_handler = NATSRetryHandler()
        self.dead_letter_queue = DeadLetterQueue()
        self.circuit_breaker = CircuitBreaker()
        # ... existing initialization ...

    async def _handle_nats_message(self, message_data: dict[str, Any]):
        """Enhanced message handling with error boundaries."""
        try:
            # Process through circuit breaker

            await self.circuit_breaker.call(
                self._process_message_with_retry,
                message_data
            )
        except CircuitBreakerOpen:
            logger.error("Circuit breaker open, rejecting message")
            # Add to DLQ immediately when circuit is open

            await self.dead_letter_queue.enqueue(
                message_data,
                Exception("Circuit breaker open"),
                retry_count=0
            )
        except Exception as e:
            logger.error("Unhandled error in message processing", error=str(e))

    async def _process_message_with_retry(self, message_data: dict[str, Any]):
        """Process message with retry logic."""
        success, result = await self.retry_handler.retry_with_backoff(
            self._process_single_message,
            message_data
        )

        if not success:
            # All retries exhausted, add to DLQ

            await self.dead_letter_queue.enqueue(
                message_data,
                result,  # This is the exception
                retry_count=self.retry_handler.config.max_attempts
            )

    async def _process_single_message(self, message_data: dict[str, Any]):
        """Process a single message (can raise exceptions)."""
        # Validate required fields

        if not all([message_data.get("channel"), message_data.get("sender_id")]):
            raise ValueError("Missing required message fields")

        # ... existing processing logic ...

```

**5. FastAPI Metrics Integration:**

```python
# server/middleware/metrics_middleware.py

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from collections import Counter
from datetime import datetime

class MetricsCollector:
    """Simple metrics collector for FastAPI."""

    def __init__(self):
        self.nats_messages_processed = Counter()
        self.nats_messages_failed = Counter()
        self.nats_messages_dlq = Counter()
        self.circuit_breaker_state = "closed"
        self.last_reset = datetime.now()

    def record_message_processed(self, channel: str):
        self.nats_messages_processed[channel] += 1

    def record_message_failed(self, channel: str):
        self.nats_messages_failed[channel] += 1

    def record_message_dlq(self, channel: str):
        self.nats_messages_dlq[channel] += 1

    def set_circuit_breaker_state(self, state: str):
        self.circuit_breaker_state = state

    def get_metrics(self) -> dict:
        """Get current metrics."""
        return {
            "nats": {
                "messages_processed": dict(self.nats_messages_processed),
                "messages_failed": dict(self.nats_messages_failed),
                "messages_dlq": dict(self.nats_messages_dlq),
                "circuit_breaker_state": self.circuit_breaker_state,
            },
            "timestamp": datetime.now().isoformat()
        }

# Global metrics instance

metrics_collector = MetricsCollector()

# Add metrics endpoint to FastAPI

@app.get("/api/metrics")
async def get_metrics():
    """Expose metrics for monitoring."""
    return metrics_collector.get_metrics()
```

**Testing Requirements:**

- Unit tests for retry logic (various failure scenarios)
- Unit tests for circuit breaker state transitions
- Unit tests for dead letter queue operations
- Integration tests for end-to-end message delivery with failures
- Chaos testing for network interruptions and NATS failures
- Performance testing for metrics collection overhead
- Test coverage: ≥80%

---

## External Dependencies

### New Dependencies Required

**Frontend:**

**xstate** (4.38.x) - State machine library for connection management

**Justification:** Industry-standard FSM library with excellent TypeScript support, visualization tools, and testing utilities. Provides robust connection state management with timeout guards and transition logging.

**Bundle Impact:** ~50KB gzipped (acceptable for reliability gains)
- **Installation:** `npm install xstate@^4.38.0`

**@xstate/react** (3.2.x) - React hooks for XState

**Justification:** Official React integration providing hooks for state machine usage

**Installation:** `npm install @xstate/react@^3.2.0`

**Backend:**

**python-statemachine** (2.1.x) - Python state machine library

**Justification:** Native async/await support, excellent type hints, cleaner API than alternatives, aligns with project's modern Python patterns

**Installation:** `pip install python-statemachine==2.1.*` or add to `pyproject.toml`

**networkx** (3.x) - Graph analysis library for alias cycle detection

**Justification:** Industry-standard graph library with efficient cycle detection algorithms (DFS-based). Required for circular alias dependency detection.

**Installation:** `pip install networkx>=3.0,<4.0`

**Note:** All other functionality uses existing dependencies (Pydantic, FastAPI, asyncio, etc.)

---

## Performance Considerations

### Expected Performance Impact

**Positive Impacts:**

**Connection Reliability:** 50% reduction in connection-related support tickets

**Server Stability:** Elimination of alias bomb DoS vulnerability

**Message Delivery:** 99.9% message delivery success rate (up from ~95%)
- **Configuration Startup:** Faster startup with early validation failures

**Potential Performance Costs:**

**Alias Expansion:** +5-10ms per alias command (graph cycle detection)

**Command Rate Limiting:** +1-2ms per command (timestamp checking)

**NATS Message Processing:** +10-20ms per message (retry logic overhead)
- **Frontend Bundle Size:** +50KB gzipped (XState)

**Mitigation Strategies:**

- Cache alias graphs per player (rebuild only on alias changes)
- Use in-memory rate limiter with periodic cleanup
- Short-circuit retry logic on success
- Lazy-load XState in production builds

### Resource Requirements

**Memory:**

- XState: +2-3MB per active connection (state machine context)
- Alias graphs: +1MB per 1000 active players
- Rate limiter: +500KB per 1000 active players
- DLQ storage: Disk-based, minimal memory impact

**CPU:**

- Alias cycle detection: O(V + E) where V=aliases, E=dependencies
- Rate limiting: O(1) per command check
- Circuit breaker: O(1) per state check

---

## Security Considerations

### Security Improvements

1. **Command Injection Prevention:**

   - Circular dependency detection prevents alias bombs
   - Command validation blocks shell injection patterns
   - Rate limiting prevents DoS attacks

2. **Configuration Security:**

   - No hardcoded secrets in code
   - Explicit validation catches misconfigurations
   - Environment-specific configs prevent production leaks

3. **Audit Trail:**

   - All admin commands logged with timestamps
   - Failed authentication attempts tracked
   - Dead letter queue preserves failed messages for forensics

### Security Testing Requirements

**Penetration Testing:** Attempt alias bomb creation, command injection

**Fuzz Testing:** Random command generation to find validation bypasses

**Load Testing:** Verify rate limiting under attack conditions
- **Audit Testing:** Verify all security-sensitive commands are logged

---

## Rollback Strategy

### Rollback Plan (If Critical Issues Arise)

**Sprint 1 Rollback:**

1. Revert commits for CRITICAL-2 (configuration) and CRITICAL-3 (command security)
2. Restore `server/config_loader.py` from main branch
3. Restore `server/command_handler_unified.py` to previous version
4. Keep CRITICAL-4 (NATS) changes if stable

**Sprint 2 Rollback:**

1. Revert frontend XState integration
2. Restore original `useGameConnection.ts`
3. Keep backend changes if frontend is the issue

**Data Migration:**

- No database migrations required, so rollback is clean
- Configuration changes require re-deploying old `.env` files

**Testing Before Rollback:**

- Verify staging environment with rollback before production
- Maintain parallel deployment during Sprint 1 (blue-green)

---

## Documentation Requirements

### Required Documentation Updates

1. **Architecture Decision Records (ADRs):**

   - ADR: Connection State Machine Selection (XState vs alternatives)
   - ADR: Configuration Management Strategy (Pydantic BaseSettings)
   - ADR: Command Security Implementation (graph-based cycle detection)
   - ADR: Error Boundary Pattern (circuit breaker + DLQ)

2. **Developer Documentation:**

   - XState debugging guide (using @xstate/inspect)
   - Configuration validation guide
   - Command security testing guide
   - NATS metrics interpretation guide

3. **Deployment Documentation:**

   - Updated `.env` file requirements
   - Configuration validation checklist
   - Monitoring setup for new metrics endpoint

4. **User Documentation:**

   - Connection status indicator explanations (for players)
   - Alias limitation documentation (preventing circular aliases)

---

## Definition of Done

### Sprint 1 Completion Criteria

✅ **CRITICAL-2: Configuration Management**

- [ ] Pydantic BaseSettings models created for all configuration categories
- [ ] All imports updated from `config_loader` to `config` module
- [ ] Environment files created (`.env.local.example`, etc.)
- [ ] Unit tests passing with ≥80% coverage
- [ ] Configuration validation tested for all invalid scenarios
- [ ] `server/config_loader.py` removed
- [ ] Deployment documentation updated

✅ **CRITICAL-3: Command Security**

- [ ] `AliasGraph` class implemented with cycle detection
- [ ] `CommandRateLimiter` implemented with sliding window
- [ ] `CommandValidator` implemented with dangerous pattern detection
- [ ] `AuditLogger` implemented for security-sensitive commands
- [ ] Integration with `command_handler_unified.py` complete
- [ ] Unit tests passing with ≥90% coverage (security-critical)
- [ ] Security testing completed (attempted alias bombs, injections)
- [ ] No regression test failures

✅ **CRITICAL-4: NATS Error Boundaries**

- [ ] `NATSRetryHandler` implemented with exponential backoff
- [ ] `DeadLetterQueue` implemented with file-based storage
- [ ] `CircuitBreaker` implemented with state transitions
- [ ] Integration with `nats_message_handler.py` complete
- [ ] Metrics endpoint `/api/metrics` created
- [ ] Unit tests passing with ≥80% coverage
- [ ] Chaos testing completed (simulated NATS failures)
- [ ] No regression test failures

✅ **Sprint 1 Deployment**

- [ ] All backend tests passing (unit + integration)
- [ ] Code coverage ≥80% for new code
- [ ] Linting passes with no errors
- [ ] Security audit log functioning
- [ ] Metrics endpoint accessible
- [ ] Staging deployment successful
- [ ] No critical bugs in staging testing

### Sprint 2 Completion Criteria

✅ **CRITICAL-1: Connection State Machine (Frontend)**

- [ ] XState machine definition created (`useConnectionStateMachine.ts`)
- [ ] `useGameConnection.ts` refactored into focused hooks
- [ ] Connection state visualizer configured (dev mode)
- [ ] Timeout guards implemented (30s connection, 5s reconnect)
- [ ] Error handling mapped to state transitions
- [ ] Unit tests passing with ≥85% coverage
- [ ] Integration tests passing (connection recovery scenarios)
- [ ] No regression test failures

✅ **CRITICAL-1: Connection State Machine (Backend)**

- [ ] `python-statemachine` integrated
- [ ] `connection_state_machine.py` module created
- [ ] NATS connection lifecycle managed by FSM
- [ ] Circuit breaker states managed by FSM
- [ ] Unit tests passing with ≥80% coverage
- [ ] No regression test failures

✅ **Sprint 2 Integration**

- [ ] End-to-end connection tests passing
- [ ] Frontend + backend connection state synchronized
- [ ] Visual connection indicators functioning
- [ ] All tests passing (unit + integration + E2E)
- [ ] Code coverage ≥80% for new code
- [ ] Linting passes with no errors

✅ **Sprint 2 Deployment**

- [ ] Full stack tests passing
- [ ] Staging deployment successful
- [ ] Production deployment successful
- [ ] Monitoring confirms improved connection reliability
- [ ] No critical bugs in production

✅ **Post-Implementation Requirements**

- [ ] ADRs written and committed
- [ ] Developer documentation updated
- [ ] Deployment documentation updated
- [ ] Security audit completed
- [ ] Metrics dashboard accessible
- [ ] Rollback procedure documented and tested

---

## Success Metrics

### Key Performance Indicators (KPIs)

**Week 1 (Sprint 1 End):**

- Backend test coverage ≥80%
- Zero critical security vulnerabilities
- Configuration validation catches 100% of invalid configs
- Command rate limiting prevents ≥95% of attempted DoS attacks
- Message delivery success rate ≥99%

**Week 2 (Sprint 2 End):**

- Frontend test coverage ≥80%
- Connection success rate ≥98%
- Connection recovery time <5 seconds
- Zero infinite reconnection loops
- Player-facing error messages clear and actionable

**Post-Deployment (Week 3):**

- Support tickets related to connections reduced by ≥50%
- Zero production incidents related to alias bombs
- Zero configuration-related deployment failures
- Message loss rate <0.1%
- System uptime ≥99.9%
