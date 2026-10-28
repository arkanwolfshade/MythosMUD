"""
Help API: GET /v1/api/help

Serves the command reference and concept guides to the Manual page. Admin-only commands are included only for
admins, so they never reach a player's browser.
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from ..auth.users import get_current_user
from ..help.help_content import HelpDocs, get_manual
from ..models.user import User
from .item_catalog import user_is_admin

help_router = APIRouter(prefix="/api/help", tags=["help"])


@help_router.get("", response_model=HelpDocs)
async def get_help_docs(current_user: Annotated[User, Depends(get_current_user)]) -> HelpDocs:
    """Return every command and guide the caller may see."""
    return get_manual(is_admin=user_is_admin(current_user))
