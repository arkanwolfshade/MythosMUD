"""
Unit tests for target_resolution schemas.

Tests the Pydantic models in target_resolution.py module.
"""

from server.schemas.shared import TargetMatch, TargetResolutionResult, TargetType


def test_target_type_enum():
    """Test TargetType enum values."""
    assert TargetType.PLAYER.value == "player"
    assert TargetType.NPC.value == "npc"
    assert TargetType.ROOM.value == "room"


def test_target_match():
    """Test TargetMatch can be instantiated."""
    match = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )

    assert match.target_id == "player_001"
    assert match.target_name == "TestPlayer"
    assert match.target_type == TargetType.PLAYER
    assert match.room_id == "room_001"
    assert match.disambiguation_suffix is None
    assert match.metadata == {}


def test_target_match_with_disambiguation():
    """Test TargetMatch with disambiguation suffix."""
    match = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
        disambiguation_suffix="-1",
    )

    assert match.disambiguation_suffix == "-1"


def test_target_resolution_result_success():
    """Test TargetResolutionResult with successful resolution."""
    match = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )
    result = TargetResolutionResult(
        success=True,
        matches=[match],
        search_term="test",
        room_id="room_001",
    )

    assert result.success is True
    assert len(result.matches) == 1
    assert result.error_message is None
    assert result.disambiguation_required is False


def test_target_resolution_result_failure():
    """Test TargetResolutionResult with failed resolution."""
    result = TargetResolutionResult(
        success=False,
        matches=[],
        error_message="Target not found",
        search_term="test",
        room_id="room_001",
    )

    assert result.success is False
    assert len(result.matches) == 0
    assert result.error_message == "Target not found"


def test_target_resolution_result_disambiguation():
    """Test TargetResolutionResult with disambiguation required."""
    match1 = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
        disambiguation_suffix="-1",
    )
    match2 = TargetMatch(
        target_id="player_002",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
        disambiguation_suffix="-2",
    )
    result = TargetResolutionResult(
        success=True,
        matches=[match1, match2],
        disambiguation_required=True,
        search_term="test",
        room_id="room_001",
    )

    assert result.disambiguation_required is True
    assert len(result.matches) == 2


def test_get_single_match():
    """Test get_single_match() returns match when exactly one."""
    match = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )
    result = TargetResolutionResult(
        success=True,
        matches=[match],
        search_term="test",
        room_id="room_001",
    )

    single_match = result.get_single_match()
    assert single_match == match


def test_get_single_match_none():
    """Test get_single_match() returns None when multiple matches."""
    match1 = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )
    match2 = TargetMatch(
        target_id="player_002",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )
    result = TargetResolutionResult(
        success=True,
        matches=[match1, match2],
        search_term="test",
        room_id="room_001",
    )

    single_match = result.get_single_match()
    assert single_match is None


def test_get_disambiguation_list():
    """Test get_disambiguation_list() returns list with suffixes."""
    match1 = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
        disambiguation_suffix="-1",
    )
    match2 = TargetMatch(
        target_id="player_002",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
        disambiguation_suffix="-2",
    )
    result = TargetResolutionResult(
        success=True,
        matches=[match1, match2],
        disambiguation_required=True,
        search_term="test",
        room_id="room_001",
    )

    options = result.get_disambiguation_list()
    assert len(options) == 2
    assert "TestPlayer-1" in options
    assert "TestPlayer-2" in options


def test_get_disambiguation_list_empty():
    """Test get_disambiguation_list() returns empty when not required."""
    match = TargetMatch(
        target_id="player_001",
        target_name="TestPlayer",
        target_type=TargetType.PLAYER,
        room_id="room_001",
    )
    result = TargetResolutionResult(
        success=True,
        matches=[match],
        disambiguation_required=False,
        search_term="test",
        room_id="room_001",
    )

    options = result.get_disambiguation_list()
    assert not options
