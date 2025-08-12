#!/usr/bin/env python3
"""Check available invite codes."""

import asyncio

from auth.invites import InviteManager
from database import get_async_session


async def main():
    """Check available invite codes."""
    session = await get_async_session().__anext__()
    try:
        invite_manager = InviteManager(session)
        invites = await invite_manager.list_invites()
        print("Available invites:")
        for invite in invites:
            print(f"  Code: {invite.code}, Used: {invite.used}, Created: {invite.created_at}")
    finally:
        await session.close()

if __name__ == "__main__":
    asyncio.run(main())
