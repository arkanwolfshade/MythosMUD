"""
Connection state machine for NATS messaging.

Implements a robust state machine for managing NATS connection lifecycle
with automatic reconnection, circuit breaker integration, and health tracking.

AI: State machines eliminate implicit state bugs and make connection logic testable.
"""

from datetime import UTC, datetime
from enum import Enum
from typing import Any

from statemachine import State, StateMachine

from ..logging_config import get_logger

logger = get_logger(__name__)


class ConnectionEvent(Enum):
    """
    Events that trigger state transitions.

    AI: Explicit events make the FSM deterministic and testable.
    """

    CONNECT_REQUESTED = "connect_requested"
    CONNECTED = "connected"
    CONNECTION_FAILED = "connection_failed"
    DISCONNECTED = "disconnected"
    RECONNECT_REQUESTED = "reconnect_requested"
    CIRCUIT_OPENED = "circuit_opened"
    CIRCUIT_CLOSED = "circuit_closed"
    HEALTH_CHECK_FAILED = "health_check_failed"
    HEALTH_CHECK_PASSED = "health_check_passed"


class NATSConnectionStateMachine(StateMachine):
    """
    State machine for NATS connection lifecycle.

    States:
    - disconnected: Not connected to NATS
    - connecting: Attempting to establish connection
    - connected: Successfully connected and healthy
    - reconnecting: Attempting to restore lost connection
    - circuit_open: Circuit breaker tripped, not attempting connections
    - degraded: Connected but failing health checks

    Transitions:
    - disconnected → connecting: connect_requested
    - connecting → connected: connected
    - connecting → disconnected: connection_failed
    - connected → disconnected: disconnected
    - connected → degraded: health_check_failed
    - connected → reconnecting: disconnected (automatic)
    - reconnecting → connected: connected
    - reconnecting → circuit_open: circuit_opened (too many failures)
    - circuit_open → disconnected: circuit_closed (timeout expired)
    - degraded → connected: health_check_passed
    - degraded → disconnected: disconnected

    AI: This FSM prevents invalid state transitions and makes connection logic explicit.
    """

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
    disconnect = connected.to(disconnected) | degraded.to(disconnected)
    start_reconnect = disconnected.to(reconnecting)
    degrade = connected.to(degraded)
    recover = degraded.to(connected)
    open_circuit = reconnecting.to(circuit_open)
    close_circuit = circuit_open.to(disconnected)

    def __init__(self, connection_id: str, max_reconnect_attempts: int = 5):
        """
        Initialize connection state machine.

        Args:
            connection_id: Unique identifier for this connection
            max_reconnect_attempts: Maximum reconnection attempts before opening circuit

        AI: State machine tracks metadata for debugging and monitoring.
        """
        # Set attributes BEFORE super().__init__() because on_enter_state is called during init
        self.connection_id = connection_id
        self.max_reconnect_attempts = max_reconnect_attempts

        # Metadata tracking
        self.reconnect_attempts = 0
        self.last_connected_time: datetime | None = None
        self.last_error: Exception | None = None
        self.total_connections = 0
        self.total_disconnections = 0

        # Initialize state machine (triggers on_enter_state for initial state)
        super().__init__()

        logger.info(
            "NATS connection state machine initialized",
            connection_id=connection_id,
            initial_state=self.current_state.id,
        )

    def on_enter_state(self, state: State, event=None, **kwargs) -> None:
        """
        Called whenever state machine enters a new state.

        Logs state transitions for debugging and monitoring.

        Args:
            state: New state being entered
            event: Event that triggered the transition (optional)
            **kwargs: Additional event data from state machine

        AI: Centralized logging for all state transitions aids debugging.
        """
        logger.info(
            "NATS connection state transition",
            connection_id=self.connection_id,
            trigger_event=str(event) if event else "unknown",
            to_state=state.id,
            reconnect_attempts=self.reconnect_attempts,
        )

    def on_connect(self) -> None:
        """
        Handler for connect transition.

        Resets reconnection counter and prepares for connection attempt.

        AI: Transition handlers encapsulate state-specific logic.
        """
        self.reconnect_attempts = 0
        logger.debug("Starting NATS connection attempt", connection_id=self.connection_id)

    def on_connected_successfully(self) -> None:
        """
        Handler for successful connection.

        Records connection time and increments connection counter.

        AI: Successful connections reset failure tracking.
        """
        self.last_connected_time = datetime.now(UTC)
        self.total_connections += 1
        self.reconnect_attempts = 0

        logger.info(
            "NATS connection established",
            connection_id=self.connection_id,
            total_connections=self.total_connections,
        )

    def on_connection_failed(self, error: Exception | None = None) -> None:
        """
        Handler for connection failure.

        Records error and increments failure counter.

        Args:
            error: Exception that caused the failure

        AI: Failure tracking enables circuit breaker logic.
        """
        self.last_error = error
        self.reconnect_attempts += 1

        logger.warning(
            "NATS connection failed",
            connection_id=self.connection_id,
            attempts=self.reconnect_attempts,
            max_attempts=self.max_reconnect_attempts,
            error=str(error) if error else "unknown",
        )

    def on_disconnect(self) -> None:
        """
        Handler for disconnection.

        Increments disconnection counter.

        AI: Track disconnections for monitoring connection stability.
        """
        self.total_disconnections += 1

        logger.info(
            "NATS connection disconnected",
            connection_id=self.connection_id,
            total_disconnections=self.total_disconnections,
        )

    def on_start_reconnect(self) -> None:
        """
        Handler for starting reconnection.

        Checks if circuit breaker should be triggered.

        AI: Automatic circuit breaker integration.
        """
        if self.reconnect_attempts >= self.max_reconnect_attempts:
            logger.error(
                "Maximum reconnection attempts reached, opening circuit",
                connection_id=self.connection_id,
                attempts=self.reconnect_attempts,
            )
            # Caller should trigger open_circuit transition
        else:
            logger.info(
                "Starting NATS reconnection attempt",
                connection_id=self.connection_id,
                attempt=self.reconnect_attempts + 1,
                max_attempts=self.max_reconnect_attempts,
            )

    def on_open_circuit(self) -> None:
        """
        Handler for circuit breaker opening.

        Logs circuit open event for alerting.

        AI: Circuit open events should trigger alerts.
        """
        logger.critical(
            "NATS connection circuit breaker opened",
            connection_id=self.connection_id,
            attempts=self.reconnect_attempts,
        )

    def on_close_circuit(self) -> None:
        """
        Handler for circuit breaker closing.

        Resets failure counters.

        AI: Circuit closure allows fresh connection attempts.
        """
        self.reconnect_attempts = 0
        self.last_error = None

        logger.info(
            "NATS connection circuit breaker closed",
            connection_id=self.connection_id,
        )

    def on_degrade(self) -> None:
        """
        Handler for connection degradation.

        Logs degraded state for monitoring.

        AI: Degraded state indicates connection issues without full failure.
        """
        logger.warning(
            "NATS connection degraded",
            connection_id=self.connection_id,
            last_connected=self.last_connected_time.isoformat() if self.last_connected_time else None,
        )

    def on_recover(self) -> None:
        """
        Handler for recovery from degraded state.

        Logs recovery for monitoring.

        AI: Recovery tracking shows system resilience.
        """
        logger.info(
            "NATS connection recovered from degraded state",
            connection_id=self.connection_id,
        )

    def can_attempt_connection(self) -> bool:
        """
        Check if connection attempt is allowed in current state.

        Returns:
            True if connection can be attempted, False otherwise

        AI: Guard method prevents invalid connection attempts.
        """
        return self.current_state in [self.disconnected, self.reconnecting, self.connecting]

    def should_open_circuit(self) -> bool:
        """
        Check if circuit breaker should be opened.

        Returns:
            True if max attempts reached, False otherwise

        AI: Circuit breaker decision logic.
        """
        return self.reconnect_attempts >= self.max_reconnect_attempts

    def get_stats(self) -> dict[str, Any]:
        """
        Get connection statistics.

        Returns:
            Dictionary with connection metrics

        AI: For monitoring dashboards and debugging.
        """
        return {
            "connection_id": self.connection_id,
            "current_state": self.current_state.id,
            "reconnect_attempts": self.reconnect_attempts,
            "max_reconnect_attempts": self.max_reconnect_attempts,
            "total_connections": self.total_connections,
            "total_disconnections": self.total_disconnections,
            "last_connected_time": self.last_connected_time.isoformat() if self.last_connected_time else None,
            "last_error": str(self.last_error) if self.last_error else None,
        }

    def reset(self) -> None:
        """
        Reset state machine to initial state.

        Clears all counters and metadata.

        AI: For testing and manual recovery.
        """
        # Transition to disconnected if not already there
        if self.current_state != self.disconnected:
            if self.current_state == self.connected:
                self.disconnect()
            elif self.current_state == self.circuit_open:
                self.close_circuit()
            elif self.current_state in [self.connecting, self.reconnecting]:
                self.connection_failed()
            elif self.current_state == self.degraded:
                self.disconnect()

        # Reset counters
        self.reconnect_attempts = 0
        self.last_error = None
        self.total_connections = 0
        self.total_disconnections = 0
        self.last_connected_time = None

        logger.warning(
            "NATS connection state machine reset",
            connection_id=self.connection_id,
        )
