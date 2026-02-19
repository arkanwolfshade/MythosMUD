"""
Invite management system for MythosMUD.

This module handles the invite-only registration system,
including invite creation, validation, and tracking.
"""

import uuid
from datetime import UTC, datetime, timedelta

from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..exceptions import LoggedHTTPException
from ..models.invite import Invite
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
        """Mark an invite as used by a specific user."""
        logger.info("Using invite", invite_code=invite_code)

        invite = await self.validate_invite(invite_code)
        invite.use_invite(str(user_id))

        await self.session.commit()
        await self.session.refresh(invite)

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


async def get_invite_manager(session: AsyncSession = Depends(get_async_session)) -> InviteManager:
    """Get invite manager dependency."""
    return InviteManager(session)
