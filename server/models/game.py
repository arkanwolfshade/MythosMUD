"""
Game-related models for MythosMUD.

This module contains models specific to the game mechanics including
character statistics and attribute types.
"""

import uuid
from datetime import UTC, datetime
from enum import StrEnum
from typing import ClassVar, cast

from pydantic import BaseModel, ConfigDict, Field, computed_field, model_validator

from .stats_random import CORE_STAT_KEYS, roll_random_core_stat_values


def _coerce_stat_int(value: object, default: int) -> int:
    """Convert persisted stat values to int with a safe fallback."""
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return default


def _new_player_id() -> str:
    return str(uuid.uuid4())


def _utc_now_naive() -> datetime:
    return datetime.now(UTC).replace(tzinfo=None)


class WeaponStats(BaseModel):
    """
    Weapon statistics for items that can be used as weapons.

    This model represents the combat properties of a weapon item, including
    damage range, modifiers, damage types, and magical properties.
    """

    model_config: ClassVar[ConfigDict] = ConfigDict(
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
    # Effects system (ADR-019): game-entry warded (login grace period)
    LOGIN_WARDED = "login_warded"
    # CoC spell-driven status effects
    DOMINATED = "dominated"
    CLOUD_MEMORY = "cloud_memory"
    FEAR = "fear"
    EVIL_EYE = "evil_eye"
    BLINDED = "blinded"
    WARDED = "warded"
    EXTINGUISH_FIRE = "extinguish_fire"


class PositionState(StrEnum):
    """Permitted posture states for a character."""

    STANDING = "standing"
    SITTING = "sitting"
    LYING = "lying"


class StatusEffect(BaseModel):
    """Represents a status effect applied to a character."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
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

    model_config: ClassVar[ConfigDict] = ConfigDict(
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

    @model_validator(mode="before")
    @classmethod
    def _ensure_core_stats(cls, data: object) -> object:
        """
        Generate random core stats when missing or None.

        Callers may pass ``_test_seed`` (int) for reproducible rolls in tests.
        """
        if not isinstance(data, dict):
            return data
        raw: dict[str, object] = cast(dict[str, object], data).copy()
        needs_random_stats = not any(key in raw for key in CORE_STAT_KEYS) or any(
            raw.get(key) is None for key in CORE_STAT_KEYS
        )
        if needs_random_stats:
            seed_obj = raw.pop("_test_seed", None)
            seed = seed_obj if isinstance(seed_obj, int) else None
            random_values = roll_random_core_stat_values(seed=seed)
            for key in CORE_STAT_KEYS:
                if key not in raw or raw.get(key) is None:
                    raw[key] = random_values[key]
        return raw

    @model_validator(mode="before")
    @classmethod
    def _compute_max_dp_if_missing(cls, data: object) -> object:
        """Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes precedence)."""
        if not isinstance(data, dict):
            return data
        raw: dict[str, object] = cast(dict[str, object], data).copy()
        if raw.get("max_dp") is None:
            con = _coerce_stat_int(raw.get("constitution"), 50)
            siz = _coerce_stat_int(raw.get("size"), 50)
            raw["max_dp"] = (con + siz) // 5
        return raw

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

    model_config: ClassVar[ConfigDict] = ConfigDict(
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

    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )

    id: str = Field(default_factory=_new_player_id, description="Player unique identifier")
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
        default_factory=_utc_now_naive,
        description="Last activity timestamp",
    )

    def _inventory_list(self) -> list[InventoryItem]:
        return cast(list[InventoryItem], object.__getattribute__(self, "inventory"))

    def _status_effects_list(self) -> list[StatusEffect]:
        return cast(list[StatusEffect], object.__getattribute__(self, "status_effects"))

    def _player_stats(self) -> Stats:
        return cast(Stats, object.__getattribute__(self, "stats"))

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
        inventory = self._inventory_list()
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
        inventory = self._inventory_list()
        for i, inv_item in enumerate(inventory):
            if inv_item.item_id == item_id:
                if inv_item.quantity >= quantity:
                    new_quantity = inv_item.quantity - quantity
                    if not new_quantity:
                        # Remove item completely
                        _ = inventory.pop(i)
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
        status_effects = self._status_effects_list()
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
        status_effects = self._status_effects_list()
        for i, effect in enumerate(status_effects):
            if effect.effect_type == effect_type:
                _ = status_effects.pop(i)
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
        status_effects = self._status_effects_list()
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
        stats = self._player_stats()
        max_capacity = (stats.strength or 10) * 10
        return weight <= max_capacity
