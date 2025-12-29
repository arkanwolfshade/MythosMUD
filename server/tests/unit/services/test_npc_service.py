"""
Unit tests for NPC service.

Tests the NPCService class.
"""

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.npc import NPCDefinition, NPCSpawnRule
from server.services.npc_service import NPCService


@pytest.fixture
def mock_session():
    """Create a mock AsyncSession."""
    session = AsyncMock()
    return session


@pytest.fixture
def npc_service():
    """Create NPCService instance."""
    return NPCService()


@pytest.fixture
def sample_npc_definition():
    """Create a sample NPC definition."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.name = "Test NPC"
    definition.description = "A test NPC"
    definition.npc_type = "passive_mob"
    definition.sub_zone_id = "arkhamcity/downtown"
    definition.room_id = "earth_arkhamcity_downtown_001"
    definition.required_npc = False
    definition.max_population = 5
    definition.spawn_probability = 0.8
    definition.base_stats = '{"hp": 100, "mp": 50}'
    definition.behavior_config = '{"wander": true}'
    definition.ai_integration_stub = "{}"
    definition.created_at = datetime.now(UTC).replace(tzinfo=None)
    definition.updated_at = datetime.now(UTC).replace(tzinfo=None)
    return definition


@pytest.fixture
def sample_spawn_rule():
    """Create a sample spawn rule."""
    rule = MagicMock(spec=NPCSpawnRule)
    rule.id = 1
    rule.npc_definition_id = 1
    rule.sub_zone_id = "arkhamcity/downtown"
    rule.min_population = 0
    rule.max_population = 10
    rule.spawn_conditions = '{"time_of_day": "day"}'
    return rule


@pytest.mark.asyncio
async def test_npc_service_init():
    """Test NPCService initialization."""
    service = NPCService()
    assert service is not None


@pytest.mark.asyncio
async def test_get_npc_definitions_success(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definitions() successfully retrieves definitions."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [sample_npc_definition]
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_npc_definitions(mock_session)

    assert len(result) == 1
    assert result[0] == sample_npc_definition
    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_npc_definitions_empty(mock_session, npc_service):
    """Test get_npc_definitions() returns empty list when no definitions."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_npc_definitions(mock_session)

    assert result == []


@pytest.mark.asyncio
async def test_get_npc_definitions_database_error(mock_session, npc_service):
    """Test get_npc_definitions() handles database errors."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with pytest.raises(DatabaseError):
        await npc_service.get_npc_definitions(mock_session)


@pytest.mark.asyncio
async def test_get_npc_definition_found(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definition() returns definition when found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_npc_definition(mock_session, 1)

    assert result == sample_npc_definition
    assert result.id == 1
    assert result.name == "Test NPC"


@pytest.mark.asyncio
async def test_get_npc_definition_not_found(mock_session, npc_service):
    """Test get_npc_definition() returns None when not found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_npc_definition(mock_session, 999)

    assert result is None


@pytest.mark.asyncio
async def test_get_npc_definition_error(mock_session, npc_service):
    """Test get_npc_definition() handles errors."""
    mock_session.execute.side_effect = Exception("Unexpected error")

    with pytest.raises(Exception, match="Unexpected error"):
        await npc_service.get_npc_definition(mock_session, 1)


@pytest.mark.asyncio
async def test_create_npc_definition_success(mock_session, npc_service):
    """Test create_npc_definition() successfully creates definition."""
    with patch("server.services.npc_service.NPCDefinition") as mock_npc_def:
        mock_definition = MagicMock()
        mock_definition.id = 1
        mock_definition.name = "Test NPC"
        mock_npc_def.return_value = mock_definition

        result = await npc_service.create_npc_definition(
            mock_session,
            name="Test NPC",
            description="A test NPC",
            npc_type="passive_mob",
            sub_zone_id="arkhamcity/downtown",
        )

        assert result == mock_definition
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()


@pytest.mark.asyncio
async def test_create_npc_definition_invalid_type(mock_session, npc_service):
    """Test create_npc_definition() raises ValueError for invalid type."""
    with pytest.raises(ValueError, match="Invalid NPC type"):
        await npc_service.create_npc_definition(
            mock_session,
            name="Test NPC",
            description="A test NPC",
            npc_type="invalid_type",
            sub_zone_id="arkhamcity/downtown",
        )


@pytest.mark.asyncio
async def test_create_npc_definition_invalid_probability(mock_session, npc_service):
    """Test create_npc_definition() raises ValueError for invalid probability."""
    with pytest.raises(ValueError, match="Spawn probability must be between"):
        await npc_service.create_npc_definition(
            mock_session,
            name="Test NPC",
            description="A test NPC",
            npc_type="passive_mob",
            sub_zone_id="arkhamcity/downtown",
            spawn_probability=1.5,  # Invalid: > 1.0
        )


@pytest.mark.asyncio
async def test_create_npc_definition_invalid_max_population(mock_session, npc_service):
    """Test create_npc_definition() raises ValueError for invalid max population."""
    with pytest.raises(ValueError, match="Max population must be at least 1"):
        await npc_service.create_npc_definition(
            mock_session,
            name="Test NPC",
            description="A test NPC",
            npc_type="passive_mob",
            sub_zone_id="arkhamcity/downtown",
            max_population=0,  # Invalid: < 1
        )


@pytest.mark.asyncio
async def test_create_npc_definition_with_base_stats(mock_session, npc_service):
    """Test create_npc_definition() handles base_stats."""
    with patch("server.services.npc_service.NPCDefinition") as mock_npc_def:
        mock_definition = MagicMock()
        mock_definition.id = 1
        mock_npc_def.return_value = mock_definition

        base_stats = {"hp": 100, "mp": 50}
        await npc_service.create_npc_definition(
            mock_session,
            name="Test NPC",
            description="A test NPC",
            npc_type="passive_mob",
            sub_zone_id="arkhamcity/downtown",
            base_stats=base_stats,
        )

        # Verify json.dumps was called with base_stats
        call_args = mock_npc_def.call_args[1]
        assert "base_stats" in call_args


@pytest.mark.asyncio
async def test_update_npc_definition_success(mock_session, npc_service, sample_npc_definition):
    """Test update_npc_definition() successfully updates definition."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    with patch("server.services.npc_service.datetime") as mock_datetime:
        mock_datetime.now.return_value.replace.return_value = datetime.now(UTC).replace(tzinfo=None)

        result = await npc_service.update_npc_definition(
            mock_session,
            definition_id=1,
            name="Updated Name",
        )

        assert result == sample_npc_definition
        mock_session.execute.assert_called()  # Update query
        mock_session.refresh.assert_called_once()


@pytest.mark.asyncio
async def test_update_npc_definition_not_found(mock_session, npc_service):
    """Test update_npc_definition() returns None when not found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    result = await npc_service.update_npc_definition(mock_session, definition_id=999, name="Updated Name")

    assert result is None


@pytest.mark.asyncio
async def test_update_npc_definition_invalid_type(mock_session, npc_service, sample_npc_definition):
    """Test update_npc_definition() raises ValueError for invalid type."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    with pytest.raises(ValueError, match="Invalid NPC type"):
        await npc_service.update_npc_definition(mock_session, definition_id=1, npc_type="invalid_type")


@pytest.mark.asyncio
async def test_update_npc_definition_invalid_probability(mock_session, npc_service, sample_npc_definition):
    """Test update_npc_definition() raises ValueError for invalid probability."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    with pytest.raises(ValueError, match="Spawn probability must be between"):
        await npc_service.update_npc_definition(mock_session, definition_id=1, spawn_probability=1.5)


@pytest.mark.asyncio
async def test_delete_npc_definition_success(mock_session, npc_service, sample_npc_definition):
    """Test delete_npc_definition() successfully deletes definition."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    result = await npc_service.delete_npc_definition(mock_session, 1)

    assert result is True
    # Should call execute twice: once for get, once for delete
    assert mock_session.execute.call_count == 2


@pytest.mark.asyncio
async def test_delete_npc_definition_not_found(mock_session, npc_service):
    """Test delete_npc_definition() returns False when not found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    result = await npc_service.delete_npc_definition(mock_session, 999)

    assert result is False


@pytest.mark.asyncio
async def test_get_spawn_rules_success(mock_session, npc_service, sample_spawn_rule):
    """Test get_spawn_rules() successfully retrieves rules."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [sample_spawn_rule]
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_spawn_rules(mock_session)

    assert len(result) == 1
    assert result[0] == sample_spawn_rule


@pytest.mark.asyncio
async def test_get_spawn_rules_database_error(mock_session, npc_service):
    """Test get_spawn_rules() handles database errors."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with pytest.raises(DatabaseError):
        await npc_service.get_spawn_rules(mock_session)


@pytest.mark.asyncio
async def test_get_spawn_rule_found(mock_session, npc_service, sample_spawn_rule):
    """Test get_spawn_rule() returns rule when found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_spawn_rule
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_spawn_rule(mock_session, 1)

    assert result == sample_spawn_rule


@pytest.mark.asyncio
async def test_get_spawn_rule_not_found(mock_session, npc_service):
    """Test get_spawn_rule() returns None when not found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_spawn_rule(mock_session, 999)

    assert result is None


@pytest.mark.asyncio
async def test_create_spawn_rule_success(mock_session, npc_service, sample_npc_definition):
    """Test create_spawn_rule() successfully creates rule."""
    # Mock get_npc_definition to return a definition
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    with patch("server.services.npc_service.NPCSpawnRule") as mock_spawn_rule:
        mock_rule = MagicMock()
        mock_rule.id = 1
        mock_spawn_rule.return_value = mock_rule

        result = await npc_service.create_spawn_rule(
            mock_session,
            npc_definition_id=1,
            sub_zone_id="arkhamcity/downtown",
        )

        assert result == mock_rule
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()


@pytest.mark.asyncio
async def test_create_spawn_rule_definition_not_found(mock_session, npc_service):
    """Test create_spawn_rule() raises ValueError when definition not found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    with pytest.raises(ValueError, match="NPC definition not found"):
        await npc_service.create_spawn_rule(
            mock_session,
            npc_definition_id=999,
            sub_zone_id="arkhamcity/downtown",
        )


@pytest.mark.asyncio
async def test_create_spawn_rule_invalid_min_population(mock_session, npc_service, sample_npc_definition):
    """Test create_spawn_rule() raises ValueError for invalid min population."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    with pytest.raises(ValueError, match="Min population must be non-negative"):
        await npc_service.create_spawn_rule(
            mock_session,
            npc_definition_id=1,
            sub_zone_id="arkhamcity/downtown",
            min_population=-1,
        )


@pytest.mark.asyncio
async def test_create_spawn_rule_invalid_max_population(mock_session, npc_service, sample_npc_definition):
    """Test create_spawn_rule() raises ValueError when max < min."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_npc_definition
    mock_session.execute.return_value = mock_result

    with pytest.raises(ValueError, match="Max population must be >= min population"):
        await npc_service.create_spawn_rule(
            mock_session,
            npc_definition_id=1,
            sub_zone_id="arkhamcity/downtown",
            min_population=10,
            max_population=5,  # Invalid: max < min
        )


@pytest.mark.asyncio
async def test_delete_spawn_rule_success(mock_session, npc_service, sample_spawn_rule):
    """Test delete_spawn_rule() successfully deletes rule."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = sample_spawn_rule
    mock_session.execute.return_value = mock_result

    result = await npc_service.delete_spawn_rule(mock_session, 1)

    assert result is True
    assert mock_session.execute.call_count == 2  # get + delete


@pytest.mark.asyncio
async def test_delete_spawn_rule_not_found(mock_session, npc_service):
    """Test delete_spawn_rule() returns False when not found."""
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = None
    mock_session.execute.return_value = mock_result

    result = await npc_service.delete_spawn_rule(mock_session, 999)

    assert result is False


@pytest.mark.asyncio
async def test_get_npc_definitions_by_type(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definitions_by_type() filters by type."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [sample_npc_definition]
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_npc_definitions_by_type(mock_session, "passive_mob")

    assert len(result) == 1
    assert result[0] == sample_npc_definition


@pytest.mark.asyncio
async def test_get_npc_definitions_by_sub_zone(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definitions_by_sub_zone() filters by sub-zone."""
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [sample_npc_definition]
    mock_session.execute.return_value = mock_result

    result = await npc_service.get_npc_definitions_by_sub_zone(mock_session, "arkhamcity/downtown")

    assert len(result) == 1
    assert result[0] == sample_npc_definition


@pytest.mark.asyncio
async def test_get_system_statistics_success(mock_session, npc_service):
    """Test get_system_statistics() successfully generates stats."""
    # Mock multiple execute calls for different queries
    mock_result1 = MagicMock()
    mock_result1.all.return_value = [("passive_mob", 5), ("aggressive_mob", 3)]
    mock_result2 = MagicMock()
    mock_result2.scalar.return_value = 8
    mock_result3 = MagicMock()
    mock_result3.scalar.return_value = 10

    mock_session.execute.side_effect = [mock_result1, mock_result2, mock_result3]

    result = await npc_service.get_system_statistics(mock_session)

    assert "total_npc_definitions" in result
    assert "npc_definitions_by_type" in result
    assert "total_spawn_rules" in result
    assert "generated_at" in result
    assert result["total_npc_definitions"] == 8
    assert result["total_spawn_rules"] == 10


@pytest.mark.asyncio
async def test_get_system_statistics_database_error(mock_session, npc_service):
    """Test get_system_statistics() handles database errors."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with pytest.raises(DatabaseError):
        await npc_service.get_system_statistics(mock_session)
