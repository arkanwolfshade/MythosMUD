"""Stable strftime patterns for log filenames and aggregation keys.

These are machine-oriented path/key formats, not user-facing locale strings.
"""

# ISO calendar date for daily log file suffixes
LOG_DATE = "%Y-%m-%d"
# Rotation suffix when renaming existing log files at startup
LOG_FILE_TIMESTAMP = "%Y_%m_%d_%H%M%S"
# Export dump filename timestamp
LOG_EXPORT_TIMESTAMP = "%Y%m%d_%H%M%S"
# Hour bucket key for aggregation
LOG_HOUR_BUCKET = "%Y-%m-%d %H:00"
