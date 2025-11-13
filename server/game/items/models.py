from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from server.game.items.constants import ALLOWED_FLAGS, ALLOWED_ITEM_TYPES, ALLOWED_WEAR_SLOTS


class ItemPrototypeModel(BaseModel):
    """Validated representation of an item prototype definition.

    This model keeps the prototype payload aligned with the Restricted Archive
    canon while ensuring downstream systems receive guaranteed shapes.
    """

    model_config = ConfigDict(extra="forbid")

    prototype_id: str = Field(min_length=1, max_length=120)
    name: str = Field(min_length=1, max_length=120)
    short_description: str = Field(min_length=1, max_length=120)
    long_description: str = Field(min_length=1, max_length=2048)
    item_type: str
    weight: float = Field(ge=0)
    base_value: int = Field(ge=0)
    durability: int | None = Field(default=None, ge=0)
    flags: list[str] = Field(default_factory=list)
    wear_slots: list[str] = Field(default_factory=list)
    usage_restrictions: dict[str, Any] = Field(default_factory=dict)
    stacking_rules: dict[str, Any] = Field(default_factory=dict)
    effect_components: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)

    @field_validator("item_type")
    @classmethod
    def validate_item_type(cls, value: str) -> str:
        if value not in ALLOWED_ITEM_TYPES:
            msg = f"item_type must be one of: {sorted(ALLOWED_ITEM_TYPES)}"
            raise ValueError(msg)
        return value

    @field_validator("flags")
    @classmethod
    def validate_flags(cls, value: list[str]) -> list[str]:
        invalid = [flag for flag in value if flag not in ALLOWED_FLAGS]
        if invalid:
            raise ValueError(f"Invalid flags: {invalid}")
        return value

    @field_validator("wear_slots")
    @classmethod
    def validate_wear_slots(cls, value: list[str]) -> list[str]:
        invalid = [slot for slot in value if slot not in ALLOWED_WEAR_SLOTS]
        if invalid:
            raise ValueError(f"Invalid wear slots: {invalid}")
        return value

    @field_validator("effect_components")
    @classmethod
    def validate_effect_components(cls, value: list[str]) -> list[str]:
        normalised: list[str] = []
        for component in value:
            if not isinstance(component, str) or not component.strip():
                raise ValueError("effect_components must contain non-empty strings")
            normalised.append(component.strip())
        return normalised

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, value: list[str]) -> list[str]:
        return [tag.strip() for tag in value if tag.strip()]


PrototypeValidationError = ValidationError
