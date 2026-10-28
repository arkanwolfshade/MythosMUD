"""
Skipping First Exposure at character creation (#1081, ADR-028 D22/D24).

A new character may skip the tutorial once some character on the account, deleted ones included, has finished it.
The client asks ``GET /api/players/characters/tutorial-skip`` whether to offer the option; ``create-character``
checks again (the client is never trusted) and, for a skip, gives the new character the state a finished run leaves.
"""

import uuid
from typing import Annotated, cast

from fastapi import Depends

from ..async_persistence import AsyncPersistenceLayer
from ..auth.users import get_current_user
from ..dependencies import get_async_persistence, get_quest_service
from ..exceptions import LoggedHTTPException
from ..game.first_exposure import FinishPersistence, account_completed_first_exposure, skip_first_exposure
from ..game.quest import QuestService
from ..models.user import User
from ..schemas.players import TutorialSkipEligibilityResponse
from .player_router import player_router


async def tutorial_skip_eligible(
    current_user: User, persistence: AsyncPersistenceLayer, quest_service: QuestService
) -> bool:
    """Whether some character on the user's account, deleted ones included, has finished First Exposure."""
    characters = await persistence.get_players_by_user_id(str(current_user.id))
    return await account_completed_first_exposure(characters, quest_service)


@player_router.get("/characters/tutorial-skip", response_model=TutorialSkipEligibilityResponse)
async def tutorial_skip_eligibility(
    current_user: Annotated[User, Depends(get_current_user)],
    persistence: Annotated[AsyncPersistenceLayer, Depends(get_async_persistence)],
    quest_service: Annotated[QuestService, Depends(get_quest_service)],
) -> TutorialSkipEligibilityResponse:
    """Whether a new character may skip the First Exposure tutorial (the client shows the option only then)."""
    return TutorialSkipEligibilityResponse(
        eligible=await tutorial_skip_eligible(current_user, persistence, quest_service)
    )


async def refuse_ineligible_skip(
    current_user: User, persistence: AsyncPersistenceLayer, quest_service: QuestService
) -> None:
    """Raise 403 unless the account has earned the skip."""
    if not await tutorial_skip_eligible(current_user, persistence, quest_service):
        raise LoggedHTTPException(
            status_code=403,
            detail="Skipping First Exposure is only possible once a character on this account has finished it.",
            user_id=str(current_user.id),
            operation="create_character",
        )


async def apply_tutorial_skip(
    player_id: uuid.UUID, persistence: AsyncPersistenceLayer, quest_service: QuestService
) -> None:
    """Give a character just created with the tutorial skipped the end state of a finished run."""
    # The corruption writer's protocol takes any corruption-capable player; the layer saves Player rows.
    await skip_first_exposure(player_id, cast(FinishPersistence, cast(object, persistence)), quest_service)
