"""
Skills catalog API endpoints.

GET /v1/skills returns the skills catalog for character creation (plan 4.2).
"""

from fastapi import APIRouter, Depends, Request

from ..auth.users import get_current_user
from ..dependencies import SkillRepositoryDep
from ..error_types import ErrorMessages
from ..exceptions import LoggedHTTPException
from ..models.user import User
from ..persistence.repositories.skill_repository import SkillRepository
from ..schemas.players.skill import SkillData, SkillListResponse
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

skills_router = APIRouter(prefix="/skills", tags=["skills"])


@skills_router.get("/", response_model=SkillListResponse)
async def get_skills_catalog(
    _request: Request,
    current_user: User = Depends(get_current_user),
    skill_repository: SkillRepository = SkillRepositoryDep,
) -> SkillListResponse:
    """Return the  skills catalog (base values, allow_at_creation).

    Cthulhu Mythos is included with allow_at_creation=false.
    Used by the client for skill allocation during character creation.
    """
    if not current_user:
        raise LoggedHTTPException(
            status_code=401,
            detail=ErrorMessages.AUTHENTICATION_REQUIRED,
            operation="get_skills_catalog",
        )

    try:
        skills = await skill_repository.get_all_skills()
        skill_data = [
            SkillData(
                id=s.id,
                key=s.key,
                name=s.name,
                description=s.description,
                base_value=s.base_value,
                allow_at_creation=s.allow_at_creation,
                category=s.category,
            )
            for s in skills
        ]
        return SkillListResponse(skills=skill_data)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Catalog errors unpredictable, must create error context
        logger.error("Error retrieving skills catalog", error=str(e))
        raise LoggedHTTPException(
            status_code=500,
            detail=ErrorMessages.INTERNAL_ERROR,
            user_id=str(current_user.id) if current_user else None,
            operation="get_skills_catalog",
        ) from e
