"""Check the status of a specific invite code."""

from pathlib import Path

from anyio import run
from dotenv import load_dotenv
from sqlalchemy import text

from server.database import get_session_maker

# Load environment variables
load_dotenv(Path(".env.local"))


async def check_invite(invite_code: str):
    """Check the status of an invite code."""
    async with get_session_maker()() as session:
        result = await session.execute(
            text(
                "SELECT invite_code, is_active, used_by_user_id, created_at, expires_at FROM invites WHERE invite_code = :code"
            ),
            {"code": invite_code},
        )
        row = result.fetchone()
        if row:
            print(f"Invite Code: {row[0]}")
            print(f"is_active: {row[1]}")
            print(f"used_by_user_id: {row[2]}")
            print(f"created_at: {row[3]}")
            print(f"expires_at: {row[4]}")
        else:
            print(f"Invite code '{invite_code}' not found")


if __name__ == "__main__":
    import sys

    invite_code = sys.argv[1] if len(sys.argv) > 1 else "COSMOS202541"
    run(check_invite, invite_code)  # anyio.run supports *args for async functions
