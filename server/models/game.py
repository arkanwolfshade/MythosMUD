"""
Game-related models for MythosMUD.

This module contains models specific to the game mechanics including
character statistics and attribute types.
"""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, computed_field, model_validator


class WeaponStats(BaseModel):
    """
    Weapon statistics for items that can be used as weapons.

    This model represents the combat properties of a weapon item, including
    damage range, modifiers, damage types, and magical properties.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    min_damage: int = Field(..., ge=0, description="Minimum damage dealt by this weapon")
    max_damage: int = Field(..., ge=0, description="Maximum damage dealt by this weapon")
    modifier: int = Field(default=0, description="Damage modifier added to rolled damage")
    damage_types: list[str] = Field(
        default_factory=list, description="List of damage types this weapon can deal (e.g., ['slashing', 'piercing'])"
    )
    magical: bool = Field(default=False, description="Whether this weapon has magical properties")


class AttributeType(StrEnum):
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


class StatusEffectType(StrEnum):
    """Status effects that can be applied to characters."""

    STUNNED = "stunned"
    POISONED = "poisoned"
    HALLUCINATING = "hallucinating"
    PARANOID = "paranoid"
    TREMBLING = "trembling"
    CORRUPTED = "corrupted"
    DELIRIOUS = "delirious"
    BUFF = "buff"
    # Effects system (ADR-009): game-entry warded (login grace period)
    LOGIN_WARDED = "login_warded"


class PositionState(StrEnum):
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

        AI: This method handles backward compatibility by generating random stats when core attributes
        are missing or None. The logic ensures that any explicitly provided values take precedence
        over generated random values.
        """
        # Core stats that must be present for a valid Stats instance
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

        # Check if we need to generate random stats (either missing or None values)
        needs_random_stats = not any(key in data for key in core_stats) or any(
            data.get(key) is None for key in core_stats
        )

        if needs_random_stats:
            # Import here to avoid circular dependency
            from ..game.stats_generator import generate_random_stats

            # Generate random stats and merge with provided data
            seed = data.pop("_test_seed", None)
            random_stats = generate_random_stats(seed=seed)

            # Merge random stats with any provided data (provided data takes precedence)
            for key in core_stats:
                if key not in data or data.get(key) is None:
                    data[key] = getattr(random_stats, key, None)

        super().__init__(**data)

    @model_validator(mode="before")
    @classmethod
    def _compute_max_dp_if_missing(cls, data: Any) -> Any:
        """Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes precedence)."""
        if isinstance(data, dict) and data.get("max_dp") is None:
            con = data.get("constitution", 50)
            siz = data.get("size", 50)
            data = {**data, "max_dp": (con + siz) // 5}
        return data

    # Derived stats - use stored max_dp from persistence when present, else compute from (CON+SIZ)/5
    max_dp: int | None = Field(
        default=None,
        description="Max DP from persistence; if None, computed from (CON+SIZ)/5",
    )

    @computed_field
    def max_magic_points(self) -> int:
        """
        Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).

        AI: This computed field uses the same calculation logic as _calculate_max_magic_points()
        but is exposed as a property for external access. The calculation is duplicated
        here to avoid mypy inference issues with @computed_field decorators.
        """
        return self._calculate_max_magic_points()

    @computed_field
    def max_lucidity(self) -> int:
        """
        Calculate max lucidity based on education.

        AI: This computed field uses the same calculation logic as _calculate_max_lucidity()
        but is exposed as a property for external access. The calculation is duplicated
        here to avoid mypy inference issues with @computed_field decorators.
        """
        return self._calculate_max_lucidity()

    def _calculate_max_dp(self) -> int:
        """
        Calculate max determination points (DP) using formula: (CON + SIZ) / 5.

        AI: Helper method to calculate max_dp. Uses the same logic as the computed field
        but can be called during validation before computed fields are fully initialized.
        """
        con = self.constitution or 50
        siz = self.size or 50
        return (con + siz) // 5

    def _calculate_max_magic_points(self) -> int:
        """
        Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).

        AI: Helper method to calculate max_magic_points. Uses the same logic as the computed field
        but can be called during validation before computed fields are fully initialized.
        """
        import math

        pow_val = self.power or 50
        return math.ceil(pow_val * 0.2)

    def _calculate_max_lucidity(self) -> int:
        """
        Calculate max lucidity based on education.

        AI: Helper method to calculate max_lucidity. Uses the same logic as the computed field
        but can be called during validation before computed fields are fully initialized.
        """
        return self.education or 50

    @model_validator(mode="after")
    def validate_current_vs_max_stats(self) -> "Stats":
        """
        Ensure current_dp (DP), magic_points (MP), and lucidity don't exceed their max values.

        Validation Rules:
        - current_dp is capped at max_dp (calculated as (CON + SIZ) / 5)
        - magic_points is capped at max_magic_points (calculated as ceil(POW * 0.2))
        - lucidity is capped at max_lucidity (equals education), but preserves:
          * Default value (100) to allow characters to start with full mental clarity
          * Reasonable explicit values (<= 100) that slightly exceed max_lucidity
          * Only unreasonably high values (> 100) are capped

        AI: This validator ensures that current values never exceed their maximums, preventing
        impossible stat configurations. The lucidity logic preserves intentional user-specified
        values while preventing unreasonably high values. Uses object.__setattr__ to bypass
        Pydantic's validation cycle and prevent recursion.
        """
        # Use stored max_dp when present (persistence), else computed; prevents capping 73 to formula max
        max_dp = self.max_dp if self.max_dp is not None else self._calculate_max_dp()
        max_mp = self._calculate_max_magic_points()
        max_lucidity_value = self._calculate_max_lucidity()

        # Cap current_dp at max_dp
        # Use object.__setattr__ to bypass Pydantic validation and prevent recursion
        if self.current_dp > max_dp:
            object.__setattr__(self, "current_dp", max_dp)

        # Cap magic_points at max_magic_points
        if self.magic_points > max_mp:
            object.__setattr__(self, "magic_points", max_mp)

        # Cap lucidity at max_lucidity with special handling for default/reasonable values
        # Preserve default value (100) and reasonable explicit values (<= 100)
        # Only cap unreasonably high values (> 100) that exceed max_lucidity
        if self.lucidity > max_lucidity_value and self.lucidity > 100:
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
    weapon: WeaponStats | None = Field(
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
