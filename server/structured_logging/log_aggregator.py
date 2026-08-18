"""
Log aggregation and centralized collection system for MythosMUD server.

This module provides centralized log collection, aggregation, and processing
capabilities for the MythosMUD server, enabling better monitoring and analysis.

As noted in the Pnakotic Manuscripts, proper aggregation of knowledge is
essential for understanding the deeper patterns and mysteries of our systems.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments  # Reason: Log aggregator requires many state tracking attributes and complex aggregation logic

import json
import queue
import threading
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from ..structured_logging.enhanced_logging_config import get_logger
from .log_time_formats import LOG_EXPORT_TIMESTAMP, LOG_HOUR_BUCKET

logger = get_logger(__name__)


@dataclass
class LogEntry:  # pylint: disable=too-many-instance-attributes  # Reason: Log entry dataclass requires many fields to capture complete log entry context
    """Represents a single log entry."""

    timestamp: datetime
    level: str
    logger_name: str
    message: str
    data: dict[str, object] = field(default_factory=dict)
    correlation_id: str | None = None
    user_id: str | None = None
    session_id: str | None = None


@dataclass
class LogAggregationStats:  # pylint: disable=too-many-instance-attributes  # Reason: Log stats dataclass requires many fields to capture complete statistics
    """Statistics for log aggregation."""

    total_entries: int
    entries_by_level: dict[str, int]
    entries_by_logger: dict[str, int]
    entries_by_hour: dict[str, int]
    error_rate: float
    warning_rate: float


@dataclass
class LogQueryFilter:
    """Optional filters for get_logs / export."""

    level: str | None = None
    logger_name: str | None = None
    user_id: str | None = None
    correlation_id: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    limit: int = 1000


def _query_filter_from_mapping(filters: dict[str, object]) -> LogQueryFilter:
    """Build a LogQueryFilter from untyped export filter keys."""
    limit_raw = filters.get("limit", 1000)
    limit = limit_raw if isinstance(limit_raw, int) else 1000
    return LogQueryFilter(
        level=_optional_str_from_object(filters.get("level")),
        logger_name=_optional_str_from_object(filters.get("logger_name")),
        user_id=_optional_str_from_object(filters.get("user_id")),
        correlation_id=_optional_str_from_object(filters.get("correlation_id")),
        start_time=_optional_datetime_from_object(filters.get("start_time")),
        end_time=_optional_datetime_from_object(filters.get("end_time")),
        limit=limit,
    )


def _optional_str_from_object(value: object) -> str | None:
    return value if isinstance(value, str) else None


def _optional_datetime_from_object(value: object) -> datetime | None:
    return value if isinstance(value, datetime) else None


class LogAggregator:
    """
    Centralized log aggregation and collection system.

    This class provides comprehensive log aggregation capabilities including
    collection, processing, filtering, and export functionality.
    """

    def __init__(
        self, max_entries: int = 50000, aggregation_interval: float = 60.0, export_path: str | None = None
    ) -> None:
        """
        Initialize the log aggregator.

        Args:
            max_entries: Maximum number of log entries to keep in memory
            aggregation_interval: Interval for log aggregation (seconds)
            export_path: Path for log export files
        """
        self.max_entries: int = max_entries
        self.aggregation_interval: float = aggregation_interval
        self.export_path: Path | None = Path(export_path) if export_path else None

        # Log storage
        self.log_entries: queue.Queue[LogEntry] = queue.Queue(maxsize=max_entries)
        self.aggregated_logs: list[LogEntry] = []

        # Statistics
        self.stats: LogAggregationStats = LogAggregationStats(
            total_entries=0,
            entries_by_level=defaultdict(int),
            entries_by_logger=defaultdict(int),
            entries_by_hour=defaultdict(int),
            error_rate=0.0,
            warning_rate=0.0,
        )

        # Processing
        self.processing_thread: threading.Thread | None = None
        self.shutdown_event: threading.Event = threading.Event()
        self.aggregation_callbacks: list[Callable[[LogEntry], None]] = []

        # Start processing thread
        self._start_processing_thread()

        logger.info(
            "Log aggregator initialized",
            max_entries=max_entries,
            aggregation_interval=aggregation_interval,
            export_path=str(self.export_path) if self.export_path else None,
        )

    def add_log_entry(self, log_entry: LogEntry) -> None:
        """Add a log entry to the aggregation system."""
        try:
            self.log_entries.put_nowait(log_entry)
        except queue.Full:
            try:
                _ = self.log_entries.get_nowait()
                self.log_entries.put_nowait(log_entry)
            except queue.Empty:
                pass
        self._update_stats(log_entry)

    @staticmethod
    def _eq_if_set(expected: str | None, actual: str | None) -> bool:
        return not expected or actual == expected

    def _log_matches_filter(self, log_entry: LogEntry, query: LogQueryFilter) -> bool:
        return (
            self._eq_if_set(query.level, log_entry.level)
            and self._eq_if_set(query.logger_name, log_entry.logger_name)
            and self._eq_if_set(query.user_id, log_entry.user_id)
            and self._eq_if_set(query.correlation_id, log_entry.correlation_id)
            and (not query.start_time or log_entry.timestamp >= query.start_time)
            and (not query.end_time or log_entry.timestamp <= query.end_time)
        )

    def get_logs(self, query: LogQueryFilter | None = None) -> list[LogEntry]:
        """Get filtered log entries."""
        query = query or LogQueryFilter()
        filtered_logs: list[LogEntry] = []
        for log_entry in self.aggregated_logs:
            if not self._log_matches_filter(log_entry, query):
                continue
            filtered_logs.append(log_entry)
            if len(filtered_logs) >= query.limit:
                break
        return filtered_logs

    def get_stats(self) -> LogAggregationStats:
        """
        Get log aggregation statistics.

        Returns:
            Current log aggregation statistics
        """
        return self.stats

    def get_error_logs(self, limit: int = 100) -> list[LogEntry]:
        """
        Get recent error logs.

        Args:
            limit: Maximum number of error logs to return

        Returns:
            List of recent error logs
        """
        return self.get_logs(LogQueryFilter(level="ERROR", limit=limit))

    def get_warning_logs(self, limit: int = 100) -> list[LogEntry]:
        """
        Get recent warning logs.

        Args:
            limit: Maximum number of warning logs to return

        Returns:
            List of recent warning logs
        """
        return self.get_logs(LogQueryFilter(level="WARNING", limit=limit))

    def get_user_logs(self, user_id: str, limit: int = 100) -> list[LogEntry]:
        """
        Get logs for a specific user.

        Args:
            user_id: User ID to filter by
            limit: Maximum number of logs to return

        Returns:
            List of logs for the specified user
        """
        return self.get_logs(LogQueryFilter(user_id=user_id, limit=limit))

    def get_correlation_logs(self, correlation_id: str) -> list[LogEntry]:
        """
        Get logs for a specific correlation ID.

        Args:
            correlation_id: Correlation ID to filter by

        Returns:
            List of logs for the specified correlation ID
        """
        return self.get_logs(LogQueryFilter(correlation_id=correlation_id))

    def export_logs(
        self,
        file_path: str | None = None,
        format_type: str = "json",
        filters: dict[str, object] | None = None,  # pylint: disable=redefined-builtin  # noqa: F811  # Reason: 'format' renamed to 'format_type' to avoid builtin shadowing
    ) -> str:
        """
        Export logs to a file.

        Args:
            file_path: Path to export file (uses default if None)
            format_type: Export format (json, csv)
            filters: Filters to apply to exported logs

        Returns:
            Path to the exported file
        """
        export_path: Path
        if file_path is None:
            if self.export_path is None:
                raise ValueError("No export path specified")
            timestamp = datetime.now(UTC).strftime(LOG_EXPORT_TIMESTAMP)
            export_path = self.export_path / f"logs_export_{timestamp}.{format_type}"
        else:
            export_path = Path(file_path)

        export_path.parent.mkdir(parents=True, exist_ok=True)

        # Get logs to export
        if filters:
            logs = self.get_logs(_query_filter_from_mapping(filters))
        else:
            logs = self.aggregated_logs

        # Export in specified format
        if format_type == "json":
            self._export_json(export_path, logs)
        elif format_type == "csv":
            self._export_csv(export_path, logs)
        else:
            raise ValueError(f"Unsupported export format: {format_type}")

        logger.info("Logs exported", file_path=str(export_path), format=format_type, log_count=len(logs))

        return str(export_path)

    def add_aggregation_callback(self, callback: Callable[[LogEntry], None]) -> None:
        """
        Add a callback function for log aggregation events.

        Args:
            callback: Function to call during aggregation with each log entry
        """
        self.aggregation_callbacks.append(callback)

    def shutdown(self) -> None:
        """Shutdown the log aggregator."""
        self.shutdown_event.set()
        if self.processing_thread and self.processing_thread.is_alive():
            self.processing_thread.join(timeout=5.0)

        logger.info("Log aggregator shutdown")

    def _start_processing_thread(self) -> None:
        """Start the log processing thread."""
        self.processing_thread = threading.Thread(target=self._process_logs, daemon=True, name="LogAggregator")
        self.processing_thread.start()

    def _process_logs(self) -> None:
        """Process log entries in the background."""
        while not self.shutdown_event.is_set():
            try:
                # Get log entry from queue
                log_entry = self.log_entries.get(timeout=1.0)

                # Add to aggregated logs
                self.aggregated_logs.append(log_entry)

                # Maintain max entries limit
                if len(self.aggregated_logs) > self.max_entries:
                    self.aggregated_logs = self.aggregated_logs[-self.max_entries :]

                # Call aggregation callbacks
                for callback in self.aggregation_callbacks:
                    try:
                        callback(log_entry)
                    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Callback errors unpredictable, must log but continue
                        logger.error("Aggregation callback failed", callback=str(callback), error=str(e), exc_info=True)

                self.log_entries.task_done()

            except queue.Empty:
                continue
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Log processing errors unpredictable, must log but continue
                logger.error("Error processing log entry", error=str(e), exc_info=True)

    def _update_stats(self, log_entry: LogEntry) -> None:
        """Update aggregation statistics."""
        self.stats.total_entries += 1
        self.stats.entries_by_level[log_entry.level] += 1
        self.stats.entries_by_logger[log_entry.logger_name] += 1

        # Group by hour
        hour_key = log_entry.timestamp.strftime(LOG_HOUR_BUCKET)
        self.stats.entries_by_hour[hour_key] += 1

        # Calculate rates
        if self.stats.total_entries > 0:
            self.stats.error_rate = self.stats.entries_by_level.get("ERROR", 0) / self.stats.total_entries * 100
            self.stats.warning_rate = self.stats.entries_by_level.get("WARNING", 0) / self.stats.total_entries * 100

    def _export_json(self, file_path: Path, logs: list[LogEntry]) -> None:
        """Export logs in JSON format."""
        export_data: list[dict[str, object]] = []
        for log_entry in logs:
            export_data.append(
                {
                    "timestamp": log_entry.timestamp.isoformat(),
                    "level": log_entry.level,
                    "logger_name": log_entry.logger_name,
                    "message": log_entry.message,
                    "data": log_entry.data,
                    "correlation_id": log_entry.correlation_id,
                    "user_id": log_entry.user_id,
                    "session_id": log_entry.session_id,
                }
            )

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

    def _export_csv(self, file_path: Path, logs: list[LogEntry]) -> None:
        """Export logs in CSV format."""
        import csv

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["timestamp", "level", "logger_name", "message", "correlation_id", "user_id", "session_id", "data"]
            )

            for log_entry in logs:
                writer.writerow(
                    [
                        log_entry.timestamp.isoformat(),
                        log_entry.level,
                        log_entry.logger_name,
                        log_entry.message,
                        log_entry.correlation_id,
                        log_entry.user_id,
                        log_entry.session_id,
                        json.dumps(log_entry.data),
                    ]
                )


# Global log aggregator instance
_log_aggregator: LogAggregator | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def peek_log_aggregator() -> LogAggregator | None:
    """Return the live singleton, or None if it was never constructed.

    Idle sampling uses this so the in-memory aggregator is not created as a side effect.
    """
    return _log_aggregator


def get_log_aggregator() -> LogAggregator:
    """
    Get the global log aggregator instance.

    Returns:
        Global LogAggregator instance
    """
    global _log_aggregator  # pylint: disable=global-statement  # Reason: Required for singleton pattern
    if _log_aggregator is None:
        _log_aggregator = LogAggregator()
    return _log_aggregator


def aggregate_log_entry(
    log_entry: LogEntry,
    aggregator: LogAggregator | None = None,
) -> None:
    """Add a log entry to the aggregation system (global aggregator if none given)."""
    if aggregator is None:
        aggregator = get_log_aggregator()
    aggregator.add_log_entry(log_entry)
