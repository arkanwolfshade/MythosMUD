# Migration Examples: From Default Logging to Enhanced Logging
# This file shows before/after examples of migrating from default logging to enhanced logging

# ❌ BEFORE - Default Python logging
import logging

logger = logging.getLogger(__name__)

# ✅ AFTER - Enhanced logging
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def migration_example_1():
    """Example 1: Basic logging migration."""

    # ❌ BEFORE - String formatting
    user_id = "user123"
    action = "login"
    logger.info(f"User {user_id} performed action {action}")

    # ✅ AFTER - Structured logging
    logger.info("User action performed", user_id=user_id, action=action)


def migration_example_2():
    """Example 2: Context parameter migration."""

    # ❌ BEFORE - Deprecated context parameter
    logger.info("User action completed", context={"user_id": "user123", "action": "login"})

    # ✅ AFTER - Direct key-value pairs
    logger.info("User action completed", user_id="user123", action="login")


def migration_example_3():
    """Example 3: Error logging migration."""

    # ❌ BEFORE - Minimal error information
    try:
        result = risky_operation()
    except Exception as e:
        logger.error(f"Error: {e}")
        raise

    # ✅ AFTER - Rich error context
    try:
        result = risky_operation()
    except Exception as e:
        logger.error("Operation failed", operation="user_creation", error=str(e), error_type=type(e).__name__)
        raise


def migration_example_4():
    """Example 4: Performance logging migration."""

    # ❌ BEFORE - No performance logging
    result = expensive_operation()

    # ✅ AFTER - Performance logging with context manager
    with measure_performance("expensive_operation"):
        result = expensive_operation()


def migration_example_5():
    """Example 5: Request context migration."""

    # ❌ BEFORE - Manual context passing
    logger.info("API request", user_id=user_id, session_id=session_id, request_id=request_id)

    # ✅ AFTER - Context binding
    bind_request_context(
        correlation_id=str(uuid.uuid4()), user_id=user_id, session_id=session_id, request_id=request_id
    )
    logger.info("API request received", method="POST", path="/api/users")


def migration_example_6():
    """Example 6: Security logging migration."""

    # ❌ BEFORE - Logging sensitive data
    logger.info("User login attempt", username="john", password="secret123")

    # ✅ AFTER - Automatic sanitization
    logger.info("User login attempt", username="john", password="secret123")
    # Automatically logs: {"username": "john", "password": "[REDACTED]"}


def migration_example_7():
    """Example 7: Database logging migration."""

    # ❌ BEFORE - No database logging
    result = database.execute("SELECT * FROM players WHERE id = ?", (player_id,))

    # ✅ AFTER - Structured database logging
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
    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            "Database query failed",
            query="SELECT * FROM players WHERE id = ?",
            error=str(e),
            duration_ms=duration * 1000,
        )
        raise


def migration_example_8():
    """Example 8: API logging migration."""

    # ❌ BEFORE - String formatting
    logger.info(f"API request: {method} {path} from {client_ip}")

    # ✅ AFTER - Structured API logging
    logger.info(
        "API request received",
        method=method,
        path=path,
        client_ip=client_ip,
        user_agent=request.headers.get("user-agent"),
    )


def migration_example_9():
    """Example 9: WebSocket logging migration."""

    # ❌ BEFORE - String formatting
    logger.info(f"WebSocket message: {message} from {client_ip}")

    # ✅ AFTER - Structured WebSocket logging
    logger.info(
        "WebSocket message received",
        message_type="text",
        message_length=len(message),
        client_ip=client_ip,
        connection_id=connection_id,
    )


def migration_example_10():
    """Example 10: Batch processing logging migration."""

    # ❌ BEFORE - String formatting in loops
    for i, item in enumerate(items):
        logger.info(f"Processing item {i + 1} of {len(items)}: {item}")

    # ✅ AFTER - Batch logging with context
    logger.info("Batch processing started", batch_size=len(items), batch_id=batch_id)

    for i, item in enumerate(items):
        process_item(item)
        if (i + 1) % 100 == 0:
            logger.info("Batch processing progress", batch_id=batch_id, processed=i + 1, remaining=len(items) - i - 1)

    logger.info("Batch processing completed", batch_id=batch_id, total_processed=len(items))


def migration_example_11():
    """Example 11: Exception tracking migration."""

    # ❌ BEFORE - No exception tracking
    try:
        risky_operation()
    except Exception:
        logger.error("Operation failed")
        raise

    # ✅ AFTER - Exception tracking with context
    try:
        risky_operation()
    except Exception as e:
        track_exception(e, user_id=user_id, severity="error", operation="user_creation")
        raise


def migration_example_12():
    """Example 12: Async logging migration."""

    # ❌ BEFORE - No context binding in async operations
    async def async_operation():
        logger.info("Starting async operation")
        result = await async_work()
        logger.info("Async operation completed")
        return result

    # ✅ AFTER - Context binding in async operations
    async def async_operation():
        bind_request_context(correlation_id=str(uuid.uuid4()), operation="async_task")
        try:
            logger.info("Starting async operation", operation="async_task")
            result = await async_work()
            logger.info("Async operation completed", operation="async_task", result=result)
            return result
        finally:
            clear_request_context()


def migration_example_13():
    """Example 13: Log level correction migration."""

    # ❌ BEFORE - Wrong log levels
    logger.error("User logged in successfully")  # Should be info
    logger.info("Critical system failure")  # Should be critical
    logger.warning("Normal operation completed")  # Should be info

    # ✅ AFTER - Correct log levels
    logger.info("User logged in successfully", user_id=user_id, login_method="password")
    logger.critical("Critical system failure", component="database", error="Connection pool exhausted")
    logger.info("Normal operation completed", operation="user_creation", success=True)


def migration_example_14():
    """Example 14: Logging in loops migration."""

    # ❌ BEFORE - Logging in tight loops
    for i in range(10000):
        logger.debug(f"Processing item {i}")

    # ✅ AFTER - Batched logging
    logger.info("Batch processing started", batch_size=10000, batch_id="batch_001")

    for i in range(10000):
        process_item(i)
        if (i + 1) % 1000 == 0:
            logger.info("Batch processing progress", batch_id="batch_001", processed=i + 1, remaining=10000 - i - 1)

    logger.info("Batch processing completed", batch_id="batch_001", total_processed=10000)


def migration_example_15():
    """Example 15: Complete function migration."""

    # ❌ BEFORE - Complete function with deprecated logging
    def create_user(username, email, password):
        logger.info(f"Creating user {username} with email {email}")
        try:
            user = database.create_user(username, email, password)
            logger.info(f"User {username} created successfully")
            return user
        except Exception as e:
            logger.error(f"Failed to create user {username}: {e}")
            raise

    # ✅ AFTER - Complete function with enhanced logging
    def create_user(username, email, password):
        logger.info("Creating user", username=username, email=email)
        try:
            user = database.create_user(username, email, password)
            logger.info("User created successfully", user_id=user.id, username=username)
            return user
        except Exception as e:
            logger.error("Failed to create user", username=username, error=str(e), error_type=type(e).__name__)
            raise


# Helper functions for examples
def risky_operation():
    """Simulate a risky operation."""
    pass


def expensive_operation():
    """Simulate an expensive operation."""
    return "result"


def process_item(item):
    """Simulate item processing."""
    pass


async def async_work():
    """Simulate async work."""
    pass


class database:
    """Simulate database operations."""

    @staticmethod
    def execute(sql, params):
        """Simulate database execute."""

        class Result:
            rowcount = 1

        return Result()

    @staticmethod
    def create_user(username, email, password):
        """Simulate user creation."""

        class User:
            id = "user123"

        return User()


# Example variables
user_id = "user123"
session_id = "session456"
request_id = "req789"
player_id = "player123"
method = "POST"
path = "/api/users"
client_ip = "192.168.1.1"
message = "Hello World"
connection_id = "ws-123"
batch_id = "batch_001"
items = [1, 2, 3, 4, 5]
username = "john"
email = "john@example.com"
password = "secret123"
