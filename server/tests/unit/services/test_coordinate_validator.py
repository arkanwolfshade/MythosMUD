"""Unit tests for coordinate validation."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.coordinate_validator import CoordinateValidator


@pytest.fixture
def validator():
    session = MagicMock()
    session.execute = AsyncMock()
    session.commit = AsyncMock()
    return CoordinateValidator(session)


@pytest.mark.asyncio
async def test_validate_coordinates_no_conflicts(validator):
    conflicts_result = MagicMock()
    conflicts_result.__iter__ = MagicMock(return_value=iter([]))
    count_result = MagicMock()
    count_result.scalar_one.return_value = 0
    validator._session.execute = AsyncMock(side_effect=[conflicts_result, count_result])

    result = await validator.validate_coordinates("earth", "arkham", "downtown")

    assert result["valid"] is True
    assert result["conflicts"] == []
    assert result["total_rooms"] == 0


@pytest.mark.asyncio
async def test_validate_coordinates_reports_conflicts(validator):
    conflict_row = ("room_a", "Room A", "room_b", "Room B", 1.0, 2.0)
    conflicts_result = MagicMock()
    conflicts_result.__iter__ = MagicMock(return_value=iter([conflict_row]))
    count_result = MagicMock()
    count_result.scalar_one.return_value = 2
    validator._session.execute = AsyncMock(side_effect=[conflicts_result, count_result])

    result = await validator.validate_coordinates("earth", "arkham")

    assert result["valid"] is False
    assert len(result["conflicts"]) == 1
    assert result["conflicts"][0]["room1_id"] == "room_a"
    assert result["total_rooms"] == 2
