"""
Test data for dual connection system testing scenarios.

This module provides comprehensive test data for various dual connection
scenarios including session management, error handling, and performance testing.
"""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta
from typing import Any


@dataclass
class TestPlayer:
    """Test player data structure"""

    player_id: str
    username: str
    session_id: str
    auth_token: str
    created_at: datetime
    last_activity: datetime
    connection_count: int = 0
    is_online: bool = False


@dataclass
class TestConnection:
    """Test connection data structure"""

    connection_id: str
    player_id: str
    connection_type: str  # 'websocket' or 'sse'
    session_id: str
    established_at: datetime
    last_ping: datetime
    is_healthy: bool = True
    message_count: int = 0


@dataclass
class TestSession:
    """Test session data structure"""

    session_id: str
    player_id: str
    created_at: datetime
    last_activity: datetime
    connection_count: int
    is_active: bool = True


@dataclass
class TestMessage:
    """Test message data structure"""

    message_id: str
    player_id: str
    message_type: str
    content: str
    timestamp: datetime
    delivery_status: str = "pending"  # 'pending', 'delivered', 'failed'
    connection_ids: list[str] = None


class DualConnectionTestData:
    """Comprehensive test data for dual connection scenarios"""

    def __init__(self):
        self.players: list[TestPlayer] = []
        self.connections: list[TestConnection] = []
        self.sessions: list[TestSession] = []
        self.messages: list[TestMessage] = []
        self._generate_test_data()

    def _generate_test_data(self):
        """Generate comprehensive test data"""
        self._generate_players()
        self._generate_sessions()
        self._generate_connections()
        self._generate_messages()

    def _generate_players(self):
        """Generate test players with various scenarios"""
        base_time = datetime.now(UTC)

        # Single connection players
        for i in range(10):
            player = TestPlayer(
                player_id=f"single_player_{i}",
                username=f"SingleUser{i}",
                session_id=f"session_single_{i}",
                auth_token=f"token_single_{i}",
                created_at=base_time - timedelta(hours=i),
                last_activity=base_time - timedelta(minutes=i * 5),
                connection_count=1,
                is_online=True,
            )
            self.players.append(player)

        # Dual connection players
        for i in range(15):
            player = TestPlayer(
                player_id=f"dual_player_{i}",
                username=f"DualUser{i}",
                session_id=f"session_dual_{i}",
                auth_token=f"token_dual_{i}",
                created_at=base_time - timedelta(hours=i + 10),
                last_activity=base_time - timedelta(minutes=i * 3),
                connection_count=2,
                is_online=True,
            )
            self.players.append(player)

        # Multiple connection players
        for i in range(5):
            player = TestPlayer(
                player_id=f"multi_player_{i}",
                username=f"MultiUser{i}",
                session_id=f"session_multi_{i}",
                auth_token=f"token_multi_{i}",
                created_at=base_time - timedelta(hours=i + 25),
                last_activity=base_time - timedelta(minutes=i * 2),
                connection_count=3,
                is_online=True,
            )
            self.players.append(player)

        # Offline players
        for i in range(10):
            player = TestPlayer(
                player_id=f"offline_player_{i}",
                username=f"OfflineUser{i}",
                session_id=f"session_offline_{i}",
                auth_token=f"token_offline_{i}",
                created_at=base_time - timedelta(hours=i + 30),
                last_activity=base_time - timedelta(hours=i + 1),
                connection_count=0,
                is_online=False,
            )
            self.players.append(player)

    def _generate_sessions(self):
        """Generate test sessions"""
        base_time = datetime.now(UTC)

        for player in self.players:
            if player.is_online:
                session = TestSession(
                    session_id=player.session_id,
                    player_id=player.player_id,
                    created_at=player.created_at,
                    last_activity=player.last_activity,
                    connection_count=player.connection_count,
                    is_active=True,
                )
                self.sessions.append(session)

    def _generate_connections(self):
        """Generate test connections"""
        base_time = datetime.now(UTC)

        for player in self.players:
            if not player.is_online:
                continue

            # Generate connections based on player type
            if player.connection_count >= 1:
                # WebSocket connection
                ws_conn = TestConnection(
                    connection_id=f"ws_{player.player_id}",
                    player_id=player.player_id,
                    connection_type="websocket",
                    session_id=player.session_id,
                    established_at=base_time - timedelta(minutes=30),
                    last_ping=base_time - timedelta(minutes=1),
                    is_healthy=True,
                    message_count=10,
                )
                self.connections.append(ws_conn)

            if player.connection_count >= 2:
                # SSE connection
                sse_conn = TestConnection(
                    connection_id=f"sse_{player.player_id}",
                    player_id=player.player_id,
                    connection_type="sse",
                    session_id=player.session_id,
                    established_at=base_time - timedelta(minutes=25),
                    last_ping=base_time - timedelta(minutes=2),
                    is_healthy=True,
                    message_count=8,
                )
                self.connections.append(sse_conn)

            if player.connection_count >= 3:
                # Additional WebSocket connection
                ws2_conn = TestConnection(
                    connection_id=f"ws2_{player.player_id}",
                    player_id=player.player_id,
                    connection_type="websocket",
                    session_id=player.session_id,
                    established_at=base_time - timedelta(minutes=20),
                    last_ping=base_time - timedelta(minutes=3),
                    is_healthy=True,
                    message_count=5,
                )
                self.connections.append(ws2_conn)

    def _generate_messages(self):
        """Generate test messages"""
        base_time = datetime.now(UTC)

        message_types = [
            "chat",
            "system",
            "notification",
            "command",
            "error",
            "status",
            "update",
            "broadcast",
            "whisper",
            "emote",
        ]

        for i, player in enumerate(self.players[:20]):  # Only for first 20 players
            for j in range(5):  # 5 messages per player
                message = TestMessage(
                    message_id=f"msg_{player.player_id}_{j}",
                    player_id=player.player_id,
                    message_type=message_types[j % len(message_types)],
                    content=f"Test message {j} for {player.username}",
                    timestamp=base_time - timedelta(minutes=j * 10),
                    delivery_status="delivered" if j < 3 else "pending",
                    connection_ids=[
                        conn.connection_id for conn in self.connections if conn.player_id == player.player_id
                    ],
                )
                self.messages.append(message)

    def get_players_by_connection_type(self, connection_type: str) -> list[TestPlayer]:
        """Get players with specific connection type"""
        if connection_type == "single":
            return [p for p in self.players if p.connection_count == 1]
        elif connection_type == "dual":
            return [p for p in self.players if p.connection_count == 2]
        elif connection_type == "multi":
            return [p for p in self.players if p.connection_count >= 3]
        elif connection_type == "offline":
            return [p for p in self.players if not p.is_online]
        else:
            return self.players

    def get_connections_by_type(self, connection_type: str) -> list[TestConnection]:
        """Get connections by type"""
        return [c for c in self.connections if c.connection_type == connection_type]

    def get_connections_by_player(self, player_id: str) -> list[TestConnection]:
        """Get all connections for a specific player"""
        return [c for c in self.connections if c.player_id == player_id]

    def get_messages_by_player(self, player_id: str) -> list[TestMessage]:
        """Get all messages for a specific player"""
        return [m for m in self.messages if m.player_id == player_id]

    def get_unhealthy_connections(self) -> list[TestConnection]:
        """Get connections that are marked as unhealthy"""
        return [c for c in self.connections if not c.is_healthy]

    def get_old_sessions(self, hours: int = 1) -> list[TestSession]:
        """Get sessions older than specified hours"""
        cutoff_time = datetime.utcnow() - timedelta(hours=hours)
        return [s for s in self.sessions if s.last_activity < cutoff_time]

    def get_pending_messages(self) -> list[TestMessage]:
        """Get messages with pending delivery status"""
        return [m for m in self.messages if m.delivery_status == "pending"]

    def get_failed_messages(self) -> list[TestMessage]:
        """Get messages with failed delivery status"""
        return [m for m in self.messages if m.delivery_status == "failed"]

    def to_dict(self) -> dict[str, Any]:
        """Convert test data to dictionary format"""
        return {
            "players": [asdict(p) for p in self.players],
            "connections": [asdict(c) for c in self.connections],
            "sessions": [asdict(s) for s in self.sessions],
            "messages": [asdict(m) for m in self.messages],
        }

    def get_statistics(self) -> dict[str, Any]:
        """Get statistics about the test data"""
        return {
            "total_players": len(self.players),
            "online_players": len([p for p in self.players if p.is_online]),
            "offline_players": len([p for p in self.players if not p.is_online]),
            "single_connection_players": len(self.get_players_by_connection_type("single")),
            "dual_connection_players": len(self.get_players_by_connection_type("dual")),
            "multi_connection_players": len(self.get_players_by_connection_type("multi")),
            "total_connections": len(self.connections),
            "websocket_connections": len(self.get_connections_by_type("websocket")),
            "sse_connections": len(self.get_connections_by_type("sse")),
            "healthy_connections": len([c for c in self.connections if c.is_healthy]),
            "unhealthy_connections": len(self.get_unhealthy_connections()),
            "total_sessions": len(self.sessions),
            "active_sessions": len([s for s in self.sessions if s.is_active]),
            "total_messages": len(self.messages),
            "delivered_messages": len([m for m in self.messages if m.delivery_status == "delivered"]),
            "pending_messages": len(self.get_pending_messages()),
            "failed_messages": len(self.get_failed_messages()),
        }


# Performance test data generators
class PerformanceTestData:
    """Test data generators for performance testing scenarios"""

    @staticmethod
    def generate_load_test_players(count: int) -> list[TestPlayer]:
        """Generate players for load testing"""
        players = []
        base_time = datetime.now(UTC)

        for i in range(count):
            player = TestPlayer(
                player_id=f"load_player_{i}",
                username=f"LoadUser{i}",
                session_id=f"load_session_{i}",
                auth_token=f"load_token_{i}",
                created_at=base_time - timedelta(minutes=i),
                last_activity=base_time - timedelta(seconds=i * 10),
                connection_count=2,  # Dual connections for load testing
                is_online=True,
            )
            players.append(player)

        return players

    @staticmethod
    def generate_stress_test_connections(player_count: int, connections_per_player: int = 4) -> list[TestConnection]:
        """Generate connections for stress testing"""
        connections = []
        base_time = datetime.now(UTC)

        for i in range(player_count):
            for j in range(connections_per_player):
                conn_type = "websocket" if j % 2 == 0 else "sse"
                connection = TestConnection(
                    connection_id=f"stress_{i}_{j}",
                    player_id=f"stress_player_{i}",
                    connection_type=conn_type,
                    session_id=f"stress_session_{i}",
                    established_at=base_time - timedelta(minutes=j),
                    last_ping=base_time - timedelta(seconds=j * 30),
                    is_healthy=j % 10 != 0,  # 10% unhealthy connections
                    message_count=j * 5,
                )
                connections.append(connection)

        return connections

    @staticmethod
    def generate_message_burst(count: int, player_id: str) -> list[TestMessage]:
        """Generate a burst of messages for testing"""
        messages = []
        base_time = datetime.now(UTC)

        for i in range(count):
            message = TestMessage(
                message_id=f"burst_{player_id}_{i}",
                player_id=player_id,
                message_type="test",
                content=f"Burst message {i}",
                timestamp=base_time - timedelta(milliseconds=i * 10),
                delivery_status="pending",
            )
            messages.append(message)

        return messages


# Error scenario test data
class ErrorTestData:
    """Test data for error handling scenarios"""

    @staticmethod
    def get_authentication_errors() -> list[dict[str, Any]]:
        """Get test data for authentication errors"""
        return [
            {
                "player_id": "invalid_player",
                "auth_token": "invalid_token",
                "error_type": "authentication_error",
                "error_message": "Invalid authentication token",
            },
            {
                "player_id": "expired_player",
                "auth_token": "expired_token",
                "error_type": "authentication_error",
                "error_message": "Authentication token expired",
            },
            {
                "player_id": "malformed_player",
                "auth_token": "malformed_token_!@#",
                "error_type": "authentication_error",
                "error_message": "Malformed authentication token",
            },
        ]

    @staticmethod
    def get_connection_errors() -> list[dict[str, Any]]:
        """Get test data for connection errors"""
        return [
            {
                "player_id": "timeout_player",
                "connection_type": "websocket",
                "error_type": "connection_timeout",
                "error_message": "Connection timeout",
            },
            {
                "player_id": "network_player",
                "connection_type": "sse",
                "error_type": "network_error",
                "error_message": "Network connection lost",
            },
            {
                "player_id": "protocol_player",
                "connection_type": "websocket",
                "error_type": "protocol_error",
                "error_message": "Invalid protocol message",
            },
        ]

    @staticmethod
    def get_session_errors() -> list[dict[str, Any]]:
        """Get test data for session errors"""
        return [
            {
                "player_id": "invalid_session_player",
                "session_id": "invalid_session",
                "error_type": "session_error",
                "error_message": "Invalid session ID",
            },
            {
                "player_id": "expired_session_player",
                "session_id": "expired_session",
                "error_type": "session_error",
                "error_message": "Session expired",
            },
            {
                "player_id": "conflict_session_player",
                "session_id": "conflict_session",
                "error_type": "session_error",
                "error_message": "Session conflict detected",
            },
        ]


# Test data for specific scenarios
class ScenarioTestData:
    """Test data for specific testing scenarios"""

    @staticmethod
    def get_dual_connection_scenario() -> dict[str, Any]:
        """Get test data for dual connection scenario"""
        return {
            "player_id": "dual_test_player",
            "websocket_connection": {
                "connection_id": "ws_dual_test",
                "connection_type": "websocket",
                "session_id": "dual_test_session",
                "is_healthy": True,
            },
            "sse_connection": {
                "connection_id": "sse_dual_test",
                "connection_type": "sse",
                "session_id": "dual_test_session",
                "is_healthy": True,
            },
            "expected_behavior": {
                "both_connections_active": True,
                "messages_delivered_to_both": True,
                "session_shared": True,
            },
        }

    @staticmethod
    def get_session_switch_scenario() -> dict[str, Any]:
        """Get test data for session switching scenario"""
        return {
            "player_id": "session_switch_player",
            "old_session": {"session_id": "old_session_123", "connections": ["ws_old", "sse_old"], "active": True},
            "new_session": {"session_id": "new_session_456", "connections": [], "active": False},
            "expected_behavior": {
                "old_connections_disconnected": True,
                "new_session_created": True,
                "player_reconnects": True,
            },
        }

    @staticmethod
    def get_connection_cleanup_scenario() -> dict[str, Any]:
        """Get test data for connection cleanup scenario"""
        return {
            "player_id": "cleanup_test_player",
            "healthy_connections": [
                {
                    "connection_id": "ws_healthy",
                    "connection_type": "websocket",
                    "last_ping": datetime.utcnow() - timedelta(minutes=1),
                    "is_healthy": True,
                }
            ],
            "unhealthy_connections": [
                {
                    "connection_id": "ws_unhealthy",
                    "connection_type": "websocket",
                    "last_ping": datetime.utcnow() - timedelta(minutes=10),
                    "is_healthy": False,
                },
                {
                    "connection_id": "sse_unhealthy",
                    "connection_type": "sse",
                    "last_ping": datetime.utcnow() - timedelta(minutes=15),
                    "is_healthy": False,
                },
            ],
            "expected_behavior": {
                "unhealthy_connections_removed": True,
                "healthy_connections_preserved": True,
                "cleanup_logged": True,
            },
        }


# Export the main test data instance
test_data = DualConnectionTestData()
