"""
Pydantic request/response models and helpers for NPC Admin API.

Extracted from npc.py to keep file NLOC under complexity limits.
"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ...models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from ...services.npc_service import NPCDefinitionUpdateParams


class NPCBaseStatsModel(BaseModel):
    """Model for NPC base statistics."""

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    determination_points: int | None = Field(default=None, ge=0, description="Current determination points (DP)")
    max_dp: int | None = Field(default=None, ge=0, description="Maximum determination points")
    magic_points: int | None = Field(default=None, ge=0, description="Current magic points (MP)")
    max_mp: int | None = Field(default=None, ge=0, description="Maximum magic points")
    strength: int | None = Field(default=None, ge=0, description="Strength attribute")
    dexterity: int | None = Field(default=None, ge=0, description="Dexterity attribute")
    constitution: int | None = Field(default=None, ge=0, description="Constitution attribute")


class NPCBehaviorConfigModel(BaseModel):
    """Model for NPC behavior configuration."""

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    aggression_level: int | None = Field(
        default=None,
        ge=0,
        le=10,
        description="Aggression level (0-10); scales threat from damage/healing (0 -> 0.5x, 10 -> 1.0x; None = full)",
    )
    wander_radius: int | None = Field(default=None, ge=0, description="Maximum wander radius")
    idle_behavior: str | None = Field(default=None, description="Idle behavior type")


class NPCAIIntegrationModel(BaseModel):
    """Model for NPC AI integration stub configuration."""

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    ai_enabled: bool | None = Field(default=None, description="Whether AI integration is enabled")
    ai_provider: str | None = Field(default=None, description="AI provider identifier")


class NPCSpawnConditionsModel(BaseModel):
    """Model for NPC spawn conditions."""

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    time_of_day: list[str] | None = Field(default=None, description="Allowed times of day for spawning")
    weather_conditions: list[str] | None = Field(default=None, description="Required weather conditions")
    room_tags: list[str] | None = Field(default=None, description="Required room tags")


class NPCDefinitionCreate(BaseModel):
    """Model for creating NPC definitions."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    name: str = Field(..., min_length=1, max_length=100)
    npc_type: NPCDefinitionType
    sub_zone_id: str = Field(..., min_length=1, max_length=100)
    room_id: str = Field(..., min_length=1, max_length=100)
    base_stats: NPCBaseStatsModel = Field(default_factory=NPCBaseStatsModel)
    behavior_config: NPCBehaviorConfigModel = Field(default_factory=NPCBehaviorConfigModel)
    ai_integration_stub: NPCAIIntegrationModel = Field(default_factory=NPCAIIntegrationModel)


class NPCDefinitionUpdate(BaseModel):
    """Model for updating NPC definitions."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    name: str | None = Field(None, min_length=1, max_length=100)
    npc_type: NPCDefinitionType | None = None
    sub_zone_id: str | None = Field(None, min_length=1, max_length=100)
    room_id: str | None = Field(None, min_length=1, max_length=100)
    base_stats: NPCBaseStatsModel | None = None
    behavior_config: NPCBehaviorConfigModel | None = None
    ai_integration_stub: NPCAIIntegrationModel | None = None


class NPCDefinitionResponse(BaseModel):
    """Model for NPC definition responses."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    npc_type: str
    sub_zone_id: str
    room_id: str | None
    base_stats: NPCBaseStatsModel
    behavior_config: NPCBehaviorConfigModel
    ai_integration_stub: NPCAIIntegrationModel

    @classmethod
    def from_orm(cls, npc_def: NPCDefinition) -> NPCDefinitionResponse:  # pylint: disable=arguments-renamed
        """Create response from ORM object."""
        base_stats_str = str(npc_def.base_stats)
        base_stats_raw = json.loads(base_stats_str) if base_stats_str else {}
        behavior_config_str = str(npc_def.behavior_config)
        behavior_config_raw = json.loads(behavior_config_str) if behavior_config_str else {}
        ai_integration_stub_str = str(npc_def.ai_integration_stub)
        ai_integration_stub_raw = json.loads(ai_integration_stub_str) if ai_integration_stub_str else {}

        base_stats_dict: dict[str, Any] = base_stats_raw if isinstance(base_stats_raw, dict) else {}
        behavior_config_dict: dict[str, Any] = behavior_config_raw if isinstance(behavior_config_raw, dict) else {}
        ai_integration_stub_dict: dict[str, Any] = (
            ai_integration_stub_raw if isinstance(ai_integration_stub_raw, dict) else {}
        )

        return cls(
            id=int(npc_def.id),
            name=str(npc_def.name),
            npc_type=str(npc_def.npc_type),
            sub_zone_id=str(npc_def.sub_zone_id),
            room_id=str(npc_def.room_id),
            base_stats=NPCBaseStatsModel(**base_stats_dict),
            behavior_config=NPCBehaviorConfigModel(**behavior_config_dict),
            ai_integration_stub=NPCAIIntegrationModel(**ai_integration_stub_dict),
        )


class NPCSpawnRequest(BaseModel):
    """Model for NPC spawn requests."""

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True, validate_default=True
    )
    definition_id: int = Field(..., gt=0)
    room_id: str = Field(..., min_length=1, max_length=100)


class NPCMoveRequest(BaseModel):
    """Model for NPC movement requests."""

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True, validate_default=True
    )
    room_id: str = Field(..., min_length=1, max_length=100)


class NPCSpawnRuleCreate(BaseModel):
    """Model for creating NPC spawn rules."""

    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, str_strip_whitespace=True, validate_default=True
    )
    npc_definition_id: int = Field(..., gt=0)
    sub_zone_id: str = Field(..., min_length=1, max_length=50)
    min_population: int = Field(default=0, ge=0)
    max_population: int = Field(default=999, ge=0)
    spawn_conditions: NPCSpawnConditionsModel = Field(default_factory=NPCSpawnConditionsModel)


class NPCSpawnRuleResponse(BaseModel):
    """Model for NPC spawn rule responses."""

    model_config = ConfigDict(from_attributes=True)
    id: int
    npc_definition_id: int
    sub_zone_id: str
    min_population: int
    max_population: int
    spawn_conditions: NPCSpawnConditionsModel

    @classmethod
    def from_orm(cls, spawn_rule: NPCSpawnRule) -> NPCSpawnRuleResponse:  # pylint: disable=arguments-renamed
        """Create response from ORM object."""
        spawn_conditions_str = str(spawn_rule.spawn_conditions)
        spawn_conditions_raw = json.loads(spawn_conditions_str) if spawn_conditions_str else {}
        spawn_conditions_dict: dict[str, Any] = spawn_conditions_raw if isinstance(spawn_conditions_raw, dict) else {}
        return cls(
            id=int(spawn_rule.id),
            npc_definition_id=int(spawn_rule.npc_definition_id),
            sub_zone_id=str(spawn_rule.sub_zone_id),
            min_population=int(spawn_rule.min_population),
            max_population=int(spawn_rule.max_population),
            spawn_conditions=NPCSpawnConditionsModel(**spawn_conditions_dict),
        )


def build_update_params_from_model(npc_data: NPCDefinitionUpdate) -> NPCDefinitionUpdateParams:
    """Convert NPCDefinitionUpdate model into NPCDefinitionUpdateParams for service layer."""
    base_stats_dict: dict[str, Any] | None = npc_data.base_stats.model_dump() if npc_data.base_stats else None
    behavior_config_dict: dict[str, Any] | None = (
        npc_data.behavior_config.model_dump() if npc_data.behavior_config else None
    )
    ai_integration_stub_dict: dict[str, Any] | None = (
        npc_data.ai_integration_stub.model_dump() if npc_data.ai_integration_stub else None
    )
    return {
        "name": npc_data.name,
        "description": None,
        "npc_type": npc_data.npc_type.value if npc_data.npc_type else None,
        "sub_zone_id": npc_data.sub_zone_id,
        "room_id": npc_data.room_id,
        "base_stats": base_stats_dict,
        "behavior_config": behavior_config_dict,
        "ai_integration_stub": ai_integration_stub_dict,
    }
