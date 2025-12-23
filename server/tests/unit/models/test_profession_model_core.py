"""
Core model tests for professions in MythosMUD.
"""

import json
import os
from collections.abc import Generator

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError, PendingRollbackError, SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from server.models.profession import Profession


class TestProfessionModel:
    """Test the Profession SQLAlchemy model."""

    @pytest.fixture
    def db_session(self) -> Generator[Session, None, None]:
        """Create a PostgreSQL database session for testing."""
        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be set to a PostgreSQL URL.")
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()
        try:
            session.execute(text("DELETE FROM professions WHERE id >= 0"))
            session.commit()
            yield session
        except (SQLAlchemyError, PendingRollbackError):
            # Rollback on database exceptions before cleanup
            session.rollback()
            raise
        except Exception:  # pylint: disable=broad-exception-caught
            # Rollback on any other unexpected exception before cleanup
            # This ensures database state is clean even for unexpected errors
            session.rollback()
            raise
        finally:
            try:
                session.execute(text("DELETE FROM professions WHERE id >= 0"))
                session.commit()
            except (SQLAlchemyError, PendingRollbackError):
                # Rollback if cleanup fails due to database errors
                session.rollback()
            except Exception:  # pylint: disable=broad-exception-caught
                # Rollback if cleanup fails for any other reason
                # This ensures we always attempt cleanup even for unexpected errors
                session.rollback()
            finally:
                session.close()

    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared database state and fixed ID conflicts
    @pytest.mark.xdist_group(name="serial_profession_tests")  # Force serial execution with pytest-xdist
    def test_profession_creation(self, db_session: Session) -> None:
        """Test creating a profession with all required fields."""
        profession = Profession(
            id=0,
            name="Tramp",
            description="A wandering soul",
            flavor_text="Survival on the streets.",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )
        db_session.add(profession)
        db_session.commit()
        saved = db_session.query(Profession).filter_by(id=0).first()
        assert saved is not None
        assert saved.name == "Tramp"

    def test_profession_with_stat_requirements(self, db_session: Session) -> None:
        """Test creating a profession with stat requirements."""
        stat_reqs = json.dumps({"strength": 12})
        profession = Profession(
            id=1,
            name="Scholar",
            description="A learned individual",
            flavor_text="Knowledge is power.",
            stat_requirements=stat_reqs,
            mechanical_effects="{}",
            is_available=True,
        )
        db_session.add(profession)
        db_session.commit()
        saved = db_session.query(Profession).filter_by(id=1).first()
        assert saved is not None
        assert saved.stat_requirements == stat_reqs

    def test_profession_unique_name_constraint(self, db_session: Session) -> None:
        """Test that profession names must be unique."""
        p1 = Profession(
            id=0,
            name="Tramp",
            description="D1",
            flavor_text="F1",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )
        p2 = Profession(
            id=1,
            name="Tramp",
            description="D2",
            flavor_text="F2",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )
        db_session.add(p1)
        db_session.commit()
        db_session.add(p2)
        with pytest.raises(IntegrityError):
            db_session.commit()
