"""
Unit tests for skills catalog API (GET /v1/skills).

Character creation revamp 4.2: catalog list, base_value and allow_at_creation.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import Request

from server.models.skill import Skill
from server.schemas.players.skill import SkillListResponse


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = MagicMock(spec=Request)
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_user():
    """Create a mock user for auth."""
    from server.models.user import User

    return User(
        id=uuid.uuid4(),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )


@pytest.fixture
def sample_skills():
    """Sample skills for catalog response."""
    return [
        Skill(
            id=1,
            key="accounting",
            name="Accounting",
            description="Ledgers and financial records",
            base_value=5,
            allow_at_creation=True,
            category="knowledge",
        ),
        Skill(
            id=2,
            key="cthulhu_mythos",
            name="Cthulhu Mythos",
            description="Forbidden knowledge",
            base_value=0,
            allow_at_creation=False,
            category="knowledge",
        ),
        Skill(
            id=3,
            key="library_use",
            name="Library Use",
            description="Research and find information",
            base_value=5,
            allow_at_creation=True,
            category="knowledge",
        ),
    ]


@pytest.fixture
def mock_skill_repository(sample_skills):
    """Mock SkillRepository that returns sample skills."""
    repo = AsyncMock()
    repo.get_all_skills = AsyncMock(return_value=sample_skills)
    return repo


@pytest.mark.asyncio
async def test_get_skills_catalog_returns_list(mock_request, mock_user, mock_skill_repository):
    """GET /v1/skills returns SkillListResponse with skills list."""
    from server.api.skills import get_skills_catalog

    response = await get_skills_catalog(mock_request, current_user=mock_user, skill_repository=mock_skill_repository)

    assert isinstance(response, SkillListResponse)
    assert len(response.skills) == 3
    assert response.skills[0].key == "accounting"
    assert response.skills[0].base_value == 5
    assert response.skills[0].allow_at_creation is True
    assert response.skills[1].key == "cthulhu_mythos"
    assert response.skills[1].allow_at_creation is False
    assert response.skills[2].key == "library_use"
    assert response.skills[2].base_value == 5


@pytest.mark.asyncio
async def test_get_skills_catalog_unauthorized(mock_request, mock_skill_repository):
    """GET /v1/skills without authenticated user returns 401."""
    from server.api.skills import get_skills_catalog
    from server.exceptions import LoggedHTTPException

    with pytest.raises(LoggedHTTPException) as exc_info:
        await get_skills_catalog(
            mock_request,
            current_user=None,
            skill_repository=mock_skill_repository,
        )

    assert exc_info.value.status_code == 401
