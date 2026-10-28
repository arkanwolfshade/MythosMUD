"""Scripted actions: the declarative vocabulary content uses to make things happen.

Dialogue nodes and container ``on_put`` rules attach lists of these; ``game.scripted_actions`` is the one runner.
Content composes verbs instead of Python growing a special case per scene. A script that fails validation is dropped
whole (see ``parse_scripted_actions``): half a script is worse than none.
"""

# pylint: disable=too-few-public-methods  # Reason: Pydantic models; validators are the behavior

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, Literal

from pydantic import Field, TypeAdapter, ValidationError, field_validator

from ..structured_logging.enhanced_logging_config import get_logger
from .shared.base import SecureBaseModel

logger = get_logger(__name__)


class NarrateAction(SecureBaseModel):
    """Send the player a line of system narration."""

    type: Literal["narrate"] = "narrate"
    text: str = Field(min_length=1)


class ApplyEffectAction(SecureBaseModel):
    """Add a status effect (any shape the tick loop understands, e.g. heal_over_time) to the player."""

    type: Literal["apply_effect"] = "apply_effect"
    effect: dict[str, object]

    @field_validator("effect")
    @classmethod
    def _effect_is_typed(cls, effect: dict[str, object]) -> dict[str, object]:
        effect_type = effect.get("type")
        if not isinstance(effect_type, str) or not effect_type:
            raise ValueError("effect needs a non-empty string 'type'")
        return effect


class CorruptionAtLeastAction(SecureBaseModel):
    """Raise the player's corruption to ``value`` if it is lower; never adds, so it is idempotent."""

    type: Literal["corruption_at_least"] = "corruption_at_least"
    value: int = Field(ge=1, le=100)
    reason: str = Field(default="scripted_action", min_length=1)


class StartQuestAction(SecureBaseModel):
    """Start a quest for the player (refused quietly if prerequisites are unmet or it is already active)."""

    type: Literal["start_quest"] = "start_quest"
    quest_id: str = Field(min_length=1)


class QuestActivityAction(SecureBaseModel):
    """Record a complete_activity target for the player's active quests."""

    type: Literal["quest_activity"] = "quest_activity"
    target: str = Field(min_length=1)


class DebriefAction(SecureBaseModel):
    """Run the player's pending debrief (recap, optional immediate therapy) and clear DEBRIEF_PENDING."""

    type: Literal["debrief"] = "debrief"
    therapy: bool = False


ScriptedAction = Annotated[
    NarrateAction
    | ApplyEffectAction
    | CorruptionAtLeastAction
    | StartQuestAction
    | QuestActivityAction
    | DebriefAction,
    Field(discriminator="type"),
]


class OnPutRule(SecureBaseModel):
    """Run ``actions`` when an item with prototype id ``item`` is put into the container."""

    item: str = Field(min_length=1)
    actions: list[ScriptedAction]


_ACTIONS = TypeAdapter(list[ScriptedAction])
_ON_PUT_RULES = TypeAdapter(list[OnPutRule])


def parse_scripted_actions(raw: object) -> list[ScriptedAction]:
    """Validate raw JSON into actions; a malformed script yields [] (and a warning) rather than a partial run."""
    try:
        return _ACTIONS.validate_python(raw)
    except ValidationError as e:
        logger.warning("Malformed scripted actions ignored", error=str(e))
        return []


def on_put_actions(container_metadata: Mapping[str, object], prototype_id: str) -> list[ScriptedAction]:
    """Actions a container's ``on_put`` rules attach to putting ``prototype_id`` into it."""
    raw = container_metadata.get("on_put")
    if raw is None:
        return []
    try:
        rules = _ON_PUT_RULES.validate_python(raw)
    except ValidationError as e:
        logger.warning("Malformed container on_put ignored", error=str(e))
        return []
    return [action for rule in rules if rule.item == prototype_id for action in rule.actions]
