"""Tests for zone and subzone configuration database schema and data loading.

These tests verify that:
1. The database schema has all required columns
2. Data is correctly loaded from JSON files into the database
3. ZoneConfiguration objects are correctly populated from database data
"""

import json

import pytest

from server.npc.population_control import ZoneConfiguration


class TestZoneConfigurationDatabaseSchema:
    """Test the zone_configurations table schema - now a mapping table only."""

    @pytest.mark.asyncio
    async def test_zone_configurations_table_columns(self):
        """Test that zone_configurations table is a mapping table with only id, zone_id, subzone_id."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Check table exists and has only mapping columns
            query = """
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = 'zone_configurations'
                ORDER BY column_name
            """
            rows = await conn.fetch(query)
            columns = {row["column_name"]: (row["data_type"], row["is_nullable"]) for row in rows}

            # Verify only mapping columns exist
            required_columns = {
                "id": ("uuid", "NO"),
                "zone_id": ("uuid", "NO"),
                "subzone_id": ("uuid", "NO"),
            }

            # Ensure no old config columns exist
            forbidden_columns = [
                "configuration_type",
                "zone_type",
                "environment",
                "description",
                "weather_patterns",
                "special_rules",
            ]

            for col_name in forbidden_columns:
                assert col_name not in columns, f"Old config column {col_name} should not exist in mapping table"

            # Verify required mapping columns exist and are NOT NULL
            for col_name, (expected_type, expected_nullable) in required_columns.items():
                assert col_name in columns, f"Missing column: {col_name}"
                actual_type, actual_nullable = columns[col_name]
                # Note: PostgreSQL returns 'USER-DEFINED' for uuid type
                assert actual_type in (
                    expected_type,
                    "USER-DEFINED",
                ), f"Column {col_name} has wrong type: {actual_type}"
                assert actual_nullable == expected_nullable, (
                    f"Column {col_name} should be NOT NULL, but is_nullable={actual_nullable}"
                )
        finally:
            await conn.close()

    @pytest.mark.asyncio
    async def test_zone_configurations_mapping_constraint(self):
        """Test that zone_configurations has unique constraint on (zone_id, subzone_id)."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Check unique constraint exists
            query = """
                SELECT constraint_name, constraint_type
                FROM information_schema.table_constraints
                WHERE table_schema = 'public'
                AND table_name = 'zone_configurations'
                AND constraint_type = 'UNIQUE'
            """
            rows = await conn.fetch(query)

            # Should have unique constraint on (zone_id, subzone_id)
            constraint_names = [row["constraint_name"] for row in rows]
            assert any("zone_id_subzone_id" in name for name in constraint_names), (
                f"Missing unique constraint on (zone_id, subzone_id). Found: {constraint_names}"
            )
        finally:
            await conn.close()

    @pytest.mark.asyncio
    async def test_zone_configurations_only_mappings(self):
        """Test that zone_configurations only contains zone-to-subzone mappings (no NULL subzone_id)."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Check that all entries have both zone_id and subzone_id
            query = """
                SELECT
                    COUNT(*) as total,
                    COUNT(zone_id) as has_zone_id,
                    COUNT(subzone_id) as has_subzone_id
                FROM zone_configurations
            """
            row = await conn.fetchrow(query)

            assert row["total"] == row["has_zone_id"], "All entries must have zone_id"
            assert row["total"] == row["has_subzone_id"], "All entries must have subzone_id (no zone-only entries)"
            assert row["has_zone_id"] == row["has_subzone_id"], "zone_id and subzone_id counts should match"
        finally:
            await conn.close()


class TestSubzonesDatabaseSchema:
    """Test the subzones table schema."""

    @pytest.mark.asyncio
    async def test_subzones_table_columns(self):
        """Test that subzones table has all required columns."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Check table exists and has required columns
            query = """
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = 'subzones'
                ORDER BY column_name
            """
            rows = await conn.fetch(query)
            columns = {row["column_name"]: row["data_type"] for row in rows}

            # Verify all required columns exist
            required_columns = {
                "id": "uuid",
                "zone_id": "uuid",
                "stable_id": "text",
                "name": "text",
                "environment": "text",
                "description": "text",
                "special_rules": "jsonb",
            }

            for col_name, expected_type in required_columns.items():
                assert col_name in columns, f"Missing column: {col_name}"
                # Note: PostgreSQL returns 'USER-DEFINED' for uuid type
                assert columns[col_name] in (
                    expected_type,
                    "USER-DEFINED",
                    "character varying",
                ), f"Column {col_name} has wrong type: {columns[col_name]}"
        finally:
            await conn.close()

    @pytest.mark.asyncio
    async def test_subzones_environment_constraint(self):
        """Test that subzones environment constraint allows valid values."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Check constraint exists
            query = """
                SELECT constraint_name, check_clause
                FROM information_schema.check_constraints
                WHERE constraint_name = 'chk_subzones_environment'
            """
            row = await conn.fetchrow(query)
            assert row is not None, "Environment CHECK constraint must exist"

            # Verify constraint includes all valid values
            check_clause = row["check_clause"].lower()
            valid_values = ["indoors", "outdoors", "underwater", "void"]
            for value in valid_values:
                assert f"'{value}'" in check_clause or value in check_clause, (
                    f"Environment constraint must allow '{value}'"
                )
        finally:
            await conn.close()

    @pytest.mark.asyncio
    async def test_subzones_data_populated(self):
        """Test that subzones have environment, description, and special_rules populated."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Check that subzones have required fields populated
            query = """
                SELECT
                    COUNT(*) as total,
                    COUNT(environment) as has_environment,
                    COUNT(description) as has_description,
                    COUNT(special_rules) as has_special_rules
                FROM subzones
            """
            row = await conn.fetchrow(query)

            # All subzones should have special_rules (default is '{}')
            assert row["has_special_rules"] == row["total"], "All subzones must have special_rules"

            # Most subzones should have environment and description from config files
            # Allow some flexibility for subzones without config files
            assert row["has_environment"] > 0, "At least some subzones must have environment"
            assert row["has_description"] > 0, "At least some subzones must have description"
        finally:
            await conn.close()


class TestZoneConfigurationDataLoading:
    """Test that ZoneConfiguration objects are correctly populated from database data."""

    @pytest.mark.asyncio
    async def test_zone_configuration_loads_all_fields(self):
        """Test that ZoneConfiguration loads all fields from database."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Query a zone directly from zones table (authoritative source)
            query = """
                SELECT
                    z.zone_type,
                    z.environment,
                    z.description,
                    z.weather_patterns,
                    z.special_rules
                FROM zones z
                LIMIT 1
            """
            row = await conn.fetchrow(query)

            if row is None:
                pytest.skip("No zones in database")

            # Convert asyncpg results to dict format
            # asyncpg returns JSONB as strings, so we need to parse them
            weather_patterns = row["weather_patterns"]
            if isinstance(weather_patterns, str):
                weather_patterns = json.loads(weather_patterns) if weather_patterns else []
            elif weather_patterns is None:
                weather_patterns = []

            special_rules = row["special_rules"]
            if isinstance(special_rules, str):
                special_rules = json.loads(special_rules) if special_rules else {}
            elif special_rules is None:
                special_rules = {}

            config_data = {
                "zone_type": row["zone_type"],
                "environment": row["environment"],
                "description": row["description"],
                "weather_patterns": weather_patterns,
                "special_rules": special_rules,
            }

            # Create ZoneConfiguration object
            zone_config = ZoneConfiguration(config_data)

            # Verify all fields are populated
            assert zone_config.zone_type is not None, "ZoneConfiguration must have zone_type"
            assert zone_config.environment is not None, "ZoneConfiguration must have environment"
            assert zone_config.description is not None, "ZoneConfiguration must have description"
            assert zone_config.weather_patterns is not None, "ZoneConfiguration must have weather_patterns"
            assert zone_config.special_rules is not None, "ZoneConfiguration must have special_rules"

            # Verify special_rules fields are accessible
            assert "npc_spawn_modifier" in zone_config.special_rules or zone_config.npc_spawn_modifier is not None
            assert "Lucidity_drain_rate" in zone_config.special_rules or zone_config.Lucidity_drain_rate is not None

        finally:
            await conn.close()

    @pytest.mark.asyncio
    async def test_subzone_configuration_loads_all_fields(self):
        """Test that subzone ZoneConfiguration loads all fields from database."""
        import os

        import asyncpg

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            pytest.skip("DATABASE_URL not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        conn = await asyncpg.connect(database_url)
        try:
            # Query a subzone directly from subzones table (authoritative source) with zone data
            query = """
                SELECT
                    sz.environment,
                    sz.description,
                    sz.special_rules,
                    z.zone_type,
                    z.weather_patterns
                FROM subzones sz
                JOIN zones z ON sz.zone_id = z.id
                LIMIT 1
            """
            row = await conn.fetchrow(query)

            if row is None:
                pytest.skip("No subzones in database")

            # Convert asyncpg results to dict format
            # asyncpg returns JSONB as strings, so we need to parse them
            weather_patterns = row["weather_patterns"]
            if isinstance(weather_patterns, str):
                weather_patterns = json.loads(weather_patterns) if weather_patterns else []
            elif weather_patterns is None:
                weather_patterns = []

            special_rules = row["special_rules"]
            if isinstance(special_rules, str):
                special_rules = json.loads(special_rules) if special_rules else {}
            elif special_rules is None:
                special_rules = {}

            config_data = {
                "zone_type": row["zone_type"],  # Inherited from zone
                "environment": row["environment"],
                "description": row["description"],
                "weather_patterns": weather_patterns,  # Inherited from zone
                "special_rules": special_rules,
            }

            # Create ZoneConfiguration object
            subzone_config = ZoneConfiguration(config_data)

            # Verify all fields are populated
            assert subzone_config.environment is not None, "SubzoneConfiguration must have environment"
            assert subzone_config.description is not None, "SubzoneConfiguration must have description"
            assert subzone_config.special_rules is not None, "SubzoneConfiguration must have special_rules"

            # Verify special_rules fields are accessible
            assert "npc_spawn_modifier" in subzone_config.special_rules or subzone_config.npc_spawn_modifier is not None
            assert (
                "Lucidity_drain_rate" in subzone_config.special_rules or subzone_config.Lucidity_drain_rate is not None
            )

        finally:
            await conn.close()
