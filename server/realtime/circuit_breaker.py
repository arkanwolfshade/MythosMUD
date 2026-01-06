"""
Circuit breaker pattern for NATS message processing.

Implements three-state circuit breaker (CLOSED/OPEN/HALF_OPEN) to prevent
cascading failures when NATS is experiencing issues.

AI: Circuit breakers protect upstream systems from overwhelming failing downstream systems.
"""

from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from enum import Enum
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CircuitState(Enum):
    """
    Circuit breaker states.

    - CLOSED: Normal operation, requests pass through
    - OPEN: Too many failures, reject requests immediately
    - HALF_OPEN: Testing if service recovered, allow limited requests

    AI: State transitions prevent cascading failures while allowing recovery.
    """

    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreakerOpen(Exception):
    """
    Exception raised when circuit breaker is open.

    Indicates the protected service is currently unavailable and
    requests are being rejected to prevent further load.

    AI: Fast-fail behavior prevents resource exhaustion.
    """


class CircuitBreaker:
    """
    Circuit breaker for NATS message processing.

    Implements Martin Fowler's circuit breaker pattern with three states:
    - CLOSED: Normal operation, tracks failures
    - OPEN: Failing, reject requests and give service time to recover
    - HALF_OPEN: Testing recovery, allow limited requests

    State transitions:
    - CLOSED → OPEN: After failure_threshold consecutive failures
    - OPEN → HALF_OPEN: After timeout period expires
    - HALF_OPEN → CLOSED: After success_threshold consecutive successes
    - HALF_OPEN → OPEN: On any failure

    AI: Prevents overwhelming a failing service while allowing automatic recovery.
    """

    def __init__(
        self, failure_threshold: int = 5, timeout: timedelta = timedelta(seconds=60), success_threshold: int = 2
    ):
        """
        Initialize circuit breaker.

        Args:
            failure_threshold: Number of failures before opening circuit
            timeout: Time to wait before attempting reset from OPEN
            success_threshold: Successes needed to close from HALF_OPEN

        AI: Default values balance responsiveness vs. stability.
        """
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.success_threshold = success_threshold

        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: datetime | None = None
        self.last_state_change: datetime = datetime.now(UTC)

        logger.info(
            "CircuitBreaker initialized",
            failure_threshold=failure_threshold,
            timeout=timeout.total_seconds(),
            success_threshold=success_threshold,
        )

    async def call(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function through circuit breaker.

        Enforces circuit breaker logic:
        - CLOSED: Execute normally, track failures
        - OPEN: Reject immediately, check if should transition to HALF_OPEN
        - HALF_OPEN: Execute, track successes for recovery

        Args:
            func: Async function to execute
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Function result if successful

        Raises:
            CircuitBreakerOpen: If circuit is open and timeout hasn't expired
            Exception: Any exception raised by func

        AI: Caller must handle both CircuitBreakerOpen and function exceptions.
        """
        # Check if circuit is open
        if self.state == CircuitState.OPEN:
            if self._should_attempt_reset():
                self._transition_to(CircuitState.HALF_OPEN)
            else:
                raise CircuitBreakerOpen(
                    f"Circuit breaker is OPEN. "
                    f"Failures: {self.failure_count}/{self.failure_threshold}. "
                    f"Retry after: {self._time_until_retry():.1f}s"
                )

        # Attempt function call
        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result

        except Exception as e:
            self._on_failure()
            logger.error("Circuit breaker caught exception", error=str(e), error_type=type(e).__name__)
            raise

    def _on_success(self) -> None:
        """
        Handle successful function call.

        Updates state based on current circuit state:
        - CLOSED: Reset failure count
        - HALF_OPEN: Increment success count, close if threshold met

        AI: Gradual recovery prevents premature circuit closure.
        """
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            logger.debug(
                "Success in HALF_OPEN state", success_count=self.success_count, threshold=self.success_threshold
            )

            if self.success_count >= self.success_threshold:
                self._transition_to(CircuitState.CLOSED)
                self.failure_count = 0
                self.success_count = 0
                logger.info("Circuit breaker closed after successful recovery")

        elif self.state == CircuitState.CLOSED:
            # Reset failure count on any success
            if self.failure_count > 0:
                logger.debug("Resetting failure count after success", previous_count=self.failure_count)
                self.failure_count = 0

    def _on_failure(self) -> None:
        """
        Handle failed function call.

        Updates state based on failure count:
        - Increments failure count
        - Opens circuit if threshold exceeded
        - Resets success count in HALF_OPEN

        AI: Quick failure detection prevents prolonged outages.
        """
        self.failure_count += 1
        self.last_failure_time = datetime.now(UTC)
        self.success_count = 0  # Reset success count on any failure

        logger.warning(
            "Circuit breaker recorded failure",
            failure_count=self.failure_count,
            threshold=self.failure_threshold,
            state=self.state.value,
        )

        # Open circuit if threshold exceeded
        if self.failure_count >= self.failure_threshold:
            if self.state != CircuitState.OPEN:
                self._transition_to(CircuitState.OPEN)
                logger.error(
                    "Circuit breaker opened due to failures",
                    failure_count=self.failure_count,
                    threshold=self.failure_threshold,
                )

    def _should_attempt_reset(self) -> bool:
        """
        Check if enough time has passed to attempt circuit reset.

        Returns:
            True if timeout has expired, False otherwise

        AI: Timeout gives downstream service time to recover.
        """
        # Use last_state_change when circuit is OPEN to track when it opened
        # This is more reliable than last_failure_time which might be set earlier
        if self.state == CircuitState.OPEN:
            time_since_open = datetime.now(UTC) - self.last_state_change
            should_reset = time_since_open >= self.timeout

            if should_reset:
                logger.info(
                    "Circuit breaker timeout expired, attempting reset",
                    time_since_open=time_since_open.total_seconds(),
                )

            return should_reset

        # Fallback to last_failure_time for other states (shouldn't happen in normal flow)
        if self.last_failure_time is None:
            return True

        time_since_failure = datetime.now(UTC) - self.last_failure_time
        should_reset = time_since_failure >= self.timeout

        if should_reset:
            logger.info(
                "Circuit breaker timeout expired, attempting reset",
                time_since_failure=time_since_failure.total_seconds(),
            )

        return should_reset

    def _time_until_retry(self) -> float:
        """
        Calculate seconds until circuit can attempt reset.

        Returns:
            Seconds until retry (0 if can retry now)

        AI: For user feedback and monitoring.
        """
        if self.state != CircuitState.OPEN:
            return 0.0

        # Use last_state_change when circuit is OPEN to track when it opened
        time_since_open = datetime.now(UTC) - self.last_state_change
        time_until = self.timeout - time_since_open
        return max(0.0, time_until.total_seconds())

    def _transition_to(self, new_state: CircuitState) -> None:
        """
        Transition circuit to new state.

        Args:
            new_state: State to transition to

        AI: Logs all state transitions for debugging and monitoring.
        """
        old_state = self.state
        self.state = new_state
        self.last_state_change = datetime.now(UTC)

        logger.info(
            "Circuit breaker state transition",
            old_state=old_state.value,
            new_state=new_state.value,
            failure_count=self.failure_count,
            success_count=self.success_count,
        )

    def get_state(self) -> CircuitState:
        """
        Get current circuit state.

        Returns:
            Current CircuitState

        AI: For monitoring and health checks.
        """
        return self.state

    def get_stats(self) -> dict[str, Any]:
        """
        Get circuit breaker statistics.

        Returns:
            Dictionary with circuit breaker metrics

        AI: For monitoring dashboards and debugging.
        """
        return {
            "state": self.state.value,
            "failure_count": self.failure_count,
            "success_count": self.success_count,
            "failure_threshold": self.failure_threshold,
            "success_threshold": self.success_threshold,
            "timeout_seconds": self.timeout.total_seconds(),
            "last_failure_time": self.last_failure_time.isoformat() if self.last_failure_time else None,
            "last_state_change": self.last_state_change.isoformat(),
            "time_until_retry": self._time_until_retry(),
        }

    def reset(self) -> None:
        """
        Manually reset circuit breaker to CLOSED state.

        Clears all counters and timers.

        AI: Use for admin/debugging purposes or after manual service recovery.
        """
        old_state = self.state
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self.last_state_change = datetime.now(UTC)

        logger.warning("Circuit breaker manually reset", previous_state=old_state.value)
