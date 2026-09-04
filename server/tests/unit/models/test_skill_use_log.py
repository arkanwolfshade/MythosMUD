"""Unit tests for SkillUseLog ORM model."""

from datetime import UTC, datetime
from uuid import uuid4

from server.models.skill_use_log import SkillUseLog


def test_skill_use_log_creation() -> None:
    """SkillUseLog can be instantiated with required fields."""
    player_id = uuid4()
    used_at = datetime.now(UTC).replace(tzinfo=None)
    entry = SkillUseLog(
        player_id=player_id,
        skill_id=42,
        character_level_at_use=3,
        used_at=used_at,
    )

    assert entry.player_id == player_id
    assert entry.skill_id == 42
    assert entry.character_level_at_use == 3
    assert entry.used_at == used_at
    assert entry.id is None


def test_skill_use_log_table_name() -> None:
    """SkillUseLog maps to the expected table."""
    assert SkillUseLog.__tablename__ == "skill_use_log"


def test_skill_use_log_repr() -> None:
    """SkillUseLog __repr__ includes key identifiers."""
    player_id = uuid4()
    entry = SkillUseLog(
        id=7,
        player_id=player_id,
        skill_id=99,
        character_level_at_use=5,
        used_at=datetime.now(UTC).replace(tzinfo=None),
    )

    repr_str = repr(entry)
    assert "SkillUseLog" in repr_str
    assert str(player_id) in repr_str
    assert "99" in repr_str
    assert "5" in repr_str
