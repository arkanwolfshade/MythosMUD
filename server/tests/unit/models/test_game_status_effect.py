"""
Unit tests for StatusEffect model.
"""

from datetime import datetime

import pytest
from pydantic import ValidationError

from server.models.game import StatusEffect, StatusEffectType


def test_status_effect_creation():
    """Test StatusEffect can be created with required fields."""
    effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)

    assert effect.effect_type == StatusEffectType.STUNNED
    assert effect.duration == 10
    assert effect.intensity == 5
    assert effect.source is None
    assert isinstance(effect.applied_at, datetime)


def test_status_effect_with_source():
    """Test StatusEffect can have optional source."""
    effect = StatusEffect(effect_type=StatusEffectType.POISONED, duration=20, intensity=3, source="poison_spell")

    assert effect.source == "poison_spell"


def test_status_effect_is_active_permanent():
    """Test is_active returns True for permanent effects (duration=0)."""
    effect = StatusEffect(effect_type=StatusEffectType.CORRUPTED, duration=0, intensity=1)

    assert effect.is_active(current_tick=0) is True
    assert effect.is_active(current_tick=100) is True
    assert effect.is_active(current_tick=1000) is True


def test_status_effect_is_active_before_duration():
    """Test is_active returns True when current_tick < duration."""
    effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)

    assert effect.is_active(current_tick=0) is True
    assert effect.is_active(current_tick=5) is True
    assert effect.is_active(current_tick=9) is True


def test_status_effect_is_active_at_duration():
    """Test is_active returns False when current_tick >= duration."""
    effect = StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5)

    assert effect.is_active(current_tick=10) is False
    assert effect.is_active(current_tick=11) is False
    assert effect.is_active(current_tick=100) is False


def test_status_effect_duration_validation_min():
    """Test StatusEffect validates duration is >= 0."""
    with pytest.raises(ValidationError):
        StatusEffect(effect_type=StatusEffectType.STUNNED, duration=-1, intensity=5)


def test_status_effect_intensity_validation_min():
    """Test StatusEffect validates intensity is >= 1."""
    with pytest.raises(ValidationError):
        StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=0)


def test_status_effect_intensity_validation_max():
    """Test StatusEffect validates intensity is <= 10."""
    with pytest.raises(ValidationError):
        StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=11)


def test_status_effect_rejects_extra_fields():
    """Test StatusEffect rejects unknown fields (extra='forbid')."""
    with pytest.raises(ValidationError) as exc_info:
        # Reason: Intentionally testing Pydantic validation with extra='forbid' - extra fields should be rejected
        StatusEffect(effect_type=StatusEffectType.STUNNED, duration=10, intensity=5, unknown_field="value")  # type: ignore[call-arg]

    error_str = str(exc_info.value).lower()
    assert "extra" in error_str and ("not permitted" in error_str or "forbidden" in error_str)
