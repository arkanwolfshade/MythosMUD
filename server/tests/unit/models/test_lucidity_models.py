"""
Unit tests for lucidity models.

Tests the PlayerLucidity, LucidityAdjustmentLog, LucidityExposureState, and LucidityCooldown SQLAlchemy models.
"""

from datetime import UTC, datetime
from uuid import uuid4

from server.models.lucidity import (
    LucidityAdjustmentLog,
    LucidityCooldown,
    LucidityExposureState,
    PlayerLucidity,
)

# --- Tests for PlayerLucidity model ---


def test_player_lucidity_creation() -> None:
    """Test PlayerLucidity can be instantiated with required fields."""
    player_id = uuid4()
    lucidity = PlayerLucidity(
        player_id=player_id,
        current_lcd=100,
        current_tier="lucid",
        liabilities="[]",
    )

    assert lucidity.player_id == player_id
    assert lucidity.current_lcd == 100
    assert lucidity.current_tier == "lucid"
    assert lucidity.liabilities == "[]"
    assert lucidity.catatonia_entered_at is None


def test_player_lucidity_defaults() -> None:
    """Test PlayerLucidity has correct default values."""
    player_id = uuid4()
    lucidity = PlayerLucidity(player_id=player_id)

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    # With Mapped types, non-nullable fields have default values applied
    assert lucidity.current_lcd == 100
    assert lucidity.current_tier == "lucid"
    assert lucidity.liabilities == "[]"
    # last_updated_at uses insert_default=func.now(); set at INSERT time, so None until persisted
    assert lucidity.last_updated_at is None or isinstance(lucidity.last_updated_at, datetime)
    assert lucidity.catatonia_entered_at is None


def test_player_lucidity_with_catatonia() -> None:
    """Test PlayerLucidity can have catatonia_entered_at."""
    player_id = uuid4()
    catatonia_time = datetime.now(UTC).replace(tzinfo=None)
    lucidity = PlayerLucidity(
        player_id=player_id,
        current_lcd=-50,
        current_tier="catatonic",
        catatonia_entered_at=catatonia_time,
    )

    assert lucidity.catatonia_entered_at == catatonia_time


def test_player_lucidity_table_name() -> None:
    """Test PlayerLucidity has correct table name."""
    assert PlayerLucidity.__tablename__ == "player_lucidity"


def test_player_lucidity_repr() -> None:
    """Test PlayerLucidity __repr__ method."""
    player_id = uuid4()
    lucidity = PlayerLucidity(player_id=player_id)

    repr_str = repr(lucidity)
    assert "PlayerLucidity" in repr_str


def test_player_lucidity_tiers() -> None:
    """Test PlayerLucidity can have different tiers."""
    tiers = ["lucid", "uneasy", "fractured", "deranged", "catatonic"]

    for tier in tiers:
        lucidity = PlayerLucidity(player_id=uuid4(), current_tier=tier)
        assert lucidity.current_tier == tier


# --- Tests for LucidityAdjustmentLog model ---


def test_lucidity_adjustment_log_creation() -> None:
    """Test LucidityAdjustmentLog can be instantiated with required fields."""
    player_id = uuid4()
    log = LucidityAdjustmentLog(
        player_id=player_id,
        delta=-10,
        reason_code="combat_loss",
        metadata_payload="{}",
    )

    assert log.player_id == player_id
    assert log.delta == -10
    assert log.reason_code == "combat_loss"
    assert log.metadata_payload == "{}"
    assert log.location_id is None
    # created_at uses insert_default=func.now(); set at INSERT time, so None until persisted
    assert log.created_at is None or isinstance(log.created_at, datetime)


def test_lucidity_adjustment_log_with_location() -> None:
    """Test LucidityAdjustmentLog can have optional location_id."""
    player_id = uuid4()
    log = LucidityAdjustmentLog(
        player_id=player_id,
        delta=5,
        reason_code="recovery",
        metadata_payload="{}",
        location_id="room_001",
    )

    assert log.location_id == "room_001"


def test_lucidity_adjustment_log_default_metadata() -> None:
    """Test LucidityAdjustmentLog defaults metadata_payload to '{}'."""
    player_id = uuid4()
    log = LucidityAdjustmentLog(
        player_id=player_id,
        delta=-5,
        reason_code="test",
    )

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    assert log.metadata_payload == "{}"


def test_lucidity_adjustment_log_table_name() -> None:
    """Test LucidityAdjustmentLog has correct table name."""
    assert LucidityAdjustmentLog.__tablename__ == "lucidity_adjustment_log"


def test_lucidity_adjustment_log_repr() -> None:
    """Test LucidityAdjustmentLog __repr__ method."""
    player_id = uuid4()
    log = LucidityAdjustmentLog(
        player_id=player_id,
        delta=-10,
        reason_code="test",
    )

    repr_str = repr(log)
    assert "LucidityAdjustmentLog" in repr_str


def test_lucidity_adjustment_log_positive_delta() -> None:
    """Test LucidityAdjustmentLog can have positive delta (gain)."""
    player_id = uuid4()
    log = LucidityAdjustmentLog(
        player_id=player_id,
        delta=15,
        reason_code="recovery_ritual",
    )

    assert log.delta == 15


def test_lucidity_adjustment_log_negative_delta() -> None:
    """Test LucidityAdjustmentLog can have negative delta (loss)."""
    player_id = uuid4()
    log = LucidityAdjustmentLog(
        player_id=player_id,
        delta=-20,
        reason_code="eldritch_exposure",
    )

    assert log.delta == -20


# --- Tests for LucidityExposureState model ---


def test_lucidity_exposure_state_creation() -> None:
    """Test LucidityExposureState can be instantiated with required fields."""
    player_id = uuid4()
    exposure = LucidityExposureState(
        player_id=player_id,
        entity_archetype="cthulhu",
        encounter_count=3,
    )

    assert exposure.player_id == player_id
    assert exposure.entity_archetype == "cthulhu"
    assert exposure.encounter_count == 3
    # last_encounter_at uses insert_default=func.now(); set at INSERT time, so None until persisted
    assert exposure.last_encounter_at is None or isinstance(exposure.last_encounter_at, datetime)


def test_lucidity_exposure_state_default_encounter_count() -> None:
    """Test LucidityExposureState defaults encounter_count to 0."""
    player_id = uuid4()
    exposure = LucidityExposureState(
        player_id=player_id,
        entity_archetype="shoggoth",
    )

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    assert exposure.encounter_count == 0


def test_lucidity_exposure_state_table_name() -> None:
    """Test LucidityExposureState has correct table name."""
    assert LucidityExposureState.__tablename__ == "lucidity_exposure_state"


def test_lucidity_exposure_state_repr() -> None:
    """Test LucidityExposureState __repr__ method."""
    player_id = uuid4()
    exposure = LucidityExposureState(
        player_id=player_id,
        entity_archetype="deep_one",
    )

    repr_str = repr(exposure)
    assert "LucidityExposureState" in repr_str


def test_lucidity_exposure_state_multiple_archetypes() -> None:
    """Test LucidityExposureState can track multiple archetypes for same player."""
    player_id = uuid4()
    exposure1 = LucidityExposureState(
        player_id=player_id,
        entity_archetype="cthulhu",
        encounter_count=5,
    )
    exposure2 = LucidityExposureState(
        player_id=player_id,
        entity_archetype="nyarlathotep",
        encounter_count=2,
    )

    assert exposure1.entity_archetype != exposure2.entity_archetype
    assert exposure1.encounter_count != exposure2.encounter_count


# --- Tests for LucidityCooldown model ---


def test_lucidity_cooldown_creation() -> None:
    """Test LucidityCooldown can be instantiated with required fields."""
    player_id = uuid4()
    expires_at = datetime.now(UTC).replace(tzinfo=None)
    cooldown = LucidityCooldown(
        player_id=player_id,
        action_code="recovery_ritual",
        cooldown_expires_at=expires_at,
    )

    assert cooldown.player_id == player_id
    assert cooldown.action_code == "recovery_ritual"
    assert cooldown.cooldown_expires_at == expires_at


def test_lucidity_cooldown_table_name() -> None:
    """Test LucidityCooldown has correct table name."""
    assert LucidityCooldown.__tablename__ == "lucidity_cooldowns"


def test_lucidity_cooldown_repr() -> None:
    """Test LucidityCooldown __repr__ method."""
    player_id = uuid4()
    expires_at = datetime.now(UTC).replace(tzinfo=None)
    cooldown = LucidityCooldown(
        player_id=player_id,
        action_code="hallucination_timer",
        cooldown_expires_at=expires_at,
    )

    repr_str = repr(cooldown)
    assert "LucidityCooldown" in repr_str


def test_lucidity_cooldown_different_action_codes() -> None:
    """Test LucidityCooldown can track different action codes for same player."""
    player_id = uuid4()
    expires_at1 = datetime.now(UTC).replace(tzinfo=None)
    expires_at2 = datetime.now(UTC).replace(tzinfo=None)

    cooldown1 = LucidityCooldown(
        player_id=player_id,
        action_code="recovery_ritual",
        cooldown_expires_at=expires_at1,
    )
    cooldown2 = LucidityCooldown(
        player_id=player_id,
        action_code="hallucination_timer",
        cooldown_expires_at=expires_at2,
    )

    assert cooldown1.action_code != cooldown2.action_code
