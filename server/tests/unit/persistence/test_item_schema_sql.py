"""Tests verifying item schema and seed data scripts work correctly with PostgreSQL."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.database import get_database_url
from server.models.base import Base

EXPECTED_SLOTS = {
    "HEAD",
    "TORSO",
    "LEGS",
    "MAIN_HAND",
    "OFF_HAND",
    "FEET",
    "HANDS",
    "ACCESSORY",
    "RING",
    "AMULET",
    "BELT",
}


def project_path(*parts: str) -> Path:
    """Get a path relative to the project root."""
    return Path(__file__).resolve().parents[4].joinpath(*parts)


def load_sql(path: Path) -> str:
    """Load SQL file content."""
    return path.read_text(encoding="utf-8")


def convert_sqlite_to_postgresql(sql: str) -> str:
    """
    Convert SQLite-specific SQL to PostgreSQL syntax.

    Converts:
    - INSERT OR REPLACE -> INSERT ... ON CONFLICT DO UPDATE
    - PRAGMA statements -> removed (not needed in PostgreSQL)
    - datetime('now') -> now()
    """
    # Remove PRAGMA statements
    sql = re.sub(r"PRAGMA\s+\w+\s*=\s*\w+;?\s*", "", sql, flags=re.IGNORECASE)

    # Convert INSERT OR REPLACE to PostgreSQL UPSERT
    # Pattern: INSERT OR REPLACE INTO table (cols) VALUES (...)
    def replace_insert_or_replace(match):
        full_match = match.group(0)
        # Extract columns from the INSERT statement
        cols_match = re.search(r"INSERT\s+OR\s+REPLACE\s+INTO\s+\w+\s*\(([^)]+)\)", full_match, re.IGNORECASE)
        if cols_match:
            columns_str = cols_match.group(1)
            # Parse columns and create UPDATE SET clause
            columns = [col.strip() for col in columns_str.split(",")]
            # Create UPDATE SET clause: col1=EXCLUDED.col1, col2=EXCLUDED.col2, ...
            update_clause = ", ".join(f"{col}=EXCLUDED.{col}" for col in columns)
            # Replace INSERT OR REPLACE with INSERT and add ON CONFLICT
            result = full_match.replace("INSERT OR REPLACE", "INSERT")
            # Add ON CONFLICT clause before semicolon
            if result.rstrip().endswith(";"):
                result = result.rstrip()[:-1] + f" ON CONFLICT (prototype_id) DO UPDATE SET {update_clause};"
            else:
                result = result + f" ON CONFLICT (prototype_id) DO UPDATE SET {update_clause}"
            return result
        return full_match

    sql = re.sub(
        r"INSERT\s+OR\s+REPLACE\s+INTO\s+\w+\s*\([^)]+\)\s+VALUES[^;]+;",
        replace_insert_or_replace,
        sql,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Convert datetime('now') to now()
    sql = re.sub(r"datetime\s*\(\s*['\"]now['\"]\s*\)", "now()", sql, flags=re.IGNORECASE)

    return sql


@pytest.fixture
async def async_session_factory():
    """Create an async session factory for PostgreSQL testing."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # Create tables using PostgreSQL schema
        # Load the PostgreSQL schema for items from db/schema/04_runtime_tables.sql
        schema_path = project_path("db", "schema", "04_runtime_tables.sql")
        if schema_path.exists():
            schema_sql = load_sql(schema_path)
            # Extract item table creation statements (from "-- Item system tables" to next major section)
            item_schema_match = re.search(
                r"-- Item system tables.*?(?=-- NPC|\Z)",
                schema_sql,
                re.IGNORECASE | re.DOTALL,
            )
            if item_schema_match:
                item_schema = item_schema_match.group(0)
                # Execute the item schema
                await conn.execute(text(item_schema))
            else:
                # Fallback: create tables using SQLAlchemy metadata
                await conn.run_sync(Base.metadata.create_all)
        else:
            # Fallback: create tables using SQLAlchemy metadata
            await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        # Clean up: drop tables
        async with engine.begin() as conn:
            await conn.execute(text("DROP TABLE IF EXISTS item_component_states CASCADE"))
            await conn.execute(text("DROP TABLE IF EXISTS item_instances CASCADE"))
            await conn.execute(text("DROP TABLE IF EXISTS item_prototypes CASCADE"))
        await engine.dispose()


@pytest.mark.asyncio
async def test_item_schema_and_seed_scripts_create_expected_artifacts(async_session_factory):
    """Test that item schema and seed scripts create expected database artifacts."""
    # Load seed data SQL file (SQLite format, will be converted to PostgreSQL)
    seed_sql = load_sql(project_path("server", "sql", "items_seed_data.sql"))

    # Convert SQLite SQL to PostgreSQL
    seed_sql_pg = convert_sqlite_to_postgresql(seed_sql)

    async with async_session_factory() as session:
        # Verify tables exist using PostgreSQL information_schema
        result = await session.execute(
            text(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name IN ('item_prototypes', 'item_instances', 'item_component_states')
                """
            )
        )
        tables = {row[0] for row in result.fetchall()}
        assert {"item_prototypes", "item_instances", "item_component_states"} <= tables

        # Check indexes using PostgreSQL system queries
        result = await session.execute(
            text(
                """
                SELECT indexname
                FROM pg_indexes
                WHERE tablename = 'item_instances'
                AND schemaname = 'public'
                """
            )
        )
        indexes = {row[0] for row in result.fetchall()}
        assert "idx_item_instances_owner" in indexes or "ix_item_instances_owner" in indexes
        assert "idx_item_instances_prototype_id" in indexes or "ix_item_instances_prototype_id" in indexes

        # Check foreign keys using PostgreSQL system queries
        result = await session.execute(
            text(
                """
                SELECT
                    tc.table_name,
                    kcu.column_name,
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                    ON tc.constraint_name = kcu.constraint_name
                    AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                    ON ccu.constraint_name = tc.constraint_name
                    AND ccu.table_schema = tc.table_schema
                WHERE tc.constraint_type = 'FOREIGN KEY'
                AND tc.table_name = 'item_instances'
                AND tc.table_schema = 'public'
                """
            )
        )
        fk_list = list(result.fetchall())
        assert fk_list, "item_instances should include a foreign key to item_prototypes"
        # Check that at least one FK references item_prototypes
        assert any(fk[2] == "item_prototypes" for fk in fk_list), "FK should reference item_prototypes"

        # Execute seed data (converted to PostgreSQL)
        # Split by semicolons and execute each statement
        statements = [s.strip() for s in seed_sql_pg.split(";") if s.strip() and not s.strip().startswith("--")]
        for statement in statements:
            if statement:
                try:
                    # Use execute with commit=False to batch statements
                    await session.execute(text(statement))
                except Exception as e:
                    # Log the statement that failed for debugging
                    print(f"Failed statement: {statement[:500]}...")
                    print(f"Error: {e}")
                    # If it's a ProgrammingError, it might be due to invalid SQL conversion
                    # Try to provide more context
                    if "ProgrammingError" in str(type(e)):
                        print(f"Full statement: {statement}")
                    raise
        await session.commit()

        # Verify prototype count
        result = await session.execute(text("SELECT COUNT(*) FROM item_prototypes"))
        prototype_count = result.scalar()
        assert prototype_count == 22

        # Re-running the seed should be idempotent thanks to ON CONFLICT DO UPDATE
        for statement in statements:
            if statement:
                await session.execute(text(statement))
        await session.commit()

        result = await session.execute(text("SELECT COUNT(*) FROM item_prototypes"))
        prototype_count_again = result.scalar()
        assert prototype_count_again == prototype_count

        # Check slot totals
        slot_totals = dict.fromkeys(EXPECTED_SLOTS, 0)
        result = await session.execute(text("SELECT prototype_id, wear_slots FROM item_prototypes"))
        for row in result.fetchall():
            slots = json.loads(row[1]) if isinstance(row[1], str) else row[1]
            for slot in slots:
                if slot in slot_totals:
                    slot_totals[slot] += 1
        assert all(count >= 2 for count in slot_totals.values()), slot_totals

        # Check ordered IDs
        result = await session.execute(text("SELECT prototype_id FROM item_prototypes ORDER BY prototype_id"))
        ordered_ids = [row[0] for row in result.fetchall()]
        assert ordered_ids == sorted(ordered_ids)
