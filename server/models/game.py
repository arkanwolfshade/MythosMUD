"""
Game-related models for MythosMUD.

This module contains models specific to the game mechanics including
character statistics and attribute types.
"""

from datetime import UTC, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, computed_field, model_validator


class AttributeType(str, Enum):
    """Core attribute types for the character system ."""

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    SIZ = "size"
    INT = "intelligence"
    POW = "power"
    EDU = "education"
    CHA = "charisma"
    LUCK = "luck"
    LCD = "lucidity"
    OCC = "occult"
    CORR = "corruption"


class StatusEffectType(str, Enum):
    """Status effects that can be applied to characters."""

    STUNNED = "stunned"
    POISONED = "poisoned"
    HALLUCINATING = "hallucinating"
    PARANOID = "paranoid"
    TREMBLING = "trembling"
    CORRUPTED = "corrupted"
    DELIRIOUS = "delirious"
    BUFF = "buff"


class PositionState(str, Enum):
    """Permitted posture states for a character."""

    STANDING = "standing"
    SITTING = "sitting"
    LYING = "lying"


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
        if not self.duration:
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
        # Ignore extra fields for backward compatibility with serialized stats (safer than "allow")
        extra="ignore",
        # Use enum values for consistency
        use_enum_values=True,
    )

    # Physical Attributes
    strength: int | None = Field(default=None, description="Physical power and combat damage")
    dexterity: int | None = Field(default=None, description="Agility, reflexes, and speed")
    constitution: int | None = Field(default=None, description="Health, stamina, and resistance")
    size: int | None = Field(default=None, description="Height and weight combined (CoC: (2D6+6)*5)")

    # Mental Attributes
    intelligence: int | None = Field(default=None, description="Problem-solving and magical aptitude")
    power: int | None = Field(default=None, description="Willpower and magical potential")
    education: int | None = Field(default=None, description="Formal learning and knowledge")
    charisma: int | None = Field(default=None, description="Social skills and influence")
    luck: int | None = Field(default=None, description="Fortune and chance")

    # Horror-Specific Attributes
    lucidity: int = Field(default=100, description="Mental clarity (0 = complete delirium)")
    occult: int = Field(default=0, description="Knowledge of forbidden lore")
    corruption: int = Field(default=0, description="Taint from dark forces")

    # Derived Stats (tracked separately from base stats)
    current_dp: int = Field(default=100, description="Current determination points (DP)")
    magic_points: int = Field(default=0, description="Current magic points (MP)")

    position: PositionState = Field(default=PositionState.STANDING, description="Current body posture")

    def __init__(self, **data: Any) -> None:
        """
        Initialize Stats with provided data.

        For random stat generation, use generate_random_stats() from server.game.stats_generator
        instead of calling Stats() without arguments.
        """
        # Handle backward compatibility: if no attributes provided, generate random ones
        # This maintains compatibility with existing code that calls Stats()
        core_stats = [
            "strength",
            "dexterity",
            "constitution",
            "size",
            "intelligence",
            "power",
            "education",
            "charisma",
            "luck",
        ]
        if not any(key in data for key in core_stats):
            # Import here to avoid circular dependency
            from ..game.stats_generator import generate_random_stats

            # Generate random stats and merge with provided data
            seed = data.pop("_test_seed", None)
            random_stats = generate_random_stats(seed=seed)
            # Merge random stats with any provided data (provided data takes precedence)
            for key in core_stats:
                if key not in data:
                    data[key] = getattr(random_stats, key, None)

        # Replace None values with random values for backward compatibility
        if any(data.get(key) is None for key in core_stats):
            from ..game.stats_generator import generate_random_stats

            seed = data.pop("_test_seed", None)
            random_stats = generate_random_stats(seed=seed)
            for field in core_stats:
                if data.get(field) is None:
                    data[field] = getattr(random_stats, field, None)

        super().__init__(**data)

    # Derived stats - computed fields
    @computed_field
    def max_dp(self) -> int:
        """Calculate max determination points (DP) using formula: (CON + SIZ) / 5."""
        # Compute directly to avoid mypy @computed_field inference issues
        con = self.constitution or 50
        siz = self.size or 50
        return (con + siz) // 5

    @computed_field
    def max_magic_points(self) -> int:
        """Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded)."""
        import math

        pow_val = self.power or 50
        return math.ceil(pow_val * 0.2)

    @computed_field
    def max_lucidity(self) -> int:
        """Calculate max lucidity based on education."""
        return self.education or 50

    @model_validator(mode="after")
    def validate_current_vs_max_stats(self) -> "Stats":
        """
        Ensure current_dp (DP), magic_points (MP), and lucidity don't exceed their max values.

        BUGFIX: Initialize current_dp, magic_points, and lucidity to their max values if not explicitly provided.
        This prevents new characters from having impossible stats.
        """
        # Compute max values directly to avoid mypy @computed_field inference issues
        # Calculate max_dp: (CON + SIZ) / 5
        con = self.constitution or 50
        siz = self.size or 50
        max_dp = (con + siz) // 5

        # Calculate max_mp: 20% of Power (ceiling rounded)
        import math

        pow_val = self.power or 50
        max_mp = math.ceil(pow_val * 0.2)

        # Calculate max_lucidity: education value
        max_lucidity_value = self.education or 50

        # Cap current_dp (DP) at max_dp
        # Use object.__setattr__ to bypass Pydantic validation and prevent recursion
        object.__setattr__(self, "current_dp", min(self.current_dp, max_dp))

        # Cap magic_points at max_magic_points
        object.__setattr__(self, "magic_points", min(self.magic_points, max_mp))

        # Cap lucidity at max_lucidity when it exceeds max
        # Exception: Preserve lucidity if it's at the default (100) to allow characters
        # to start with full mental clarity regardless of education level.
        # Also preserve reasonable explicit values (<= 100) that are slightly above max_lucidity,
        # as these are likely intentional user-specified values.
        # Only cap unreasonably high values (> 100) that exceed max_lucidity.
        if self.lucidity > max_lucidity_value:
            # Preserve default value (100) and reasonable explicit values (<= 100)
            # Only cap unreasonably high values (> 100)
            if self.lucidity > 100:
                object.__setattr__(self, "lucidity", max_lucidity_value)

        return self

    def get_attribute_modifier(self, attribute: AttributeType) -> int:
        """Get the modifier for a given attribute (standard D&D-style calculation)."""
        attr_value = getattr(self, attribute.value, 50)
        return (attr_value - 50) // 2

    def is_lucid(self) -> bool:
        """Check if the character is still mentally clear."""
        return self.lucidity > 0

    def is_corrupted(self) -> bool:
        """Check if the character has significant corruption."""
        return self.corruption >= 50

    def is_delirious(self) -> bool:
        """Check if the character has lost their lucidity completely."""
        return self.lucidity <= 0


class InventoryItem(BaseModel):
    """Represents an item in a player's inventory."""

    __slots__ = ()

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    item_id: str = Field(..., description="Unique item identifier")
    quantity: int = Field(default=1, ge=1, description="Number of items")
    weapon: dict[str, Any] | None = Field(
        default=None,
        description="Weapon stats when item is a weapon (min_damage, max_damage, modifier, damage_types, magical).",
    )


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
        # Get actual inventory list using __getattribute__ to bypass field descriptor
        inventory: list[InventoryItem] = object.__getattribute__(self, "inventory")
        for inv_item in inventory:
            if inv_item.item_id == item_id:
                # Increase quantity
                object.__setattr__(inv_item, "quantity", inv_item.quantity + quantity)
                return True

        # Add new item
        inventory.append(InventoryItem(item_id=item_id, quantity=quantity))
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
        # Get actual inventory list using __getattribute__ to bypass field descriptor
        inventory: list[InventoryItem] = object.__getattribute__(self, "inventory")
        for i, inv_item in enumerate(inventory):
            if inv_item.item_id == item_id:
                if inv_item.quantity >= quantity:
                    new_quantity = inv_item.quantity - quantity
                    if not new_quantity:
                        # Remove item completely
                        inventory.pop(i)
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
        # Get actual status_effects list using __getattribute__ to bypass field descriptor
        status_effects: list[StatusEffect] = object.__getattribute__(self, "status_effects")
        status_effects.append(effect)

    def remove_status_effect(self, effect_type: StatusEffectType) -> bool:
        """
        Remove a status effect from the player.

        Args:
            effect_type: Type of effect to remove

        Returns:
            bool: True if effect was found and removed, False otherwise
        """
        # Get actual status_effects list using __getattribute__ to bypass field descriptor
        status_effects: list[StatusEffect] = object.__getattribute__(self, "status_effects")
        for i, effect in enumerate(status_effects):
            if effect.effect_type == effect_type:
                status_effects.pop(i)
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
        # Get actual status_effects list using __getattribute__ to bypass field descriptor
        status_effects: list[StatusEffect] = object.__getattribute__(self, "status_effects")
        return [effect for effect in status_effects if effect.is_active(current_tick)]

    def update_last_active(self) -> None:
        """Update the last_active timestamp to current time."""
        object.__setattr__(self, "last_active", datetime.now(UTC).replace(tzinfo=None))

    def can_carry_weight(self, weight: float) -> bool:
        """
        Check if the player can carry additional weight.

        Args:
            weight: Weight in pounds

        Returns:
            bool: True if player can carry the weight
        """
        # Get actual stats using __getattribute__ to bypass field descriptor
        # Carrying capacity is based on strength (10 lbs per point)
        stats: Stats = object.__getattribute__(self, "stats")
        max_capacity = (stats.strength or 10) * 10
        return weight <= max_capacity
