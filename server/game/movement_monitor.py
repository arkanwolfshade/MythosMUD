"""
Movement monitoring and validation system for MythosMUD.

This module provides comprehensive monitoring, validation, and logging
for the movement system to ensure data integrity and performance.

As noted in the Pnakotic Manuscripts, proper monitoring of complex
systems is essential for maintaining the integrity of our eldritch architecture.
"""

import threading
from collections import defaultdict
from datetime import UTC, datetime
from typing import Any

from ..logging.enhanced_logging_config import get_logger


class MovementMonitor:
    """
    Comprehensive monitoring system for the movement system.

    This class provides:
    - Real-time metrics tracking
    - Data integrity validation
    - Performance monitoring
    - Detailed logging for debugging
    - Alert system for anomalies
    """

    def __init__(self):
        """Initialize the movement monitor with empty metrics."""
        self._logger = get_logger("MovementMonitor")
        self._lock = threading.RLock()

        # Metrics tracking
        self._movement_count = 0
        self._failed_movements = 0
        self._concurrent_movements = 0
        self._max_concurrent_movements = 0
        self._movement_times = []
        self._room_occupancy = defaultdict(int)
        self._player_movements = defaultdict(int)

        # Validation tracking
        self._integrity_checks = 0
        self._integrity_violations = 0
        self._last_validation_time = None

        # Performance tracking
        self._start_time = datetime.now(UTC)
        self._last_movement_time = None

        # Alert thresholds
        self._alert_thresholds = {
            "max_concurrent_movements": 50,
            "movement_failure_rate": 0.1,  # 10%
            "integrity_violation_rate": 0.01,  # 1%
            "avg_movement_time_ms": 1000,  # 1 second
        }

        self._logger.info("MovementMonitor initialized")

    def record_movement_attempt(
        self, player_id: str, from_room_id: str, to_room_id: str, success: bool, duration_ms: float
    ):
        """Record a movement attempt with metrics."""
        with self._lock:
            self._movement_count += 1
            if not success:
                self._failed_movements += 1

            self._movement_times.append(duration_ms)
            self._player_movements[player_id] += 1
            self._last_movement_time = datetime.now(UTC)

            # Update room occupancy
            if success:
                self._room_occupancy[from_room_id] = max(0, self._room_occupancy[from_room_id] - 1)
                self._room_occupancy[to_room_id] += 1

            # Log movement details
            self._logger.debug(
                f"Movement recorded: {player_id} {from_room_id}->{to_room_id} "
                f"(success={success}, duration={duration_ms:.2f}ms)"
            )

            # Check for alerts
            self._check_alerts()

    def record_concurrent_movement(self, count: int):
        """Record concurrent movement count."""
        with self._lock:
            self._concurrent_movements = count
            self._max_concurrent_movements = max(self._max_concurrent_movements, count)

    def record_integrity_check(self, violation_found: bool):
        """Record an integrity check result."""
        with self._lock:
            self._integrity_checks += 1
            if violation_found:
                self._integrity_violations += 1
            self._last_validation_time = datetime.now(UTC)

    def validate_room_integrity(self, rooms: dict[str, Any]) -> dict[str, Any]:
        """
        Validate room data integrity.

        Returns a dictionary with validation results and any violations found.
        """
        violations = []
        total_players = 0

        # Check for players in multiple rooms
        player_rooms: dict[str, list[str]] = {}
        for room_id, room in rooms.items():
            if hasattr(room, "get_players"):
                players = room.get_players()
                total_players += len(players)

                for player_id in players:
                    if player_id in player_rooms:
                        violations.append(
                            f"Player {player_id} found in multiple rooms: {player_rooms[player_id]} and {room_id}"
                        )
                    else:
                        player_rooms[player_id] = room_id

        # Check for orphaned players (players not in any room)
        orphaned_players = set()
        for _room_id, room in rooms.items():
            if hasattr(room, "get_players"):
                for player_id in room.get_players():
                    orphaned_players.discard(player_id)

        if orphaned_players:
            violations.append(f"Orphaned players found: {orphaned_players}")

        # Calculate metrics
        avg_occupancy = total_players / len(rooms) if rooms else 0
        max_occupancy = max(
            (len(room.get_players()) for room in rooms.values() if hasattr(room, "get_players")), default=0
        )

        result = {
            "valid": len(violations) == 0,
            "violations": violations,
            "total_rooms": len(rooms),
            "total_players": total_players,
            "avg_occupancy": avg_occupancy,
            "max_occupancy": max_occupancy,
            "timestamp": datetime.now(UTC),
        }

        self.record_integrity_check(len(violations) > 0)

        if violations:
            self._logger.warning("Room integrity violations found", violations=violations)
        else:
            self._logger.debug("Room integrity check passed")

        return result

    def get_metrics(self) -> dict[str, Any]:
        """Get comprehensive movement metrics."""
        with self._lock:
            total_movements = self._movement_count
            success_rate = (total_movements - self._failed_movements) / total_movements if total_movements > 0 else 1.0
            failure_rate = self._failed_movements / total_movements if total_movements > 0 else 0.0

            avg_movement_time = sum(self._movement_times) / len(self._movement_times) if self._movement_times else 0
            max_movement_time = max(self._movement_times) if self._movement_times else 0
            min_movement_time = min(self._movement_times) if self._movement_times else 0

            uptime = (datetime.now(UTC) - self._start_time).total_seconds()
            movements_per_second = total_movements / uptime if uptime > 0 else 0

            integrity_rate = (
                (self._integrity_checks - self._integrity_violations) / self._integrity_checks
                if self._integrity_checks > 0
                else 1.0
            )

            return {
                "total_movements": total_movements,
                "successful_movements": total_movements - self._failed_movements,
                "failed_movements": self._failed_movements,
                "success_rate": success_rate,
                "failure_rate": failure_rate,
                "current_concurrent_movements": self._concurrent_movements,
                "max_concurrent_movements": self._max_concurrent_movements,
                "avg_movement_time_ms": avg_movement_time,
                "max_movement_time_ms": max_movement_time,
                "min_movement_time_ms": min_movement_time,
                "movements_per_second": movements_per_second,
                "uptime_seconds": uptime,
                "integrity_checks": self._integrity_checks,
                "integrity_violations": self._integrity_violations,
                "integrity_rate": integrity_rate,
                "last_movement_time": self._last_movement_time,
                "last_validation_time": self._last_validation_time,
                "room_occupancy": dict(self._room_occupancy),
                "player_movement_counts": dict(self._player_movements),
                "timestamp": datetime.now(UTC),
            }

    def get_alerts(self) -> list[str]:
        """Get current alerts based on thresholds."""
        alerts = []
        metrics = self.get_metrics()

        if metrics["current_concurrent_movements"] > self._alert_thresholds["max_concurrent_movements"]:
            alerts.append(f"High concurrent movements: {metrics['current_concurrent_movements']}")

        if metrics["failure_rate"] > self._alert_thresholds["movement_failure_rate"]:
            alerts.append(f"High failure rate: {metrics['failure_rate']:.2%}")

        if metrics["integrity_rate"] < (1 - self._alert_thresholds["integrity_violation_rate"]):
            alerts.append(f"High integrity violation rate: {1 - metrics['integrity_rate']:.2%}")

        if metrics["avg_movement_time_ms"] > self._alert_thresholds["avg_movement_time_ms"]:
            alerts.append(f"Slow average movement time: {metrics['avg_movement_time_ms']:.2f}ms")

        return alerts

    def _check_alerts(self):
        """Check for alerts and log them."""
        alerts = self.get_alerts()
        if alerts:
            self._logger.warning("Movement system alerts", alerts=alerts)

    def reset_metrics(self):
        """Reset all metrics (useful for testing)."""
        with self._lock:
            self._movement_count = 0
            self._failed_movements = 0
            self._concurrent_movements = 0
            self._max_concurrent_movements = 0
            self._movement_times.clear()
            self._room_occupancy.clear()
            self._player_movements.clear()
            self._integrity_checks = 0
            self._integrity_violations = 0
            self._start_time = datetime.now(UTC)
            self._last_movement_time = None
            self._last_validation_time = None
            self._logger.info("Movement metrics reset")

    def log_performance_summary(self):
        """Log a comprehensive performance summary."""
        metrics = self.get_metrics()
        alerts = self.get_alerts()

        self._logger.info(
            f"Movement Performance Summary:\n"
            f"  Total Movements: {metrics['total_movements']}\n"
            f"  Success Rate: {metrics['success_rate']:.2%}\n"
            f"  Avg Movement Time: {metrics['avg_movement_time_ms']:.2f}ms\n"
            f"  Current Concurrent: {metrics['current_concurrent_movements']}\n"
            f"  Max Concurrent: {metrics['max_concurrent_movements']}\n"
            f"  Integrity Rate: {metrics['integrity_rate']:.2%}\n"
            f"  Uptime: {metrics['uptime_seconds']:.1f}s\n"
            f"  Alerts: {len(alerts)}"
        )

        if alerts:
            for alert in alerts:
                self._logger.warning("Alert", alert=alert)


# Global monitor instance
_movement_monitor: MovementMonitor | None = None
_monitor_lock = threading.RLock()


def get_movement_monitor() -> MovementMonitor:
    """Get the global movement monitor instance."""
    global _movement_monitor

    with _monitor_lock:
        if _movement_monitor is None:
            _movement_monitor = MovementMonitor()

        return _movement_monitor


def reset_movement_monitor():
    """Reset the global movement monitor (useful for testing)."""
    global _movement_monitor

    with _monitor_lock:
        if _movement_monitor:
            _movement_monitor.reset_metrics()
        else:
            _movement_monitor = MovementMonitor()
