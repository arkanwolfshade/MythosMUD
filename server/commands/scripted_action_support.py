"""Command-layer glue for scripted actions: build the context from the request's app, run container on_put rules."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import Protocol, cast

from ..game.scripted_actions import QuestActionService, ScriptedActionContext, run_scripted_actions
from ..models.player import Player
from ..schemas.scripted_actions import on_put_actions
from ..services.corruption_service import CorruptionPersistenceProtocol
from ..services.lucidity_service import CatatoniaObserverProtocol
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class _ContainerReader(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    async def get_container(self, container_id: uuid.UUID) -> Mapping[str, object] | None:
        """Container row by id, or None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


def _quest_service(app: object | None) -> QuestActionService | None:
    state = cast(object | None, getattr(app, "state", None))
    container = cast(object | None, getattr(state, "container", None))
    return cast(QuestActionService | None, getattr(container, "quest_service", None))


def _catatonia_observer(app: object | None) -> CatatoniaObserverProtocol | None:
    state = cast(object | None, getattr(app, "state", None))
    container = cast(object | None, getattr(state, "container", None))
    return cast(CatatoniaObserverProtocol | None, getattr(container, "catatonia_registry", None))


def action_context(app: object | None, player: object, persistence: object | None) -> ScriptedActionContext | None:
    """Context for running scripted actions on ``player``; None if the player or persistence is not usable."""
    if not isinstance(player, Player) or persistence is None:
        return None
    return ScriptedActionContext(
        player=player,
        persistence=cast(CorruptionPersistenceProtocol, persistence),
        quest_service=_quest_service(app),
        catatonia_observer=_catatonia_observer(app),
    )


async def run_on_put(
    app: object | None, persistence: object, player: Player, container_id: uuid.UUID, prototype_id: str | None
) -> None:
    """Run the container's ``on_put`` rules for the item just put in it (nothing if it declares none for the item)."""
    if not prototype_id:
        return
    try:
        container = await cast(_ContainerReader, persistence).get_container(container_id)
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: the put already succeeded; a lookup failure must not turn it into an error
        logger.error("on_put container lookup failed", container_id=str(container_id), error=str(e))
        return
    if container is None:
        return
    metadata = container.get("metadata_json")
    actions = on_put_actions(cast(dict[str, object], metadata) if isinstance(metadata, dict) else {}, prototype_id)
    ctx = action_context(app, player, persistence)
    if actions and ctx is not None:
        await run_scripted_actions(actions, ctx)
