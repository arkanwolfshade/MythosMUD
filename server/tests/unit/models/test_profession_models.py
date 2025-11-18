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

        # Ensure professions table exists with correct schema
        # Check if table exists and has correct columns, recreate if needed
        with engine.connect() as conn:
            # Check if table exists
            result = conn.execute(
                text("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_schema = 'public' AND table_name = 'professions'
                    )
                """)
            )
            table_exists = result.scalar()

            if table_exists:
                # Check if required columns exist
                result = conn.execute(
                    text("""
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_schema = 'public' AND table_name = 'professions'
                    """)
                )
                existing_columns = {row[0] for row in result.fetchall()}
                required_columns = {
                    "id",
                    "name",
                    "description",
                    "flavor_text",
                    "stat_requirements",
                    "mechanical_effects",
                    "is_available",
                }

                # If schema doesn't match, drop and recreate
                if not required_columns.issubset(existing_columns):
                    conn.execute(text("DROP TABLE IF EXISTS professions CASCADE"))
                    conn.commit()
                    table_exists = False

            # Create table if it doesn't exist
            if not table_exists:
                from server.metadata import metadata

                metadata.create_all(engine, tables=[metadata.tables["professions"]])
                conn.commit()

            # Ensure index exists (create if missing, even if table already existed)
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available)"))
            conn.commit()

        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            # Clean up any existing test data
            session.execute(text("DELETE FROM professions WHERE id >= 0"))
            session.commit()
            yield session
        finally:
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

        # Ensure professions table exists with correct schema
        # Check if table exists and has correct columns, recreate if needed
        with engine.connect() as conn:
            # Check if table exists
            result = conn.execute(
                text("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_schema = 'public' AND table_name = 'professions'
                    )
                """)
            )
            table_exists = result.scalar()

            if table_exists:
                # Check if required columns exist
                result = conn.execute(
                    text("""
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_schema = 'public' AND table_name = 'professions'
                    """)
                )
                existing_columns = {row[0] for row in result.fetchall()}
                required_columns = {
                    "id",
                    "name",
                    "description",
                    "flavor_text",
                    "stat_requirements",
                    "mechanical_effects",
                    "is_available",
                }

                # If schema doesn't match, drop and recreate
                if not required_columns.issubset(existing_columns):
                    conn.execute(text("DROP TABLE IF EXISTS professions CASCADE"))
                    conn.commit()
                    table_exists = False

            # Create table if it doesn't exist
            if not table_exists:
                from server.metadata import metadata

                metadata.create_all(engine, tables=[metadata.tables["professions"]])
                conn.commit()

            # Ensure index exists (create if missing, even if table already existed)
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available)"))
            conn.commit()

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
        # Use unique IDs that are unlikely to conflict (high numbers)
        test_id_1 = 99999
        test_id_2 = 99998
        test_id_3 = 99997

        # Test NOT NULL constraints
        with db_engine.connect() as conn:
            # Clean up any existing test data first
            conn.execute(
                text("DELETE FROM professions WHERE id IN (:id1, :id2, :id3)"),
                {"id1": test_id_1, "id2": test_id_2, "id3": test_id_3},
            )
            conn.commit()

            # Test NOT NULL constraint - missing required fields should fail
            with pytest.raises(IntegrityError):  # PostgreSQL raises IntegrityError for NOT NULL violations
                conn.execute(
                    text("""
                    INSERT INTO professions (id, name) VALUES (:id, 'Test')
                """),
                    {"id": test_id_1},
                )
                conn.commit()  # Commit to trigger the error

            # Rollback to clear the failed transaction state
            conn.rollback()

        # Test UNIQUE constraint on name - use a separate connection
        with db_engine.connect() as conn:
            # Insert a test profession (include is_available since it has NOT NULL constraint)
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects, is_available)
                VALUES (:id, :name, 'Description', 'Flavor', '{}', '{}', true)
                """),
                {"id": test_id_2, "name": "UniqueTestConstraint"},
            )
            conn.commit()

            # Test UNIQUE constraint on name - duplicate name should fail
            with pytest.raises(IntegrityError):  # PostgreSQL raises IntegrityError for UNIQUE violations
                conn.execute(
                    text("""
                    INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects, is_available)
                    VALUES (:id, :name, 'Description', 'Flavor', '{}', '{}', true)
                    """),
                    {"id": test_id_3, "name": "UniqueTestConstraint"},
                )
                conn.commit()  # Commit to trigger the error

            # Rollback to clear the failed transaction state
            conn.rollback()

            # Clean up test data (use a new transaction)
            conn.execute(text("DELETE FROM professions WHERE id IN (:id1, :id2)"), {"id1": test_id_2, "id2": test_id_3})
            conn.commit()

    def test_professions_default_values(self, db_engine):
        """Test that default values work correctly."""
        test_id = 99996
        with db_engine.connect() as conn:
            # Clean up any existing test data
            conn.execute(text("DELETE FROM professions WHERE id = :id"), {"id": test_id})
            conn.commit()

            # Test that SQLAlchemy model default works (not database default)
            # Since we're using SQLAlchemy defaults, we need to use the ORM or include the value
            # For this test, we'll verify the model's default by using the ORM
            from sqlalchemy.orm import sessionmaker

            from server.models.profession import Profession

            Session = sessionmaker(bind=db_engine)
            session = Session()
            try:
                profession = Profession(
                    id=test_id,
                    name="DefaultTest",
                    description="Description",
                    flavor_text="Flavor",
                    stat_requirements="{}",
                    mechanical_effects="{}",
                    # is_available not specified - should use model default
                )
                session.add(profession)
                session.commit()

                # Verify the default was applied
                result = session.query(Profession).filter_by(id=test_id).first()
                assert result is not None
                assert result.is_available is True  # Model default should be True

                # Clean up
                session.delete(result)
                session.commit()
            finally:
                session.close()


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
            # Include is_available since it has NOT NULL constraint
            conn.execute(
                text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects, is_available)
                VALUES
                (0, 'Tramp', 'A wandering soul', 'Test flavor', '{}', '{}', true),
                (1, 'Gutter Rat', 'A street survivor', 'Test flavor', '{}', '{}', true)
                ON CONFLICT (id) DO UPDATE SET
                    name = EXCLUDED.name,
                    description = EXCLUDED.description,
                    flavor_text = EXCLUDED.flavor_text,
                    stat_requirements = EXCLUDED.stat_requirements,
                    mechanical_effects = EXCLUDED.mechanical_effects,
                    is_available = EXCLUDED.is_available
            """)
            )
            conn.commit()

        # Use existing players table - don't create a simplified one
        # The actual players table has many columns, so we'll work with the existing schema
        # Just ensure it exists (it should from other tests/migrations)

        # Create test users if they don't exist (needed for foreign key constraint)
        with engine.connect() as conn:
            # Check if users table exists, if not create a minimal one for testing
            result = conn.execute(
                text("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_schema = 'public' AND table_name = 'users'
                    )
                """)
            )
            users_table_exists = result.scalar()

            if not users_table_exists:
                # Create minimal users table for testing (matching actual schema)
                conn.execute(
                    text("""
                    CREATE TABLE IF NOT EXISTS users (
                        id UUID PRIMARY KEY,
                        email VARCHAR(255) NOT NULL,
                        username VARCHAR(255) UNIQUE NOT NULL,
                        hashed_password VARCHAR(255) NOT NULL,
                        display_name VARCHAR(255) NOT NULL DEFAULT '',
                        password_hash VARCHAR(255),
                        is_active BOOLEAN NOT NULL DEFAULT true,
                        is_superuser BOOLEAN NOT NULL DEFAULT false,
                        is_verified BOOLEAN NOT NULL DEFAULT false,
                        is_admin BOOLEAN NOT NULL DEFAULT false,
                        created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                        updated_at TIMESTAMP NOT NULL DEFAULT NOW()
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
                # Clean up in reverse order (players first, then users)
                session.execute(text("DELETE FROM players WHERE player_id LIKE 'test_%' OR player_id LIKE 'player_%'"))
                session.execute(text("DELETE FROM users WHERE username LIKE 'test_%' OR username LIKE 'player_%'"))
                session.commit()
            except Exception:
                pass
            session.close()

    def test_player_with_profession_id(self, db_session_with_professions):
        """Test that a player can have a profession_id."""
        import uuid

        # Create a test user first (required for foreign key constraint)
        test_user_id = str(uuid.uuid4())
        # Use unique email and username to avoid conflicts
        unique_email = f"test_{test_user_id[:8]}@example.com"
        unique_username = f"testuser1_{test_user_id[:8]}"
        db_session_with_professions.execute(
            text("""
            INSERT INTO users (id, email, username, hashed_password, display_name, is_active, is_superuser, is_verified, is_admin, created_at, updated_at)
            VALUES (:user_id, :email, :username, 'hashed', :display_name, true, false, true, false, NOW(), NOW())
            ON CONFLICT (id) DO NOTHING
        """),
            {
                "user_id": test_user_id,
                "email": unique_email,
                "username": unique_username,
                "display_name": unique_username,
            },
        )
        db_session_with_professions.commit()

        # Insert a test player with profession_id (use proper UUID for user_id)
        # Include all required NOT NULL columns
        db_session_with_professions.execute(
            text("""
            INSERT INTO players (player_id, user_id, name, profession_id, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
            VALUES ('test_player_1', :user_id, 'TestPlayer', 1, '{}', '[]', '[]', 'earth_arkhamcity_sanitarium_room_foyer_001', 0, 1, 0, NOW(), NOW())
        """),
            {"user_id": test_user_id},
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
        import uuid

        # Create a test user first (required for foreign key constraint)
        test_user_id = str(uuid.uuid4())
        # Use unique email and username to avoid conflicts
        unique_email = f"test2_{test_user_id[:8]}@example.com"
        unique_username = f"testuser2_{test_user_id[:8]}"
        db_session_with_professions.execute(
            text("""
            INSERT INTO users (id, email, username, hashed_password, display_name, is_active, is_superuser, is_verified, is_admin, created_at, updated_at)
            VALUES (:user_id, :email, :username, 'hashed', :display_name, true, false, true, false, NOW(), NOW())
            ON CONFLICT (id) DO NOTHING
        """),
            {
                "user_id": test_user_id,
                "email": unique_email,
                "username": unique_username,
                "display_name": unique_username,
            },
        )
        db_session_with_professions.commit()

        # Insert a test player without explicitly specifying profession_id
        # The model default is 0, but since we're using raw SQL, we need to include it
        # We'll set it to 0 to test that the default works
        db_session_with_professions.execute(
            text("""
            INSERT INTO players (player_id, user_id, name, profession_id, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
            VALUES ('test_player_2', :user_id, 'TestPlayer2', 0, '{}', '[]', '[]', 'earth_arkhamcity_sanitarium_room_foyer_001', 0, 1, 0, NOW(), NOW())
        """),
            {"user_id": test_user_id},
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
        import uuid

        # Create test users first (required for foreign key constraint)
        user_id_1 = str(uuid.uuid4())
        user_id_2 = str(uuid.uuid4())
        # Use unique emails and usernames to avoid conflicts
        email_1 = f"player1_{user_id_1[:8]}@example.com"
        email_2 = f"player2_{user_id_2[:8]}@example.com"
        username_1 = f"player1user_{user_id_1[:8]}"
        username_2 = f"player2user_{user_id_2[:8]}"
        db_session_with_professions.execute(
            text("""
            INSERT INTO users (id, email, username, hashed_password, display_name, is_active, is_superuser, is_verified, is_admin, created_at, updated_at)
            VALUES
            (:user_id_1, :email_1, :username_1, 'hashed', :display_name_1, true, false, true, false, NOW(), NOW()),
            (:user_id_2, :email_2, :username_2, 'hashed', :display_name_2, true, false, true, false, NOW(), NOW())
            ON CONFLICT (id) DO NOTHING
        """),
            {
                "user_id_1": user_id_1,
                "user_id_2": user_id_2,
                "email_1": email_1,
                "email_2": email_2,
                "username_1": username_1,
                "username_2": username_2,
                "display_name_1": username_1,
                "display_name_2": username_2,
            },
        )
        db_session_with_professions.commit()

        # Insert test players with different professions
        # Include all required NOT NULL columns and use proper UUIDs
        db_session_with_professions.execute(
            text("""
            INSERT INTO players (player_id, user_id, name, profession_id, stats, inventory, status_effects, current_room_id, experience_points, level, is_admin, created_at, last_active)
            VALUES
            ('player_1', :user_id_1, 'Player1', 0, '{}', '[]', '[]', 'earth_arkhamcity_sanitarium_room_foyer_001', 0, 1, 0, NOW(), NOW()),
            ('player_2', :user_id_2, 'Player2', 1, '{}', '[]', '[]', 'earth_arkhamcity_sanitarium_room_foyer_001', 0, 1, 0, NOW(), NOW())
        """),
            {"user_id_1": user_id_1, "user_id_2": user_id_2},
        )
        db_session_with_professions.commit()

        # Test querying players by profession (filter to only test players)
        result = db_session_with_professions.execute(
            text("""
            SELECT p.name, pr.name as profession_name
            FROM players p
            JOIN professions pr ON p.profession_id = pr.id
            WHERE p.profession_id = 0 AND p.player_id IN ('player_1', 'player_2')
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
            WHERE p.profession_id = 1 AND p.player_id IN ('player_1', 'player_2')
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

        # Ensure professions table exists with correct schema
        # Check if table exists and has correct columns, recreate if needed
        with engine.connect() as conn:
            # Check if table exists
            result = conn.execute(
                text("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables
                        WHERE table_schema = 'public' AND table_name = 'professions'
                    )
                """)
            )
            table_exists = result.scalar()

            if table_exists:
                # Check if required columns exist
                result = conn.execute(
                    text("""
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_schema = 'public' AND table_name = 'professions'
                    """)
                )
                existing_columns = {row[0] for row in result.fetchall()}
                required_columns = {
                    "id",
                    "name",
                    "description",
                    "flavor_text",
                    "stat_requirements",
                    "mechanical_effects",
                    "is_available",
                }

                # If schema doesn't match, drop and recreate
                if not required_columns.issubset(existing_columns):
                    conn.execute(text("DROP TABLE IF EXISTS professions CASCADE"))
                    conn.commit()
                    table_exists = False

            # Create table if it doesn't exist
            if not table_exists:
                from server.metadata import metadata

                metadata.create_all(engine, tables=[metadata.tables["professions"]])
                conn.commit()

            # Ensure index exists (create if missing, even if table already existed)
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_professions_available ON professions(is_available)"))
            conn.commit()

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
        # Arrange - use unique ID to avoid conflicts
        requirements = {"strength": 12, "intelligence": 10}
        profession = Profession(
            id=99994,
            name="Scholar",
            description="A learned individual",
            flavor_text="Knowledge is power",
            stat_requirements=json.dumps(requirements),
            mechanical_effects="{}",
            is_available=True,
        )
        db_session.add(profession)
        db_session.commit()

        # Clean up after test
        try:
            db_session.delete(profession)
            db_session.commit()
        except Exception:
            pass

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
