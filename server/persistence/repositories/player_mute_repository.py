"""PlayerMute repository (#681).

Durable store behind UserManager's in-memory mute index, via the PostgreSQL
functions in db/procedures/player_mutes.sql.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Protocol, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)

MuteType = Literal["player", "channel", "global"]


class _MuteRow(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Shape of get_active_player_mutes() result rows."""

    mute_type: str
    muter_id: uuid.UUID
    muter_name: str
    target_id: uuid.UUID | None
    target_name: str | None
    channel: str | None
    reason: str
    muted_at: datetime
    expires_at: datetime | None


@dataclass(frozen=True, slots=True)
class PlayerMute:  # pylint: disable=too-many-instance-attributes  # Reason: mirrors player_mutes columns
    """One persisted mute. Channel mutes have ``channel`` set and no target; the others the reverse."""

    mute_type: MuteType
    muter_id: uuid.UUID
    muter_name: str
    target_id: uuid.UUID | None
    target_name: str | None
    channel: str | None
    reason: str
    muted_at: datetime
    expires_at: datetime | None


def _as_uuid(value: object) -> uuid.UUID:
    return value if isinstance(value, uuid.UUID) else uuid.UUID(str(value))


def _row_to_mute(row: object) -> PlayerMute:
    r = cast(_MuteRow, row)
    return PlayerMute(
        mute_type=cast(MuteType, r.mute_type),
        muter_id=_as_uuid(r.muter_id),
        muter_name=r.muter_name,
        target_id=_as_uuid(r.target_id) if r.target_id is not None else None,
        target_name=r.target_name,
        channel=r.channel,
        reason=r.reason,
        muted_at=r.muted_at,
        expires_at=r.expires_at,
    )


def _opt_str(value: uuid.UUID | None) -> str | None:
    return str(value) if value is not None else None


class PlayerMuteRepository:
    """Repository for player_mutes via stored procedures."""

    async def load_active(self) -> list[PlayerMute]:
        """Return every unexpired mute."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; SQL literal, no user-built query.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text(
                        """
                        SELECT
                            mute_type,
                            muter_id,
                            muter_name,
                            target_id,
                            target_name,
                            channel,
                            reason,
                            muted_at,
                            expires_at
                        FROM get_active_player_mutes()
                        """
                    )
                )
                return [_row_to_mute(row) for row in result.all()]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading player mutes: {e}",
                operation="load_active",
                details={"error": str(e)},
                user_friendly="Failed to load mutes",
            )

    async def upsert(self, mute: PlayerMute) -> None:
        """Apply a mute, replacing any existing mute with the same identity."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; bind params for values.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                _ = await session.execute(
                    text(
                        """
                        SELECT upsert_player_mute(
                            :mute_type, :muter_id, :muter_name, :target_id,
                            :target_name, :channel, :reason, :muted_at, :expires_at
                        )
                        """
                    ),
                    {
                        "mute_type": mute.mute_type,
                        "muter_id": str(mute.muter_id),
                        "muter_name": mute.muter_name,
                        "target_id": _opt_str(mute.target_id),
                        "target_name": mute.target_name,
                        "channel": mute.channel,
                        "reason": mute.reason,
                        "muted_at": mute.muted_at,
                        "expires_at": mute.expires_at,
                    },
                )
                await session.commit()
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving player mute: {e}",
                operation="upsert",
                details={"mute_type": mute.mute_type, "error": str(e)},
                user_friendly="Failed to save mute",
            )

    async def delete(
        self,
        mute_type: MuteType,
        muter_id: uuid.UUID | None,
        target_id: uuid.UUID | None,
        channel: str | None,
    ) -> bool:
        """Remove a mute by identity (global mutes ignore muter_id). True if a row was removed."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; bind params for values.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(
                    text("SELECT delete_player_mute(:mute_type, :muter_id, :target_id, :channel)"),
                    {
                        "mute_type": mute_type,
                        "muter_id": _opt_str(muter_id),
                        "target_id": _opt_str(target_id),
                        "channel": channel,
                    },
                )
                deleted = cast(object, result.scalar()) is True
                await session.commit()
                return deleted
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player mute: {e}",
                operation="delete",
                details={"mute_type": mute_type, "error": str(e)},
                user_friendly="Failed to delete mute",
            )
