"""
Unit tests for player_requests schemas.

Tests the Pydantic models in player_requests.py module.
"""

import pytest
from pydantic import ValidationError

from server.schemas.player_requests import (
    CorruptionRequest,
    CreateCharacterRequest,
    DamageRequest,
    FearRequest,
    HealRequest,
    LucidityLossRequest,
    OccultKnowledgeRequest,
    RollStatsRequest,
    SelectCharacterRequest,
)


def test_create_character_request():
    """Test CreateCharacterRequest can be instantiated."""
    request = CreateCharacterRequest(name="TestCharacter", stats={"strength": 50})

    assert request.name == "TestCharacter"
    assert request.stats == {"strength": 50}
    assert request.profession_id == 0


def test_create_character_request_validation():
    """Test CreateCharacterRequest validates name."""
    with pytest.raises(ValidationError):
        CreateCharacterRequest(name="", stats={})


def test_create_character_request_name_stripped():
    """Test CreateCharacterRequest strips whitespace from name."""
    request = CreateCharacterRequest(name="  TestCharacter  ", stats={})

    assert request.name == "TestCharacter"


def test_select_character_request():
    """Test SelectCharacterRequest can be instantiated."""
    request = SelectCharacterRequest(character_id="player_001")

    assert request.character_id == "player_001"


def test_roll_stats_request():
    """Test RollStatsRequest can be instantiated."""
    request = RollStatsRequest()

    assert request.method == "3d6"
    assert request.required_class is None
    assert request.timeout_seconds == 5.0
    assert request.profession_id is None


def test_roll_stats_request_custom():
    """Test RollStatsRequest with custom values."""
    request = RollStatsRequest(method="4d6", required_class="investigator", profession_id=1)

    assert request.method == "4d6"
    assert request.required_class == "investigator"
    assert request.profession_id == 1


def test_lucidity_loss_request():
    """Test LucidityLossRequest can be instantiated."""
    request = LucidityLossRequest(amount=10)

    assert request.amount == 10
    assert request.source == "unknown"


def test_lucidity_loss_request_validation():
    """Test LucidityLossRequest validates amount range."""
    with pytest.raises(ValidationError):
        LucidityLossRequest(amount=101)

    with pytest.raises(ValidationError):
        LucidityLossRequest(amount=-1)


def test_fear_request():
    """Test FearRequest can be instantiated."""
    request = FearRequest(amount=20)

    assert request.amount == 20
    assert request.source == "unknown"


def test_fear_request_validation():
    """Test FearRequest validates amount range."""
    with pytest.raises(ValidationError):
        FearRequest(amount=101)


def test_corruption_request():
    """Test CorruptionRequest can be instantiated."""
    request = CorruptionRequest(amount=15)

    assert request.amount == 15
    assert request.source == "unknown"


def test_corruption_request_validation():
    """Test CorruptionRequest validates amount range."""
    with pytest.raises(ValidationError):
        CorruptionRequest(amount=101)


def test_occult_knowledge_request():
    """Test OccultKnowledgeRequest can be instantiated."""
    request = OccultKnowledgeRequest(amount=25)

    assert request.amount == 25
    assert request.source == "unknown"


def test_occult_knowledge_request_validation():
    """Test OccultKnowledgeRequest validates amount range."""
    with pytest.raises(ValidationError):
        OccultKnowledgeRequest(amount=101)


def test_heal_request():
    """Test HealRequest can be instantiated."""
    request = HealRequest(amount=50)

    assert request.amount == 50


def test_heal_request_validation():
    """Test HealRequest validates amount range."""
    with pytest.raises(ValidationError):
        HealRequest(amount=1001)


def test_damage_request():
    """Test DamageRequest can be instantiated."""
    request = DamageRequest(amount=30)

    assert request.amount == 30
    assert request.damage_type == "physical"


def test_damage_request_custom_type():
    """Test DamageRequest with custom damage type."""
    request = DamageRequest(amount=30, damage_type="magical")

    assert request.damage_type == "magical"


def test_damage_request_validation():
    """Test DamageRequest validates amount range."""
    with pytest.raises(ValidationError):
        DamageRequest(amount=1001)
