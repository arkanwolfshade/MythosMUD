# Error Logging Implementation Guide

## Overview

This guide provides practical implementation examples and patterns for integrating comprehensive error logging
throughout the MythosMUD codebase. As noted in the Pnakotic Manuscripts, the proper documentation of anomalous events
requires both theoretical understanding and practical application.

## Core Implementation Patterns

### Pattern 1: MythosMUDError with Automatic Logging

**Use Case**: Custom application errors that need structured logging

```python
from server.exceptions import MythosMUDError, create_error_context
from server.logging_config import get_logger

logger = get_logger(__name__)

def authenticate_user(user_id: str, password: str) -> bool:
    """Authenticate user with proper error logging."""
    try:
        # Authentication logic here

        if not validate_credentials(user_id, password):
            # Automatic logging via base class

            raise AuthenticationError(
                "Invalid credentials provided",
                context=create_error_context(
                    user_id=user_id,
                    request_id=get_current_request_id(),
                    metadata={
                        "ip_address": get_client_ip(),
                        "user_agent": get_user_agent(),
                        "attempt_count": get_attempt_count(user_id)
                    }
                ),
                details={
                    "validation_failed": True,
                    "timestamp": datetime.now(UTC).isoformat()
                },
                user_friendly="Login failed. Please check your credentials."
            )
        return True
    except Exception as e:
        # Convert and log any unexpected errors

        context = create_error_context(
            user_id=user_id,
            request_id=get_current_request_id(),
            metadata={"operation": "authentication"}
        )
        mythos_error = handle_exception(e, context)
        raise mythos_error
```

### Pattern 2: HTTPException with Pre-logging

**Use Case**: FastAPI endpoints that need to raise HTTPExceptions

```python
from fastapi import HTTPException
from server.logging_config import get_logger
from server.utils.error_logging import log_and_raise_http

logger = get_logger(__name__)

@router.get("/players/{player_id}")
async def get_player(player_id: str, current_user: User = Depends(get_current_user)):
    """Get player information with proper error logging."""
    try:
        player = persistence.get_player_by_id(player_id)
        if not player:
            # Log before raising HTTPException

            log_and_raise_http(
                status_code=404,
                detail=f"Player {player_id} not found",
                context=create_error_context(
                    user_id=current_user.id,
                    request_id=get_current_request_id(),
                    metadata={
                        "requested_player_id": player_id,
                        "endpoint": "/players/{player_id}",
                        "method": "GET"
                    }
                ),
                logger_name=__name__
            )

        return {"player": player.to_dict()}
    except HTTPException:
        # Re-raise HTTPExceptions (already logged)

        raise
    except Exception as e:
        # Log and convert unexpected errors

        context = create_error_context(
            user_id=current_user.id,
            request_id=get_current_request_id(),
            metadata={"endpoint": "/players/{player_id}", "method": "GET"}
        )
        mythos_error = handle_exception(e, context)
        raise mythos_error
```

### Pattern 3: Third-party Exception Wrapping

**Use Case**: Handling exceptions from external libraries

```python
from server.utils.error_logging import wrap_third_party_exception
from server.logging_config import get_logger
import aiosqlite

logger = get_logger(__name__)

async def execute_database_query(query: str, params: tuple) -> list:
    """Execute database query with proper error handling."""
    try:
        async with aiosqlite.connect(DATABASE_URL) as db:
            cursor = await db.execute(query, params)
            results = await cursor.fetchall()
            return results
    except aiosqlite.Error as e:
        # Wrap third-party exception with proper logging

        context = create_error_context(
            request_id=get_current_request_id(),
            metadata={
                "query": query[:100],  # Truncate for security
                "param_count": len(params),
                "operation": "database_query"
            }
        )
        mythos_error = wrap_third_party_exception(e, context)
        raise mythos_error
    except Exception as e:
        # Handle any other unexpected errors

        context = create_error_context(
            request_id=get_current_request_id(),
            metadata={"operation": "database_query"}
        )
        mythos_error = handle_exception(e, context)
        raise mythos_error
```

### Pattern 4: WebSocket Error Handling

**Use Case**: WebSocket connections and real-time communication

```python
from server.logging_config import get_logger
from server.exceptions import CommunicationError, create_error_context

logger = get_logger(__name__)

async def handle_websocket_message(websocket: WebSocket, player_id: str, message: dict):
    """Handle WebSocket message with proper error logging."""
    try:
        # Message processing logic

        if not validate_message(message):
            raise CommunicationError(
                "Invalid message format",
                context=create_error_context(
                    user_id=player_id,
                    session_id=get_session_id(websocket),
                    metadata={
                        "message_type": message.get("type"),
                        "message_size": len(str(message)),
                        "websocket_state": websocket.state
                    }
                ),
                details={"message": message},
                user_friendly="Message could not be processed"
            )

        # Process the message

        await process_message(player_id, message)

    except CommunicationError:
        # Re-raise (already logged)

        raise
    except Exception as e:
        # Log and convert unexpected errors

        context = create_error_context(
            user_id=player_id,
            session_id=get_session_id(websocket),
            metadata={"operation": "websocket_message_processing"}
        )
        mythos_error = handle_exception(e, context)
        raise mythos_error
```

### Pattern 5: Command Processing Error Handling

**Use Case**: Game command processing with context

```python
from server.logging_config import get_logger
from server.exceptions import CommandError, create_error_context

logger = get_logger(__name__)

async def process_game_command(player_id: str, command: str, args: list) -> dict:
    """Process game command with proper error logging."""
    try:
        # Command validation

        if not validate_command(command):
            raise CommandError(
                f"Unknown command: {command}",
                context=create_error_context(
                    user_id=player_id,
                    command=command,
                    metadata={
                        "args": args,
                        "command_length": len(command),
                        "arg_count": len(args)
                    }
                ),
                details={"available_commands": get_available_commands()},
                user_friendly=f"Command '{command}' is not recognized"
            )

        # Execute command

        result = await execute_command(player_id, command, args)
        return result

    except CommandError:
        # Re-raise (already logged)

        raise
    except Exception as e:
        # Log and convert unexpected errors

        context = create_error_context(
            user_id=player_id,
            command=command,
            metadata={"args": args, "operation": "command_processing"}
        )
        mythos_error = handle_exception(e, context)
        raise mythos_error
```

## Utility Functions Implementation

### Error Logging Utilities

```python
# server/utils/error_logging.py

from typing import Type, Any
from fastapi import Request, WebSocket
from server.exceptions import MythosMUDError, create_error_context, handle_exception
from server.logging_config import get_logger

def log_and_raise(
    exception_class: Type[MythosMUDError],
    message: str,
    context: ErrorContext | None = None,
    details: dict[str, Any] | None = None,
    user_friendly: str | None = None,
    logger_name: str | None = None
) -> None:
    """Log and raise a MythosMUD error."""
    logger = get_logger(logger_name or __name__)

    # Log the error before raising

    logger.error(
        f"Raising {exception_class.__name__}",
        error_type=exception_class.__name__,
        message=message,
        context=context.to_dict() if context else {},
        details=details or {},
        user_friendly=user_friendly
    )

    # Raise the exception (which will also log via base class)

    raise exception_class(message, context, details, user_friendly)

def log_and_raise_http(
    status_code: int,
    detail: str,
    context: ErrorContext | None = None,
    logger_name: str | None = None
) -> None:
    """Log and raise an HTTPException."""
    logger = get_logger(logger_name or __name__)

    # Log the error before raising

    logger.warning(
        "Raising HTTPException",
        status_code=status_code,
        detail=detail,
        context=context.to_dict() if context else {}
    )

    # Raise the HTTPException

    raise HTTPException(status_code=status_code, detail=detail)

def create_context_from_request(request: Request) -> ErrorContext:
    """Create error context from FastAPI request."""
    return create_error_context(
        request_id=str(request.url),
        metadata={
            "path": str(request.url),
            "method": request.method,
            "user_agent": request.headers.get("user-agent", ""),
            "content_type": request.headers.get("content-type", ""),
            "content_length": request.headers.get("content-length", "0")
        }
    )

def create_context_from_websocket(websocket: WebSocket) -> ErrorContext:
    """Create error context from WebSocket connection."""
    return create_error_context(
        session_id=websocket.query_params.get("session_id"),
        metadata={
            "websocket_state": websocket.state,
            "client_host": websocket.client.host if websocket.client else None,
            "client_port": websocket.client.port if websocket.client else None,
            "query_params": dict(websocket.query_params)
        }
    )

def wrap_third_party_exception(
    exc: Exception,
    context: ErrorContext | None = None
) -> MythosMUDError:
    """Wrap third-party exceptions with proper logging."""
    logger = get_logger(__name__)

    # Log the original exception

    logger.error(
        "Third-party exception occurred",
        original_type=type(exc).__name__,
        original_message=str(exc),
        context=context.to_dict() if context else {}
    )

    # Convert to MythosMUD error

    return handle_exception(exc, context)
```

## Context Creation Helpers

### Request Context Helpers

```python
# server/utils/context_helpers.py

from typing import Any
from fastapi import Request
from server.exceptions import create_error_context

def get_current_request_id() -> str:
    """Get current request ID from context."""
    # Implementation depends on your request ID system

    return "req_" + str(uuid.uuid4())[:8]

def get_client_ip(request: Request) -> str:
    """Extract client IP from request."""
    return request.client.host if request.client else "unknown"

def get_user_agent(request: Request) -> str:
    """Extract user agent from request."""
    return request.headers.get("user-agent", "unknown")

def create_api_context(
    request: Request,
    user_id: str | None = None,
    additional_metadata: dict[str, Any] | None = None
) -> ErrorContext:
    """Create standardized API error context."""
    metadata = {
        "path": str(request.url),
        "method": request.method,
        "user_agent": get_user_agent(request),
        "client_ip": get_client_ip(request),
        "content_type": request.headers.get("content-type", ""),
        "content_length": request.headers.get("content-length", "0")
    }

    if additional_metadata:
        metadata.update(additional_metadata)

    return create_error_context(
        user_id=user_id,
        request_id=get_current_request_id(),
        metadata=metadata
    )
```

## Testing Patterns

### Error Logging Test Utilities

```python
# server/tests/utils/test_error_logging.py

import pytest
from unittest.mock import patch, MagicMock
from server.utils.error_logging import log_and_raise, log_and_raise_http
from server.exceptions import AuthenticationError, create_error_context

class ErrorLoggingTestMixin:
    """Mixin for testing error logging functionality."""

    def assert_error_logged(self, log_file: str, error_type: str, message: str):
        """Assert that an error was logged to the specified file."""
        # Implementation depends on your log testing setup

        pass

    def assert_error_context(self, context: ErrorContext, expected_fields: list[str]):
        """Assert that error context contains expected fields."""
        context_dict = context.to_dict()
        for field in expected_fields:
            assert field in context_dict, f"Missing field: {field}"

    def assert_no_sensitive_data(self, log_content: str):
        """Assert that no sensitive data appears in logs."""
        sensitive_patterns = [
            r'password["\']?\s*[:=]\s*["\'][^"\']+["\']',
            r'token["\']?\s*[:=]\s*["\'][^"\']+["\']',
            r'secret["\']?\s*[:=]\s*["\'][^"\']+["\']'
        ]

        for pattern in sensitive_patterns:
            assert not re.search(pattern, log_content, re.IGNORECASE), \
                f"Sensitive data found in logs: {pattern}"

class TestErrorLogging(ErrorLoggingTestMixin):
    """Test error logging functionality."""

    def test_log_and_raise_mythos_error(self):
        """Test logging and raising MythosMUD errors."""
        context = create_error_context(
            user_id="test_user",
            metadata={"test": True}
        )

        with pytest.raises(AuthenticationError):
            log_and_raise(
                AuthenticationError,
                "Test authentication error",
                context=context,
                details={"test": True},
                user_friendly="Test error message"
            )

    def test_log_and_raise_http_exception(self):
        """Test logging and raising HTTP exceptions."""
        context = create_error_context(
            user_id="test_user",
            metadata={"test": True}
        )

        with pytest.raises(HTTPException) as exc_info:
            log_and_raise_http(
                status_code=404,
                detail="Test not found",
                context=context
            )

        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Test not found"

    def test_error_context_creation(self):
        """Test error context creation and validation."""
        context = create_error_context(
            user_id="test_user",
            command="test_command",
            metadata={"test": True}
        )

        self.assert_error_context(
            context,
            ["user_id", "command", "metadata", "timestamp"]
        )

        context_dict = context.to_dict()
        assert context_dict["user_id"] == "test_user"
        assert context_dict["command"] == "test_command"
        assert context_dict["metadata"]["test"] is True
```

## Migration Checklist

### For Each File Being Updated

1. **Import Required Modules**

   ```python
   from server.exceptions import MythosMUDError, create_error_context, handle_exception
   from server.logging_config import get_logger
   from server.utils.error_logging import log_and_raise, log_and_raise_http
   ```

2. **Replace Direct Exception Raising**

   - Find all `raise SomeError(...)` statements
   - Replace with proper logging patterns
   - Add appropriate error context

3. **Update HTTPException Usage**

   - Find all `raise HTTPException(...)` statements
   - Replace with `log_and_raise_http(...)`
   - Add proper error context

4. **Add Error Context**

   - Include relevant user information
   - Add request/session context
   - Include operation metadata

5. **Test Error Handling**

   - Verify errors are logged correctly
   - Check log file categorization
   - Validate error responses

### Common Migration Patterns

**Before:**

```python
if not player:
    raise HTTPException(status_code=404, detail="Player not found")
```

**After:**

```python
if not player:
    log_and_raise_http(
        status_code=404,
        detail="Player not found",
        context=create_error_context(
            user_id=current_user.id,
            request_id=get_current_request_id(),
            metadata={"requested_player_id": player_id}
        )
    )
```

**Before:**

```python
except ValueError as e:
    raise ValidationError(str(e))
```

**After:**

```python
except ValueError as e:
    context = create_error_context(
        user_id=user_id,
        metadata={"operation": "validation"}
    )
    mythos_error = handle_exception(e, context)
    raise mythos_error
```

## Best Practices

### Do's

Always include relevant context in errors

- Use appropriate log levels (ERROR for exceptions, WARNING for recoverable issues)
- Include user-friendly messages for client responses
- Test error handling thoroughly
- Monitor error rates and patterns

### Don'ts

Don't log sensitive information (passwords, tokens, secrets)

- Don't raise exceptions without proper logging
- Don't use generic error messages
- Don't ignore error context
- Don't skip error handling tests

### Security Considerations

Sanitize user input in error messages

- Avoid logging sensitive data
- Use appropriate error detail levels
- Implement proper access controls for logs
- Monitor for security-related errors

---

*As the restricted archives of Miskatonic University teach us, the proper implementation of error handling is not merely
a technical exercise, but a critical component of maintaining the delicate balance between order and chaos in our
digital realm. This guide ensures that every error, every exception, and every anomaly is properly catalogued for
posterity and analysis.*
