"""Alias storage for MythosMUD.

As noted in the restricted archives of Miskatonic University, this module
persists player command aliases in PostgreSQL (table ``player_aliases``, #680)
via the stored functions in ``db/procedures/player_aliases.sql``.
"""

import re
from datetime import UTC, datetime
from typing import Protocol, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from .database import get_session_maker
from .models.alias import Alias
from .structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

MAX_ALIASES_PER_PLAYER = 50
_RESERVED_COMMANDS = frozenset({"alias", "aliases", "unalias", "help"})
_ALIAS_NAME_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]*$")


class _AliasRow(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Shape of player_aliases procedure result rows."""

    id: object
    name: str
    command: str
    created_at: datetime
    updated_at: datetime


def _naive_utc(value: datetime) -> datetime:
    """Alias stores naive UTC timestamps (see models/alias.py)."""
    return value.astimezone(UTC).replace(tzinfo=None) if value.tzinfo else value


def _row_to_alias(row: object) -> Alias:
    r = cast(_AliasRow, row)
    return Alias(
        id=str(r.id),
        name=r.name,
        command=r.command,
        created_at=_naive_utc(r.created_at),
        updated_at=_naive_utc(r.updated_at),
    )


class AliasStorage:
    """Player alias persistence backed by the ``player_aliases`` table.

    Aliases are addressed by player name (all the command pipeline carries) and
    stored against the active player's ``player_id``. Database failures are logged
    and reported as "no alias" / ``False`` so a DB hiccup never breaks command input.
    """

    async def _fetch(self, sql: str, params: dict[str, str]) -> list[Alias] | None:
        """Run a row-returning alias function; None on database error."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; SQL literal, values bound.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(text(sql), params)
                rows = [_row_to_alias(row) for row in result.all()]
                await session.commit()
                return rows
        except (SQLAlchemyError, OSError) as e:
            logger.error("Alias database error", error=str(e), player_name=params.get("player_name"))
            return None

    async def get_player_aliases(self, player_name: str) -> list[Alias]:
        """Get all aliases for a player (empty on unknown player or DB error)."""
        rows = await self._fetch(
            "SELECT id, name, command, created_at, updated_at FROM get_player_aliases(:player_name)",
            {"player_name": player_name},
        )
        return rows or []

    async def get_alias(self, player_name: str, alias_name: str) -> Alias | None:
        """Get a specific alias for a player (case-insensitive name match)."""
        rows = await self._fetch(
            "SELECT id, name, command, created_at, updated_at FROM get_player_alias(:player_name, :alias_name)",
            {"player_name": player_name, "alias_name": alias_name},
        )
        return rows[0] if rows else None

    async def create_alias(self, player_name: str, name: str, command: str) -> Alias | None:
        """Create (or replace the command of) an alias; None if invalid, over the limit, or on error."""
        if not self.validate_alias_name(name) or not self.validate_alias_command(command):
            return None

        if len(await self.get_player_aliases(player_name)) >= MAX_ALIASES_PER_PLAYER:
            return None

        rows = await self._fetch(
            "SELECT id, name, command, created_at, updated_at FROM upsert_player_alias(:player_name, :alias_name, :command)",
            {"player_name": player_name, "alias_name": name, "command": command},
        )
        return rows[0] if rows else None

    async def _call_scalar(self, sql: str, params: dict[str, str]) -> object:
        """Run a scalar-returning alias function; None on database error."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # text() required to call PG function; SQL literal, values bound.
                # nosemgrep: python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text
                result = await session.execute(text(sql), params)
                value = cast(object, result.scalar())
                await session.commit()
                return value
        except (SQLAlchemyError, OSError) as e:
            logger.error("Alias database error", error=str(e), player_name=params.get("player_name"))
            return None

    async def remove_alias(self, player_name: str, alias_name: str) -> bool:
        """Remove an alias for a player. False if not found or on error."""
        deleted = await self._call_scalar(
            "SELECT delete_player_alias(:player_name, :alias_name)",
            {"player_name": player_name, "alias_name": alias_name},
        )
        return deleted is True

    async def delete_player_aliases_by_id(self, player_id: str) -> bool:
        """Delete every alias of a player (used when a character is deleted)."""
        deleted = await self._call_scalar(
            "SELECT delete_player_aliases_by_id(:player_id)",
            {"player_id": str(player_id)},
        )
        return deleted is not None

    def validate_alias_name(self, alias_name: str) -> bool:
        """Validate alias name format."""
        if not alias_name or len(alias_name) > 20:
            return False
        if alias_name.lower() in _RESERVED_COMMANDS:
            return False
        # Alphanumeric + underscore, must start with a letter
        return bool(_ALIAS_NAME_PATTERN.match(alias_name))

    def validate_alias_command(self, command: str) -> bool:
        """Validate alias command."""
        if not command or len(command) > 200:
            return False
        first_word = command.strip().split()[0].lower() if command.strip() else ""
        return first_word not in _RESERVED_COMMANDS
