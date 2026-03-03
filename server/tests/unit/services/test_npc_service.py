"""
Unit tests for NPC service.

Tests the NPCService class.
"""

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.models.npc import NPCDefinition, NPCSpawnRule
from server.services.npc_service import NPCService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=too-many-lines  # Reason: Comprehensive test file for AsyncPersistenceLayer requires extensive test coverage across many scenarios


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


def _def_row(definition):
    """Build procedure result row (mappings().all()[i] or .first()) for NPCDefinition."""
    row = MagicMock()
    row.id = definition.id
    row.name = definition.name
    row.description = definition.description
    row.npc_type = definition.npc_type
    row.sub_zone_id = definition.sub_zone_id
    row.room_id = definition.room_id
    row.required_npc = definition.required_npc
    row.max_population = definition.max_population
    row.spawn_probability = definition.spawn_probability
    row.base_stats = definition.base_stats
    row.behavior_config = definition.behavior_config
    row.ai_integration_stub = getattr(definition, "ai_integration_stub", "{}")
    row.created_at = definition.created_at
    row.updated_at = definition.updated_at
    return row


def _spawn_rule_row(rule):
    """Build procedure result row for NPCSpawnRule."""
    row = MagicMock()
    row.id = rule.id
    row.npc_definition_id = rule.npc_definition_id
    row.sub_zone_id = rule.sub_zone_id
    row.min_population = rule.min_population
    row.max_population = rule.max_population
    row.spawn_conditions = rule.spawn_conditions
    return row


@pytest.mark.asyncio
async def test_npc_service_init():
    """Test NPCService initialization."""
    service = NPCService()
    assert service is not None


def _mock_result_mappings_all(rows):
    """Build mock result such that result.mappings().all() returns rows."""
    mock_result = MagicMock()
    mock_mappings = MagicMock()
    mock_mappings.all.return_value = rows
    mock_result.mappings.return_value = mock_mappings
    return mock_result


@pytest.mark.asyncio
async def test_get_npc_definitions_success(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definitions() successfully retrieves definitions."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    result = await npc_service.get_npc_definitions(mock_session)

    assert len(result) == 1
    assert result[0].id == sample_npc_definition.id
    assert result[0].name == sample_npc_definition.name
    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_get_npc_definitions_empty(mock_session, npc_service):
    """Test get_npc_definitions() returns empty list when no definitions."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

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
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    result = await npc_service.get_npc_definition(mock_session, 1)

    assert result is not None
    assert result.id == 1
    assert result.name == "Test NPC"


@pytest.mark.asyncio
async def test_get_npc_definition_not_found(mock_session, npc_service):
    """Test get_npc_definition() returns None when not found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

    result = await npc_service.get_npc_definition(mock_session, 999)

    assert result is None


@pytest.mark.asyncio
async def test_get_npc_definition_error(mock_session, npc_service):
    """Test get_npc_definition() handles errors."""
    mock_session.execute.side_effect = Exception("Unexpected error")

    with pytest.raises(Exception, match="Unexpected error"):
        await npc_service.get_npc_definition(mock_session, 1)


@pytest.mark.asyncio
async def test_create_npc_definition_success(mock_session, npc_service, sample_npc_definition):
    """Test create_npc_definition() successfully creates definition."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    result = await npc_service.create_npc_definition(
        mock_session,
        {
            "name": "Test NPC",
            "description": "A test NPC",
            "npc_type": "passive_mob",
            "sub_zone_id": "arkhamcity/downtown",
        },
    )

    assert result.id == sample_npc_definition.id
    assert result.name == "Test NPC"
    mock_session.execute.assert_called_once()


@pytest.mark.asyncio
async def test_create_npc_definition_invalid_type(mock_session, npc_service):
    """Test create_npc_definition() raises ValueError for invalid type."""
    with pytest.raises(ValueError, match="Invalid NPC type"):
        await npc_service.create_npc_definition(
            mock_session,
            {
                "name": "Test NPC",
                "description": "A test NPC",
                "npc_type": "invalid_type",
                "sub_zone_id": "arkhamcity/downtown",
            },
        )


@pytest.mark.asyncio
async def test_create_npc_definition_invalid_probability(mock_session, npc_service):
    """Test create_npc_definition() raises ValueError for invalid probability."""
    with pytest.raises(ValueError, match="Spawn probability must be between"):
        await npc_service.create_npc_definition(
            mock_session,
            {
                "name": "Test NPC",
                "description": "A test NPC",
                "npc_type": "passive_mob",
                "sub_zone_id": "arkhamcity/downtown",
                "spawn_probability": 1.5,  # Invalid: > 1.0
            },
        )


@pytest.mark.asyncio
async def test_create_npc_definition_invalid_max_population(mock_session, npc_service):
    """Test create_npc_definition() raises ValueError for invalid max population."""
    with pytest.raises(ValueError, match="Max population must be at least 1"):
        await npc_service.create_npc_definition(
            mock_session,
            {
                "name": "Test NPC",
                "description": "A test NPC",
                "npc_type": "passive_mob",
                "sub_zone_id": "arkhamcity/downtown",
                "max_population": 0,  # Invalid: < 1
            },
        )


@pytest.mark.asyncio
async def test_create_npc_definition_with_base_stats(mock_session, npc_service, sample_npc_definition):
    """Test create_npc_definition() handles base_stats."""
    row = _def_row(sample_npc_definition)
    row.base_stats = '{"hp": 100, "mp": 50}'
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([row]))

    base_stats = {"hp": 100, "mp": 50}
    result = await npc_service.create_npc_definition(
        mock_session,
        {
            "name": "Test NPC",
            "description": "A test NPC",
            "npc_type": "passive_mob",
            "sub_zone_id": "arkhamcity/downtown",
            "base_stats": base_stats,
        },
    )

    assert result.base_stats == '{"hp": 100, "mp": 50}'


@pytest.mark.asyncio
async def test_update_npc_definition_success(mock_session, npc_service, sample_npc_definition):
    """Test update_npc_definition() successfully updates definition."""
    updated_def = MagicMock(spec=NPCDefinition)
    updated_def.id = 1
    updated_def.name = "Updated Name"
    updated_def.description = sample_npc_definition.description
    updated_def.npc_type = sample_npc_definition.npc_type
    updated_def.sub_zone_id = sample_npc_definition.sub_zone_id
    updated_def.room_id = sample_npc_definition.room_id
    updated_def.required_npc = sample_npc_definition.required_npc
    updated_def.max_population = sample_npc_definition.max_population
    updated_def.spawn_probability = sample_npc_definition.spawn_probability
    updated_def.base_stats = sample_npc_definition.base_stats
    updated_def.behavior_config = sample_npc_definition.behavior_config
    updated_def.ai_integration_stub = getattr(sample_npc_definition, "ai_integration_stub", "{}")
    updated_def.created_at = sample_npc_definition.created_at
    updated_def.updated_at = datetime.now(UTC).replace(tzinfo=None)
    mock_session.execute = AsyncMock(
        side_effect=[
            _mock_result_mappings_all([_def_row(sample_npc_definition)]),
            _mock_result_mappings_all([_def_row(updated_def)]),
        ]
    )

    result = await npc_service.update_npc_definition(
        mock_session,
        definition_id=1,
        params={"name": "Updated Name"},
    )

    assert result is not None
    assert result.name == "Updated Name"
    assert mock_session.execute.call_count == 2


@pytest.mark.asyncio
async def test_update_npc_definition_not_found(mock_session, npc_service):
    """Test update_npc_definition() returns None when not found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

    result = await npc_service.update_npc_definition(mock_session, definition_id=999, params={"name": "Updated Name"})

    assert result is None


@pytest.mark.asyncio
async def test_update_npc_definition_invalid_type(mock_session, npc_service, sample_npc_definition):
    """Test update_npc_definition() raises ValueError for invalid type."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    with pytest.raises(ValueError, match="Invalid NPC type"):
        await npc_service.update_npc_definition(mock_session, definition_id=1, params={"npc_type": "invalid_type"})


@pytest.mark.asyncio
async def test_update_npc_definition_invalid_probability(mock_session, npc_service, sample_npc_definition):
    """Test update_npc_definition() raises ValueError for invalid probability."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    with pytest.raises(ValueError, match="Spawn probability must be between"):
        await npc_service.update_npc_definition(mock_session, definition_id=1, params={"spawn_probability": 1.5})


@pytest.mark.asyncio
async def test_delete_npc_definition_success(mock_session, npc_service, sample_npc_definition):
    """Test delete_npc_definition() successfully deletes definition."""
    mock_delete_result = MagicMock()
    mock_delete_result.scalar.return_value = True
    mock_session.execute = AsyncMock(
        side_effect=[
            _mock_result_mappings_all([_def_row(sample_npc_definition)]),
            mock_delete_result,
        ]
    )

    result = await npc_service.delete_npc_definition(mock_session, 1)

    assert result is True
    assert mock_session.execute.call_count == 2


@pytest.mark.asyncio
async def test_delete_npc_definition_not_found(mock_session, npc_service):
    """Test delete_npc_definition() returns False when not found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

    result = await npc_service.delete_npc_definition(mock_session, 999)

    assert result is False


@pytest.mark.asyncio
async def test_get_spawn_rules_success(mock_session, npc_service, sample_spawn_rule):
    """Test get_spawn_rules() successfully retrieves rules."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_spawn_rule_row(sample_spawn_rule)]))

    result = await npc_service.get_spawn_rules(mock_session)

    assert len(result) == 1
    assert result[0].id == sample_spawn_rule.id
    assert result[0].npc_definition_id == sample_spawn_rule.npc_definition_id


@pytest.mark.asyncio
async def test_get_spawn_rules_database_error(mock_session, npc_service):
    """Test get_spawn_rules() handles database errors."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with pytest.raises(DatabaseError):
        await npc_service.get_spawn_rules(mock_session)


@pytest.mark.asyncio
async def test_get_spawn_rule_found(mock_session, npc_service, sample_spawn_rule):
    """Test get_spawn_rule() returns rule when found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_spawn_rule_row(sample_spawn_rule)]))

    result = await npc_service.get_spawn_rule(mock_session, 1)

    assert result is not None
    assert result.id == sample_spawn_rule.id
    assert result.npc_definition_id == sample_spawn_rule.npc_definition_id


@pytest.mark.asyncio
async def test_get_spawn_rule_not_found(mock_session, npc_service):
    """Test get_spawn_rule() returns None when not found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

    result = await npc_service.get_spawn_rule(mock_session, 999)

    assert result is None


@pytest.mark.asyncio
async def test_create_spawn_rule_success(mock_session, npc_service, sample_npc_definition, sample_spawn_rule):
    """Test create_spawn_rule() successfully creates rule."""
    mock_session.execute = AsyncMock(
        side_effect=[
            _mock_result_mappings_all([_def_row(sample_npc_definition)]),
            _mock_result_mappings_all([_spawn_rule_row(sample_spawn_rule)]),
        ]
    )

    result = await npc_service.create_spawn_rule(
        mock_session,
        npc_definition_id=1,
        sub_zone_id="arkhamcity/downtown",
    )

    assert result.id == sample_spawn_rule.id
    assert result.npc_definition_id == sample_spawn_rule.npc_definition_id
    assert mock_session.execute.call_count == 2


@pytest.mark.asyncio
async def test_create_spawn_rule_definition_not_found(mock_session, npc_service):
    """Test create_spawn_rule() raises ValueError when definition not found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

    with pytest.raises(ValueError, match="NPC definition not found"):
        await npc_service.create_spawn_rule(
            mock_session,
            npc_definition_id=999,
            sub_zone_id="arkhamcity/downtown",
        )


@pytest.mark.asyncio
async def test_create_spawn_rule_invalid_min_population(mock_session, npc_service, sample_npc_definition):
    """Test create_spawn_rule() raises ValueError for invalid min population."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

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
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

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
    mock_delete_result = MagicMock()
    mock_delete_result.scalar.return_value = True
    mock_session.execute = AsyncMock(
        side_effect=[
            _mock_result_mappings_all([_spawn_rule_row(sample_spawn_rule)]),
            mock_delete_result,
        ]
    )

    result = await npc_service.delete_spawn_rule(mock_session, 1)

    assert result is True
    assert mock_session.execute.call_count == 2


@pytest.mark.asyncio
async def test_delete_spawn_rule_not_found(mock_session, npc_service):
    """Test delete_spawn_rule() returns False when not found."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([]))

    result = await npc_service.delete_spawn_rule(mock_session, 999)

    assert result is False


@pytest.mark.asyncio
async def test_get_npc_definitions_by_type(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definitions_by_type() filters by type."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    result = await npc_service.get_npc_definitions_by_type(mock_session, "passive_mob")

    assert len(result) == 1
    assert result[0].npc_type == "passive_mob"


@pytest.mark.asyncio
async def test_get_npc_definitions_by_sub_zone(mock_session, npc_service, sample_npc_definition):
    """Test get_npc_definitions_by_sub_zone() filters by sub-zone."""
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([_def_row(sample_npc_definition)]))

    result = await npc_service.get_npc_definitions_by_sub_zone(mock_session, "arkhamcity/downtown")

    assert len(result) == 1
    assert result[0].sub_zone_id == "arkhamcity/downtown"


@pytest.mark.asyncio
async def test_get_system_statistics_success(mock_session, npc_service):
    """Test get_system_statistics() successfully generates stats."""
    stats_row = MagicMock()
    stats_row.total_npc_definitions = 8
    stats_row.npc_definitions_by_type = {"passive_mob": 5, "aggressive_mob": 3}
    stats_row.total_spawn_rules = 10
    mock_session.execute = AsyncMock(return_value=_mock_result_mappings_all([stats_row]))

    result = await npc_service.get_system_statistics(mock_session)

    assert "total_npc_definitions" in result
    assert "npc_definitions_by_type" in result
    assert "total_spawn_rules" in result
    assert "generated_at" in result
    assert result["total_npc_definitions"] == 8
    assert result["total_spawn_rules"] == 10
    assert result["npc_definitions_by_type"] == {"passive_mob": 5, "aggressive_mob": 3}


@pytest.mark.asyncio
async def test_get_system_statistics_database_error(mock_session, npc_service):
    """Test get_system_statistics() handles database errors."""
    mock_session.execute.side_effect = SQLAlchemyError("Database error")

    with pytest.raises(DatabaseError):
        await npc_service.get_system_statistics(mock_session)
