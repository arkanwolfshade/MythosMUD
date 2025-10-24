# Correct Enhanced Logging Patterns for MythosMUD
# This file demonstrates the CORRECT way to use the enhanced logging system

import asyncio
import time

from server.logging.enhanced_logging_config import bind_request_context, clear_request_context, get_logger
from server.monitoring.exception_tracker import track_exception
from server.monitoring.performance_monitor import measure_performance

# ✅ CORRECT - Enhanced logging import
logger = get_logger(__name__)


def correct_basic_logging():
    """Demonstrate correct basic logging patterns."""

    # ✅ CORRECT - Structured logging with key-value pairs
    logger.info("User action completed", user_id="user123", action="login", success=True)

    # ✅ CORRECT - Error logging with rich context
    logger.error("Operation failed", operation="user_creation", error="Database connection failed", retry_count=3)

    # ✅ CORRECT - Debug logging with appropriate detail
    logger.debug("Processing batch", batch_size=100, batch_id="batch_001")

    # ✅ CORRECT - Warning logging for potential issues
    logger.warning("High memory usage detected", memory_percent=85.5, threshold=80.0)


def correct_error_handling():
    """Demonstrate correct error handling with logging."""

    try:
        result = risky_operation()
        logger.info("Operation completed successfully", result=result)
        return result
    except ValueError as e:
        logger.error("Validation error occurred", error=str(e), error_type=type(e).__name__)
        raise
    except Exception as e:
        logger.error("Unexpected error occurred", error=str(e), error_type=type(e).__name__)
        raise


def correct_performance_logging():
    """Demonstrate correct performance logging patterns."""

    # ✅ CORRECT - Performance logging with context manager
    with measure_performance("database_query", user_id="user123"):
        result = database.query("SELECT * FROM players")

    # ✅ CORRECT - Manual performance logging
    start_time = time.time()
    result = process_data()
    duration = time.time() - start_time

    logger.info("Data processing completed", duration_ms=duration * 1000, records_processed=len(result))


def correct_request_context():
    """Demonstrate correct request context binding."""

    # ✅ CORRECT - Bind request context
    bind_request_context(correlation_id="req-123", user_id="user-456", session_id="session-789", request_id="req-001")

    try:
        # All subsequent logs automatically include this context
        logger.info("User action performed", action="move", direction="north")
        logger.info("User action completed", action="move", success=True)
    finally:
        clear_request_context()


def correct_security_logging():
    """Demonstrate correct security logging patterns."""

    # ✅ CORRECT - Logging without sensitive data
    logger.info("User authentication attempt", username="john", success=False)

    # ✅ CORRECT - Logging with automatic sanitization
    logger.info("API request", endpoint="/api/users", api_key="sk-123456789")
    # Automatically logs: {"endpoint": "/api/users", "api_key": "[REDACTED]"}

    # ✅ CORRECT - Logging security events
    logger.warning("Suspicious activity detected", user_id="user123", activity_type="multiple_failed_logins")


async def correct_async_logging():
    """Demonstrate correct async logging patterns."""

    # ✅ CORRECT - Async operation with context binding
    bind_request_context(correlation_id="async-123", operation="async_task")

    try:
        logger.info("Starting async operation", operation="data_processing")

        # Perform async work
        result = await async_work()

        logger.info("Async operation completed", operation="data_processing", result=result)
        return result
    except Exception as e:
        logger.error("Async operation failed", operation="data_processing", error=str(e))
        raise
    finally:
        clear_request_context()


def correct_exception_tracking():
    """Demonstrate correct exception tracking."""

    try:
        risky_operation()
    except Exception as e:
        # ✅ CORRECT - Exception tracking with context
        track_exception(e, user_id="user123", severity="error", operation="user_creation")
        raise


def correct_database_logging():
    """Demonstrate correct database operation logging."""

    start_time = time.time()

    try:
        result = database.execute("SELECT * FROM players WHERE id = ?", (player_id,))
        duration = time.time() - start_time

        logger.debug(
            "Database query executed",
            query="SELECT * FROM players WHERE id = ?",
            duration_ms=duration * 1000,
            rows_affected=result.rowcount,
        )
        return result
    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            "Database query failed",
            query="SELECT * FROM players WHERE id = ?",
            error=str(e),
            duration_ms=duration * 1000,
        )
        raise


def correct_api_logging():
    """Demonstrate correct API request/response logging."""

    # ✅ CORRECT - Request logging
    logger.info(
        "API request received", method="POST", path="/api/players", client_ip="192.168.1.1", user_agent="Mozilla/5.0"
    )

    # ✅ CORRECT - Response logging
    logger.info("API response sent", method="POST", path="/api/players", status_code=201, response_time_ms=150)


def correct_websocket_logging():
    """Demonstrate correct WebSocket logging patterns."""

    # ✅ CORRECT - WebSocket connection logging
    logger.info("WebSocket connection established", client_ip="192.168.1.1", connection_id="ws-123")

    # ✅ CORRECT - WebSocket message logging
    logger.debug("WebSocket message received", message_type="text", length=100, connection_id="ws-123")

    # ✅ CORRECT - WebSocket disconnection logging
    logger.info("WebSocket disconnected", client_ip="192.168.1.1", connection_id="ws-123")


def correct_batch_logging():
    """Demonstrate correct batch operation logging."""

    # ✅ CORRECT - Batch processing start
    logger.info("Batch processing started", batch_size=1000, batch_id="batch_001")

    # ✅ CORRECT - Batch processing progress
    logger.info("Batch processing progress", batch_id="batch_001", processed=500, remaining=500)

    # ✅ CORRECT - Batch processing completion
    logger.info(
        "Batch processing completed", batch_id="batch_001", total_processed=1000, success_count=950, error_count=50
    )


# Helper functions for examples
def risky_operation():
    """Simulate a risky operation."""
    pass


def process_data():
    """Simulate data processing."""
    return [1, 2, 3, 4, 5]


async def async_work():
    """Simulate async work."""
    await asyncio.sleep(0.1)
    return "async_result"


class database:
    """Simulate database operations."""

    @staticmethod
    def query(sql):
        """Simulate database query."""
        pass

    @staticmethod
    def execute(sql, params):
        """Simulate database execute."""

        class Result:
            rowcount = 1

        return Result()
