"""
Invite management system for MythosMUD.

This module handles the invite-only registration system,
including invite creation, validation, and tracking.
"""

import uuid
from datetime import UTC, datetime, timedelta
from typing import cast

from fastapi import Depends, Request
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..exceptions import LoggedHTTPException
from ..models.invite import Invite
from ..models.user import User
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class InviteManager:
    """
    Manages invite creation, validation, and tracking.

    Handles the invite-only registration system for MythosMUD.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        logger.info("InviteManager initialized")

    async def create_invite(
        self,
        expires_in_days: int = 30,
        expires_at: datetime | None = None,
    ) -> Invite:
        """Create a new invite."""
        if expires_at is not None:
            # Use explicit expiration (naive UTC for PostgreSQL)
            expires_at_naive = expires_at.replace(tzinfo=None) if expires_at.tzinfo else expires_at
        else:
            # Persist naive UTC timestamps
            expires_at_naive = (datetime.now(UTC) + timedelta(days=expires_in_days)).replace(tzinfo=None)
        logger.info(
            "Creating new invite",
            expires_in_days=expires_in_days,
            expires_at=expires_at_naive,
        )

        invite_code = Invite._generate_invite_code()  # pylint: disable=protected-access  # Reason: Class method access required for invite code generation
        invite = Invite(
            invite_code=invite_code,
            is_active=True,
            expires_at=expires_at_naive,
        )

        self.session.add(invite)
        await self.session.commit()
        await self.session.refresh(invite)

        logger.info(
            "Invite created successfully",
            invite_code=invite_code,
            expires_at=expires_at_naive,
        )
        return invite

    async def list_invites(self) -> list[Invite]:
        """Get all invites."""
        logger.debug("Listing all invites")

        result = await self.session.execute(select(Invite))
        invites = result.scalars().all()

        logger.debug("Invites listed", count=len(invites))
        return list(invites)

    async def validate_invite(self, invite_code: str | None, _request: Request | None = None) -> Invite:
        """Validate an invite code."""
        if not invite_code:
            logger.warning("No invite code provided")
            raise LoggedHTTPException(
                status_code=400,
                detail="Invite code is required",
                operation="validate_invite",
            )

        logger.debug("Validating invite code", invite_code=invite_code)

        # Find invite by code
        result = await self.session.execute(select(Invite).where(Invite.invite_code == invite_code))
        invite = result.scalar_one_or_none()

        if not invite:
            logger.warning("Invalid invite code", invite_code=invite_code)
            raise LoggedHTTPException(
                status_code=400,
                detail="Invalid invite code",
                invite_code=invite_code,
                operation="validate_invite",
            )

        if not invite.is_valid():
            logger.warning(
                "Invalid invite - expired or already used",
                invite_code=invite_code,
                is_active=invite.is_active,
                expires_at=invite.expires_at,
            )
            raise LoggedHTTPException(
                status_code=400,
                detail="Invite code is expired or already used",
                invite_code=invite_code,
                is_active=invite.is_active,
                expires_at=str(invite.expires_at),
                operation="validate_invite",
            )

        logger.debug("Invite validation successful", invite_code=invite_code)
        return invite

    async def use_invite(self, invite_code: str, user_id: uuid.UUID) -> Invite:
        """Mark an invite as used by a specific user (atomic auth-and-capture).

        Uses the same reserve_invite/capture_invite pair as server.auth.endpoints.register_user
        rather than a read-then-write ORM mutation, which had the same TOCTOU race #733 fixed
        there: validate_invite() is a plain SELECT, and a separate commit() of an in-memory
        mutation leaves a window between them with no lock.
        """
        logger.info("Using invite", invite_code=invite_code)

        reserved = await self.session.execute(text("SELECT reserve_invite(:invite_code)"), {"invite_code": invite_code})
        if not cast(bool, reserved.scalar_one()):
            logger.warning("Invite not reservable", invite_code=invite_code)
            raise LoggedHTTPException(
                status_code=400,
                detail="Invalid invite code",
                invite_code=invite_code,
                operation="use_invite",
            )

        captured = await self.session.execute(
            text("SELECT capture_invite(:invite_code, CAST(:used_by_user_id AS UUID))"),
            {"invite_code": invite_code, "used_by_user_id": str(user_id)},
        )
        if not cast(bool, captured.scalar_one()):
            # Should be unreachable given reserve_invite's held lock; fail closed if violated.
            raise LoggedHTTPException(
                status_code=400,
                detail="Invalid invite code",
                invite_code=invite_code,
                operation="use_invite",
            )

        await self.session.commit()

        # Row was mutated via raw SQL, not the tracked ORM object - re-fetch rather than refresh().
        result = await self.session.execute(select(Invite).where(Invite.invite_code == invite_code))
        invite = result.scalar_one()

        logger.info("Invite marked as used", invite_code=invite_code)
        return invite

    async def get_user_invites(self, user_id: uuid.UUID) -> list[Invite]:
        """Get all invites used by a user."""
        logger.debug("Getting user invites")

        result = await self.session.execute(select(Invite).where(Invite.used_by_user_id == str(user_id)))
        invites = result.scalars().all()

        logger.debug("User invites retrieved", count=len(invites))
        return list(invites)

    async def get_unused_invites(self) -> list[Invite]:
        """Get all unused invites."""
        logger.debug("Getting unused invites")

        result = await self.session.execute(select(Invite).where(Invite.is_active.is_(True)))
        invites = result.scalars().all()

        logger.debug("Unused invites retrieved", count=len(invites))
        return list(invites)

    async def cleanup_expired_invites(self) -> int:
        """Remove expired invites and return count of removed invites."""
        logger.info("Cleaning up expired invites")

        # Find expired invites
        # Compare using naive UTC to match PostgreSQL TIMESTAMP WITHOUT TIME ZONE stored values
        result = await self.session.execute(
            select(Invite).where(Invite.expires_at < datetime.now(UTC).replace(tzinfo=None))
        )
        expired_invites = result.scalars().all()

        # Remove expired invites
        for invite in expired_invites:
            await self.session.delete(invite)

        await self.session.commit()

        logger.info("Expired invites cleaned up", removed_count=len(expired_invites))
        return len(expired_invites)


async def reserve_invite(session: AsyncSession, invite_code: str) -> None:
    """AUTH phase: take a row lock on the invite and confirm it is claimable, or raise.

    Used by server.auth.endpoints.register_user. Must run before any user object is built. The
    lock taken by reserve_invite() (SQL) is held until the caller's transaction ends (commit or
    rollback) - not released when this call returns - so it stays held across the rest of
    registration up to capture_invite(). Errors are NOT caught here; they must propagate so the
    caller's rollback runs.
    """
    result = await session.execute(
        text("SELECT reserve_invite(:invite_code)"),
        {"invite_code": invite_code},
    )
    if not cast(bool, result.scalar_one()):
        logger.warning("Invite not reservable", invite_code=invite_code)
        raise LoggedHTTPException(
            status_code=400,
            detail="Invalid invite code",
            invite_code=invite_code,
            operation="register_user",
        )


async def capture_invite(session: AsyncSession, user: User, invite_code: str) -> None:
    """CAPTURE phase: finalize a reservation already held by reserve_invite() in this transaction.

    Used by server.auth.endpoints.register_user. Must run after session.flush() (so user.id is
    populated) and before session.commit() (so a capture failure rolls the user back via
    get_async_session's exception handler). Errors from the procedure call are NOT caught here -
    they must propagate so the caller's rollback runs; swallowing them would leave a committed
    user against an unclaimed or already-claimed invite.
    """
    result = await session.execute(
        text("SELECT capture_invite(:invite_code, CAST(:used_by_user_id AS UUID))"),
        {
            "used_by_user_id": str(user.id),
            "invite_code": invite_code,
        },
    )
    if not cast(bool, result.scalar_one()):
        # Should be unreachable given reserve_invite's held lock; fail closed if violated.
        logger.warning(
            "Invite capture failed after reservation",
            invite_code=invite_code,
            user_id=user.id,
        )
        raise LoggedHTTPException(
            status_code=400,
            detail="Invalid invite code",
            invite_code=invite_code,
            operation="register_user",
        )
    logger.info(
        "Invite captured during registration",
        invite_code=invite_code,
        user_id=user.id,
        username=user.username,
    )


async def get_invite_manager(  # lizard: allow (FastAPI dep factory; real usage spans dependencies.py/endpoints.py/tests - guard's usage count is scoped to the changed-file set, not the repo)
    session: AsyncSession = Depends(get_async_session),
) -> InviteManager:
    """Get invite manager dependency."""
    return InviteManager(session)
