"""Is a player catatonic right now? Shared by the command gate and the ``use`` command (#1148).

Lives outside ``command_handler`` because ``commands`` cannot import that package without an import cycle.
"""

from __future__ import annotations

import uuid
from typing import Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from ..database import get_async_session
from ..models.lucidity import PlayerLucidity
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

CATATONIA_BLOCK_MESSAGE = (
    "Your body lies unresponsive, trapped in catatonia. Only an ally's grounding, or something to restore your mind, "
    "can reach you."
)


class _CatatoniaLookup(Protocol):  # pylint: disable=too-few-public-methods
    """The slice of ``CatatoniaRegistry`` this check needs."""

    def is_catatonic(self, player_id: uuid.UUID | str) -> bool:  # pylint: disable=missing-function-docstring
        ...


def is_catatonic_record(record: PlayerLucidity | None) -> bool:
    """Catatonic by the stored lucidity: the tier says so, or LCD is at or below zero."""
    return record is not None and (record.current_tier == "catatonic" or record.current_lcd <= 0)


async def player_is_catatonic(app_state: object, player_id: uuid.UUID) -> bool:
    """True when the in-memory registry or, failing that, the stored lucidity says the player is catatonic.

    The registry is empty after a restart, so the database is the fallback. Any lookup failure answers False: this
    gates convenience, and a broken lookup must not lock a player out of their own inventory.
    """
    registry = cast(_CatatoniaLookup | None, getattr(app_state, "catatonia_registry", None))
    if registry is not None and registry.is_catatonic(player_id):
        return True
    try:
        async for session in get_async_session():
            return is_catatonic_record(await session.get(PlayerLucidity, player_id))
    except (SQLAlchemyError, RuntimeError, OSError) as e:
        logger.warning("Catatonia lookup failed", player_id=str(player_id), error=str(e))
    return False
