"""Unit tests for ProfessionService."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.exceptions import ValidationError
from server.game.profession_service import ProfessionService


def _profession(**overrides):
    prof = MagicMock()
    prof.id = overrides.get("id", 1)
    prof.name = overrides.get("name", "Scholar")
    prof.description = "Desc"
    prof.flavor_text = "Flavor"
    prof.is_available = True
    prof.get_stat_requirements.return_value = overrides.get("stat_requirements", {"int": 50})
    prof.get_mechanical_effects.return_value = overrides.get(
        "mechanical_effects",
        {"bonus_mp": 2, "structured": {"effect_type": "mp", "value": 1}},
    )
    return prof


@pytest.fixture
def persistence():
    p = MagicMock()
    p.get_professions = AsyncMock(return_value=[])
    p.get_profession_by_id = AsyncMock(return_value=None)
    return p


@pytest.fixture
def service(persistence):
    return ProfessionService(persistence)


def test_profession_to_dict_list_formats(service):
    prof = _profession()
    result = service.profession_to_dict(prof)
    assert result["id"] == 1
    assert result["stat_requirements"] == [{"stat": "int", "minimum": 50}]
    assert any(e.get("effect_type") == "bonus_mp" for e in result["mechanical_effects"])
    assert any(e.get("effect_type") == "mp" for e in result["mechanical_effects"])


@pytest.mark.asyncio
async def test_get_all_professions_dict(service, persistence):
    persistence.get_professions.return_value = [_profession(id=2, name="Detective")]
    rows = await service.get_all_professions_dict()
    assert len(rows) == 1
    assert rows[0]["name"] == "Detective"


@pytest.mark.asyncio
async def test_get_profession_by_id_dict_missing(service):
    assert await service.get_profession_by_id_dict(99) is None


@pytest.mark.asyncio
async def test_get_profession_by_id_dict_found(service, persistence):
    persistence.get_profession_by_id.return_value = _profession(id=3)
    row = await service.get_profession_by_id_dict(3)
    assert row is not None
    assert row["id"] == 3


@pytest.mark.asyncio
async def test_validate_and_get_profession_none_raises(service):
    with pytest.raises(ValidationError, match="profession_id is required"):
        await service.validate_and_get_profession(None)


@pytest.mark.asyncio
async def test_validate_and_get_profession_not_found_raises(service):
    with pytest.raises(ValidationError, match="not found"):
        await service.validate_and_get_profession(404)


@pytest.mark.asyncio
async def test_validate_and_get_profession_success(service, persistence):
    prof = _profession(id=7)
    persistence.get_profession_by_id.return_value = prof
    assert await service.validate_and_get_profession(7) is prof
