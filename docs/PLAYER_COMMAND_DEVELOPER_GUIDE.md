# 🐙 MythosMUD Player Command Developer's Guide

*"The proper study of mankind is the command line."* - H.P. Lovecraft (probably)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Command System Overview](#command-system-overview)
3. [Quick Start: Your First Command](#quick-start-your-first-command)
4. [Command Anatomy](#command-anatomy)
5. [Development Workflow](#development-workflow)
6. [Testing Your Commands](#testing-your-commands)
7. [Common Patterns](#common-patterns)
8. [Security Considerations](#security-considerations)
9. [AI-Assisted Development](#ai-assisted-development)
10. [Troubleshooting](#troubleshooting)
11. [Reference Documents](#reference-documents)

---

## Introduction

Welcome, junior researcher! You've been assigned to the forbidden task of implementing player commands for MythosMUD.
Fear not - this guide will illuminate the dark corners of our command system and prepare you for the eldritch knowledge
that lies ahead.

### What You'll Learn

How to implement new player commands from scratch

- Understanding the command processing pipeline
- Writing secure, testable command code
- Using AI to accelerate your development
- Following project conventions and best practices

### Prerequisites

Basic Python knowledge (functions, classes, async/await)

- Familiarity with FastAPI concepts (optional, we'll explain as we go)
- Understanding of the MythosMUD project structure
- A healthy respect for the unknown

---

## Command System Overview

The MythosMUD command system is built on a multi-layered architecture that ensures security, maintainability, and
extensibility. Here's how it all fits together:

### Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    Client (React/TypeScript)                │
├─────────────────────────────────────────────────────────────┤
│                 WebSocket/HTTP API Layer                    │
├─────────────────────────────────────────────────────────────┤
│                Command Handler (Unified)                    │
├─────────────────────────────────────────────────────────────┤
│              Command Validation & Parsing                   │
├─────────────────────────────────────────────────────────────┤
│                Command Service (Routing)                    │
├─────────────────────────────────────────────────────────────┤
│              Individual Command Handlers                    │
├─────────────────────────────────────────────────────────────┤
│              Game Systems (Persistence, Events)             │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

1. **Command Handler (`command_handler_unified.py`)**: Entry point for all commands
2. **Command Validator (`validators/command_validator.py`)**: Security and format validation
3. **Command Parser (`utils/command_parser.py`)**: Pydantic-based command parsing
4. **Command Service (`commands/command_service.py`)**: Routes commands to handlers
5. **Command Models (`models/command.py`)**: Type-safe command definitions
6. **Individual Handlers**: Specific command implementations

### Command Flow

1. Player types command in client
2. Command sent via WebSocket/HTTP to server
3. Command validated for security and format
4. Command parsed into structured data
5. Command routed to appropriate handler
6. Handler executes game logic
7. Result returned to player

---

## Quick Start: Your First Command

Let's implement a simple `dance` command to get you started. This command will make the player perform a dance and
notify others in the room.

### Step 1: Define the Command Model

First, we need to define what our command looks like. Open `server/models/command.py` and add:

```python
class DanceCommand(BaseCommand):
    """Command for performing a dance."""

    command_type: Literal[CommandType.DANCE] = CommandType.DANCE
    dance_style: str | None = Field(None, description="Style of dance to perform")

    @field_validator("dance_style")
    @classmethod
    def validate_dance_style(cls, v):
        """Validate dance style is reasonable."""
        if v is not None and len(v) > 50:
            raise ValueError("Dance style description too long")
        return v
```

Also add `DANCE = "dance"` to the `CommandType` enum.

### Step 2: Create the Command Handler

Create a new file `server/commands/social_commands.py`:

```python
"""
Social commands for MythosMUD.

This module contains handlers for social interaction commands.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..logging_config import get_logger

logger = get_logger(__name__)


def get_username_from_user(user_obj):
    """Safely extract username from user object or dictionary."""
    if hasattr(user_obj, "username"):
        return user_obj.username
    elif hasattr(user_obj, "name"):
        return user_obj.name
    elif isinstance(user_obj, dict) and "username" in user_obj:
        return user_obj["username"]
    elif isinstance(user_obj, dict) and "name" in user_obj:
        return user_obj["name"]
    else:
        raise ValueError("User object must have username or name attribute or key")


async def handle_dance_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the dance command for social interaction.

    Args:
        command_data: Command data dictionary containing validated command information
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Dance command result
    """
    logger.debug("Processing dance command", player=player_name, args=command_data)

    # Get the persistence layer

    app = request.app if request else None
    persistence = app.state.persistence if app else None

    if not persistence:
        logger.warning("Dance command failed - no persistence layer", player=player_name)
        return {"result": "You can't dance right now."}

    # Get the player

    player = persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        logger.warning("Dance command failed - player not found", player=player_name)
        return {"result": "You can't dance right now."}

    # Get dance style from command data

    dance_style = command_data.get("dance_style", "wildly")

    # Create the dance message

    dance_message = f"{player_name} dances {dance_style}!"

    # Get other players in the room

    room_id = player.current_room_id
    room_players = persistence.get_players_in_room(room_id)

    # Send message to all players in the room

    for room_player in room_players:
        if room_player.username != player_name:  # Don't send to self
            # In a real implementation, you'd use the event system
            # For now, we'll just return a message

            pass

    logger.info(f"Player {player_name} danced {dance_style} in room {room_id}")
    return {"result": dance_message}
```

### Step 3: Register the Command

Add the dance command to the command service. In `server/commands/command_service.py`, add the import:

```python
from .social_commands import handle_dance_command
```

And add it to the `command_handlers` dictionary in the `__init__` method:

```python
"dance": handle_dance_command,
```

### Step 4: Update the Command Parser

In `server/utils/command_parser.py`, add the dance command to the parsing logic:

```python
def _create_command_object(self, command: str, args: list[str]) -> Command:
    """Create the appropriate command object based on command type."""
    if command == "dance":
        dance_style = " ".join(args) if args else None
        return DanceCommand(dance_style=dance_style)
    # ... existing commands ...

```

### Step 5: Test Your Command

Create a test file `server/tests/test_social_commands.py`:

```python
"""
Tests for social commands.
"""

import pytest
from unittest.mock import Mock, MagicMock

from ..commands.social_commands import handle_dance_command


class TestDanceCommand:
    """Test the dance command functionality."""

    @pytest.mark.asyncio
    async def test_dance_command_basic(self):
        """Test basic dance command without style."""
        # Mock dependencies

        mock_request = Mock()
        mock_app = Mock()
        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.username = "testuser"
        mock_player.current_room_id = "room_001"

        # Setup mocks

        mock_request.app = mock_app
        mock_app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_persistence.get_players_in_room.return_value = []

        # Test data

        command_data = {"command_type": "dance", "dance_style": None}
        current_user = {"username": "testuser"}
        alias_storage = Mock()

        # Execute command

        result = await handle_dance_command(
            command_data, current_user, mock_request, alias_storage, "testuser"
        )

        # Verify result

        assert "result" in result
        assert "testuser dances wildly!" in result["result"]

    @pytest.mark.asyncio
    async def test_dance_command_with_style(self):
        """Test dance command with specific style."""
        # Mock dependencies

        mock_request = Mock()
        mock_app = Mock()
        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.username = "testuser"
        mock_player.current_room_id = "room_001"

        # Setup mocks

        mock_request.app = mock_app
        mock_app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_persistence.get_players_in_room.return_value = []

        # Test data

        command_data = {"command_type": "dance", "dance_style": "elegantly"}
        current_user = {"username": "testuser"}
        alias_storage = Mock()

        # Execute command

        result = await handle_dance_command(
            command_data, current_user, mock_request, alias_storage, "testuser"
        )

        # Verify result

        assert "result" in result
        assert "testuser dances elegantly!" in result["result"]
```

### Step 6: Run Tests

```bash
make test
```

Congratulations! You've implemented your first command. This basic example shows the fundamental pattern for all
commands in MythosMUD.

---

## Command Anatomy

Every command in MythosMUD follows a consistent structure. Let's break down the components:

### 1. Command Model (Pydantic)

```python
class YourCommand(BaseCommand):
    """Command for doing something awesome."""

    command_type: Literal[CommandType.YOUR_COMMAND] = CommandType.YOUR_COMMAND
    parameter1: str = Field(..., description="Required parameter")
    parameter2: str | None = Field(None, description="Optional parameter")

    @field_validator("parameter1")
    @classmethod
    def validate_parameter1(cls, v):
        """Validate parameter1."""
        if len(v) > 100:
            raise ValueError("Parameter too long")
        return v
```

**Purpose**: Defines the structure and validation rules for your command.

### 2. Command Handler Function

```python
async def handle_your_command(
    command_data: dict,
    current_user: dict,
    request: Any,
    alias_storage: AliasStorage,
    player_name: str
) -> dict[str, str]:
    """
    Handle the your_command command.

    Args:
        command_data: Validated command data
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name for logging

    Returns:
        dict: Command result with 'result' key
    """
    # Your command logic here

    return {"result": "Success!"}
```

**Purpose**: Contains the actual game logic for your command.

### 3. Command Registration

```python
# In command_service.py

"your_command": handle_your_command,
```

**Purpose**: Maps command names to their handlers.

### 4. Command Parsing

```python
# In command_parser.py

if command == "your_command":
    param1 = args[0] if args else None
    param2 = args[1] if len(args) > 1 else None
    return YourCommand(parameter1=param1, parameter2=param2)
```

**Purpose**: Converts raw command input into structured data.

---

## Development Workflow

### 1. Plan Your Command

Before writing code, ask yourself:

- What should this command do?
- What parameters does it need?
- Who can use it (all players, admins only)?
- What validation is required?
- How should it interact with other game systems?

### 2. Write Tests First (TDD)

```python
@pytest.mark.asyncio
async def test_your_command_success(self):
    """Test successful command execution."""
    # Arrange

    command_data = {"command_type": "your_command", "param1": "value"}
    # Act

    result = await handle_your_command(...)
    # Assert

    assert result["result"] == "Expected output"
```

### 3. Implement the Command

Follow the pattern from the Quick Start section:

1. Define the command model
2. Create the handler function
3. Register the command
4. Update the parser

### 4. Test Thoroughly

```bash
# Run all tests

make test

# Run specific test file

python -m pytest server/tests/test_your_commands.py -v

# Run with coverage

make coverage
```

### 5. Validate and Deploy

```bash
# Check code quality

make lint

# Run security checks

make security
```

---

## Testing Your Commands

### Test Structure

Every command should have comprehensive tests covering:

1. **Happy Path**: Normal command execution
2. **Edge Cases**: Boundary conditions and unusual inputs
3. **Error Conditions**: Invalid inputs, missing data
4. **Security**: Injection attempts, unauthorized access
5. **Integration**: Interaction with other game systems

### Example Test Suite

```python
class TestYourCommand:
    """Test the your_command functionality."""

    @pytest.mark.asyncio
    async def test_your_command_success(self):
        """Test successful command execution."""
        # Test implementation

    @pytest.mark.asyncio
    async def test_your_command_missing_parameter(self):
        """Test command with missing required parameter."""
        # Test implementation

    @pytest.mark.asyncio
    async def test_your_command_invalid_input(self):
        """Test command with invalid input."""
        # Test implementation

    @pytest.mark.asyncio
    async def test_your_command_unauthorized(self):
        """Test command with unauthorized user."""
        # Test implementation

```

### Mocking Dependencies

```python
# Mock the persistence layer

mock_persistence = Mock()
mock_persistence.get_player_by_name.return_value = mock_player

# Mock the request object

mock_request = Mock()
mock_request.app = Mock()
mock_request.app.state.persistence = mock_persistence
```

### Testing Command Validation

```python
def test_your_command_validation(self):
    """Test command model validation."""
    # Valid command

    valid_cmd = YourCommand(parameter1="valid", parameter2="optional")
    assert valid_cmd.parameter1 == "valid"

    # Invalid command

    with pytest.raises(ValidationError):
        YourCommand(parameter1="")  # Empty required field
```

---

## Common Patterns

### 1. Room-Based Commands

Commands that affect the current room:

```python
# Get player's current room

player = persistence.get_player_by_name(get_username_from_user(current_user))
room_id = player.current_room_id
room = persistence.get_room(room_id)

# Get other players in room

room_players = persistence.get_players_in_room(room_id)
```

### 2. Player-Targeted Commands

Commands that target other players:

```python
target_player_name = command_data.get("target_player")
if not target_player_name:
    return {"result": "Target who?"}

target_player = persistence.get_player_by_name(target_player_name)
if not target_player:
    return {"result": "Player not found."}
```

### 3. Admin-Only Commands

Commands restricted to administrators:

```python
if not current_user.get("is_admin", False):
    return {"result": "You don't have permission for that command."}
```

### 4. Event-Driven Commands

Commands that trigger game events:

```python
from ..game.events import GameEvent, EventType

# Create and publish event

event = GameEvent(
    event_type=EventType.PLAYER_ACTION,
    player_id=str(player.player_id),
    room_id=room_id,
    data={"action": "dance", "style": dance_style}
)
persistence._event_bus.publish(event)
```

### 5. Parameter Validation

```python
# In your command model

@field_validator("parameter")
@classmethod
def validate_parameter(cls, v):
    """Validate parameter meets requirements."""
    if v is not None:
        if len(v) < 1:
            raise ValueError("Parameter cannot be empty")
        if len(v) > 100:
            raise ValueError("Parameter too long")
        if not v.isalnum():
            raise ValueError("Parameter must be alphanumeric")
    return v
```

---

## Security Considerations

### 1. Input Validation

Always validate user input:

```python
# Use Pydantic models for automatic validation

class SafeCommand(BaseCommand):
    parameter: str = Field(..., min_length=1, max_length=100)

    @field_validator("parameter")
    @classmethod
    def validate_parameter(cls, v):
        # Custom validation logic

        if any(char in v for char in ["<", ">", "&", '"', "'"]):
            raise ValueError("Invalid characters in parameter")
        return v
```

### 2. Authorization

Check permissions before executing commands:

```python
# Check if user is admin

if not current_user.get("is_admin", False):
    return {"result": "Insufficient permissions."}

# Check if user is muted

if current_user.get("is_muted", False):
    return {"result": "You are currently muted."}
```

### 3. Rate Limiting

Consider implementing rate limiting for commands:

```python
# Example rate limiting (implement as needed)

from ..utils.rate_limiter import RateLimiter

rate_limiter = RateLimiter()
if not rate_limiter.allow_command(player_name, "your_command"):
    return {"result": "You're using that command too frequently."}
```

### 4. Logging

Log all command executions for security:

```python
logger.info(
    "Command executed",
    player=player_name,
    command="your_command",
    parameters=command_data,
    room_id=room_id
)
```

---

## AI-Assisted Development

### Working with AI Tools

When using AI to help implement commands:

1. **Provide Context**: Share the relevant parts of the codebase
2. **Be Specific**: Describe exactly what you want the command to do
3. **Review Carefully**: Always review AI-generated code before using it
4. **Test Thoroughly**: AI code should be tested just like human code

### Example AI Prompt

```
I'm implementing a new command called "whisper" for MythosMUD.
The command should allow players to send private messages to other players.

Requirements:
- Syntax: whisper <player> <message>
- Only the target player should see the message
- Players can't whisper to themselves
- Invalid player names should return an error
- Messages should be logged for moderation

Here's the existing command structure:
[Include relevant code examples]

Can you help me implement this command following the project's patterns?
```

### AI Code Review Checklist

[ ] Follows project naming conventions

- [ ] Includes proper error handling
- [ ] Has appropriate logging
- [ ] Includes security validation
- [ ] Follows the established command pattern
- [ ] Has proper type hints
- [ ] Includes docstrings

---

## Troubleshooting

### Common Issues

#### 1. Command Not Found

**Problem**: Command returns "Unknown command" error.

**Solution**: Check that the command is properly registered in `command_service.py`.

#### 2. Validation Errors

**Problem**: Command fails validation with cryptic error messages.

**Solution**: Check your Pydantic model validation rules and ensure input matches expected format.

#### 3. Persistence Layer Issues

**Problem**: Command can't access player or room data.

**Solution**: Verify that the persistence layer is properly mocked in tests and available in production.

#### 4. Permission Denied

**Problem**: Admin commands fail for non-admin users.

**Solution**: Check the user's admin status in the `current_user` object.

### Debugging Tips

1. **Use Logging**: Add debug logs to trace command execution
2. **Check Tests**: Run tests to isolate issues
3. **Validate Input**: Use the command validator to test input
4. **Review Models**: Ensure Pydantic models match your expectations

### Getting Help

1. Check the reference documents below
2. Review existing command implementations
3. Look at test files for examples
4. Ask in the project's communication channels

---

## Reference Documents

For detailed information on specific aspects of command development, see:

- [Command Models Reference](COMMAND_MODELS_REFERENCE.md) - Complete Pydantic model documentation
- [Command Handler Patterns](COMMAND_HANDLER_PATTERNS.md) - Common handler implementation patterns
- [Command Testing Guide](COMMAND_TESTING_GUIDE.md) - Comprehensive testing strategies
- [Command Security Guide](COMMAND_SECURITY_GUIDE.md) - Security best practices and validation
- [AI Development Workflow](AI_DEVELOPMENT_WORKFLOW.md) - Using AI tools effectively

---

## Conclusion

You now have the foundational knowledge to implement commands in MythosMUD! Remember:

**Start Simple**: Begin with basic commands and add complexity gradually

**Test First**: Write tests before implementing features

**Follow Patterns**: Use the established patterns for consistency

**Security First**: Always validate input and check permissions

**Document Everything**: Good documentation helps everyone

The command system is designed to be extensible and maintainable. As you become more familiar with the patterns, you'll
be able to implement increasingly complex commands that enhance the MythosMUD experience.

*"The most merciful thing in the world, I think, is the inability of the human brain to correlate all its contents."* -
H.P. Lovecraft

Good luck with your eldritch coding endeavors!

---

*This guide is a living document. As the codebase evolves, so too will this guide. Please contribute improvements and
corrections as you discover them.*
