# DEPRECATED Logging Patterns - DO NOT USE
# This file demonstrates what NOT to do with logging in MythosMUD

# ❌ FORBIDDEN - Default Python logging import
import logging
from logging import getLogger

# ❌ FORBIDDEN - Using standard library logging
logger = logging.getLogger(__name__)
logger2 = getLogger(__name__)


def deprecated_basic_logging():
    """Demonstrate DEPRECATED basic logging patterns."""

    # ❌ WRONG - String formatting in logs
    logger.info(f"User {user_id} performed action {action}")

    # ❌ WRONG - Deprecated context parameter
    logger.info("User action completed", context={"user_id": user_id, "action": action})

    # ❌ WRONG - Unstructured messages
    logger.info("Error occurred")

    # ❌ WRONG - Logging sensitive data
    logger.info("Login attempt", username="john", password="secret123")

    # ❌ WRONG - Wrong log levels
    logger.error("User logged in successfully")  # Should be info
    logger.info("Critical system failure")  # Should be critical


def deprecated_error_handling():
    """Demonstrate DEPRECATED error handling patterns."""

    try:
        result = risky_operation()
        # ❌ WRONG - No logging of success
        return result
    except Exception as e:
        # ❌ WRONG - Minimal error information
        logger.error(f"Error: {e}")
        raise


def deprecated_performance_logging():
    """Demonstrate DEPRECATED performance logging patterns."""

    # ❌ WRONG - No performance logging
    result = expensive_operation()

    # ❌ WRONG - String formatting for performance
    logger.info(f"Operation took {duration} seconds")

    # ❌ WRONG - No context in performance logs
    logger.info("Operation completed")


def deprecated_request_context():
    """Demonstrate DEPRECATED request context patterns."""

    # ❌ WRONG - No context binding
    logger.info("User action performed", action="move")

    # ❌ WRONG - Manual context passing
    logger.info("User action", user_id=user_id, session_id=session_id, request_id=request_id)


def deprecated_security_logging():
    """Demonstrate DEPRECATED security logging patterns."""

    # ❌ WRONG - Logging sensitive data
    logger.info("User login", username="john", password="secret123", token="abc123")

    # ❌ WRONG - No sanitization
    logger.info("API request", api_key="sk-123456789", secret="very_secret")

    # ❌ WRONG - String formatting with sensitive data
    logger.info(f"User {username} logged in with password [REDACTED]")


def deprecated_async_logging():
    """Demonstrate DEPRECATED async logging patterns."""

    # ❌ WRONG - No context binding in async operations
    async def async_operation():
        logger.info("Starting async operation")
        result = await async_work()
        logger.info("Async operation completed")
        return result

    # ❌ WRONG - Blocking operations in async context
    async def blocking_async_operation():
        logger.info("Starting async operation")
        time.sleep(1)  # ❌ WRONG - Blocking sleep
        logger.info("Async operation completed")


def deprecated_database_logging():
    """Demonstrate DEPRECATED database logging patterns."""

    # ❌ WRONG - No database operation logging
    result = database.query("SELECT * FROM players")

    # ❌ WRONG - String formatting for database logs
    logger.info(f"Database query: {query} with params {params}")

    # ❌ WRONG - No performance metrics
    logger.info("Database query executed")


def deprecated_api_logging():
    """Demonstrate DEPRECATED API logging patterns."""

    # ❌ WRONG - No request logging
    response = process_request(request)

    # ❌ WRONG - String formatting for API logs
    logger.info(f"API request: {method} {path} from {client_ip}")

    # ❌ WRONG - No response logging
    logger.info("API request processed")


def deprecated_websocket_logging():
    """Demonstrate DEPRECATED WebSocket logging patterns - EXAMPLE ONLY."""

    # ❌ WRONG - No WebSocket connection logging
    # await websocket.accept()  # Commented out - this is just an example pattern

    # ❌ WRONG - String formatting for WebSocket logs
    logger.info(f"WebSocket message: {message} from {client_ip}")

    # ❌ WRONG - No disconnection logging
    # await websocket.close()  # Commented out - this is just an example pattern


def deprecated_batch_logging():
    """Demonstrate DEPRECATED batch logging patterns."""

    # ❌ WRONG - No batch start logging
    for item in items:
        process_item(item)

    # ❌ WRONG - String formatting for batch logs
    logger.info(f"Processed {count} items out of {total}")

    # ❌ WRONG - No batch completion logging
    logger.info("Batch processing done")


def deprecated_exception_handling():
    """Demonstrate DEPRECATED exception handling patterns."""

    try:
        risky_operation()
    except Exception:
        # ❌ WRONG - No exception tracking
        logger.error("Operation failed")
        raise

    try:
        risky_operation()
    except Exception as e:
        # ❌ WRONG - String formatting for exceptions
        logger.error(f"Operation failed: {e}")
        raise


def deprecated_logging_in_loops():
    """Demonstrate DEPRECATED logging in loops."""

    # ❌ WRONG - Logging in tight loops
    for i in range(10000):
        logger.debug(f"Processing item {i}")

    # ❌ WRONG - String formatting in loops
    for item in items:
        logger.info(f"Processing {item.name} with value {item.value}")


def deprecated_logging_without_context():
    """Demonstrate DEPRECATED logging without context."""

    # ❌ WRONG - No context in logs
    logger.info("Operation started")
    logger.info("Operation completed")

    # ❌ WRONG - No correlation IDs
    logger.info("User action performed")

    # ❌ WRONG - No request tracing
    logger.info("Database query executed")


# Helper functions for examples
def risky_operation():
    """Simulate a risky operation."""
    pass


def expensive_operation():
    """Simulate an expensive operation."""
    return "result"


def process_request(request):
    """Simulate request processing."""
    return "response"


def process_item(item):
    """Simulate item processing."""
    pass


async def async_work():
    """Simulate async work."""
    pass


class database:
    """Simulate database operations."""

    @staticmethod
    def query(sql):
        """Simulate database query."""
        pass


# Example variables for string formatting
user_id = "user123"
action = "login"
duration = 1.5
username = "john"
password = "secret123"
count = 500
total = 1000
query = "SELECT * FROM players"
params = {"id": 123}
method = "POST"
path = "/api/players"
client_ip = "192.168.1.1"
message = "Hello World"
items = [1, 2, 3, 4, 5]
