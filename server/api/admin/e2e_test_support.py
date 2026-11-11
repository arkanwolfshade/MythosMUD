"""
Test-only endpoints for the Playwright e2e suite (ADR-029 step 8b).

They replace three scripts that wrote Postgres behind the player registry's back (reset, place, read state). Every
endpoint goes through ``E2ePlayerSupport``, so a change is one registry unit and a read is the registry's own view.

The router is mounted only on the e2e server (``e2e_test_support_enabled``): logging environment ``e2e_test`` against
the ``mythos_e2e`` database. It checks the admin role itself rather than calling ``validate_permission``, whose rate
limit (100 requests per five minutes per user) the specs' ``expect.poll`` of the state endpoint would exhaust.
"""

from __future__ import annotations

from typing import Annotated
from urllib.parse import urlsplit

from fastapi import APIRouter, Depends, Request, Response, status
from pydantic import BaseModel

from ...auth.users import get_current_user
from ...config import get_config
from ...dependencies import get_async_persistence, get_player_registry, get_room_service
from ...exceptions import LoggedHTTPException
from ...models.user import User
from ...services.admin_auth_service import AdminRole, get_admin_auth_service
from ...services.e2e_player_support import E2ePlayerState, E2ePlayerSupport, UnknownPlayerError, UnknownRoomError

E2E_ENVIRONMENT = "e2e_test"
E2E_DATABASE = "mythos_e2e"

e2e_test_support_router = APIRouter(prefix="/admin/test", tags=["admin", "e2e-test"])


def e2e_test_support_enabled() -> bool:
    """True only on the e2e server: logging environment ``e2e_test`` and the ``mythos_e2e`` database."""
    config = get_config()
    if config.logging.environment != E2E_ENVIRONMENT:
        return False
    return urlsplit(config.database.url).path.lstrip("/") == E2E_DATABASE


def require_e2e_admin(current_user: Annotated[User | None, Depends(get_current_user)]) -> User:
    """The signed-in admin. 401 without a user, 403 for a non-admin."""
    role = get_admin_auth_service().get_user_role(current_user)  # raises 401 for no user
    if role not in (AdminRole.ADMIN, AdminRole.SUPERUSER) or current_user is None:
        raise LoggedHTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return current_user


def get_e2e_player_support(request: Request) -> E2ePlayerSupport:
    """The harness over the container's registry, persistence layer and room service."""
    return E2ePlayerSupport(get_player_registry(request), get_async_persistence(request), get_room_service(request))


AdminDep = Annotated[User, Depends(require_e2e_admin)]
SupportDep = Annotated[E2ePlayerSupport, Depends(get_e2e_player_support)]


class PlaceRequest(BaseModel):
    """Where to put a character."""

    room_id: str


@e2e_test_support_router.post("/players/reset", status_code=status.HTTP_204_NO_CONTENT)
async def reset_shared_players(_admin: AdminDep, support: SupportDep) -> Response:
    """Put ArkanWolfshade and Ithaqua back in the default room, standing, at 50 DP."""
    await support.reset_shared_players()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@e2e_test_support_router.post("/players/{name}/reset-tutorial", status_code=status.HTTP_204_NO_CONTENT)
async def reset_tutorial_character(name: str, _admin: AdminDep, support: SupportDep) -> Response:
    """Put a character back at the very start of First Exposure and empty the chest and their deposit box."""
    try:
        await support.reset_tutorial_character(name)
    except UnknownPlayerError as e:
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No player named {name}") from e
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@e2e_test_support_router.post("/players/{name}/place", status_code=status.HTTP_204_NO_CONTENT)
async def place_player(
    name: str,
    body: PlaceRequest,
    _admin: AdminDep,
    support: SupportDep,
) -> Response:
    """Move a character to a room, out of the tutorial."""
    try:
        await support.place(name, body.room_id)
    except UnknownPlayerError as e:
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No player named {name}") from e
    except UnknownRoomError as e:
        raise LoggedHTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No room with stable id {body.room_id}"
        ) from e
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@e2e_test_support_router.get("/players/{name}/state", response_model=E2ePlayerState)
async def player_state(name: str, _admin: AdminDep, support: SupportDep) -> E2ePlayerState:
    """One character's state as the registry holds it."""
    try:
        return await support.state(name)
    except UnknownPlayerError as e:
        raise LoggedHTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No player named {name}") from e
