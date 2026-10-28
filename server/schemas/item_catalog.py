"""
Item catalog list schemas for GET /v1/api/item-catalog.
"""

from datetime import datetime
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class ItemCatalogPlayerItem(BaseModel):
    """Player-facing catalog row (P1 columns)."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    name: str = Field(..., description="Display name")
    item_type: str = Field(..., description="Prototype item_type")
    short_description: str = Field(..., description="Short description")


class ItemCatalogAdminItem(BaseModel):
    """Admin catalog row with all stored prototype columns (A3)."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    prototype_id: str
    name: str
    short_description: str
    long_description: str
    item_type: str
    weight: float
    base_value: int
    durability: int | None = None
    flags: list[object] = Field(default_factory=list)
    wear_slots: list[object] = Field(default_factory=list)
    stacking_rules: dict[str, object] = Field(default_factory=dict)
    usage_restrictions: dict[str, object] = Field(default_factory=dict)
    effect_components: list[object] = Field(default_factory=list)
    metadata: dict[str, object] = Field(default_factory=dict)
    tags: list[object] = Field(default_factory=list)
    created_at: datetime | None = None


class ItemCatalogResponse(BaseModel):
    """Paginated item catalog response."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    items: list[ItemCatalogPlayerItem] | list[ItemCatalogAdminItem] = Field(
        ..., description="Catalog rows (player or admin projection)"
    )
    page: int = Field(..., ge=1)
    page_size: int = Field(..., ge=1)
    total: int = Field(..., ge=0)
    is_admin: bool = Field(..., description="True when admin/full columns were returned")
