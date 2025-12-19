"""
Tests for NPC Management Service.

This module tests the comprehensive NPC management service that handles
CRUD operations for NPC definitions, spawn rules, and relationships.

As documented in the Cultes des Goules: "The cataloging and management of
eldritch entities requires precise and thorough validation protocols."
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from server.services.npc_service import NPCService, npc_service


@pytest.fixture
def npc_service_instance():
    """Create an NPCService instance for testing."""
    return NPCService()


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = AsyncMock()
    return session


@pytest.fixture
def sample_npc_definition():
    """Create a sample NPC definition for testing."""
    definition = NPCDefinition(
        id=1,
        name="Test Shopkeeper",
        description="A friendly shopkeeper",
        npc_type="shopkeeper",
        sub_zone_id="arkhamcity_downtown",
        room_id="earth_arkhamcity_downtown_001",
        required_npc=False,
        max_population=1,
        spawn_probability=1.0,
        base_stats=json.dumps({"health": 100}),
        behavior_config=json.dumps({"friendly": True}),
        ai_integration_stub=json.dumps({}),
    )
    return definition


@pytest.fixture
def sample_spawn_rule():
    """Create a sample spawn rule for testing."""
    rule = NPCSpawnRule(
        id=1,
        npc_definition_id=1,
        sub_zone_id="arkhamcity_downtown",
        min_population=0,
        max_population=999,
        spawn_conditions=json.dumps({"time_of_day": "any"}),
    )
    return rule


class TestNPCServiceInitialization:
    """Test NPCService initialization."""

    def test_service_initialization(self) -> None:
        """Test service initializes correctly."""
        service = NPCService()
        assert service is not None

    def test_global_service_instance_exists(self) -> None:
        """Test global npc_service instance exists."""
        assert npc_service is not None
        assert isinstance(npc_service, NPCService)


class TestGetNPCDefinitions:
    """Test retrieving NPC definitions."""

    @pytest.mark.asyncio
    async def test_get_npc_definitions_empty(self, npc_service_instance, mock_session):
        """Test getting definitions when none exist."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = []
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definitions(mock_session)

        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_get_npc_definitions_with_data(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test getting definitions with data."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = [sample_npc_definition]
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definitions(mock_session)

        assert len(result) == 1
        assert result[0].name == "Test Shopkeeper"

    @pytest.mark.asyncio
    async def test_get_npc_definitions_handles_errors(self, npc_service_instance, mock_session):
        """Test getting definitions handles database errors."""
        mock_session.execute = AsyncMock(side_effect=Exception("Database error"))

        with pytest.raises(Exception, match="Database error"):
            await npc_service_instance.get_npc_definitions(mock_session)


class TestGetNPCDefinition:
    """Test retrieving single NPC definition."""

    @pytest.mark.asyncio
    async def test_get_npc_definition_found(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test getting definition by ID when it exists."""
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = sample_npc_definition
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definition(mock_session, definition_id=1)

        assert result is not None
        assert result.id == 1
        assert result.name == "Test Shopkeeper"

    @pytest.mark.asyncio
    async def test_get_npc_definition_not_found(self, npc_service_instance, mock_session):
        """Test getting definition by ID when it doesn't exist."""
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definition(mock_session, definition_id=999)

        assert result is None

    @pytest.mark.asyncio
    async def test_get_npc_definition_handles_errors(self, npc_service_instance, mock_session):
        """Test getting definition handles database errors."""
        mock_session.execute = AsyncMock(side_effect=RuntimeError("Database error"))

        with pytest.raises(RuntimeError, match="Database error"):
            await npc_service_instance.get_npc_definition(mock_session, definition_id=1)


class TestCreateNPCDefinition:
    """Test creating NPC definitions."""

    @pytest.mark.asyncio
    async def test_create_npc_definition_success(self, npc_service_instance, mock_session):
        """Test successful NPC definition creation."""
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        result = await npc_service_instance.create_npc_definition(
            session=mock_session,
            name="New Shopkeeper",
            description="A new shopkeeper",
            npc_type="shopkeeper",
            sub_zone_id="arkhamcity_downtown",
            room_id="earth_arkhamcity_downtown_001",
            base_stats={"health": 100},
            behavior_config={"friendly": True},
        )

        assert result.name == "New Shopkeeper"
        assert result.npc_type == "shopkeeper"
        mock_session.add.assert_called_once()
        mock_session.flush.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_npc_definition_invalid_type(self, npc_service_instance, mock_session):
        """Test creating definition with invalid NPC type."""
        with pytest.raises(ValueError, match="Invalid NPC type"):
            await npc_service_instance.create_npc_definition(
                session=mock_session,
                name="Test NPC",
                description=None,
                npc_type="invalid_type",
                sub_zone_id="arkhamcity_downtown",
            )

    @pytest.mark.asyncio
    async def test_create_npc_definition_invalid_spawn_probability(self, npc_service_instance, mock_session):
        """Test creating definition with invalid spawn probability."""
        with pytest.raises(ValueError, match="Spawn probability must be between 0.0 and 1.0"):
            await npc_service_instance.create_npc_definition(
                session=mock_session,
                name="Test NPC",
                description=None,
                npc_type="shopkeeper",
                sub_zone_id="arkhamcity_downtown",
                spawn_probability=1.5,  # Invalid
            )

    @pytest.mark.asyncio
    async def test_create_npc_definition_invalid_max_population(self, npc_service_instance, mock_session):
        """Test creating definition with invalid max population."""
        with pytest.raises(ValueError, match="Max population must be at least 1"):
            await npc_service_instance.create_npc_definition(
                session=mock_session,
                name="Test NPC",
                description=None,
                npc_type="shopkeeper",
                sub_zone_id="arkhamcity_downtown",
                max_population=0,  # Invalid
            )

    @pytest.mark.asyncio
    async def test_create_npc_definition_handles_errors(self, npc_service_instance, mock_session):
        """Test creation handles database errors."""
        mock_session.add = MagicMock(side_effect=RuntimeError("Database error"))

        with pytest.raises(RuntimeError, match="Database error"):
            await npc_service_instance.create_npc_definition(
                session=mock_session,
                name="Test NPC",
                description=None,
                npc_type="shopkeeper",
                sub_zone_id="arkhamcity_downtown",
            )


class TestUpdateNPCDefinition:
    """Test updating NPC definitions."""

    @pytest.mark.asyncio
    async def test_update_npc_definition_success(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test successful NPC definition update."""
        # Mock get_npc_definition to return existing definition
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.execute = AsyncMock()
        mock_session.refresh = AsyncMock()

        result = await npc_service_instance.update_npc_definition(
            session=mock_session, definition_id=1, name="Updated Name", description="Updated description"
        )

        assert result is not None
        mock_session.execute.assert_called_once()
        mock_session.refresh.assert_called_once()

    @pytest.mark.asyncio
    async def test_update_npc_definition_not_found(self, npc_service_instance, mock_session):
        """Test updating non-existent definition."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=None)

        result = await npc_service_instance.update_npc_definition(
            session=mock_session, definition_id=999, name="New Name"
        )

        assert result is None

    @pytest.mark.asyncio
    async def test_update_npc_definition_invalid_type(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test updating with invalid NPC type."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)

        with pytest.raises(ValueError, match="Invalid NPC type"):
            await npc_service_instance.update_npc_definition(
                session=mock_session, definition_id=1, npc_type="invalid_type"
            )

    @pytest.mark.asyncio
    async def test_update_npc_definition_invalid_spawn_probability(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test updating with invalid spawn probability."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)

        with pytest.raises(ValueError, match="Spawn probability must be between 0.0 and 1.0"):
            await npc_service_instance.update_npc_definition(
                session=mock_session, definition_id=1, spawn_probability=-0.1
            )

    @pytest.mark.asyncio
    async def test_update_npc_definition_partial_update(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test partial update of definition."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.execute = AsyncMock()
        mock_session.refresh = AsyncMock()

        # Only update name
        result = await npc_service_instance.update_npc_definition(
            session=mock_session, definition_id=1, name="New Name"
        )

        assert result is not None
        mock_session.execute.assert_called_once()


class TestDeleteNPCDefinition:
    """Test deleting NPC definitions."""

    @pytest.mark.asyncio
    async def test_delete_npc_definition_success(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test successful NPC definition deletion."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.execute = AsyncMock()

        result = await npc_service_instance.delete_npc_definition(mock_session, definition_id=1)

        assert result is True
        mock_session.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_npc_definition_not_found(self, npc_service_instance, mock_session):
        """Test deleting non-existent definition."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=None)

        result = await npc_service_instance.delete_npc_definition(mock_session, definition_id=999)

        assert result is False

    @pytest.mark.asyncio
    async def test_delete_npc_definition_handles_errors(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test deletion handles database errors."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.execute = AsyncMock(side_effect=RuntimeError("Database error"))

        with pytest.raises(RuntimeError, match="Database error"):
            await npc_service_instance.delete_npc_definition(mock_session, definition_id=1)


class TestGetSpawnRules:
    """Test retrieving spawn rules."""

    @pytest.mark.asyncio
    async def test_get_spawn_rules_empty(self, npc_service_instance, mock_session):
        """Test getting spawn rules when none exist."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = []
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_spawn_rules(mock_session)

        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_get_spawn_rules_with_data(self, npc_service_instance, mock_session, sample_spawn_rule):
        """Test getting spawn rules with data."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = [sample_spawn_rule]
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_spawn_rules(mock_session)

        assert len(result) == 1
        assert result[0].npc_definition_id == 1

    @pytest.mark.asyncio
    async def test_get_spawn_rules_handles_errors(self, npc_service_instance, mock_session):
        """Test getting spawn rules handles errors."""
        mock_session.execute = AsyncMock(side_effect=RuntimeError("Database error"))

        with pytest.raises(RuntimeError, match="Database error"):
            await npc_service_instance.get_spawn_rules(mock_session)


class TestGetSpawnRule:
    """Test retrieving single spawn rule."""

    @pytest.mark.asyncio
    async def test_get_spawn_rule_found(self, npc_service_instance, mock_session, sample_spawn_rule):
        """Test getting spawn rule by ID when it exists."""
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = sample_spawn_rule
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_spawn_rule(mock_session, rule_id=1)

        assert result is not None
        assert result.id == 1

    @pytest.mark.asyncio
    async def test_get_spawn_rule_not_found(self, npc_service_instance, mock_session):
        """Test getting spawn rule by ID when it doesn't exist."""
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_spawn_rule(mock_session, rule_id=999)

        assert result is None


class TestCreateSpawnRule:
    """Test creating spawn rules."""

    @pytest.mark.asyncio
    async def test_create_spawn_rule_success(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test successful spawn rule creation."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        result = await npc_service_instance.create_spawn_rule(
            session=mock_session,
            npc_definition_id=1,
            sub_zone_id="arkhamcity_downtown",
            min_population=0,
            max_population=10,
            spawn_conditions={"time": "day"},
        )

        assert result.npc_definition_id == 1
        assert result.sub_zone_id == "arkhamcity_downtown"
        mock_session.add.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_spawn_rule_definition_not_found(self, npc_service_instance, mock_session):
        """Test creating spawn rule for non-existent definition."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=None)

        with pytest.raises(ValueError, match="NPC definition not found"):
            await npc_service_instance.create_spawn_rule(
                session=mock_session, npc_definition_id=999, sub_zone_id="arkhamcity_downtown"
            )

    @pytest.mark.asyncio
    async def test_create_spawn_rule_invalid_min_players(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test creating spawn rule with invalid min_population."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)

        with pytest.raises(ValueError, match="Min population must be non-negative"):
            await npc_service_instance.create_spawn_rule(
                session=mock_session, npc_definition_id=1, sub_zone_id="arkhamcity_downtown", min_population=-1
            )

    @pytest.mark.asyncio
    async def test_create_spawn_rule_invalid_max_players(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test creating spawn rule with max < min population."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)

        with pytest.raises(ValueError, match="Max population must be >= min population"):
            await npc_service_instance.create_spawn_rule(
                session=mock_session,
                npc_definition_id=1,
                sub_zone_id="arkhamcity_downtown",
                min_population=10,
                max_population=5,
            )


class TestDeleteSpawnRule:
    """Test deleting spawn rules."""

    @pytest.mark.asyncio
    async def test_delete_spawn_rule_success(self, npc_service_instance, mock_session, sample_spawn_rule):
        """Test successful spawn rule deletion."""
        npc_service_instance.get_spawn_rule = AsyncMock(return_value=sample_spawn_rule)
        mock_session.execute = AsyncMock()

        result = await npc_service_instance.delete_spawn_rule(mock_session, rule_id=1)

        assert result is True
        mock_session.execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_spawn_rule_not_found(self, npc_service_instance, mock_session):
        """Test deleting non-existent spawn rule."""
        npc_service_instance.get_spawn_rule = AsyncMock(return_value=None)

        result = await npc_service_instance.delete_spawn_rule(mock_session, rule_id=999)

        assert result is False


class TestGetNPCDefinitionsByType:
    """Test retrieving definitions by type."""

    @pytest.mark.asyncio
    async def test_get_npc_definitions_by_type_found(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test getting definitions by type."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = [sample_npc_definition]
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definitions_by_type(mock_session, npc_type="shopkeeper")

        assert len(result) == 1
        assert result[0].npc_type == "shopkeeper"

    @pytest.mark.asyncio
    async def test_get_npc_definitions_by_type_empty(self, npc_service_instance, mock_session):
        """Test getting definitions by type with no matches."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = []
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definitions_by_type(mock_session, npc_type="rare_type")

        assert len(result) == 0


class TestGetNPCDefinitionsBySubZone:
    """Test retrieving definitions by sub-zone."""

    @pytest.mark.asyncio
    async def test_get_npc_definitions_by_sub_zone_found(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test getting definitions by sub-zone."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = [sample_npc_definition]
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definitions_by_sub_zone(
            mock_session, sub_zone_id="arkhamcity_downtown"
        )

        assert len(result) == 1
        assert result[0].sub_zone_id == "arkhamcity_downtown"

    @pytest.mark.asyncio
    async def test_get_npc_definitions_by_sub_zone_empty(self, npc_service_instance, mock_session):
        """Test getting definitions by sub-zone with no matches."""
        mock_result = MagicMock()
        mock_result.scalars().all.return_value = []
        mock_session.execute = AsyncMock(return_value=mock_result)

        result = await npc_service_instance.get_npc_definitions_by_sub_zone(mock_session, sub_zone_id="unknown_zone")

        assert len(result) == 0


class TestGetSystemStatistics:
    """Test system statistics retrieval."""

    @pytest.mark.asyncio
    async def test_get_system_statistics_success(self, npc_service_instance, mock_session):
        """Test successful system statistics retrieval."""
        # Mock the database queries
        mock_result1 = MagicMock()
        mock_result1.all.return_value = [("shopkeeper", 5), ("guard", 3)]

        mock_result2 = MagicMock()
        mock_result2.scalar.return_value = 8

        mock_result3 = MagicMock()
        mock_result3.scalar.return_value = 12

        call_count = [0]

        async def mock_execute(*_args, **_kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return mock_result1
            elif call_count[0] == 2:
                return mock_result2
            else:
                return mock_result3

        mock_session.execute = mock_execute
        mock_session.query = lambda x: MagicMock()

        result = await npc_service_instance.get_system_statistics(mock_session)

        assert result["total_npc_definitions"] == 8
        assert result["total_spawn_rules"] == 12
        assert "generated_at" in result

    @pytest.mark.asyncio
    async def test_get_system_statistics_handles_errors(self, npc_service_instance, mock_session):
        """Test system statistics handles database errors."""
        mock_session.execute = AsyncMock(side_effect=RuntimeError("Database error"))

        with pytest.raises(RuntimeError, match="Database error"):
            await npc_service_instance.get_system_statistics(mock_session)


class TestValidationLogic:
    """Test validation logic across service methods."""

    @pytest.mark.asyncio
    async def test_all_npc_types_are_valid(self, npc_service_instance, mock_session):
        """Test all NPCDefinitionType values are accepted."""
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        valid_types = [t.value for t in NPCDefinitionType]

        for npc_type in valid_types:
            result = await npc_service_instance.create_npc_definition(
                session=mock_session,
                name=f"Test {npc_type}",
                description=None,
                npc_type=npc_type,
                sub_zone_id="test_zone",
            )
            assert result.npc_type == npc_type

    @pytest.mark.asyncio
    async def test_spawn_probability_boundaries(self, npc_service_instance, mock_session):
        """Test spawn probability boundary values."""
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        # Test minimum (0.0)
        result = await npc_service_instance.create_npc_definition(
            session=mock_session,
            name="Test NPC",
            description=None,
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
            spawn_probability=0.0,
        )
        assert result.spawn_probability == 0.0

        # Test maximum (1.0)
        result = await npc_service_instance.create_npc_definition(
            session=mock_session,
            name="Test NPC 2",
            description=None,
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
            spawn_probability=1.0,
        )
        assert result.spawn_probability == 1.0


class TestJSONHandling:
    """Test JSON serialization/deserialization in service."""

    @pytest.mark.asyncio
    async def test_create_definition_serializes_json_fields(self, npc_service_instance, mock_session):
        """Test creation properly serializes dict fields to JSON."""
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        base_stats = {"health": 100, "mana": 50}
        behavior_config = {"aggressive": False, "wander_radius": 5}
        ai_integration = {"model": "gpt-4", "context": "shopkeeper"}

        result = await npc_service_instance.create_npc_definition(
            session=mock_session,
            name="Test NPC",
            description=None,
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
            base_stats=base_stats,
            behavior_config=behavior_config,
            ai_integration_stub=ai_integration,
        )

        # Fields should be JSON strings
        assert isinstance(result.base_stats, str)
        assert json.loads(result.base_stats) == base_stats

    @pytest.mark.asyncio
    async def test_create_spawn_rule_serializes_conditions(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test spawn rule creation serializes conditions."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        conditions = {"weather": "clear", "time_of_day": "day"}

        result = await npc_service_instance.create_spawn_rule(
            session=mock_session,
            npc_definition_id=1,
            sub_zone_id="test_zone",
            spawn_conditions=conditions,
        )

        assert isinstance(result.spawn_conditions, str)
        assert json.loads(result.spawn_conditions) == conditions


class TestErrorMessages:
    """Test error messages are informative."""

    @pytest.mark.asyncio
    async def test_create_definition_invalid_type_message(self, npc_service_instance, mock_session):
        """Test invalid type error includes the invalid value."""
        with pytest.raises(ValueError) as exc_info:
            await npc_service_instance.create_npc_definition(
                session=mock_session,
                name="Test",
                description=None,
                npc_type="not_a_real_type",
                sub_zone_id="zone",
            )

        assert "not_a_real_type" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_create_spawn_rule_invalid_range_message(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test invalid population range error is informative."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)

        with pytest.raises(ValueError) as exc_info:
            await npc_service_instance.create_spawn_rule(
                session=mock_session, npc_definition_id=1, sub_zone_id="zone", min_population=10, max_population=5
            )

        error_msg = str(exc_info.value)
        assert "10" in error_msg
        assert "5" in error_msg


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    @pytest.mark.asyncio
    async def test_update_with_no_changes(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test update with no fields changed."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.execute = AsyncMock()
        mock_session.refresh = AsyncMock()

        # Call update with no parameters
        result = await npc_service_instance.update_npc_definition(session=mock_session, definition_id=1)

        # Should still succeed
        assert result is not None

    @pytest.mark.asyncio
    async def test_create_definition_with_empty_json_objects(self, npc_service_instance, mock_session):
        """Test creating definition with empty dict fields."""
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        result = await npc_service_instance.create_npc_definition(
            session=mock_session,
            name="Test NPC",
            description=None,
            npc_type="shopkeeper",
            sub_zone_id="zone",
            base_stats={},
            behavior_config={},
            ai_integration_stub={},
        )

        # Empty dicts should be serialized as "{}"
        assert result.base_stats == "{}"
        assert result.behavior_config == "{}"

    @pytest.mark.asyncio
    async def test_create_spawn_rule_with_zero_min_players(
        self, npc_service_instance, mock_session, sample_npc_definition
    ):
        """Test creating spawn rule with min_population=0."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()

        result = await npc_service_instance.create_spawn_rule(
            session=mock_session, npc_definition_id=1, sub_zone_id="zone", min_population=0, max_population=999
        )

        assert result.min_population == 0


class TestIntegrationScenarios:
    """Test integration scenarios combining multiple operations."""

    @pytest.mark.asyncio
    async def test_complete_npc_definition_lifecycle(self, npc_service_instance, mock_session):
        """Test complete lifecycle: create, read, update, delete."""
        # Setup mocks
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()
        mock_session.execute = AsyncMock()

        # 1. Create definition
        created = await npc_service_instance.create_npc_definition(
            session=mock_session,
            name="Test NPC",
            description="Test description",
            npc_type="shopkeeper",
            sub_zone_id="test_zone",
        )
        assert created.name == "Test NPC"

        # 2. Mock read (get definition)
        npc_service_instance.get_npc_definition = AsyncMock(return_value=created)

        # 3. Update definition
        updated = await npc_service_instance.update_npc_definition(
            session=mock_session, definition_id=1, name="Updated NPC"
        )
        assert updated is not None

        # 4. Delete definition
        deleted = await npc_service_instance.delete_npc_definition(mock_session, definition_id=1)
        assert deleted is True

    @pytest.mark.asyncio
    async def test_spawn_rule_management_flow(self, npc_service_instance, mock_session, sample_npc_definition):
        """Test complete spawn rule management flow."""
        npc_service_instance.get_npc_definition = AsyncMock(return_value=sample_npc_definition)
        mock_session.add = MagicMock()
        mock_session.flush = AsyncMock()
        mock_session.refresh = AsyncMock()
        mock_session.execute = AsyncMock()

        # 1. Create spawn rule
        created = await npc_service_instance.create_spawn_rule(
            session=mock_session, npc_definition_id=1, sub_zone_id="zone", min_population=0, max_population=10
        )
        assert created.npc_definition_id == 1

        # 2. Mock read
        npc_service_instance.get_spawn_rule = AsyncMock(return_value=created)

        # 3. Delete spawn rule
        deleted = await npc_service_instance.delete_spawn_rule(mock_session, rule_id=1)
        assert deleted is True
