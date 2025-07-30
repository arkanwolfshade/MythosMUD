import uuid
from datetime import UTC, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, computed_field


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

    effect_type: StatusEffectType
    duration: int = Field(ge=0, description="Duration in game ticks (0 = permanent)")
    intensity: int = Field(ge=1, le=10, description="Effect intensity from 1-10")
    source: str | None = Field(None, description="Source of the effect (item, spell, etc.)")
    applied_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    def is_active(self, current_tick: int) -> bool:
        """Check if the status effect is still active."""
        if self.duration == 0:
            return True
        # For testing purposes, use a simple tick-based system
        # In real usage, this would be more sophisticated
        return current_tick < self.duration


class Alias(BaseModel):
    """Represents a user command alias for MythosMUD.

    As noted in the restricted archives of Miskatonic University, command
    aliases allow players to create shortcuts for commonly used commands,
    improving gameplay efficiency while maintaining the integrity of the
    command system.
    """

    name: str = Field(..., description="Alias name (case-insensitive)")
    command: str = Field(..., description="Target command to execute")
    version: str = Field(default="1.0", description="Schema version for future compatibility")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Future expansion fields (commented for now):
    # alias_type: str = Field(default="simple", description="simple|parameter|multi")
    # parameters: dict = Field(default_factory=dict,
    #                         description="Parameter definitions for future use")
    # conditions: dict = Field(default_factory=dict,
    #                         description="Conditional logic for future use")
    # metadata: dict = Field(default_factory=dict,
    #                        description="Additional metadata")

    def __eq__(self, other: object) -> bool:
        """Custom equality comparison that ignores timestamp fields.

        As noted in the Pnakotic Manuscripts, temporal signatures can create
        false distinctions between otherwise identical entities. This method
        ensures that aliases are compared by their essential properties only.
        """
        if not isinstance(other, Alias):
            return False
        return (self.name == other.name and
                self.command == other.command and
                self.version == other.version)

    def __hash__(self) -> int:
        """Custom hash method that matches the equality comparison."""
        return hash((self.name, self.command, self.version))

    def update_timestamp(self) -> None:
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now(UTC)

    def is_reserved_command(self) -> bool:
        """Check if this alias targets a reserved command."""
        reserved_commands = {"alias", "aliases", "unalias", "help"}
        return self.command.lower().split()[0] in reserved_commands

    def validate_name(self) -> bool:
        """Validate alias name follows naming conventions."""
        import re

        # Must start with letter, contain only alphanumeric and underscore
        pattern = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        return bool(re.match(pattern, self.name))

    def get_expanded_command(self, args: list[str] = None) -> str:
        """Get the expanded command with optional arguments.

        For future parameter-based aliases, this method will handle
        argument substitution. Currently returns the base command.
        """
        if args is None:
            args = []

        # For now, simple command expansion
        # Future: implement parameter substitution like $1, $2, etc.
        return self.command


class Stats(BaseModel):
    """Core character statistics with Lovecraftian horror elements."""

    # Physical Attributes
    strength: int = Field(ge=1, le=20, default=10, description="Physical power and combat damage")
    dexterity: int = Field(ge=1, le=20, default=10, description="Agility, reflexes, and speed")
    constitution: int = Field(ge=1, le=20, default=10, description="Health, stamina, and resistance")

    # Mental Attributes
    intelligence: int = Field(ge=1, le=20, default=10, description="Problem-solving and magical aptitude")
    wisdom: int = Field(ge=1, le=20, default=10, description="Perception, common sense, and willpower")
    charisma: int = Field(ge=1, le=20, default=10, description="Social skills and influence")

    # Horror-Specific Attributes
    sanity: int = Field(ge=0, le=100, default=100, description="Mental stability (0 = complete madness)")
    occult_knowledge: int = Field(ge=0, le=100, default=0, description="Knowledge of forbidden lore")
    fear: int = Field(ge=0, le=100, default=0, description="Susceptibility to terror and panic")

    # Special Attributes
    corruption: int = Field(ge=0, le=100, default=0, description="Taint from dark forces")
    cult_affiliation: int = Field(ge=0, le=100, default=0, description="Ties to cults and secret societies")

    # Current health (can be modified)
    current_health: int = Field(ge=0, default=100, description="Current health points")

    # Derived stats - computed fields
    @computed_field
    @property
    def max_health(self) -> int:
        """Calculate max health based on constitution."""
        return self.constitution * 10

    @computed_field
    @property
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


class Item(BaseModel):
    """Base item class with inheritance support."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    item_type: str
    weight: float = Field(ge=0, default=0.0)
    value: int = Field(ge=0, default=0)

    # Customizable properties that can override base values
    custom_properties: dict[str, Any] = Field(default_factory=dict)

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a property value, checking custom properties first."""
        return self.custom_properties.get(key, getattr(self, key, default))


class InventoryItem(BaseModel):
    """Represents an item in a character's inventory."""

    item_id: str
    quantity: int = Field(ge=1, default=1)
    custom_properties: dict[str, Any] = Field(default_factory=dict)

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a property value, checking custom properties first."""
        return self.custom_properties.get(key, default)


class Player(BaseModel):
    """Player character model with stats, inventory, and status effects."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(min_length=1, max_length=50)
    stats: Stats = Field(default_factory=Stats)
    inventory: list[InventoryItem] = Field(default_factory=list)
    status_effects: list[StatusEffect] = Field(default_factory=list)
    current_room_id: str = Field(default="arkham_001")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    last_active: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Game state
    experience_points: int = Field(ge=0, default=0)
    level: int = Field(ge=1, default=1)

    def add_item(self, item_id: str, quantity: int = 1, custom_properties: dict[str, Any] = None) -> bool:
        """Add an item to the player's inventory."""
        if custom_properties is None:
            custom_properties = {}

        # Check if item already exists with same custom properties
        for inv_item in self.inventory:
            if inv_item.item_id == item_id and inv_item.custom_properties == custom_properties:
                inv_item.quantity += quantity
                return True

        # Add new inventory item
        self.inventory.append(InventoryItem(item_id=item_id, quantity=quantity, custom_properties=custom_properties))
        return True

    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        """Remove an item from the player's inventory."""
        for inv_item in self.inventory:
            if inv_item.item_id == item_id:
                if inv_item.quantity <= quantity:
                    self.inventory.remove(inv_item)
                else:
                    inv_item.quantity -= quantity
                return True
        return False

    def add_status_effect(self, effect: StatusEffect) -> None:
        """Add a status effect to the player."""
        self.status_effects.append(effect)

    def remove_status_effect(self, effect_type: StatusEffectType) -> bool:
        """Remove a status effect from the player."""
        for effect in self.status_effects:
            if effect.effect_type == effect_type:
                self.status_effects.remove(effect)
                return True
        return False

    def get_active_status_effects(self, current_tick: int) -> list[StatusEffect]:
        """Get all currently active status effects."""
        return [effect for effect in self.status_effects if effect.is_active(current_tick)]

    def update_last_active(self) -> None:
        """Update the last active timestamp."""
        self.last_active = datetime.now(UTC)

    def can_carry_weight(self, additional_weight: float) -> bool:
        """Check if the player can carry additional weight."""
        current_weight = sum(inv_item.quantity * inv_item.get_property("weight", 0.0) for inv_item in self.inventory)
        # Assume carrying capacity is based on strength
        max_capacity = self.stats.strength * 10  # 10 lbs per strength point
        return (current_weight + additional_weight) <= max_capacity


class NPC(BaseModel):
    """Non-player character model."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    stats: Stats = Field(default_factory=Stats)
    current_room_id: str
    npc_type: str = Field(default="civilian")  # civilian, merchant, enemy, etc.
    is_hostile: bool = Field(default=False)
    dialogue_options: dict[str, str] = Field(default_factory=dict)

    def is_alive(self) -> bool:
        """Check if the NPC is alive."""
        return self.stats.current_health > 0
