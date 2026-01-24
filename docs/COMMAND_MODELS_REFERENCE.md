# 🐙 MythosMUD Command Models Reference

*"The structure of reality is defined by the models we create."* - Anonymous Miskatonic Scholar

---

## Table of Contents

1. [Overview](#overview)
2. [Base Command Structure](#base-command-structure)
3. [Existing Command Models](#existing-command-models)
4. [Creating New Command Models](#creating-new-command-models)
5. [Validation Patterns](#validation-patterns)
6. [Field Types and Constraints](#field-types-and-constraints)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)

---

## Overview

Command models in MythosMUD use Pydantic for type-safe validation and serialization. Each command is defined as a
Pydantic model that inherits from `BaseCommand` and includes validation rules to ensure security and data integrity.

### Key Benefits

**Type Safety**: Automatic type checking and conversion

**Security**: Built-in validation prevents injection attacks

**Documentation**: Self-documenting code with field descriptions

**Consistency**: Standardized structure across all commands

**Error Handling**: Clear error messages for invalid input

---

## Base Command Structure

All command models inherit from `BaseCommand`, which provides common configuration and security features:

```python
class BaseCommand(BaseModel):
    """
    Base class for all MythosMUD commands.

    Provides common validation and security features for all commands.
    """

    model_config = {
        # Security: reject unknown fields to prevent injection

        "extra": "forbid",
        # Use enum values for validation

        "use_enum_values": True,
        # Validate assignment

        "validate_assignment": True,
    }
```

### Configuration Options

**`extra: "forbid"`**: Prevents additional fields from being accepted, blocking injection attacks

**`use_enum_values: True`**: Uses enum values instead of enum objects for cleaner serialization

**`validate_assignment: True`**: Validates field assignments after object creation

---

## Existing Command Models

### Exploration Commands

#### LookCommand

```python
class LookCommand(BaseCommand):
    """Command for looking around or in a specific direction."""

    command_type: Literal[CommandType.LOOK] = CommandType.LOOK
    direction: Direction | None = Field(None, description="Direction to look")

    @field_validator("direction")
    @classmethod
    def validate_direction(cls, v):
        """Validate direction is one of the allowed values."""
        if v is not None and v not in Direction:
            raise ValueError(f"Invalid direction: {v}. Must be one of: {list(Direction)}")
        return v
```

**Usage**: `look` or `look north`

#### GoCommand

```python
class GoCommand(BaseCommand):
    """Command for moving in a specific direction."""

    command_type: Literal[CommandType.GO] = CommandType.GO
    direction: Direction = Field(..., description="Direction to move")

    @field_validator("direction")
    @classmethod
    def validate_direction(cls, v):
        """Validate direction is one of the allowed values."""
        if v not in Direction:
            raise ValueError(f"Invalid direction: {v}. Must be one of: {list(Direction)}")
        return v
```

**Usage**: `go north`

### Communication Commands

#### SayCommand

```python
class SayCommand(BaseCommand):
    """Command for speaking to others in the room."""

    command_type: Literal[CommandType.SAY] = CommandType.SAY
    message: str = Field(..., description="Message to say")

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content."""
        if not v.strip():
            raise ValueError("Message cannot be empty")
        if len(v) > 500:
            raise ValueError("Message too long (max 500 characters)")
        return v.strip()
```

**Usage**: `say Hello, everyone!`

#### EmoteCommand

```python
class EmoteCommand(BaseCommand):
    """Command for performing emotes."""

    command_type: Literal[CommandType.EMOTE] = CommandType.EMOTE
    action: str = Field(..., description="Action to perform")

    @field_validator("action")
    @classmethod
    def validate_action(cls, v):
        """Validate action content."""
        if not v.strip():
            raise ValueError("Action cannot be empty")
        if len(v) > 200:
            raise ValueError("Action too long (max 200 characters)")
        return v.strip()
```

**Usage**: `emote smiles warmly`

#### MeCommand

```python
class MeCommand(BaseCommand):
    """Command for describing personal actions."""

    command_type: Literal[CommandType.ME] = CommandType.ME
    action: str = Field(..., description="Action to perform")

    @field_validator("action")
    @classmethod
    def validate_action(cls, v):
        """Validate action content."""
        if not v.strip():
            raise ValueError("Action cannot be empty")
        if len(v) > 200:
            raise ValueError("Action too long (max 200 characters)")
        return v.strip()
```

**Usage**: `me examines the ancient tome`

#### PoseCommand

```python
class PoseCommand(BaseCommand):
    """Command for setting personal pose."""

    command_type: Literal[CommandType.POSE] = CommandType.POSE
    pose: str = Field(..., description="Pose to set")

    @field_validator("pose")
    @classmethod
    def validate_pose(cls, v):
        """Validate pose content."""
        if not v.strip():
            raise ValueError("Pose cannot be empty")
        if len(v) > 200:
            raise ValueError("Pose too long (max 200 characters)")
        return v.strip()
```

**Usage**: `pose stands with an air of mystery`

### Alias Commands

#### AliasCommand

```python
class AliasCommand(BaseCommand):
    """Command for creating aliases."""

    command_type: Literal[CommandType.ALIAS] = CommandType.ALIAS
    alias_name: str = Field(..., description="Name of the alias")
    alias_command: str = Field(..., description="Command to alias")

    @field_validator("alias_name")
    @classmethod
    def validate_alias_name(cls, v):
        """Validate alias name."""
        if not v.strip():
            raise ValueError("Alias name cannot be empty")
        if len(v) > 50:
            raise ValueError("Alias name too long (max 50 characters)")
        if not v.isalnum():
            raise ValueError("Alias name must be alphanumeric")
        return v.strip().lower()

    @field_validator("alias_command")
    @classmethod
    def validate_alias_command(cls, v):
        """Validate alias command."""
        if not v.strip():
            raise ValueError("Alias command cannot be empty")
        if len(v) > 200:
            raise ValueError("Alias command too long (max 200 characters)")
        return v.strip()
```

**Usage**: `alias n go north`

#### AliasesCommand

```python
class AliasesCommand(BaseCommand):
    """Command for listing aliases."""

    command_type: Literal[CommandType.ALIASES] = CommandType.ALIASES
```

**Usage**: `aliases`

#### UnaliasCommand

```python
class UnaliasCommand(BaseCommand):
    """Command for removing aliases."""

    command_type: Literal[CommandType.UNALIAS] = CommandType.UNALIAS
    alias_name: str = Field(..., description="Name of the alias to remove")

    @field_validator("alias_name")
    @classmethod
    def validate_alias_name(cls, v):
        """Validate alias name."""
        if not v.strip():
            raise ValueError("Alias name cannot be empty")
        if len(v) > 50:
            raise ValueError("Alias name too long (max 50 characters)")
        if not v.isalnum():
            raise ValueError("Alias name must be alphanumeric")
        return v.strip().lower()
```

**Usage**: `unalias n`

### Administrative Commands

#### MuteCommand

```python
class MuteCommand(BaseCommand):
    """Command for muting players."""

    command_type: Literal[CommandType.MUTE] = CommandType.MUTE
    player_name: str = Field(..., description="Player to mute")
    duration_minutes: int = Field(..., description="Duration in minutes")
    reason: str = Field(..., description="Reason for mute")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name."""
        if not v.strip():
            raise ValueError("Player name cannot be empty")
        if len(v) > 50:
            raise ValueError("Player name too long (max 50 characters)")
        return v.strip()

    @field_validator("duration_minutes")
    @classmethod
    def validate_duration(cls, v):
        """Validate duration."""
        if v < 1:
            raise ValueError("Duration must be at least 1 minute")
        if v > 10080:  # 1 week
            raise ValueError("Duration cannot exceed 1 week")
        return v

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v):
        """Validate reason."""
        if not v.strip():
            raise ValueError("Reason cannot be empty")
        if len(v) > 200:
            raise ValueError("Reason too long (max 200 characters)")
        return v.strip()
```

**Usage**: `mute player_name 60 Spamming`

#### UnmuteCommand

```python
class UnmuteCommand(BaseCommand):
    """Command for unmuting players."""

    command_type: Literal[CommandType.UNMUTE] = CommandType.UNMUTE
    player_name: str = Field(..., description="Player to unmute")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name."""
        if not v.strip():
            raise ValueError("Player name cannot be empty")
        if len(v) > 50:
            raise ValueError("Player name too long (max 50 characters)")
        return v.strip()
```

**Usage**: `unmute player_name`

#### MuteGlobalCommand

```python
class MuteGlobalCommand(BaseCommand):
    """Command for global muting."""

    command_type: Literal[CommandType.MUTE_GLOBAL] = CommandType.MUTE_GLOBAL
    duration_minutes: int = Field(..., description="Duration in minutes")
    reason: str = Field(..., description="Reason for global mute")

    @field_validator("duration_minutes")
    @classmethod
    def validate_duration(cls, v):
        """Validate duration."""
        if v < 1:
            raise ValueError("Duration must be at least 1 minute")
        if v > 1440:  # 24 hours
            raise ValueError("Global mute cannot exceed 24 hours")
        return v

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v):
        """Validate reason."""
        if not v.strip():
            raise ValueError("Reason cannot be empty")
        if len(v) > 200:
            raise ValueError("Reason too long (max 200 characters)")
        return v.strip()
```

**Usage**: `mute_global 60 Maintenance`

#### UnmuteGlobalCommand

```python
class UnmuteGlobalCommand(BaseCommand):
    """Command for removing global mute."""

    command_type: Literal[CommandType.UNMUTE_GLOBAL] = CommandType.UNMUTE_GLOBAL
```

**Usage**: `unmute_global`

#### AddAdminCommand

```python
class AddAdminCommand(BaseCommand):
    """Command for adding administrators."""

    command_type: Literal[CommandType.ADD_ADMIN] = CommandType.ADD_ADMIN
    player_name: str = Field(..., description="Player to make admin")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name."""
        if not v.strip():
            raise ValueError("Player name cannot be empty")
        if len(v) > 50:
            raise ValueError("Player name too long (max 50 characters)")
        return v.strip()
```

**Usage**: `add_admin player_name`

#### MutesCommand

```python
class MutesCommand(BaseCommand):
    """Command for listing active mutes."""

    command_type: Literal[CommandType.MUTES] = CommandType.MUTES
```

**Usage**: `mutes`

### Teleport Commands

#### TeleportCommand

```python
class TeleportCommand(BaseCommand):
    """Command for teleporting players."""

    command_type: Literal[CommandType.TELEPORT] = CommandType.TELEPORT
    player_name: str = Field(..., description="Player to teleport")
    room_id: str = Field(..., description="Destination room ID")

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v):
        """Validate player name."""
        if not v.strip():
            raise ValueError("Player name cannot be empty")
        if len(v) > 50:
            raise ValueError("Player name too long (max 50 characters)")
        return v.strip()

    @field_validator("room_id")
    @classmethod
    def validate_room_id(cls, v):
        """Validate room ID."""
        if not v.strip():
            raise ValueError("Room ID cannot be empty")
        if len(v) > 100:
            raise ValueError("Room ID too long (max 100 characters)")
        return v.strip()
```

**Usage**: `teleport player_name room_001`

#### GotoCommand

```python
class GotoCommand(BaseCommand):
    """Command for teleporting to a room."""

    command_type: Literal[CommandType.GOTO] = CommandType.GOTO
    room_id: str = Field(..., description="Destination room ID")

    @field_validator("room_id")
    @classmethod
    def validate_room_id(cls, v):
        """Validate room ID."""
        if not v.strip():
            raise ValueError("Room ID cannot be empty")
        if len(v) > 100:
            raise ValueError("Room ID too long (max 100 characters)")
        return v.strip()
```

**Usage**: `goto room_001`

#### ConfirmTeleportCommand

```python
class ConfirmTeleportCommand(BaseCommand):
    """Command for confirming teleport."""

    command_type: Literal[CommandType.CONFIRM_TELEPORT] = CommandType.CONFIRM_TELEPORT
```

**Usage**: `confirm_teleport`

#### ConfirmGotoCommand

```python
class ConfirmGotoCommand(BaseCommand):
    """Command for confirming goto."""

    command_type: Literal[CommandType.CONFIRM_GOTO] = CommandType.CONFIRM_GOTO
```

**Usage**: `confirm_goto`

### System Commands

#### HelpCommand

```python
class HelpCommand(BaseCommand):
    """Command for getting help."""

    command_type: Literal[CommandType.HELP] = CommandType.HELP
```

**Usage**: `help` or `help command_name`

---

## Creating New Command Models

### Step-by-Step Process

1. **Define the Command Type**

   Add your command to the `CommandType` enum in `server/models/command.py`:

   ```python
   class CommandType(str, Enum):
       # ... existing commands ...

       YOUR_COMMAND = "your_command"
   ```

2. **Create the Command Model**

   ```python
   class YourCommand(BaseCommand):
       """Command for doing something awesome."""

       command_type: Literal[CommandType.YOUR_COMMAND] = CommandType.YOUR_COMMAND
       required_param: str = Field(..., description="Required parameter")
       optional_param: str | None = Field(None, description="Optional parameter")

       @field_validator("required_param")
       @classmethod
       def validate_required_param(cls, v):
           """Validate required parameter."""
           if not v.strip():
               raise ValueError("Required parameter cannot be empty")
           if len(v) > 100:
               raise ValueError("Required parameter too long (max 100 characters)")
           return v.strip()

       @field_validator("optional_param")
       @classmethod
       def validate_optional_param(cls, v):
           """Validate optional parameter."""
           if v is not None:
               if len(v) > 50:
                   raise ValueError("Optional parameter too long (max 50 characters)")
               return v.strip()
           return v
   ```

3. **Add to Command Parser**

   Update `server/utils/command_parser.py` to handle your command:

   ```python
   def _create_command_object(self, command: str, args: list[str]) -> Command:
       """Create the appropriate command object based on command type."""
       if command == "your_command":
           required_param = args[0] if args else ""
           optional_param = args[1] if len(args) > 1 else None
           return YourCommand(required_param=required_param, optional_param=optional_param)
       # ... existing commands ...

   ```

### Model Structure Guidelines

#### Required Fields

**`command_type`**: Always required, must match the CommandType enum

**Required parameters**: Use `Field(..., description="...")` for mandatory fields

**Optional parameters**: Use `Field(None, description="...")` for optional fields

#### Field Types

```python
# String fields

param: str = Field(..., description="Required string")
optional_param: str | None = Field(None, description="Optional string")

# Integer fields

count: int = Field(..., description="Required integer")
optional_count: int | None = Field(None, description="Optional integer")

# Boolean fields

flag: bool = Field(False, description="Boolean flag")

# Enum fields

direction: Direction = Field(..., description="Direction enum")

# List fields

items: list[str] = Field(default_factory=list, description="List of items")
```

---

## Validation Patterns

### String Validation

```python
@field_validator("field_name")
@classmethod
def validate_field_name(cls, v):
    """Validate field content."""
    if v is not None:  # For optional fields
        if not v.strip():
            raise ValueError("Field cannot be empty")
        if len(v) > 100:
            raise ValueError("Field too long (max 100 characters)")
        # Custom validation

        if any(char in v for char in ["<", ">", "&", '"', "'"]):
            raise ValueError("Field contains invalid characters")
        return v.strip()
    return v
```

### Integer Validation

```python
@field_validator("field_name")
@classmethod
def validate_field_name(cls, v):
    """Validate integer field."""
    if v < 0:
        raise ValueError("Value must be non-negative")
    if v > 1000:
        raise ValueError("Value too large (max 1000)")
    return v
```

### Enum Validation

```python
@field_validator("field_name")
@classmethod
def validate_field_name(cls, v):
    """Validate enum field."""
    if v not in YourEnum:
        raise ValueError(f"Invalid value: {v}. Must be one of: {list(YourEnum)}")
    return v
```

### Cross-Field Validation

```python
@model_validator(mode='after')
def validate_model(self):
    """Validate relationships between fields."""
    if self.start_time and self.end_time:
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time")
    return self
```

---

## Field Types and Constraints

### Common Field Types

| Type             | Description     | Example                                            |
| ---------------- | --------------- | -------------------------------------------------- |
| `str`            | String value    | `Field(..., description="Name")`                   |
| `int`            | Integer value   | `Field(1, description="Count")`                    |
| `bool`           | Boolean value   | `Field(False, description="Flag")`                 |
| `list[str]`      | List of strings | `Field(default_factory=list, description="Items")` |
| `dict[str, Any]` | Dictionary      | `Field(default_factory=dict, description="Data")`  |
| `datetime`       | Date/time       | `Field(..., description="Timestamp")`              |

### Field Constraints

```python
# Length constraints

field: str = Field(..., min_length=1, max_length=100)

# Value constraints

field: int = Field(..., ge=0, le=100)  # greater/less than or equal

# Pattern constraints

field: str = Field(..., pattern=r"^[a-zA-Z0-9_]+$")

# Custom constraints

field: str = Field(..., description="Custom field")
```

### Default Values

```python
# Simple default

field: str = Field("default", description="Field with default")

# Factory default (for mutable objects)

field: list[str] = Field(default_factory=list, description="Empty list")

# None default

field: str | None = Field(None, description="Optional field")
```

---

## Best Practices

### 1. Always Include Descriptions

```python
# Good

field: str = Field(..., description="Player name to target")

# Bad

field: str = Field(...)
```

### 2. Use Appropriate Field Types

```python
# Good - specific type

direction: Direction = Field(..., description="Direction to move")

# Bad - generic string

direction: str = Field(..., description="Direction to move")
```

### 3. Validate Input Thoroughly

```python
@field_validator("field_name")
@classmethod
def validate_field_name(cls, v):
    """Comprehensive validation."""
    if v is not None:
        # Check for empty/whitespace

        if not v.strip():
            raise ValueError("Field cannot be empty")

        # Check length

        if len(v) > 100:
            raise ValueError("Field too long (max 100 characters)")

        # Check for dangerous characters

        if any(char in v for char in ["<", ">", "&", '"', "'"]):
            raise ValueError("Field contains invalid characters")

        # Custom business logic

        if v.lower() in ["admin", "root", "system"]:
            raise ValueError("Reserved name not allowed")

        return v.strip()
    return v
```

### 4. Use Meaningful Error Messages

```python
# Good - specific error message

raise ValueError("Player name must be between 3 and 20 characters")

# Bad - generic error message

raise ValueError("Invalid input")
```

### 5. Follow Naming Conventions

```python
# Good - descriptive names

player_name: str = Field(..., description="Target player name")
duration_minutes: int = Field(..., description="Duration in minutes")

# Bad - unclear names

name: str = Field(..., description="Name")
time: int = Field(..., description="Time")
```

### 6. Document Complex Validation

```python
@field_validator("complex_field")
@classmethod
def validate_complex_field(cls, v):
    """
    Validate complex field with business rules.

    Rules:
    1. Must be alphanumeric
    2. Must start with a letter
    3. Must be between 3 and 20 characters
    4. Cannot contain reserved words
    """
    if v is not None:
        # Implementation...

        pass
    return v
```

---

## Common Pitfalls

### 1. Forgetting to Import

```python
# Missing import

from pydantic import BaseModel, Field, field_validator

# Missing enum import

from .command import CommandType, BaseCommand
```

### 2. Incorrect Field Validation

```python
# Wrong - validates after assignment

def validate_field(self, v):
    return v

# Correct - validates during assignment

@field_validator("field")
@classmethod
def validate_field(cls, v):
    return v
```

### 3. Not Handling Optional Fields

```python
# Wrong - assumes field is always present

@field_validator("optional_field")
@classmethod
def validate_optional_field(cls, v):
    if not v.strip():  # Will fail if v is None
        raise ValueError("Field cannot be empty")
    return v

# Correct - handles None values

@field_validator("optional_field")
@classmethod
def validate_optional_field(cls, v):
    if v is not None:
        if not v.strip():
            raise ValueError("Field cannot be empty")
        return v.strip()
    return v
```

### 4. Inconsistent Error Messages

```python
# Wrong - inconsistent formatting

raise ValueError("Field too long")
raise ValueError("Field cannot be empty")
raise ValueError("Invalid characters in field")

# Correct - consistent formatting

raise ValueError("Field too long (max 100 characters)")
raise ValueError("Field cannot be empty")
raise ValueError("Field contains invalid characters")
```

### 5. Not Testing Edge Cases

```python
# Test these scenarios
# - Empty strings
# - Very long strings
# - Special characters
# - Unicode characters
# - Whitespace-only strings
# - None values (for optional fields)

```

---

## Example: Complete Command Model

Here's a complete example of a new command model:

```python
class WhisperCommand(BaseCommand):
    """Command for sending private messages to other players."""

    command_type: Literal[CommandType.WHISPER] = CommandType.WHISPER
    target_player: str = Field(..., description="Player to whisper to")
    message: str = Field(..., description="Message to send")

    @field_validator("target_player")
    @classmethod
    def validate_target_player(cls, v):
        """Validate target player name."""
        if not v.strip():
            raise ValueError("Target player cannot be empty")
        if len(v) > 50:
            raise ValueError("Target player name too long (max 50 characters)")
        if not v.replace("_", "").isalnum():
            raise ValueError("Target player name must be alphanumeric (underscores allowed)")
        return v.strip().lower()

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        """Validate message content."""
        if not v.strip():
            raise ValueError("Message cannot be empty")
        if len(v) > 500:
            raise ValueError("Message too long (max 500 characters)")
        # Check for dangerous content

        dangerous_patterns = ["<script", "javascript:", "onload="]
        for pattern in dangerous_patterns:
            if pattern.lower() in v.lower():
                raise ValueError("Message contains forbidden content")
        return v.strip()
```

This model includes:

- Proper field definitions with descriptions
- Comprehensive validation for both fields
- Security checks for dangerous content
- Consistent error messages
- Proper handling of whitespace

---

*This reference document should be updated whenever new command models are added or existing ones are modified.*
