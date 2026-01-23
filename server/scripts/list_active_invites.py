"""List active invite codes."""

from pathlib import Path

from anyio import run
from dotenv import load_dotenv
from sqlalchemy import text

from server.database import get_session_maker

# Load environment variables
load_dotenv(Path(".env.local"))


async def list_active() -> str | None:
    """List active invite codes."""
    async with get_session_maker()() as session:
        result = await session.execute(text("SELECT invite_code FROM invites WHERE is_active = true LIMIT 10"))
        codes: list[str] = [str(row[0]) for row in result.fetchall()]
        if codes:
            print("Available invite codes:", ", ".join(codes))
            return codes[0]  # Return first available
        else:
            print("No active invite codes found")
            return None


if __name__ == "__main__":
    code = run(list_active)
    if code:
        print(f"\nUsing invite code: {code}")
