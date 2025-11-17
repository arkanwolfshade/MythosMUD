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
        """Create a PostgreSQL database session for testing."""
        import os

        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
        # Convert async URL to sync URL for create_engine
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)
        # Professions table should already exist from DDL - no need to create
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
        """Create a PostgreSQL database connection for schema testing."""
        import os

        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
        # Convert async URL to sync URL for create_engine
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)
        # Professions table should already exist from DDL - no need to create
        return engine

    def test_professions_table_creation(self, db_engine):
        """Test that the professions table is created with correct schema."""
        with db_engine.connect() as conn:
            # Check that the table exists (PostgreSQL)
            result = conn.execute(
                text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public' AND table_name = 'professions'
            """)
            )
            table_exists = result.fetchone() is not None
            assert table_exists

            # Check table structure (PostgreSQL)
            result = conn.execute(
                text("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = 'professions'
                ORDER BY ordinal_position
            """)
            )
            columns = result.fetchall()

            column_names = [col[0] for col in columns]
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
                SELECT indexname
                FROM pg_indexes
                WHERE schemaname = 'public'
                AND tablename = 'professions'
                AND indexname = 'idx_professions_available'
            """)
            )
            index_exists = result.fetchone() is not None
            assert index_exists

    def test_professions_table_constraints(self, db_engine):
        """Test that table constraints work correctly."""
        with db_engine.connect() as conn:
            # Test NOT NULL constraints
            with pytest.raises(IntegrityError):  # PostgreSQL raises IntegrityError for NOT NULL violations
                conn.execute(
                    text("""
                    INSERT INTO professions (id, name) VALUES (0, 'Test')
                """)
                )
                conn.commit()  # Commit to trigger the error

            # Test UNIQUE constraint on name
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                VALUES (0, 'Test', 'Description', 'Flavor', '{}', '{}')
            """)
            )
            conn.commit()

            with pytest.raises(IntegrityError):  # PostgreSQL raises IntegrityError for UNIQUE violations
                conn.execute(
                    text("""
                    INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                    VALUES (1, 'Test', 'Description', 'Flavor', '{}', '{}')
                """)
                )
                conn.commit()  # Commit to trigger the error

    def test_professions_default_values(self, db_engine):
        """Test that default values work correctly."""
        with db_engine.connect() as conn:
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                VALUES (0, 'Test', 'Description', 'Flavor', '{}', '{}')
            """)
            )
            conn.commit()

            result = conn.execute(text("SELECT is_available FROM professions WHERE id = 0"))
            is_available = result.fetchone()[0]
            assert is_available is True  # PostgreSQL stores BOOLEAN as boolean


class TestPlayerProfessionIntegration:
    """Test the integration between Player and Profession models."""

    @pytest.fixture
    def db_session_with_professions(self):
        """Create a PostgreSQL database session with professions and players tables."""
        import os

        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
        # Convert async URL to sync URL for create_engine
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)

        # Create professions table (if not exists)
        with engine.connect() as conn:
            conn.execute(
                text("""
                CREATE TABLE IF NOT EXISTS professions (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL UNIQUE,
                    description TEXT NOT NULL,
                    flavor_text TEXT NOT NULL,
                    stat_requirements TEXT NOT NULL,
                    mechanical_effects TEXT NOT NULL,
                    is_available BOOLEAN NOT NULL DEFAULT TRUE
                )
            """)
            )
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available)"))

            # Insert test professions (using ON CONFLICT to handle existing data)
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects)
                VALUES
                (0, 'Tramp', 'A wandering soul', 'Test flavor', '{}', '{}'),
                (1, 'Gutter Rat', 'A street survivor', 'Test flavor', '{}', '{}')
                ON CONFLICT (id) DO UPDATE SET
                    name = EXCLUDED.name,
                    description = EXCLUDED.description,
                    flavor_text = EXCLUDED.flavor_text,
                    stat_requirements = EXCLUDED.stat_requirements,
                    mechanical_effects = EXCLUDED.mechanical_effects
            """)
            )
            conn.commit()

        # Create players table (simplified for testing, if not exists)
        with engine.connect() as conn:
            conn.execute(
                text("""
                CREATE TABLE IF NOT EXISTS players (
                    player_id VARCHAR(255) PRIMARY KEY,
                    user_id VARCHAR(255) NOT NULL,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    profession_id INTEGER NOT NULL DEFAULT 0,
                    stats TEXT NOT NULL DEFAULT '{}',
                    created_at TIMESTAMP NOT NULL DEFAULT NOW()
                )
            """)
            )
            conn.commit()

        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            yield session
        finally:
            # Clean up test data
            try:
                session.execute(text("DELETE FROM players WHERE player_id LIKE 'test_%' OR player_id LIKE 'player_%'"))
                session.commit()
            except Exception:
                pass
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


class TestProfessionHelperMethods:
    """Test Profession model helper methods."""

    @pytest.fixture
    def db_session(self):
        """Create a PostgreSQL database session for testing."""
        import os

        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
        # Convert async URL to sync URL for create_engine
        sync_url = database_url.replace("+asyncpg", "")
        engine = create_engine(sync_url, echo=False)
        from server.metadata import metadata

        metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            yield session
        finally:
            # Clean up test data
            try:
                session.execute(text("DELETE FROM professions WHERE id >= 0"))
                session.commit()
            except Exception:
                pass
            session.close()

    def test_get_stat_requirements_valid_json(self, db_session):
        """Test get_stat_requirements with valid JSON."""
        # Arrange
        requirements = {"strength": 12, "intelligence": 10}
        profession = Profession(
            id=0,
            name="Scholar",
            description="A learned individual",
            flavor_text="Knowledge is power",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_stat_requirements()

        # Assert
        assert result == requirements

    def test_get_stat_requirements_invalid_json(self, db_session):
        """Test get_stat_requirements with invalid JSON returns empty dict."""
        # Arrange
        profession = Profession(
            id=0,
            name="Scholar",
            description="A learned individual",
            flavor_text="Knowledge",
            stat_requirements="invalid json{",
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_stat_requirements()

        # Assert
        assert result == {}

    def test_get_stat_requirements_none_value(self, db_session):
        """Test get_stat_requirements with None value returns empty dict."""
        # Arrange
        profession = Profession(
            id=0,
            name="Scholar",
            description="A learned individual",
            flavor_text="Knowledge",
            mechanical_effects="{}",
        )
        # Manually set to None to simulate edge case
        profession.stat_requirements = None

        # Act
        result = profession.get_stat_requirements()

        # Assert
        assert result == {}

    def test_set_stat_requirements(self, db_session):
        """Test set_stat_requirements stores requirements as JSON."""
        # Arrange
        profession = Profession(
            id=0,
            name="Warrior",
            description="A fighter",
            flavor_text="Strength",
            stat_requirements="{}",
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        new_requirements = {"strength": 15, "constitution": 14}
        profession.set_stat_requirements(new_requirements)
        db_session.commit()

        # Assert
        assert profession.stat_requirements == json.dumps(new_requirements)
        assert profession.get_stat_requirements() == new_requirements

    def test_get_mechanical_effects_valid_json(self, db_session):
        """Test get_mechanical_effects with valid JSON."""
        # Arrange
        effects = {"combat_bonus": 2, "magic_bonus": 1}
        profession = Profession(
            id=0,
            name="Mage",
            description="A spellcaster",
            flavor_text="Magic",
            stat_requirements="{}",
            mechanical_effects=json.dumps(effects),
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_mechanical_effects()

        # Assert
        assert result == effects

    def test_get_mechanical_effects_invalid_json(self, db_session):
        """Test get_mechanical_effects with invalid JSON returns empty dict."""
        # Arrange
        profession = Profession(
            id=0,
            name="Mage",
            description="A spellcaster",
            flavor_text="Magic",
            stat_requirements="{}",
            mechanical_effects="invalid json{",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_mechanical_effects()

        # Assert
        assert result == {}

    def test_set_mechanical_effects(self, db_session):
        """Test set_mechanical_effects stores effects as JSON."""
        # Arrange
        profession = Profession(
            id=0,
            name="Warrior",
            description="A fighter",
            flavor_text="Strength",
            stat_requirements="{}",
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        new_effects = {"damage_bonus": 3, "armor_bonus": 2}
        profession.set_mechanical_effects(new_effects)
        db_session.commit()

        # Assert
        assert profession.mechanical_effects == json.dumps(new_effects)
        assert profession.get_mechanical_effects() == new_effects

    def test_meets_stat_requirements_all_met(self, db_session):
        """Test meets_stat_requirements when all requirements are met."""
        # Arrange
        requirements = {"strength": 12, "intelligence": 10}
        profession = Profession(
            id=0,
            name="Scholar",
            description="Learned",
            flavor_text="Knowledge",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        player_stats = {"strength": 15, "intelligence": 12, "wisdom": 10}

        # Act
        result = profession.meets_stat_requirements(player_stats)

        # Assert
        assert result is True

    def test_meets_stat_requirements_not_met(self, db_session):
        """Test meets_stat_requirements when requirements are not met."""
        # Arrange
        requirements = {"strength": 12, "intelligence": 10}
        profession = Profession(
            id=0,
            name="Scholar",
            description="Learned",
            flavor_text="Knowledge",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        player_stats = {"strength": 8, "intelligence": 12}  # strength too low

        # Act
        result = profession.meets_stat_requirements(player_stats)

        # Assert
        assert result is False

    def test_meets_stat_requirements_exact_match(self, db_session):
        """Test meets_stat_requirements with exact stat match."""
        # Arrange
        requirements = {"strength": 12, "intelligence": 10}
        profession = Profession(
            id=0,
            name="Scholar",
            description="Learned",
            flavor_text="Knowledge",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        player_stats = {"strength": 12, "intelligence": 10}  # Exact match

        # Act
        result = profession.meets_stat_requirements(player_stats)

        # Assert
        assert result is True

    def test_meets_stat_requirements_missing_stat_defaults_to_zero(self, db_session):
        """Test meets_stat_requirements when player missing a required stat."""
        # Arrange
        requirements = {"strength": 12}
        profession = Profession(
            id=0,
            name="Warrior",
            description="Fighter",
            flavor_text="Strength",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        player_stats = {"intelligence": 15}  # Missing strength stat

        # Act
        result = profession.meets_stat_requirements(player_stats)

        # Assert
        assert result is False  # 0 < 12

    def test_meets_stat_requirements_no_requirements(self, db_session):
        """Test meets_stat_requirements with no requirements."""
        # Arrange
        profession = Profession(
            id=0,
            name="Tramp",
            description="No requirements",
            flavor_text="Freedom",
            stat_requirements="{}",
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        player_stats = {"strength": 5, "intelligence": 5}

        # Act
        result = profession.meets_stat_requirements(player_stats)

        # Assert
        assert result is True  # No requirements means always passes

    def test_is_available_for_selection_true(self, db_session):
        """Test is_available_for_selection when available."""
        # Arrange
        profession = Profession(
            id=0,
            name="Warrior",
            description="Fighter",
            flavor_text="Strength",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=True,
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.is_available_for_selection()

        # Assert
        assert result is True

    def test_is_available_for_selection_false(self, db_session):
        """Test is_available_for_selection when not available."""
        # Arrange
        profession = Profession(
            id=0,
            name="Warrior",
            description="Fighter",
            flavor_text="Strength",
            stat_requirements="{}",
            mechanical_effects="{}",
            is_available=False,
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.is_available_for_selection()

        # Assert
        assert result is False

    def test_get_requirement_display_text_no_requirements(self, db_session):
        """Test get_requirement_display_text with no requirements."""
        # Arrange
        profession = Profession(
            id=0,
            name="Tramp",
            description="No requirements",
            flavor_text="Freedom",
            stat_requirements="{}",
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_requirement_display_text()

        # Assert
        assert result == "No requirements"

    def test_get_requirement_display_text_single_requirement(self, db_session):
        """Test get_requirement_display_text with single requirement."""
        # Arrange
        requirements = {"strength": 12}
        profession = Profession(
            id=0,
            name="Warrior",
            description="Fighter",
            flavor_text="Strength",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_requirement_display_text()

        # Assert
        assert result == "Minimum: Strength 12"

    def test_get_requirement_display_text_multiple_requirements(self, db_session):
        """Test get_requirement_display_text with multiple requirements."""
        # Arrange
        requirements = {"strength": 12, "intelligence": 10, "wisdom": 8}
        profession = Profession(
            id=0,
            name="Paladin",
            description="Holy warrior",
            flavor_text="Faith and steel",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_requirement_display_text()

        # Assert
        assert result.startswith("Minimum: ")
        assert "Strength 12" in result
        assert "Intelligence 10" in result
        assert "Wisdom 8" in result

    def test_get_requirement_display_text_capitalization(self, db_session):
        """Test that stat names are properly capitalized in display text."""
        # Arrange
        requirements = {"occult_knowledge": 15}
        profession = Profession(
            id=0,
            name="Cultist",
            description="Dark practitioner",
            flavor_text="Forbidden knowledge",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
        )
        db_session.add(profession)
        db_session.commit()

        # Act
        result = profession.get_requirement_display_text()

        # Assert
        assert result == "Minimum: Occult_knowledge 15"  # capitalize() only caps first letter
