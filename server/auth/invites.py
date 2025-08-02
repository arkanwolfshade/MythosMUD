"""
Invite management system for MythosMUD.

This module handles the invite-only registration system,
including invite creation, validation, and tracking.
"""

import uuid
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_async_session
from ..models.invite import Invite


class InviteManager:
    """
    Manages invite creation, validation, and tracking.

    Handles the invite-only registration system for MythosMUD.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_invite(self, expires_in_days: int = 30) -> Invite:
        """Create a new invite."""

        invite_code = Invite.generate_code()
        expires_at = datetime.utcnow() + timedelta(days=expires_in_days)

        invite = Invite(invite_code=invite_code, is_used=False, expires_at=expires_at)

        self.session.add(invite)
        await self.session.commit()
        await self.session.refresh(invite)

        return invite

    async def validate_invite(self, invite_code: str) -> Invite:
        """Validate an invite code."""

        # Find invite by code
        result = await self.session.execute(select(Invite).where(Invite.invite_code == invite_code))
        invite = result.scalar_one_or_none()

        if not invite:
            raise HTTPException(status_code=400, detail="Invalid invite code")

        if not invite.is_valid():
            raise HTTPException(status_code=400, detail="Invite code is expired or already used")

        return invite

    async def use_invite(self, invite_code: str, user_id: uuid.UUID) -> Invite:
        """Mark an invite as used by a specific user."""

        invite = await self.validate_invite(invite_code)
        invite.use_invite(user_id)

        await self.session.commit()
        await self.session.refresh(invite)

        return invite

    async def get_user_invites(self, user_id: uuid.UUID) -> list[Invite]:
        """Get all invites used by a user."""

        result = await self.session.execute(select(Invite).where(Invite.used_by_user_id == str(user_id)))
        return result.scalars().all()

    async def get_unused_invites(self) -> list[Invite]:
        """Get all unused invites."""

        result = await self.session.execute(select(Invite).where(Invite.is_used.is_(False)))
        return result.scalars().all()

    async def cleanup_expired_invites(self) -> int:
        """Remove expired invites and return count of removed invites."""

        # Find expired invites
        result = await self.session.execute(select(Invite).where(Invite.expires_at < datetime.utcnow()))
        expired_invites = result.scalars().all()

        # Remove expired invites
        for invite in expired_invites:
            await self.session.delete(invite)

        await self.session.commit()
        return len(expired_invites)


async def get_invite_manager(session: AsyncSession = Depends(get_async_session)) -> InviteManager:
    """Get invite manager dependency."""
    return InviteManager(session)
