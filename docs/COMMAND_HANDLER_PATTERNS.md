# 🐙 MythosMUD Command Handler Patterns

*"Patterns emerge from chaos, and in those patterns we find the structure of our reality."* - Dr. Henry Armitage,
Miskatonic University

---

## Table of Contents

1. [Overview](#overview)
2. [Basic Handler Structure](#basic-handler-structure)
3. [Common Handler Patterns](#common-handler-patterns)
4. [Accessing Game Systems](#accessing-game-systems)
5. [Error Handling Patterns](#error-handling-patterns)
6. [Logging Patterns](#logging-patterns)
7. [Security Patterns](#security-patterns)
8. [Performance Patterns](#performance-patterns)
9. [Testing Patterns](#testing-patterns)
10. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Overview

Command handlers in MythosMUD are async functions that process validated command data and interact with the game
systems. They follow consistent patterns to ensure maintainability, security, and performance.

### Handler Signature

All command handlers follow this signature:

```python
async def handle_command_name(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str
) -> dict[str, str]:
    """
    Handle the command_name command.

    Args:
        command_data: Validated command data from Pydantic model
        current_user: Current user information (dict with username, is_admin, etc.)
        request: FastAPI request object for accessing app state
        alias_storage: Alias storage instance for command expansion
        player_name: Player name for logging and identification

    Returns:
        dict: Command result with 'result' key containing response message
    """
```

---

## Basic Handler Structure

### Minimal Handler

```python
async def handle_simple_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a simple command with no game system interaction."""

    logger.debug("Processing simple command", player=player_name, args=command_data)

    # Extract command parameters

    param1 = command_data.get("param1", "default")

    # Process command logic

    result_message = f"You performed action: {param1}"

    logger.info(f"Simple command completed for {player_name}")
    return {"result": result_message}
```

### Standard Handler with Game Systems

```python
async def handle_standard_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a standard command with game system interaction."""

    logger.debug("Processing standard command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Standard command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Standard command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract command parameters

    param1 = command_data.get("param1")
    if not param1:
        return {"result": "Missing required parameter. Usage: command <param1>"}

    # Perform command logic

    try:
        # Your command logic here

        result_message = f"You successfully used {param1}"

        logger.info(f"Standard command completed for {player_name}: {param1}")
        return {"result": result_message}

    except Exception as e:
        logger.error(f"Standard command error for {player_name}: {str(e)}")
        return {"result": "An error occurred while processing your command."}
```

---

## Common Handler Patterns

### 1. Room-Based Commands

Commands that affect or interact with the current room:

```python
async def handle_room_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command that affects the current room."""

    logger.debug("Processing room command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Room command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player and room data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Room command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    room_id = player.current_room_id
    room = persistence.get_room(room_id)
    if not room:
        logger.warning("Room command failed - room not found", player=player_name, room_id=room_id)
        return {"result": "You can't perform that action right now."}

    # Get other players in room

    room_players = persistence.get_players_in_room(room_id)

    # Extract command parameters

    action = command_data.get("action", "default")

    # Perform room-based action

    result_message = f"{player_name} performs {action} in {room.name}"

    # Notify other players in room (if needed)

    for room_player in room_players:
        if room_player.username != player_name:
            # Send message to other players
            # This would typically use the event system

            pass

    logger.info(f"Room command completed for {player_name}: {action} in {room_id}")
    return {"result": result_message}
```

### 2. Player-Targeted Commands

Commands that target other players:

```python
async def handle_target_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command that targets another player."""

    logger.debug("Processing target command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Target command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get current player

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Target command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract target player

    target_player_name = command_data.get("target_player")
    if not target_player_name:
        return {"result": "Target who? Usage: command <player_name>"}

    # Validate target player

    if target_player_name.lower() == player_name.lower():
        return {"result": "You can't target yourself."}

    target_player = persistence.get_player_by_name(target_player_name)
    if not target_player:
        return {"result": "Player not found."}

    # Check if target is in same room

    if target_player.current_room_id != player.current_room_id:
        return {"result": "That player is not here."}

    # Extract action parameter

    action = command_data.get("action", "default")

    # Perform targeted action

    result_message = f"You {action} {target_player_name}"
    target_message = f"{player_name} {action}s you"

    # Send messages to both players
    # This would typically use the event system

    logger.info(f"Target command completed: {player_name} -> {target_player_name} ({action})")
    return {"result": result_message}
```

### 3. Admin-Only Commands

Commands restricted to administrators:

```python
async def handle_admin_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle an admin-only command."""

    logger.debug("Processing admin command", player=player_name, args=command_data)

    # Check admin permissions

    if not current_user.get("is_admin", False):
        logger.warning("Admin command attempted by non-admin user", player=player_name)
        return {"result": "You don't have permission for that command."}

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Admin command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract command parameters

    target = command_data.get("target")
    action = command_data.get("action")

    if not target or not action:
        return {"result": "Missing parameters. Usage: command <target> <action>"}

    # Perform admin action

    try:
        # Admin-specific logic here

        result_message = f"Admin action completed: {action} on {target}"

        logger.info(f"Admin command completed by {player_name}: {action} on {target}")
        return {"result": result_message}

    except Exception as e:
        logger.error(f"Admin command error for {player_name}: {str(e)}")
        return {"result": "An error occurred while processing the admin command."}
```

### 4. Event-Driven Commands

Commands that trigger game events:

```python
async def handle_event_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command that triggers game events."""

    logger.debug("Processing event command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Event command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Event command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract command parameters

    action = command_data.get("action")
    target = command_data.get("target")

    # Create and publish event

    from ..game.events import GameEvent, EventType

    event = GameEvent(
        event_type=EventType.PLAYER_ACTION,
        player_id=str(player.player_id),
        room_id=player.current_room_id,
        data={
            "action": action,
            "target": target,
            "player_name": player_name
        }
    )

    try:
        persistence._event_bus.publish(event)
        result_message = f"You triggered {action}"

        logger.info(f"Event command completed for {player_name}: {action}")
        return {"result": result_message}

    except Exception as e:
        logger.error(f"Event command error for {player_name}: {str(e)}")
        return {"result": "An error occurred while processing your command."}
```

### 5. Parameter-Validation Commands

Commands with complex parameter validation:

```python
async def handle_validation_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with complex parameter validation."""

    logger.debug("Processing validation command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Validation command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Validation command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract and validate parameters

    param1 = command_data.get("param1")
    param2 = command_data.get("param2")

    # Complex validation logic

    if not param1:
        return {"result": "Missing required parameter 1."}

    if param2 and len(param2) > 100:
        return {"result": "Parameter 2 too long (max 100 characters)."}

    # Business logic validation

    if param1.lower() in ["forbidden", "restricted", "banned"]:
        return {"result": "That parameter is not allowed."}

    # Perform command logic

    result_message = f"Validation successful: {param1}"
    if param2:
        result_message += f" with {param2}"

    logger.info(f"Validation command completed for {player_name}: {param1}")
    return {"result": result_message}
```

---

## Accessing Game Systems

### Persistence Layer

```python
# Get persistence layer

app = request.app if request else None
persistence = app.state.persistence if app else None

if not persistence:
    logger.warning("Command failed - no persistence layer", player=player_name)
    return {"result": "You can't perform that action right now."}

# Common persistence operations

player = persistence.get_player_by_name(username)
room = persistence.get_room(room_id)
room_players = persistence.get_players_in_room(room_id)
```

### Event System

```python
from ..game.events import GameEvent, EventType

# Create event

event = GameEvent(
    event_type=EventType.PLAYER_ACTION,
    player_id=str(player.player_id),
    room_id=room_id,
    data={"action": "custom_action", "data": "custom_data"}
)

# Publish event

persistence._event_bus.publish(event)
```

### Movement Service

```python
from ..game.movement_service import MovementService

# Create movement service

movement_service = MovementService(persistence._event_bus)

# Move player

success = movement_service.move_player(
    str(player.player_id),
    current_room_id,
    target_room_id
)
```

---

## Error Handling Patterns

### Graceful Degradation

```python
async def handle_robust_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with robust error handling."""

    try:
        # Get persistence layer

        app = request.app if request else None
        persistence = app.state.persistence if app else None

        if not persistence:
            logger.warning("Robust command failed - no persistence layer", player=player_name)
            return {"result": "You can't perform that action right now."}

        # Get player data

        player = persistence.get_player_by_name(get_username_from_user(current_user))
        if not player:
            logger.warning("Robust command failed - player not found", player=player_name)
            return {"result": "You can't perform that action right now."}

        # Perform command logic

        result_message = "Command completed successfully"

        logger.info(f"Robust command completed for {player_name}")
        return {"result": result_message}

    except ValueError as e:
        # Handle validation errors

        logger.warning(f"Robust command validation error for {player_name}: {str(e)}")
        return {"result": f"Invalid input: {str(e)}"}

    except PermissionError as e:
        # Handle permission errors

        logger.warning(f"Robust command permission error for {player_name}: {str(e)}")
        return {"result": "You don't have permission for that action."}

    except Exception as e:
        # Handle unexpected errors

        logger.error(f"Robust command unexpected error for {player_name}: {str(e)}", exc_info=True)
        return {"result": "An unexpected error occurred. Please try again."}
```

### Specific Error Handling

```python
async def handle_specific_errors(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with specific error handling."""

    # Check for specific error conditions

    if not command_data.get("required_param"):
        return {"result": "Missing required parameter."}

    # Get persistence layer with specific error handling

    try:
        app = request.app if request else None
        persistence = app.state.persistence if app else None
    except AttributeError:
        logger.error("Request object missing app attribute", player=player_name)
        return {"result": "System error. Please contact an administrator."}

    if not persistence:
        logger.warning("Specific errors command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player with specific error handling

    try:
        player = persistence.get_player_by_name(get_username_from_user(current_user))
    except KeyError:
        logger.error("User object missing username", player=player_name, current_user=current_user)
        return {"result": "Authentication error. Please log in again."}

    if not player:
        logger.warning("Specific errors command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Perform command logic

    result_message = "Command completed successfully"

    logger.info(f"Specific errors command completed for {player_name}")
    return {"result": result_message}
```

---

## Logging Patterns

### Standard Logging

```python
async def handle_logged_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with comprehensive logging."""

    # Entry logging

    logger.debug("Processing logged command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Logged command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Logged command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract parameters

    action = command_data.get("action")
    target = command_data.get("target")

    # Log parameter extraction

    logger.debug("Command parameters extracted", player=player_name, action=action, target=target)

    # Perform command logic

    try:
        result_message = f"Action {action} completed"
        if target:
            result_message += f" on {target}"

        # Success logging

        logger.info(f"Logged command completed for {player_name}: {action}",
                   player=player_name, action=action, target=target, room_id=player.current_room_id)

        return {"result": result_message}

    except Exception as e:
        # Error logging

        logger.error(f"Logged command error for {player_name}: {str(e)}",
                    player=player_name, action=action, target=target, error=str(e), exc_info=True)
        return {"result": "An error occurred while processing your command."}
```

### Security Logging

```python
async def handle_security_logged_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with security-focused logging."""

    # Log command attempt

    logger.info("Security command attempted",
               player=player_name,
               command_type=command_data.get("command_type"),
               parameters=command_data,
               user_agent=request.headers.get("user-agent", "unknown") if request else "unknown")

    # Check permissions

    if not current_user.get("is_admin", False):
        logger.warning("Security command attempted by non-admin user",
                      player=player_name,
                      command_type=command_data.get("command_type"))
        return {"result": "You don't have permission for that command."}

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.error("Security command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Perform security-sensitive action

    target = command_data.get("target")
    action = command_data.get("action")

    # Log security action

    logger.info("Security action performed",
               admin=player_name,
               action=action,
               target=target,
               timestamp=datetime.utcnow().isoformat())

    result_message = f"Security action {action} completed on {target}"

    return {"result": result_message}
```

---

## Security Patterns

### Input Sanitization

```python
async def handle_sanitized_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with input sanitization."""

    logger.debug("Processing sanitized command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Sanitized command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Sanitized command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract and sanitize parameters

    raw_input = command_data.get("input", "")

    # Sanitize input

    import html
    sanitized_input = html.escape(raw_input.strip())

    # Additional security checks

    dangerous_patterns = ["<script", "javascript:", "onload=", "onerror="]
    for pattern in dangerous_patterns:
        if pattern.lower() in raw_input.lower():
            logger.warning("Dangerous input detected", player=player_name, pattern=pattern, input=raw_input)
            return {"result": "Input contains forbidden content."}

    # Perform command logic with sanitized input

    result_message = f"Processed: {sanitized_input}"

    logger.info(f"Sanitized command completed for {player_name}")
    return {"result": result_message}
```

### Rate Limiting

```python
async def handle_rate_limited_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with rate limiting."""

    logger.debug("Processing rate limited command", player=player_name, args=command_data)

    # Simple rate limiting (in production, use a proper rate limiter)

    command_key = f"{player_name}:rate_limited_command"
    current_time = time.time()

    # Check rate limit (example implementation)

    last_execution = getattr(request.app.state, f"last_{command_key}", 0)
    if current_time - last_execution < 5:  # 5 second cooldown
        logger.warning("Rate limit exceeded", player=player_name, command="rate_limited_command")
        return {"result": "You're using that command too frequently. Please wait a moment."}

    # Update last execution time

    setattr(request.app.state, f"last_{command_key}", current_time)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Rate limited command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Perform command logic

    result_message = "Rate limited command completed"

    logger.info(f"Rate limited command completed for {player_name}")
    return {"result": result_message}
```

---

## Performance Patterns

### Caching

```python
async def handle_cached_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command with caching for performance."""

    logger.debug("Processing cached command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Cached command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Cached command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Check cache (example implementation)

    cache_key = f"cached_command:{player_name}:{command_data.get('action')}"
    cached_result = getattr(request.app.state, cache_key, None)

    if cached_result and time.time() - cached_result.get("timestamp", 0) < 300:  # 5 minute cache
        logger.debug("Using cached result", player=player_name, cache_key=cache_key)
        return {"result": cached_result["data"]}

    # Perform expensive operation

    expensive_result = "Expensive operation result"

    # Cache result

    setattr(request.app.state, cache_key, {
        "data": expensive_result,
        "timestamp": time.time()
    })

    logger.info(f"Cached command completed for {player_name}")
    return {"result": expensive_result}
```

### Batch Operations

```python
async def handle_batch_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """Handle a command that performs batch operations."""

    logger.debug("Processing batch command", player=player_name, args=command_data)

    # Get persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Batch command failed - no persistence layer", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Get player data

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Batch command failed - player not found", player=player_name)
        return {"result": "You can't perform that action right now."}

    # Extract batch parameters

    items = command_data.get("items", [])
    if not items:
        return {"result": "No items specified for batch operation."}

    # Limit batch size for performance

    if len(items) > 100:
        return {"result": "Too many items for batch operation (max 100)."}

    # Perform batch operation

    results = []
    for item in items:
        try:
            # Process individual item

            result = f"Processed: {item}"
            results.append(result)
        except Exception as e:
            logger.warning(f"Batch item processing failed", player=player_name, item=item, error=str(e))
            results.append(f"Failed: {item}")

    result_message = f"Batch operation completed: {len(results)} items processed"

    logger.info(f"Batch command completed for {player_name}: {len(results)} items")
    return {"result": result_message}
```

---

## Testing Patterns

### Mock Setup

```python
@pytest.mark.asyncio
async def test_command_handler():
    """Test a command handler with proper mocking."""

    # Mock dependencies

    mock_request = Mock()
    mock_app = Mock()
    mock_persistence = Mock()
    mock_player = Mock()
    mock_alias_storage = Mock()

    # Setup mocks

    mock_request.app = mock_app
    mock_app.state.persistence = mock_persistence
    mock_persistence.get_player_by_name.return_value = mock_player

    # Test data

    command_data = {"command_type": "test_command", "param1": "value1"}
    current_user = {"username": "testuser"}

    # Execute command

    result = await handle_test_command(
        command_data, current_user, mock_request, mock_alias_storage, "testuser"
    )

    # Verify result

    assert "result" in result
    assert "success" in result["result"]

    # Verify mocks were called correctly

    mock_persistence.get_player_by_name.assert_called_once_with("testuser")
```

### Error Testing

```python
@pytest.mark.asyncio
async def test_command_handler_errors():
    """Test command handler error conditions."""

    # Mock dependencies

    mock_request = Mock()
    mock_app = Mock()
    mock_persistence = Mock()
    mock_alias_storage = Mock()

    # Setup mocks for error condition

    mock_request.app = mock_app
    mock_app.state.persistence = None  # Simulate missing persistence

    # Test data

    command_data = {"command_type": "test_command"}
    current_user = {"username": "testuser"}

    # Execute command

    result = await handle_test_command(
        command_data, current_user, mock_request, mock_alias_storage, "testuser"
    )

    # Verify error handling

    assert "result" in result
    assert "can't perform" in result["result"]
```

---

## Anti-Patterns to Avoid

### 1. Blocking Operations

```python
# WRONG - blocking operation in async handler

async def handle_blocking_command(...):
    # This blocks the event loop

    time.sleep(5)  # Don't do this!
    return {"result": "Done"}

# RIGHT - use asyncio.sleep for async operations

async def handle_async_command(...):
    await asyncio.sleep(5)  # This is okay
    return {"result": "Done"}
```

### 2. Ignoring Errors

```python
# WRONG - silently ignoring errors

async def handle_ignored_errors(...):
    try:
        # Command logic

        pass
    except Exception:
        pass  # Don't do this!
    return {"result": "Success"}

# RIGHT - proper error handling

async def handle_proper_errors(...):
    try:
        # Command logic

        pass
    except Exception as e:
        logger.error(f"Command error: {str(e)}")
        return {"result": "An error occurred"}
```

### 3. Hardcoded Values

```python
# WRONG - hardcoded values

async def handle_hardcoded_command(...):
    if len(param) > 100:  # Magic number
        return {"result": "Too long"}

# RIGHT - use constants

MAX_PARAM_LENGTH = 100

async def handle_constants_command(...):
    if len(param) > MAX_PARAM_LENGTH:
        return {"result": f"Too long (max {MAX_PARAM_LENGTH} characters)"}
```

### 4. Inconsistent Logging

```python
# WRONG - inconsistent logging

async def handle_inconsistent_logging(...):
    logger.info("Command started")  # Different log levels
    logger.debug("Processing")      # for same operation
    logger.warning("Completed")     # Don't do this!

# RIGHT - consistent logging

async def handle_consistent_logging(...):
    logger.debug("Command started")
    logger.debug("Processing")
    logger.info("Command completed successfully")
```

### 5. Not Validating Input

```python
# WRONG - no input validation

async def handle_unvalidated_command(...):
    param = command_data.get("param")
    # Use param directly without validation

    result = f"Processed: {param}"

# RIGHT - validate input

async def handle_validated_command(...):
    param = command_data.get("param")
    if not param or len(param) > 100:
        return {"result": "Invalid parameter"}
    result = f"Processed: {param}"
```

---

*This reference document should be updated as new patterns emerge and existing ones evolve.*
