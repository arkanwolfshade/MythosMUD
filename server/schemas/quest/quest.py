"""
Quest subsystem Pydantic schemas for MythosMUD server.

Defines schemas for quest definition JSONB (goals, rewards, triggers, prerequisites)
and quest instance progress. Used by QuestService and API responses.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class QuestGoalSchema(BaseModel):
    """Single goal in a quest definition (complete_activity, kill_n, etc.)."""

    type: str = Field(..., description="Goal type: complete_activity, kill_n")
    target: str | None = Field(default=None, description="Target identifier (e.g. exit_tutorial_room, npc def id)")
    config: dict[str, Any] = Field(default_factory=dict, description="Type-specific config (e.g. count for kill_n)")

    model_config = ConfigDict(extra="allow")


class QuestRewardSchema(BaseModel):
    """Single reward in a quest definition (xp, item, spell)."""

    type: str = Field(..., description="Reward type: xp, item, spell")
    config: dict[str, Any] = Field(default_factory=dict, description="Type-specific config (amount, item_id, spell_id)")

    model_config = ConfigDict(extra="allow")


class QuestTriggerSchema(BaseModel):
    """Single trigger that can start a quest (room, npc, item)."""

    type: str = Field(..., description="Trigger type: room, npc, item")
    entity_id: str = Field(..., description="Entity identifier (room id, npc def id, item id)")

    model_config = ConfigDict(extra="allow")


class QuestDefinitionSchema(BaseModel):
    """
    Parsed quest definition (stored as JSONB in quest_definitions.definition).

    Used to validate and parse definition blob from DB.
    """

    name: str = Field(..., description="Canonical quest name (player-facing, unique)")
    title: str = Field(..., description="Display title")
    description: str = Field(default="", description="Quest description")
    goals: list[QuestGoalSchema] = Field(default_factory=list, description="List of goals")
    rewards: list[QuestRewardSchema] = Field(default_factory=list, description="List of rewards")
    triggers: list[QuestTriggerSchema] = Field(default_factory=list, description="Triggers that can start the quest")
    requires_all: list[str] = Field(default_factory=list, description="Quest IDs all of which must be completed")
    requires_any: list[str] = Field(default_factory=list, description="Quest IDs any of which must be completed")
    auto_complete: bool = Field(default=True, description="If true, complete when goals met; else require turn-in")
    turn_in_entities: list[str] = Field(
        default_factory=list,
        description="Entity IDs (npc/room) where player can turn in when auto_complete is false",
    )

    model_config = ConfigDict(extra="forbid")


# Per-goal progress in quest_instances.progress JSONB: keys are goal index or id, values are counts/state.
QuestProgressDict = dict[str, Any]


class QuestLogEntryResponse(BaseModel):
    """Single quest entry in GET /quests (quest log) response."""

    quest_id: str = Field(..., description="Internal quest ID")
    name: str = Field(..., description="Quest common name (player-facing)")
    title: str = Field(..., description="Display title")
    description: str = Field(default="", description="Quest description")
    goals_with_progress: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Goals with current progress (e.g. { goal_type, target, current, required, done })",
    )
    state: str = Field(..., description="Instance state: active, completed, abandoned")

    model_config = ConfigDict(extra="forbid")


class QuestLogResponse(BaseModel):
    """Response model for GET /quests (quest log)."""

    quests: list[QuestLogEntryResponse] = Field(
        default_factory=list, description="Active and optionally completed quests"
    )

    model_config = ConfigDict(extra="forbid")
