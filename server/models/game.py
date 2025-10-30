"""
Game-related models for MythosMUD.

This module contains models specific to the game mechanics including
character statistics and attribute types.
"""

from datetime import UTC, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, computed_field


class AttributeType(str, Enum):
    """Core attribute types for the character system."""

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"
    SAN = "sanity"
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
    INSANE = "insane"


class StatusEffect(BaseModel):
    """Represents a status effect applied to a character."""

    __slots__ = ()  # Performance optimization for frequently instantiated status effects

    model_config = ConfigDict(
        # Security: reject unknown fields to prevent injection
        extra="forbid",
        # Performance: validate assignment for computed fields
        validate_assignment=True,
    )

    effect_type: StatusEffectType
    duration: int = Field(ge=0, description="Duration in game ticks (0 = permanent)")
    intensity: int = Field(ge=1, le=10, description="Effect intensity from 1-10")
    source: str | None = Field(None, description="Source of the effect (item, spell, etc.)")
    applied_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC).replace(tzinfo=None), description="When the effect was applied"
    )

    def is_active(self, current_tick: int) -> bool:
        """Check if the status effect is still active."""
        if self.duration == 0:
            return True
        # For testing purposes, use a simple tick-based system
        # In real usage, this would be more sophisticated
        return current_tick < self.duration


class Stats(BaseModel):
    """Core character statistics with Lovecraftian horror elements."""

    __slots__ = ()  # Performance optimization for frequently instantiated stats

    model_config = ConfigDict(
        # Performance: validate assignment for computed fields
        validate_assignment=True,
        # Allow extra fields for backward compatibility with serialized stats
        extra="allow",
        # Use enum values for consistency
        use_enum_values=True,
    )

    # Physical Attributes
    strength: int = Field(ge=1, le=20, default=None, description="Physical power and combat damage")
    dexterity: int = Field(ge=1, le=20, default=None, description="Agility, reflexes, and speed")
    constitution: int = Field(ge=1, le=20, default=None, description="Health, stamina, and resistance")

    # Mental Attributes
    intelligence: int = Field(ge=1, le=20, default=None, description="Problem-solving and magical aptitude")
    wisdom: int = Field(ge=1, le=20, default=None, description="Perception, common sense, and willpower")
    charisma: int = Field(ge=1, le=20, default=None, description="Social skills and influence")

    # Horror-Specific Attributes
    sanity: int = Field(ge=0, le=100, default=100, description="Mental stability (0 = complete madness)")
    occult_knowledge: int = Field(ge=0, le=100, default=0, description="Knowledge of forbidden lore")
    fear: int = Field(ge=0, le=100, default=0, description="Susceptibility to terror and panic")

    # Special Attributes
    corruption: int = Field(ge=0, le=100, default=0, description="Taint from dark forces")
    cult_affiliation: int = Field(ge=0, le=100, default=0, description="Ties to cults and secret societies")

    # Current health (can be modified)
    current_health: int = Field(ge=0, default=100, description="Current health points")

    def __init__(self, **data: Any) -> None:
        """Initialize Stats with proper random number generation."""
        # Use a local random generator to avoid affecting global state
        import random

        # Use system random for production, optional seed for testing
        seed = data.pop("_test_seed", None)
        local_rng = random.Random(seed) if seed is not None else random.Random()

        # Generate random values for any field that is None or not provided
        data.setdefault("strength", local_rng.randint(3, 18))
        data.setdefault("dexterity", local_rng.randint(3, 18))
        data.setdefault("constitution", local_rng.randint(3, 18))
        data.setdefault("intelligence", local_rng.randint(3, 18))
        data.setdefault("wisdom", local_rng.randint(3, 18))
        data.setdefault("charisma", local_rng.randint(3, 18))

        # Replace None values with random values
        for field in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            if data.get(field) is None:
                data[field] = local_rng.randint(3, 18)

        super().__init__(**data)

    # Derived stats - computed fields
    @computed_field  # type: ignore[misc]
    def max_health(self) -> int:
        """Calculate max health based on constitution."""
        return self.constitution * 10

    @computed_field  # type: ignore[misc]
    def max_sanity(self) -> int:
        """Calculate max sanity based on wisdom."""
        return self.wisdom * 5

    def get_attribute_modifier(self, attribute: AttributeType) -> int:
        """Get the modifier for a given attribute (standard D&D-style calculation)."""
        attr_value = getattr(self, attribute.value, 10)
        return (attr_value - 10) // 2

    def is_sane(self) -> bool:
        """Check if the character is still mentally stable."""
        return self.sanity > 0

    def is_corrupted(self) -> bool:
        """Check if the character has significant corruption."""
        return self.corruption >= 50

    def is_insane(self) -> bool:
        """Check if the character has lost their sanity completely."""
        return self.sanity <= 0


class InventoryItem(BaseModel):
    """Represents an item in a player's inventory."""

    __slots__ = ()

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    item_id: str = Field(..., description="Unique item identifier")
    quantity: int = Field(default=1, ge=1, description="Number of items")


class Player(BaseModel):
    """
    Pydantic Player model for game logic and validation.

    This is separate from the SQLAlchemy ORM model in models/player.py
    and is used for game logic, validation, and testing.
    """

    __slots__ = ()

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    id: str = Field(default_factory=lambda: str(__import__("uuid").uuid4()), description="Player unique identifier")
    name: str = Field(..., min_length=1, max_length=50, description="Player name")
    current_room_id: str = Field(
        default="earth_arkhamcity_sanitarium_room_foyer_001", description="Current room location"
    )
    experience_points: int = Field(default=0, ge=0, description="Total experience points")
    level: int = Field(default=1, ge=1, le=100, description="Player level")
    stats: Stats = Field(default_factory=Stats, description="Player statistics")
    inventory: list[InventoryItem] = Field(default_factory=list, description="Player inventory")
    status_effects: list[StatusEffect] = Field(default_factory=list, description="Active status effects")
    last_active: datetime = Field(
        default_factory=lambda: __import__("datetime").datetime.now(__import__("datetime").UTC).replace(tzinfo=None),
        description="Last activity timestamp",
    )

    def add_item(self, item_id: str, quantity: int = 1) -> bool:
        """
        Add an item to the player's inventory.

        Args:
            item_id: Unique identifier for the item
            quantity: Number of items to add

        Returns:
            bool: True if successful
        """
        # Check if item already exists
        for inv_item in self.inventory:
            if inv_item.item_id == item_id:
                # Increase quantity
                object.__setattr__(inv_item, "quantity", inv_item.quantity + quantity)
                return True

        # Add new item
        self.inventory.append(InventoryItem(item_id=item_id, quantity=quantity))
        return True

    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        """
        Remove an item from the player's inventory.

        Args:
            item_id: Unique identifier for the item
            quantity: Number of items to remove

        Returns:
            bool: True if successful, False if item not found or insufficient quantity
        """
        for i, inv_item in enumerate(self.inventory):
            if inv_item.item_id == item_id:
                if inv_item.quantity >= quantity:
                    new_quantity = inv_item.quantity - quantity
                    if new_quantity == 0:
                        # Remove item completely
                        self.inventory.pop(i)
                    else:
                        # Decrease quantity
                        object.__setattr__(inv_item, "quantity", new_quantity)
                    return True
                return False

        return False

    def add_status_effect(self, effect: StatusEffect) -> None:
        """
        Add a status effect to the player.

        Args:
            effect: StatusEffect to add
        """
        self.status_effects.append(effect)

    def remove_status_effect(self, effect_type: StatusEffectType) -> bool:
        """
        Remove a status effect from the player.

        Args:
            effect_type: Type of effect to remove

        Returns:
            bool: True if effect was found and removed, False otherwise
        """
        for i, effect in enumerate(self.status_effects):
            if effect.effect_type == effect_type:
                self.status_effects.pop(i)
                return True
        return False

    def get_active_status_effects(self, current_tick: int) -> list[StatusEffect]:
        """
        Get all currently active status effects.

        Args:
            current_tick: Current game tick

        Returns:
            list[StatusEffect]: List of active effects
        """
        return [effect for effect in self.status_effects if effect.is_active(current_tick)]

    def update_last_active(self) -> None:
        """Update the last_active timestamp to current time."""
        from datetime import UTC, datetime

        object.__setattr__(self, "last_active", datetime.now(UTC).replace(tzinfo=None))

    def can_carry_weight(self, weight: float) -> bool:
        """
        Check if the player can carry additional weight.

        Args:
            weight: Weight in pounds

        Returns:
            bool: True if player can carry the weight
        """
        # Carrying capacity is based on strength (10 lbs per point)
        max_capacity = self.stats.strength * 10
        return weight <= max_capacity
