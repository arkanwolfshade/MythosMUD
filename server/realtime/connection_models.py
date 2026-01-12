"""
Data models for connection management.

This module defines data structures used by the connection manager
for tracking connection state and metadata.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Connection models require many fields to capture complete connection state

import uuid
from dataclasses import dataclass


@dataclass
class ConnectionMetadata:
    """
    Metadata for tracking connection details in the WebSocket-only system.

    This dataclass stores information about each connection to enable
    proper management of multiple connections per player.
    """

    connection_id: str
    player_id: uuid.UUID
    connection_type: str  # "websocket"
    established_at: float
    last_seen: float
    is_healthy: bool
    session_id: str | None = None  # For tracking new game client sessions
    token: str | None = None  # JWT token for periodic revalidation
    last_token_validation: float | None = None  # Timestamp of last token validation
