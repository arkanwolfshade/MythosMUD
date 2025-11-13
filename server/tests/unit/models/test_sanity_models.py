"""Unit tests for sanity persistence models."""

from __future__ import annotations

import uuid
from datetime import datetime

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.models.base import Base
from server.models.player import Player
from server.models.sanity import (
    PlayerSanity,
    SanityAdjustmentLog,
    SanityCooldown,
    SanityExposureState,
)
from server.models.user import User


def build_engine():
    engine = create_engine("sqlite:///:memory:", future=True)
    with engine.begin() as connection:
        connection.exec_driver_sql("PRAGMA foreign_keys=ON")
    return engine


def create_user_and_player(session: Session, player_id: str, username: str) -> Player:
    """Create a basic user/player pair for sanity testing."""
    user = User(
        id=str(uuid.uuid4()),
        email=f"{username}@example.com",
        username=username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=username.capitalize(),
    )
    session.add_all([user, player])
    session.flush()
    return player


def test_player_sanity_defaults_and_constraints():
    engine = build_engine()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        player = create_user_and_player(session, "investigator-1", "arkhamite")

        player_sanity = PlayerSanity()
        player.sanity = player_sanity
        session.commit()

        persisted = session.get(PlayerSanity, "investigator-1")
        assert persisted is not None
        assert persisted.current_san == 100
        assert persisted.current_tier == "lucid"
        assert persisted.liabilities == "[]"

        persisted.current_san = -25
        persisted.current_tier = "uneasy"
        session.commit()

        persisted.current_san = 120
        with pytest.raises(IntegrityError):
            session.flush()
        session.rollback()

        persisted.current_tier = "eldritch"
        with pytest.raises(IntegrityError):
            session.flush()
        session.rollback()

        rogue_sanity = PlayerSanity(player_id="nonexistent")
        session.add(rogue_sanity)
        with pytest.raises(IntegrityError):
            session.flush()
        session.rollback()


def test_sanity_relationships_cascade():
    engine = build_engine()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        player = create_user_and_player(session, "investigator-2", "miskatonic")

        player.sanity = PlayerSanity(current_san=88, current_tier="uneasy")
        player.sanity_adjustments.append(
            SanityAdjustmentLog(
                delta=-12,
                reason_code="eldritch_whispers",
                metadata_payload='{"source":"library"}',
            )
        )
        player.sanity_exposures.append(SanityExposureState(entity_archetype="star_vampire", encounter_count=3))
        player.sanity_cooldowns.append(
            SanityCooldown(
                action_code="pray",
                cooldown_expires_at=datetime.fromisoformat("2099-01-01T00:00:00"),
            )
        )

        session.commit()

        session.delete(player)
        session.commit()

        sanity_rows = session.execute(select(PlayerSanity)).all()
        adjustment_rows = session.execute(select(SanityAdjustmentLog)).all()
        exposure_rows = session.execute(select(SanityExposureState)).all()
        cooldown_rows = session.execute(select(SanityCooldown)).all()

        assert not sanity_rows
        assert not adjustment_rows
        assert not exposure_rows
        assert not cooldown_rows
