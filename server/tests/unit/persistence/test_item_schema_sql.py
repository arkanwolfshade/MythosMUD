"""Tests verifying item schema and seed data scripts work correctly with PostgreSQL."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.database import get_database_url
from server.logging.enhanced_logging_config import get_logger
from server.models.base import Base

logger = get_logger(__name__)

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
    # Since regex can't handle quoted strings properly, we'll find INSERT OR REPLACE
    # and then process character-by-character to find the real statement end
    result_parts = []
    i = 0

    while i < len(sql):
        # Look for INSERT OR REPLACE (case-insensitive)
        remaining = sql[i:]
        insert_match = re.search(r"INSERT\s+OR\s+REPLACE", remaining, re.IGNORECASE)

        if not insert_match:
            # No more INSERT OR REPLACE, append rest and break
            result_parts.append(remaining)
            break

        # Append everything before the INSERT OR REPLACE
        insert_start = i + insert_match.start()
        result_parts.append(sql[i:insert_start])

        # Find the column list
        after_insert = sql[insert_start + insert_match.end() :]
        cols_match = re.search(r"INTO\s+\w+\s*\(([^)]+)\)", after_insert, re.IGNORECASE | re.DOTALL)

        if not cols_match:
            # Can't find columns, append as-is and continue
            result_parts.append(sql[insert_start : insert_start + 100])  # Append some to avoid infinite loop
            i = insert_start + 100
            continue

        # Extract columns
        columns_str = cols_match.group(1)
        columns = [col.strip() for col in columns_str.split(",")]
        update_clause = ", ".join(f"{col}=EXCLUDED.{col}" for col in columns)

        # Find the actual end of the statement (semicolon not in quotes)
        stmt_content_start = insert_start
        stmt_content_end = insert_start + insert_match.end() + cols_match.end()

        # Now find the semicolon that ends this statement (not in quotes)
        j = stmt_content_end
        in_quotes = False
        quote_char = None

        while j < len(sql):
            char = sql[j]
            if char in ("'", '"'):
                if in_quotes and char == quote_char and j + 1 < len(sql) and sql[j + 1] == char:
                    # Escaped quote
                    j += 2
                    continue
                elif not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char:
                    in_quotes = False
                    quote_char = None
            elif char == ";" and not in_quotes:
                # Found the end!
                stmt_content = sql[stmt_content_start : j + 1]  # Include the semicolon
                # Replace INSERT OR REPLACE with INSERT (case-insensitive, handle any whitespace including newlines)
                # Match: INSERT (whitespace) OR (whitespace) REPLACE (whitespace) INTO
                # Replace with: INSERT (space) INTO
                # Use DOTALL flag to match across newlines
                stmt_content = re.sub(
                    r"INSERT\s+OR\s+REPLACE\s+INTO",
                    "INSERT INTO",
                    stmt_content,
                    count=1,
                    flags=re.IGNORECASE | re.DOTALL,
                )
                # Also handle case where there's no INTO immediately after (shouldn't happen but be safe)
                # Check if replacement worked by looking for remaining "INSERT OR REPLACE"
                if re.search(r"INSERT\s+OR\s+REPLACE", stmt_content, re.IGNORECASE):
                    # Try a more aggressive replacement
                    stmt_content = re.sub(
                        r"INSERT\s+OR\s+REPLACE\s+", "INSERT ", stmt_content, count=1, flags=re.IGNORECASE | re.DOTALL
                    )
                # Verify the replacement worked
                if re.search(r"INSERT\s+OR\s+REPLACE", stmt_content, re.IGNORECASE):
                    # If still not replaced, do a simple string replace as fallback
                    stmt_content = stmt_content.replace("INSERT OR REPLACE INTO", "INSERT INTO")
                    stmt_content = stmt_content.replace("INSERT OR REPLACE", "INSERT")
                # Remove semicolon, add ON CONFLICT
                stmt_content = stmt_content.rstrip()
                if stmt_content.endswith(";"):
                    stmt_content = stmt_content[:-1].rstrip()
                stmt_content = stmt_content + f" ON CONFLICT (prototype_id) DO UPDATE SET {update_clause};"
                result_parts.append(stmt_content)
                i = j + 1
                break
            j += 1
        else:
            # Didn't find end, append as-is
            result_parts.append(sql[insert_start : insert_start + 100])
            i = insert_start + 100

    sql = "".join(result_parts)

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
        # Load the PostgreSQL schema for items from db/authoritative_schema.sql
        # (extracting just the item-related portions for this test)
        schema_path = project_path("db", "authoritative_schema.sql")
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
                # Split by semicolons, being careful with quoted strings and comments
                # Use quote-aware splitting similar to convert_sqlite_to_postgresql
                statements = []
                current_statement = []
                in_quotes = False
                quote_char = None
                i = 0

                while i < len(item_schema):
                    char = item_schema[i]
                    current_statement.append(char)

                    # Check for quote (single or double)
                    if char in ("'", '"'):
                        # Check if this is an escaped quote (doubled quote in SQL)
                        if i + 1 < len(item_schema) and item_schema[i + 1] == char and in_quotes and char == quote_char:
                            # This is a doubled quote (escaped), skip the next character
                            i += 1
                            if i < len(item_schema):
                                current_statement.append(item_schema[i])
                        elif not in_quotes:
                            # Starting a quoted string
                            in_quotes = True
                            quote_char = char
                        elif char == quote_char:
                            # Ending a quoted string
                            in_quotes = False
                            quote_char = None
                    elif char == ";" and not in_quotes:
                        # End of statement (semicolon outside quotes)
                        statement = "".join(current_statement).strip()
                        # Remove leading comment lines but keep the statement
                        # Split by newlines, filter out comment lines, rejoin
                        if statement:
                            lines = statement.split("\n")
                            # Remove lines that are only comments or whitespace
                            cleaned_lines = []
                            for line in lines:
                                stripped = line.strip()
                                # Keep non-comment lines, or lines that have content after removing comments
                                if stripped and not stripped.startswith("--"):
                                    cleaned_lines.append(line)
                                elif stripped.startswith("--") and len(cleaned_lines) > 0:
                                    # Comment line, but we already have content, so keep it for context
                                    pass
                            if cleaned_lines:
                                cleaned_statement = "\n".join(cleaned_lines)
                                statements.append(cleaned_statement)
                        current_statement = []

                    i += 1

                # Process any remaining statement
                if current_statement:
                    remaining = "".join(current_statement).strip()
                    if remaining:
                        # Remove leading comment lines
                        lines = remaining.split("\n")
                        cleaned_lines = [line for line in lines if line.strip() and not line.strip().startswith("--")]
                        if cleaned_lines:
                            statements.append("\n".join(cleaned_lines))

                # Execute each statement in order
                logger.debug("Extracted schema statements", statement_count=len(statements))
                for idx, statement in enumerate(statements):
                    if statement:
                        # Log first 100 chars of each statement for debugging
                        logger.debug(
                            "Executing schema statement",
                            index=idx,
                            statement_preview=statement[:100].replace("\n", " "),
                        )
                        try:
                            await conn.execute(text(statement))
                        except Exception as e:
                            # Log the statement that failed for debugging
                            logger.error(
                                "Failed to execute schema statement",
                                error=str(e),
                                statement_index=idx,
                                statement_preview=statement[:200],
                            )
                            raise
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
