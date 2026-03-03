"""
Helper types and row-mapping functions for NPCService.

Extracted from npc_service to keep that module under file-nloc limits while
preserving its public API and behavior.
"""

from __future__ import annotations

from typing import Any, TypedDict

from ..models.npc import NPCDefinition, NPCSpawnRule


class CreateNPCDefinitionInput(TypedDict, total=False):
    """Input for create_npc_definition. Must include name, npc_type, sub_zone_id; others optional."""

    name: str
    description: str | None
    npc_type: str
    sub_zone_id: str
    room_id: str | None
    required_npc: bool
    max_population: int
    spawn_probability: float
    base_stats: dict[str, Any]
    behavior_config: dict[str, Any]
    ai_integration_stub: dict[str, Any]


class NPCDefinitionCreateParams(TypedDict):
    """Internal params for create_npc_definition stored procedure call (DB uses varchar)."""

    name: str
    description: str | None
    npc_type: str
    sub_zone_id: str
    room_id: str | None
    required_npc: bool
    max_population: int
    spawn_probability: float
    base_stats: dict[str, Any]
    behavior_config: dict[str, Any]
    ai_integration_stub: dict[str, Any]


class NPCDefinitionUpdateParams(TypedDict, total=False):
    """Internal params for NPC definition update data builder."""

    name: str | None
    description: str | None
    npc_type: str | None
    sub_zone_id: str | None
    room_id: str | None
    required_npc: bool | None
    max_population: int | None
    spawn_probability: float | None
    base_stats: dict[str, Any] | None
    behavior_config: dict[str, Any] | None
    ai_integration_stub: dict[str, Any] | None


def _row_to_npc_definition(row: Any) -> NPCDefinition:
    """Map procedure result row to NPCDefinition model."""
    nd = NPCDefinition(
        name=row.name,
        description=row.description,
        npc_type=row.npc_type,
        sub_zone_id=row.sub_zone_id,
        room_id=row.room_id,
        required_npc=bool(row.required_npc) if row.required_npc is not None else False,
        max_population=int(row.max_population) if row.max_population is not None else 1,
        spawn_probability=float(row.spawn_probability) if row.spawn_probability is not None else 1.0,
        base_stats=row.base_stats or "{}",
        behavior_config=row.behavior_config or "{}",
        ai_integration_stub=row.ai_integration_stub or "{}",
    )
    object.__setattr__(nd, "id", row.id)
    object.__setattr__(nd, "created_at", row.created_at)
    object.__setattr__(nd, "updated_at", row.updated_at)
    return nd


def _row_to_npc_spawn_rule(row: Any) -> NPCSpawnRule:
    """Map procedure result row to NPCSpawnRule model."""
    rule = NPCSpawnRule(
        npc_definition_id=int(row.npc_definition_id),
        sub_zone_id=row.sub_zone_id,
        min_population=int(row.min_population) if row.min_population is not None else 0,
        max_population=int(row.max_population) if row.max_population is not None else 999,
        spawn_conditions=row.spawn_conditions or "{}",
    )
    object.__setattr__(rule, "id", row.id)
    return rule


__all__ = [
    "CreateNPCDefinitionInput",
    "NPCDefinitionCreateParams",
    "NPCDefinitionUpdateParams",
    "_row_to_npc_definition",
    "_row_to_npc_spawn_rule",
]
