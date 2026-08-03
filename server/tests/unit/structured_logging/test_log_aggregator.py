"""Unit tests for LogAggregator."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from server.structured_logging.log_aggregator import LogAggregator, LogEntry, aggregate_log_entry


def _flush_queue(aggregator: LogAggregator) -> None:
    while not aggregator.log_entries.empty():
        aggregator.aggregated_logs.append(aggregator.log_entries.get_nowait())


def test_add_log_entry_updates_stats():
    aggregator = LogAggregator(max_entries=100, aggregation_interval=3600.0)
    aggregator.add_log_entry("INFO", "test.logger", "hello", data={"k": "v"}, user_id="u1")
    stats = aggregator.get_stats()
    assert stats.total_entries >= 1
    assert stats.entries_by_logger["test.logger"] >= 1


def test_get_logs_after_flush():
    aggregator = LogAggregator(max_entries=100, aggregation_interval=3600.0)
    aggregator.add_log_entry("INFO", "test.logger", "hello")
    _flush_queue(aggregator)
    logs = aggregator.get_logs(logger_name="test.logger", limit=10)
    assert len(logs) >= 1
    assert logs[0].message == "hello"


def test_get_stats_rates():
    aggregator = LogAggregator(max_entries=100, aggregation_interval=3600.0)
    aggregator.add_log_entry("ERROR", "err.logger", "boom")
    aggregator.add_log_entry("WARNING", "warn.logger", "careful")
    aggregator.add_log_entry("INFO", "info.logger", "ok")
    stats = aggregator.get_stats()
    assert stats.total_entries >= 3
    assert stats.error_rate >= 0.0


def test_filter_error_and_warning_logs():
    aggregator = LogAggregator(max_entries=100, aggregation_interval=3600.0)
    aggregator.add_log_entry("ERROR", "e", "err")
    aggregator.add_log_entry("WARNING", "w", "warn")
    _flush_queue(aggregator)
    assert len(aggregator.get_error_logs(limit=5)) >= 1
    assert len(aggregator.get_warning_logs(limit=5)) >= 1


def test_get_user_and_correlation_logs():
    aggregator = LogAggregator(max_entries=100, aggregation_interval=3600.0)
    aggregator.add_log_entry("INFO", "l", "msg", user_id="player-1", correlation_id="cid-1")
    _flush_queue(aggregator)
    assert len(aggregator.get_user_logs("player-1")) >= 1
    assert len(aggregator.get_correlation_logs("cid-1")) >= 1


def test_export_logs_json(tmp_path: Path):
    aggregator = LogAggregator(max_entries=100, aggregation_interval=3600.0)
    aggregator.add_log_entry("INFO", "l", "export me")
    _flush_queue(aggregator)
    out = tmp_path / "logs.json"
    path = aggregator.export_logs(str(out), format_type="json")
    assert Path(path).exists()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    assert isinstance(payload, list)


def test_aggregate_log_entry_helper():
    aggregator = LogAggregator(max_entries=50, aggregation_interval=3600.0)
    aggregate_log_entry("INFO", "helper", "via helper", aggregator=aggregator)
    assert aggregator.get_stats().total_entries >= 1


def test_shutdown_stops_thread():
    aggregator = LogAggregator(max_entries=50, aggregation_interval=3600.0)
    aggregator.shutdown()


def test_update_stats_via_log_entry():
    aggregator = LogAggregator(max_entries=50, aggregation_interval=3600.0)
    entry = LogEntry(
        timestamp=datetime.now(UTC),
        level="INFO",
        logger_name="direct",
        message="direct",
    )
    aggregator._update_stats(entry)
    assert aggregator.get_stats().total_entries == 1
