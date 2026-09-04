"""
Error handling for connection management.

This module provides comprehensive error detection, logging, and recovery
for connection-related errors including WebSocket errors, authentication
failures, and security violations.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Error handling is now a focused, independently testable component.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Error handler requires many state tracking attributes and complex error processing logic

import json
import uuid
from collections.abc import Callable
from datetime import datetime
from typing import TYPE_CHECKING, Any

from ...config import get_config
from ...structured_logging.enhanced_logging_config import _resolve_log_base, get_logger

if TYPE_CHECKING:
    from collections.abc import Awaitable

logger = get_logger(__name__)

# Fatal error types that require immediate disconnection
FATAL_ERROR_TYPES = [
    "CRITICAL_WEBSOCKET_ERROR",
    "AUTHENTICATION_FAILURE",
    "SECURITY_VIOLATION",
    "MALFORMED_DATA",
    "PROTOCOL_VIOLATION",
]

# Critical WebSocket error types
CRITICAL_WEBSOCKET_ERRORS = [
    "CONNECTION_CLOSED_UNEXPECTEDLY",
    "INVALID_FRAME_FORMAT",
    "PROTOCOL_ERROR",
    "MESSAGE_TOO_LARGE",
]


class ConnectionErrorHandler:
    """
    Handles error detection, logging, and recovery for connection management.

    This class provides:
    - Error state detection and classification
    - Error logging to dedicated error log files
    - Connection termination for fatal errors
    - Connection-specific error handling
    - Error recovery mechanisms

    AI Agent: Single Responsibility - Error handling and recovery only.
    """

    def __init__(
        self,
        force_disconnect_callback: Callable[[uuid.UUID], "Awaitable[None]"],
        disconnect_connection_callback: Callable[[str], "Awaitable[bool]"],
        cleanup_dead_connections_callback: Callable[[uuid.UUID], "Awaitable[dict[str, Any]]"],
        get_player_session_callback: Callable[[uuid.UUID], str | None],
        get_session_connections_callback: Callable[[str], list[str]],
        get_player_websockets: Callable[[uuid.UUID], list[str]],
        get_online_players: Callable[[], dict[uuid.UUID, dict[str, Any]]],
        get_session_connections: Callable[[], dict[str, list[str]]],
        get_player_sessions: Callable[[], dict[uuid.UUID, str]],
    ) -> None:
        """
        Initialize the error handler.

        Args:
            force_disconnect_callback: Callback to force disconnect a player
            disconnect_connection_callback: Callback to disconnect a specific connection
            cleanup_dead_connections_callback: Callback to clean up dead connections
            get_player_session_callback: Callback to get player's current session
            get_session_connections_callback: Callback to get connections for a session
            get_player_websockets: Callback to get WebSocket connections for a player
            get_online_players: Callback to get online players dictionary
            get_session_connections: Callback to get session connections dictionary
            get_player_sessions: Callback to get player sessions dictionary
        """
        self.force_disconnect = force_disconnect_callback
        self.disconnect_connection = disconnect_connection_callback
        self.cleanup_dead_connections = cleanup_dead_connections_callback
        self.get_player_session = get_player_session_callback
        self.get_session_connections = get_session_connections_callback
        self.get_player_websockets = get_player_websockets
        self.get_online_players = get_online_players
        self.get_session_connections_dict = get_session_connections
        self.get_player_sessions = get_player_sessions

    async def detect_and_handle_error_state(
        self, player_id: uuid.UUID, error_type: str, error_details: str, connection_id: str | None = None
    ) -> dict[str, Any]:
        """
        Detect when a client is in an error state and handle it appropriately.

        Args:
            player_id: The player's ID
            error_type: Type of error detected
            error_details: Detailed error information
            connection_id: Optional specific connection ID that caused the error

        Returns:
            dict: Error handling results with detailed information
        """
        error_results: dict[str, Any] = {
            "player_id": player_id,
            "error_type": error_type,
            "error_details": error_details,
            "connection_id": connection_id,
            "connections_terminated": 0,
            "connections_kept": 0,
            "fatal_error": False,
            "success": False,
            "errors": [],
        }

        try:
            logger.error(
                "ERROR STATE DETECTED for player",
                player_id=player_id,
                error_type=error_type,
                error_details=error_details,
            )

            # Get detailed connection information
            websocket_connections = len(self.get_player_websockets(player_id))
            total_connections = websocket_connections

            # Get session information
            current_session = self.get_player_session(player_id)
            session_connections = self.get_session_connections(current_session) if current_session else []

            # Log the error state to a dedicated error log file
            error_log_entry = {
                "timestamp": datetime.now().isoformat(),
                "player_id": str(player_id),
                "error_type": error_type,
                "error_details": error_details,
                "connection_id": connection_id,
                "connections": {
                    "websocket_count": websocket_connections,
                    "total_connections": total_connections,
                    "online": player_id in self.get_online_players(),
                    "current_session": current_session,
                    "session_connections": len(session_connections),
                },
            }

            # Write to error log file using proper logging configuration
            config = get_config()
            # pylint: disable=no-member  # Pydantic FieldInfo dynamic attributes
            log_base = config.logging.log_base
            environment = config.logging.environment

            resolved_log_base = _resolve_log_base(log_base)
            error_log_path = resolved_log_base / environment / "connection_errors.log"
            error_log_path.parent.mkdir(parents=True, exist_ok=True)

            with open(error_log_path, "a", encoding="utf-8") as f:  # pylint: disable=unspecified-encoding  # Reason: Explicit UTF-8 encoding for log file
                f.write(json.dumps(error_log_entry) + "\n")

            # Determine if this is a fatal error
            error_results["fatal_error"] = error_type in FATAL_ERROR_TYPES

            if error_results["fatal_error"]:
                logger.error("FATAL ERROR: Terminating all connections for player", player_id=player_id)

                # Terminate all connections for the player
                await self.force_disconnect(player_id)
                error_results["connections_terminated"] = total_connections
                error_results["connections_kept"] = 0

            elif connection_id:
                # Handle connection-specific error (non-fatal)
                logger.warning(
                    "Connection-specific error: Terminating connection",
                    connection_id=connection_id,
                    player_id=player_id,
                )

                # Try to disconnect the specific connection
                if await self.disconnect_connection(connection_id):
                    error_results["connections_terminated"] = 1
                    error_results["connections_kept"] = total_connections - 1
                else:
                    error_results["errors"].append(f"Failed to disconnect connection {connection_id}")
                    error_results["connections_kept"] = total_connections

            else:
                # Non-fatal error, keep all connections alive
                logger.warning("Non-critical error: Keeping all connections alive for player", player_id=player_id)
                error_results["connections_terminated"] = 0
                error_results["connections_kept"] = total_connections

            error_results["success"] = True
            logger.info("Error handling completed for player", player_id=player_id, error_results=error_results)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Error state detection errors unpredictable, must handle gracefully
            error_msg = f"Error in detect_and_handle_error_state for {player_id}: {e}"
            logger.error(error_msg, exc_info=True)
            error_results["errors"].append(error_msg)
            error_results["success"] = False

        return error_results

    async def handle_websocket_error(
        self, player_id: uuid.UUID, connection_id: str, error_type: str, error_details: str
    ) -> dict[str, Any]:
        """
        Handle WebSocket-specific errors.

        Args:
            player_id: The player's ID
            connection_id: The WebSocket connection ID
            error_type: Type of WebSocket error
            error_details: Detailed error information

        Returns:
            dict: Error handling results
        """
        logger.warning(
            "WebSocket error",
            player_id=player_id,
            connection_id=connection_id,
            error_type=error_type,
            error_details=error_details,
        )

        # Check if this is a critical WebSocket error
        if error_type in CRITICAL_WEBSOCKET_ERRORS:
            return await self.detect_and_handle_error_state(
                player_id, "CRITICAL_WEBSOCKET_ERROR", f"{error_type}: {error_details}", connection_id
            )
        # Non-critical WebSocket error, just disconnect the specific connection
        return await self.detect_and_handle_error_state(
            player_id, "WEBSOCKET_ERROR", f"{error_type}: {error_details}", connection_id
        )

    async def handle_authentication_error(
        self, player_id: uuid.UUID, error_type: str, error_details: str
    ) -> dict[str, Any]:
        """
        Handle authentication-related errors.

        Args:
            player_id: The player's ID
            error_type: Type of authentication error
            error_details: Detailed error information

        Returns:
            dict: Error handling results
        """
        logger.error(
            "Authentication error for player", player_id=player_id, error_type=error_type, error_details=error_details
        )

        return await self.detect_and_handle_error_state(
            player_id, "AUTHENTICATION_FAILURE", f"{error_type}: {error_details}"
        )

    async def handle_security_violation(
        self, player_id: uuid.UUID, violation_type: str, violation_details: str
    ) -> dict[str, Any]:
        """
        Handle security violations.

        Args:
            player_id: The player's ID
            violation_type: Type of security violation
            violation_details: Detailed violation information

        Returns:
            dict: Error handling results
        """
        logger.error(
            "Security violation for player",
            player_id=player_id,
            violation_type=violation_type,
            violation_details=violation_details,
        )

        return await self.detect_and_handle_error_state(
            player_id, "SECURITY_VIOLATION", f"{violation_type}: {violation_details}"
        )

    async def recover_from_error(self, player_id: uuid.UUID, recovery_type: str = "FULL") -> dict[str, Any]:
        """
        Attempt to recover from an error state for a player.

        Args:
            player_id: The player's ID
            recovery_type: Type of recovery to attempt ("FULL", "CONNECTIONS_ONLY", "SESSION_ONLY")

        Returns:
            dict: Recovery results
        """
        recovery_results: dict[str, Any] = {
            "player_id": player_id,
            "recovery_type": recovery_type,
            "success": False,
            "connections_restored": 0,
            "sessions_cleared": 0,
            "errors": [],
        }

        try:
            logger.info("Attempting recovery for player", recovery_type=recovery_type, player_id=player_id)

            if recovery_type in ["FULL", "CONNECTIONS_ONLY"]:
                # Clean up any dead connections
                cleanup_results = await self.cleanup_dead_connections(player_id)
                recovery_results["connections_restored"] = cleanup_results.get("connections_cleaned", 0)

            if recovery_type in ["FULL", "SESSION_ONLY"]:
                # Clear session data if needed
                player_sessions = self.get_player_sessions()
                session_connections_dict = self.get_session_connections_dict()
                if player_id in player_sessions:
                    old_session = player_sessions[player_id]
                    if old_session in session_connections_dict:
                        del session_connections_dict[old_session]
                    del player_sessions[player_id]
                    recovery_results["sessions_cleared"] = 1

            recovery_results["success"] = True
            logger.info("Recovery completed for player", player_id=player_id, recovery_results=recovery_results)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Recovery errors unpredictable, must handle gracefully
            error_msg = f"Error during recovery for player {player_id}: {e}"
            logger.error(error_msg, exc_info=True)
            recovery_results["errors"].append(error_msg)
            recovery_results["success"] = False

        return recovery_results

    def get_error_statistics(
        self, online_players: dict[uuid.UUID, dict[str, Any]], player_websockets: dict[uuid.UUID, list[str]]
    ) -> dict[str, Any]:
        """
        Get error handling statistics.

        Args:
            online_players: Online players dictionary
            player_websockets: Player to WebSocket connection mapping

        Returns:
            dict: Error statistics
        """
        # Get the proper error log path using logging configuration
        config = get_config()
        # pylint: disable=no-member  # Pydantic FieldInfo dynamic attributes
        log_base = config.logging.log_base
        environment = config.logging.environment

        resolved_log_base = _resolve_log_base(log_base)
        error_log_path = resolved_log_base / environment / "connection_errors.log"

        return {
            "total_players": len(online_players),
            "total_connections": sum(len(conns) for conns in player_websockets.values()),
            "active_sessions": len(self.get_session_connections_dict()),
            "players_with_sessions": len(self.get_player_sessions()),
            "error_log_path": str(error_log_path),
        }
