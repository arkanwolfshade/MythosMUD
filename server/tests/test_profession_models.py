"""
Tests for profession models and database schema.

This module tests the Profession SQLAlchemy model and related database functionality
for the profession system feature.
"""

import json

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

# Import the profession model (will be created)
from server.models.profession import Profession


class TestProfessionModel:
    """Test the Profession SQLAlchemy model."""

    @pytest.fixture
    def db_session(self):
        """Create an in-memory SQLite database for testing."""
        engine = create_engine("sqlite:///:memory:", echo=False)

        # Create tables
        from server.metadata import metadata

        metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
        session.close()

    def test_profession_creation(self, db_session):
        """Test creating a profession with all required fields."""
        profession = Profession(
            id=0,
            name="Tramp",
            description="A wandering soul with no fixed abode",
            flavor_text="You have learned to survive on the streets, finding shelter where you can and making do with what you have.",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )

        db_session.add(profession)
        db_session.commit()

        # Verify the profession was created
        saved_profession = db_session.query(Profession).filter_by(id=0).first()
        assert saved_profession is not None
        assert saved_profession.name == "Tramp"
        assert saved_profession.description == "A wandering soul with no fixed abode"
        assert (
            saved_profession.flavor_text
            == "You have learned to survive on the streets, finding shelter where you can and making do with what you have."
        )
        assert saved_profession.stat_requirements == "{}"
        assert saved_profession.mechanical_effects == "{}"
        assert saved_profession.is_available is True

    def test_profession_with_stat_requirements(self, db_session):
        """Test creating a profession with stat requirements."""
        stat_reqs = json.dumps({"strength": 12, "intelligence": 10})
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

        saved_profession = db_session.query(Profession).filter_by(id=1).first()
        assert saved_profession.stat_requirements == stat_reqs

        # Test parsing the JSON
        requirements = json.loads(saved_profession.stat_requirements)
        assert requirements["strength"] == 12
        assert requirements["intelligence"] == 10

    def test_profession_with_mechanical_effects(self, db_session):
        """Test creating a profession with mechanical effects."""
        effects = json.dumps({"combat_bonus": 2, "social_bonus": 1})
        profession = Profession(
            id=2,
            name="Warrior",
            description="A skilled fighter",
            flavor_text="Strength through combat.",
            stat_requirements="{}",
            mechanical_effects=effects,
            is_available=True,
        )

        db_session.add(profession)
        db_session.commit()

        saved_profession = db_session.query(Profession).filter_by(id=2).first()
        assert saved_profession.mechanical_effects == effects

        # Test parsing the JSON
        mechanical_effects = json.loads(saved_profession.mechanical_effects)
        assert mechanical_effects["combat_bonus"] == 2
        assert mechanical_effects["social_bonus"] == 1

    def test_profession_unique_name_constraint(self, db_session):
        """Test that profession names must be unique."""
        profession1 = Profession(
            id=0,
            name="Tramp",
            description="A wandering soul",
            flavor_text="Test flavor",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )

        profession2 = Profession(
            id=1,
            name="Tramp",  # Same name
            description="Another wandering soul",
            flavor_text="Test flavor 2",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )

        db_session.add(profession1)
        db_session.commit()

        # Adding a second profession with the same name should fail
        db_session.add(profession2)
        with pytest.raises(IntegrityError):
            db_session.commit()

    def test_profession_default_values(self, db_session):
        """Test that profession has correct default values."""
        profession = Profession(
            id=0,
            name="Test Profession",
            description="A test profession",
            flavor_text="Test flavor text",
            stat_requirements="{}",
            mechanical_effects="{}",
            # is_available not specified, should default to True
        )

        db_session.add(profession)
        db_session.commit()

        saved_profession = db_session.query(Profession).filter_by(id=0).first()
        assert saved_profession.is_available is True

    def test_profession_availability_filtering(self, db_session):
        """Test filtering professions by availability."""
        # Create available profession
        available_profession = Profession(
            id=0,
            name="Available",
            description="Available profession",
            flavor_text="Test",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )

        # Create unavailable profession
        unavailable_profession = Profession(
            id=1,
            name="Unavailable",
            description="Unavailable profession",
            flavor_text="Test",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=False,
        )

        db_session.add_all([available_profession, unavailable_profession])
        db_session.commit()

        # Test filtering by availability
        available_professions = db_session.query(Profession).filter_by(is_available=True).all()
        assert len(available_professions) == 1
        assert available_professions[0].name == "Available"

        unavailable_professions = db_session.query(Profession).filter_by(is_available=False).all()
        assert len(unavailable_professions) == 1
        assert unavailable_professions[0].name == "Unavailable"

    def test_profession_string_representation(self, db_session):
        """Test the string representation of a profession."""
        profession = Profession(
            id=0,
            name="Test Profession",
            description="A test profession",
            flavor_text="Test flavor text",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )

        db_session.add(profession)
        db_session.commit()

        saved_profession = db_session.query(Profession).filter_by(id=0).first()
        expected_repr = "<Profession(id=0, name='Test Profession', is_available=True)>"
        assert repr(saved_profession) == expected_repr


class TestProfessionDatabaseSchema:
    """Test the profession database schema and constraints."""

    @pytest.fixture
    def db_engine(self):
        """Create an in-memory SQLite database for schema testing."""
        engine = create_engine("sqlite:///:memory:", echo=False)

        # Create the professions table
        with engine.connect() as conn:
            conn.execute(
                text("""
                CREATE TABLE professions (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT NOT NULL,
                    flavor_text TEXT NOT NULL,
                    stat_requirements TEXT NOT NULL,
                    mechanical_effects TEXT NOT NULL,
                    is_available BOOLEAN NOT NULL DEFAULT 1
                )
            """)
            )
            conn.execute(text("CREATE INDEX idx_professions_available ON professions(is_available)"))
            conn.commit()

        return engine

    def test_professions_table_creation(self, db_engine):
        """Test that the professions table is created with correct schema."""
        with db_engine.connect() as conn:
            # Check that the table exists
            result = conn.execute(
                text("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='professions'
            """)
            )
            table_exists = result.fetchone() is not None
            assert table_exists

            # Check table structure
            result = conn.execute(text("PRAGMA table_info(professions)"))
            columns = result.fetchall()

            column_names = [col[1] for col in columns]
            expected_columns = [
                "id",
                "name",
                "description",
                "flavor_text",
                "stat_requirements",
                "mechanical_effects",
                "is_available",
            ]

            for expected_col in expected_columns:
                assert expected_col in column_names

    def test_professions_index_creation(self, db_engine):
        """Test that the availability index is created."""
        with db_engine.connect() as conn:
            result = conn.execute(
                text("""
                SELECT name FROM sqlite_master
                WHERE type='index' AND name='idx_professions_available'
            """)
            )
            index_exists = result.fetchone() is not None
            assert index_exists

    def test_professions_table_constraints(self, db_engine):
        """Test that table constraints work correctly."""
        with db_engine.connect() as conn:
            # Test NOT NULL constraints
            with pytest.raises(IntegrityError):  # SQLite raises IntegrityError for NOT NULL violations
                conn.execute(
                    text("""
                    INSERT INTO professions (id, name) VALUES (0, 'Test')
                """)
                )

            # Test UNIQUE constraint on name
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                VALUES (0, 'Test', 'Description', 'Flavor', '{}', '{}')
            """)
            )

            with pytest.raises(IntegrityError):  # SQLite raises IntegrityError for UNIQUE violations
                conn.execute(
                    text("""
                    INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                    VALUES (1, 'Test', 'Description', 'Flavor', '{}', '{}')
                """)
                )

            conn.commit()

    def test_professions_default_values(self, db_engine):
        """Test that default values work correctly."""
        with db_engine.connect() as conn:
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                VALUES (0, 'Test', 'Description', 'Flavor', '{}', '{}')
            """)
            )

            result = conn.execute(text("SELECT is_available FROM professions WHERE id = 0"))
            is_available = result.fetchone()[0]
            assert is_available == 1  # SQLite stores BOOLEAN as INTEGER


class TestPlayerProfessionIntegration:
    """Test the integration between Player and Profession models."""

    @pytest.fixture
    def db_session_with_professions(self):
        """Create a database session with professions table."""
        engine = create_engine("sqlite:///:memory:", echo=False)

        # Create professions table
        with engine.connect() as conn:
            conn.execute(
                text("""
                CREATE TABLE professions (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT NOT NULL,
                    flavor_text TEXT NOT NULL,
                    stat_requirements TEXT NOT NULL,
                    mechanical_effects TEXT NOT NULL,
                    is_available BOOLEAN NOT NULL DEFAULT 1
                )
            """)
            )
            conn.execute(text("CREATE INDEX idx_professions_available ON professions(is_available)"))

            # Insert test professions
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                VALUES
                (0, 'Tramp', 'A wandering soul', 'Test flavor', '{}', '{}'),
                (1, 'Gutter Rat', 'A street survivor', 'Test flavor', '{}', '{}')
            """)
            )
            conn.commit()

        # Create players table (simplified for testing)
        with engine.connect() as conn:
            conn.execute(
                text("""
                CREATE TABLE players (
                    player_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    name TEXT UNIQUE NOT NULL,
                    profession_id INTEGER NOT NULL DEFAULT 0,
                    stats TEXT NOT NULL DEFAULT '{}',
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            """)
            )
            conn.commit()

        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
        session.close()

    def test_player_with_profession_id(self, db_session_with_professions):
        """Test that a player can have a profession_id."""
        # Insert a test player with profession_id
        db_session_with_professions.execute(
            text("""
            INSERT INTO players (player_id, user_id, name, profession_id, stats)
            VALUES ('test_player_1', 'test_user_1', 'TestPlayer', 1, '{}')
        """)
        )
        db_session_with_professions.commit()

        # Verify the player was created with profession_id
        result = db_session_with_professions.execute(
            text("""
            SELECT profession_id FROM players WHERE player_id = 'test_player_1'
        """)
        )
        profession_id = result.fetchone()[0]
        assert profession_id == 1

    def test_player_default_profession_id(self, db_session_with_professions):
        """Test that a player defaults to profession_id 0."""
        # Insert a test player without specifying profession_id
        db_session_with_professions.execute(
            text("""
            INSERT INTO players (player_id, user_id, name, stats)
            VALUES ('test_player_2', 'test_user_2', 'TestPlayer2', '{}')
        """)
        )
        db_session_with_professions.commit()

        # Verify the player defaults to profession_id 0
        result = db_session_with_professions.execute(
            text("""
            SELECT profession_id FROM players WHERE player_id = 'test_player_2'
        """)
        )
        profession_id = result.fetchone()[0]
        assert profession_id == 0

    def test_profession_player_relationship(self, db_session_with_professions):
        """Test the relationship between professions and players."""
        # Insert test players with different professions
        db_session_with_professions.execute(
            text("""
            INSERT INTO players (player_id, user_id, name, profession_id, stats)
            VALUES
            ('player_1', 'user_1', 'Player1', 0, '{}'),
            ('player_2', 'user_2', 'Player2', 1, '{}')
        """)
        )
        db_session_with_professions.commit()

        # Test querying players by profession
        result = db_session_with_professions.execute(
            text("""
            SELECT p.name, pr.name as profession_name
            FROM players p
            JOIN professions pr ON p.profession_id = pr.id
            WHERE p.profession_id = 0
        """)
        )
        players_with_tramp = result.fetchall()
        assert len(players_with_tramp) == 1
        assert players_with_tramp[0][0] == "Player1"
        assert players_with_tramp[0][1] == "Tramp"

        result = db_session_with_professions.execute(
            text("""
            SELECT p.name, pr.name as profession_name
            FROM players p
            JOIN professions pr ON p.profession_id = pr.id
            WHERE p.profession_id = 1
        """)
        )
        players_with_gutter_rat = result.fetchall()
        assert len(players_with_gutter_rat) == 1
        assert players_with_gutter_rat[0][0] == "Player2"
        assert players_with_gutter_rat[0][1] == "Gutter Rat"
