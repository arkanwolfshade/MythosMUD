"""
Tests for the professions API endpoints.

This module tests all profession-related API operations including
retrieval of available professions and profession details.
Following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.
"""

import uuid
from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from server.api.professions import (
    get_all_professions,
    get_profession_by_id,
)
from server.models.profession import Profession


@pytest.fixture
def mock_current_user():
    """Mock authenticated user for testing."""
    user = Mock()
    user.id = str(uuid.uuid4())
    user.username = "testuser"
    # Make the mock support dictionary access for all attributes
    user.__getitem__ = lambda self, key: getattr(self, key)
    return user


@pytest.fixture
def sample_profession_data():
    """Sample profession data for testing."""
    profession = Mock(spec=Profession)
    profession.id = 0
    profession.name = "Tramp"
    profession.description = "A wandering soul with no fixed abode"
    profession.flavor_text = (
        "You have learned to survive on the streets, finding shelter where you can and making do with what you have."
    )
    profession.stat_requirements = "{}"
    profession.mechanical_effects = "{}"
    profession.is_available = True
    profession.get_stat_requirements.return_value = {}
    profession.get_mechanical_effects.return_value = {}
    return profession


@pytest.fixture
def sample_profession_data_2():
    """Second sample profession data for testing."""
    profession = Mock(spec=Profession)
    profession.id = 1
    profession.name = "Gutter Rat"
    profession.description = "A street-smart survivor of the urban underbelly"
    profession.flavor_text = "You know the hidden passages and dark corners of the city, where others fear to tread."
    profession.stat_requirements = "{}"
    profession.mechanical_effects = "{}"
    profession.is_available = True
    profession.get_stat_requirements.return_value = {}
    profession.get_mechanical_effects.return_value = {}
    return profession


@pytest.fixture
def sample_profession_with_requirements():
    """Sample profession with stat requirements for testing."""
    profession = Mock(spec=Profession)
    profession.id = 2
    profession.name = "Investigator"
    profession.description = "A skilled researcher and detective"
    profession.flavor_text = "You have trained your mind to uncover hidden truths and solve mysteries."
    profession.stat_requirements = '{"strength": 12, "intelligence": 14}'
    profession.mechanical_effects = "{}"
    profession.is_available = True
    profession.get_stat_requirements.return_value = {"strength": 12, "intelligence": 14}
    profession.get_mechanical_effects.return_value = {}
    return profession


@pytest.fixture
def sample_strongman_profession():
    """Sample Strongman profession with strength requirement for testing."""
    profession = Mock(spec=Profession)
    profession.id = 2
    profession.name = "Strongman"
    profession.description = "A physically powerful individual with exceptional strength"
    profession.flavor_text = "You have developed your body through years of physical training, making you capable of feats that would challenge lesser mortals."
    profession.stat_requirements = '{"strength": 10}'
    profession.mechanical_effects = "{}"
    profession.is_available = True
    profession.get_stat_requirements.return_value = {"strength": 10}
    profession.get_mechanical_effects.return_value = {}
    return profession


@pytest.fixture
def mock_persistence():
    """Mock persistence layer for testing."""
    persistence = Mock()
    persistence.get_all_professions = Mock()
    persistence.get_profession_by_id = Mock()
    return persistence


@pytest.fixture
def mock_request():
    """Mock FastAPI request object."""
    request = Mock()
    request.app.state.persistence = Mock()
    return request


class TestProfessionRetrieval:
    """Test cases for profession retrieval endpoints."""

    def test_get_all_professions_success(
        self, mock_current_user, sample_profession_data, sample_profession_data_2, mock_persistence, mock_request
    ):
        """Test successful retrieval of all available professions."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_all_professions.return_value = [sample_profession_data, sample_profession_data_2]

        result = get_all_professions(mock_current_user, mock_request)

        assert "professions" in result
        assert len(result["professions"]) == 2
        assert result["professions"][0]["id"] == 0
        assert result["professions"][0]["name"] == "Tramp"
        assert result["professions"][1]["id"] == 1
        assert result["professions"][1]["name"] == "Gutter Rat"
        mock_persistence.get_all_professions.assert_called_once()

    def test_get_all_professions_empty(self, mock_current_user, mock_persistence, mock_request):
        """Test retrieval of professions when none are available."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_all_professions.return_value = []

        result = get_all_professions(mock_current_user, mock_request)

        assert "professions" in result
        assert len(result["professions"]) == 0
        mock_persistence.get_all_professions.assert_called_once()

    def test_get_all_professions_database_error(self, mock_current_user, mock_persistence, mock_request):
        """Test retrieval of professions when database error occurs."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_all_professions.side_effect = Exception("Database connection failed")

        with pytest.raises(HTTPException) as exc_info:
            get_all_professions(mock_current_user, mock_request)

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)

    def test_get_profession_by_id_success(
        self, mock_current_user, sample_profession_data, mock_persistence, mock_request
    ):
        """Test successful retrieval of profession by ID."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_profession_data

        result = get_profession_by_id(0, mock_current_user, mock_request)

        assert result["id"] == 0
        assert result["name"] == "Tramp"
        assert result["description"] == "A wandering soul with no fixed abode"
        assert (
            result["flavor_text"]
            == "You have learned to survive on the streets, finding shelter where you can and making do with what you have."
        )
        assert result["stat_requirements"] == {}
        assert result["mechanical_effects"] == {}
        assert result["is_available"] is True
        mock_persistence.get_profession_by_id.assert_called_once_with(0)

    def test_get_profession_by_id_with_requirements(
        self, mock_current_user, sample_profession_with_requirements, mock_persistence, mock_request
    ):
        """Test successful retrieval of profession with stat requirements."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_profession_with_requirements

        result = get_profession_by_id(2, mock_current_user, mock_request)

        assert result["id"] == 2
        assert result["name"] == "Investigator"
        assert result["stat_requirements"] == {"strength": 12, "intelligence": 14}
        mock_persistence.get_profession_by_id.assert_called_once_with(2)

    def test_get_profession_by_id_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test retrieval of profession when profession not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            get_profession_by_id(999, mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Profession not found" in str(exc_info.value.detail)
        mock_persistence.get_profession_by_id.assert_called_once_with(999)

    def test_get_profession_by_id_database_error(self, mock_current_user, mock_persistence, mock_request):
        """Test retrieval of profession when database error occurs."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.side_effect = Exception("Database connection failed")

        with pytest.raises(HTTPException) as exc_info:
            get_profession_by_id(0, mock_current_user, mock_request)

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)

    def test_get_profession_by_id_invalid_id(self, mock_current_user, mock_persistence, mock_request):
        """Test retrieval of profession with invalid ID format."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            get_profession_by_id("invalid", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Profession not found" in str(exc_info.value.detail)


class TestProfessionDataValidation:
    """Test cases for profession data validation and formatting."""

    def test_profession_response_format(
        self, mock_current_user, sample_profession_data, mock_persistence, mock_request
    ):
        """Test that profession response has correct format."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_profession_data

        result = get_profession_by_id(0, mock_current_user, mock_request)

        # Check required fields are present
        required_fields = [
            "id",
            "name",
            "description",
            "flavor_text",
            "stat_requirements",
            "mechanical_effects",
            "is_available",
        ]
        for field in required_fields:
            assert field in result

        # Check data types
        assert isinstance(result["id"], int)
        assert isinstance(result["name"], str)
        assert isinstance(result["description"], str)
        assert isinstance(result["flavor_text"], str)
        assert isinstance(result["stat_requirements"], dict)
        assert isinstance(result["mechanical_effects"], dict)
        assert isinstance(result["is_available"], bool)

    def test_profession_stat_requirements_json_parsing(
        self, mock_current_user, sample_profession_with_requirements, mock_persistence, mock_request
    ):
        """Test that stat requirements JSON is properly parsed."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_profession_with_requirements

        result = get_profession_by_id(2, mock_current_user, mock_request)

        assert result["stat_requirements"] == {"strength": 12, "intelligence": 14}
        assert isinstance(result["stat_requirements"], dict)

    def test_profession_mechanical_effects_json_parsing(
        self, mock_current_user, sample_profession_data, mock_persistence, mock_request
    ):
        """Test that mechanical effects JSON is properly parsed."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_profession_data

        result = get_profession_by_id(0, mock_current_user, mock_request)

        assert result["mechanical_effects"] == {}
        assert isinstance(result["mechanical_effects"], dict)

    def test_profession_list_response_format(
        self, mock_current_user, sample_profession_data, sample_profession_data_2, mock_persistence, mock_request
    ):
        """Test that profession list response has correct format."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_all_professions.return_value = [sample_profession_data, sample_profession_data_2]

        result = get_all_professions(mock_current_user, mock_request)

        assert "professions" in result
        assert isinstance(result["professions"], list)
        assert len(result["professions"]) == 2

        # Check each profession has required fields
        for profession in result["professions"]:
            required_fields = [
                "id",
                "name",
                "description",
                "flavor_text",
                "stat_requirements",
                "mechanical_effects",
                "is_available",
            ]
            for field in required_fields:
                assert field in profession


class TestProfessionErrorHandling:
    """Test cases for profession API error handling."""

    def test_get_all_professions_persistence_none(self, mock_current_user, mock_request):
        """Test get_all_professions when persistence is None."""
        # Setup mocks
        mock_request.app.state.persistence = None

        with pytest.raises(HTTPException) as exc_info:
            get_all_professions(mock_current_user, mock_request)

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)

    def test_get_profession_by_id_persistence_none(self, mock_current_user, mock_request):
        """Test get_profession_by_id when persistence is None."""
        # Setup mocks
        mock_request.app.state.persistence = None

        with pytest.raises(HTTPException) as exc_info:
            get_profession_by_id(0, mock_current_user, mock_request)

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)

    def test_get_all_professions_authentication_failure(self, mock_request):
        """Test get_all_professions with authentication failure."""
        with pytest.raises(HTTPException) as exc_info:
            get_all_professions(None, mock_request)

        assert exc_info.value.status_code == 401
        assert "Authentication required" in str(exc_info.value.detail)

    def test_get_profession_by_id_authentication_failure(self, mock_request):
        """Test get_profession_by_id with authentication failure."""
        with pytest.raises(HTTPException) as exc_info:
            get_profession_by_id(0, None, mock_request)

        assert exc_info.value.status_code == 401
        assert "Authentication required" in str(exc_info.value.detail)


class TestStrongmanProfession:
    """Test cases specifically for the Strongman profession with stat prerequisites."""

    def test_get_strongman_profession_by_id_success(
        self, mock_current_user, sample_strongman_profession, mock_persistence, mock_request
    ):
        """Test successful retrieval of Strongman profession by ID."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_strongman_profession

        result = get_profession_by_id(2, mock_current_user, mock_request)

        assert result["id"] == 2
        assert result["name"] == "Strongman"
        assert result["description"] == "A physically powerful individual with exceptional strength"
        assert (
            result["flavor_text"]
            == "You have developed your body through years of physical training, making you capable of feats that would challenge lesser mortals."
        )
        assert result["stat_requirements"] == {"strength": 10}
        assert result["mechanical_effects"] == {}
        assert result["is_available"] is True
        mock_persistence.get_profession_by_id.assert_called_once_with(2)

    def test_strongman_profession_stat_requirements_format(
        self, mock_current_user, sample_strongman_profession, mock_persistence, mock_request
    ):
        """Test that Strongman profession stat requirements are properly formatted."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_profession_by_id.return_value = sample_strongman_profession

        result = get_profession_by_id(2, mock_current_user, mock_request)

        # Verify stat requirements are correctly parsed and formatted
        assert result["stat_requirements"] == {"strength": 10}
        assert isinstance(result["stat_requirements"], dict)
        assert "strength" in result["stat_requirements"]
        assert result["stat_requirements"]["strength"] == 10

    def test_strongman_profession_in_profession_list(
        self,
        mock_current_user,
        sample_profession_data,
        sample_profession_data_2,
        sample_strongman_profession,
        mock_persistence,
        mock_request,
    ):
        """Test that Strongman profession appears in profession list."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_all_professions.return_value = [
            sample_profession_data,
            sample_profession_data_2,
            sample_strongman_profession,
        ]

        result = get_all_professions(mock_current_user, mock_request)

        assert "professions" in result
        assert len(result["professions"]) == 3

        # Find the Strongman profession in the list
        strongman_profession = None
        for profession in result["professions"]:
            if profession["id"] == 2 and profession["name"] == "Strongman":
                strongman_profession = profession
                break

        assert strongman_profession is not None
        assert strongman_profession["stat_requirements"] == {"strength": 10}
        mock_persistence.get_all_professions.assert_called_once()
