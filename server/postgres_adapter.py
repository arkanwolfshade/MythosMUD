"""
PostgreSQL adapter for persistence layer.

Provides a PostgreSQL connection interface for the persistence layer,
using psycopg2 for synchronous database operations.
"""

import threading
from contextlib import contextmanager
from typing import Any

import psycopg2
from psycopg2.extras import RealDictCursor, register_uuid
from psycopg2.pool import ThreadedConnectionPool

from .structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Register UUID adapters for psycopg2
# This allows psycopg2 to handle Python uuid.UUID objects directly
# without manual string conversion
register_uuid()


class PostgresRow:
    """Row-like object for PostgreSQL query results."""

    def __init__(self, row_dict: dict[str, Any]):
        self._row_dict = row_dict

    def __getitem__(self, key: str | int) -> Any:
        if isinstance(key, int):
            # Convert integer index to column name
            keys = list(self._row_dict.keys())
            if 0 <= key < len(keys):
                return self._row_dict[keys[key]]
            raise IndexError(f"Column index {key} out of range")
        return self._row_dict[key]

    def __iter__(self):
        return iter(self._row_dict.values())

    def keys(self):
        return self._row_dict.keys()

    def __contains__(self, key: str) -> bool:
        return key in self._row_dict

    def __len__(self) -> int:
        return len(self._row_dict)

    def __repr__(self) -> str:
        return f"PostgresRow({self._row_dict})"


class PostgresConnection:
    """PostgreSQL connection wrapper for persistence layer operations."""

    def __init__(self, conn: psycopg2.extensions.connection):
        self._conn = conn
        self._conn.autocommit = False

    def execute(self, query: str, params: tuple | None = None) -> "PostgresCursor":
        """
        Execute a query and return a cursor.

        Args:
            query: SQL query with PostgreSQL %s placeholders
            params: Optional tuple of parameters for the query

        Returns:
            PostgresCursor: Cursor for fetching results
        """
        cursor = self._conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, params)
        return PostgresCursor(cursor)

    def cursor(self, cursor_factory=None):
        """
        Get a cursor from the underlying connection.

        This method provides direct access to the psycopg2 cursor API
        for code that needs lower-level control (e.g., container_persistence).

        Args:
            cursor_factory: Optional cursor factory (defaults to RealDictCursor)

        Returns:
            psycopg2.extensions.cursor: Raw psycopg2 cursor
        """
        from psycopg2.extras import RealDictCursor

        if cursor_factory is None:
            cursor_factory = RealDictCursor
        return self._conn.cursor(cursor_factory=cursor_factory)

    def commit(self) -> None:
        """Commit the current transaction."""
        self._conn.commit()

    def rollback(self) -> None:
        """Rollback the current transaction."""
        self._conn.rollback()

    def close(self) -> None:
        """Close the connection."""
        self._conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()


class PostgresCursor:
    """PostgreSQL cursor wrapper for query result access."""

    def __init__(self, cursor: psycopg2.extensions.cursor):
        self._cursor = cursor

    def fetchone(self) -> PostgresRow | None:
        """Fetch one row."""
        row = self._cursor.fetchone()
        if row is None:
            return None
        return PostgresRow(dict(row))

    def fetchall(self) -> list[PostgresRow]:
        """Fetch all rows."""
        rows = self._cursor.fetchall()
        return [PostgresRow(dict(row)) for row in rows]

    def rowcount(self) -> int:
        """Get the number of rows affected."""
        return self._cursor.rowcount


class PostgresConnectionPool:
    """Thread-safe PostgreSQL connection pool."""

    _pools: dict[str, ThreadedConnectionPool] = {}
    _lock = threading.Lock()

    @classmethod
    def get_pool(cls, database_url: str) -> ThreadedConnectionPool:
        """Get or create a connection pool for the given database URL."""
        with cls._lock:
            if database_url not in cls._pools:
                # Parse PostgreSQL URL
                # Format: postgresql://user:password@host:port/database
                # or postgresql+psycopg2://user:password@host:port/database
                url = database_url.replace("postgresql+psycopg2://", "postgresql://").replace(
                    "postgresql+asyncpg://", "postgresql://"
                )

                # Create connection pool
                # Minimum 1 connection, maximum 10 connections
                pool_instance = ThreadedConnectionPool(1, 10, dsn=url)
                cls._pools[database_url] = pool_instance
                logger.info("Created PostgreSQL connection pool", database_url=database_url[:50])
            return cls._pools[database_url]

    @classmethod
    @contextmanager
    def get_connection(cls, database_url: str):
        """Get a connection from the pool."""
        pool_instance = cls.get_pool(database_url)
        conn = pool_instance.getconn()
        try:
            yield PostgresConnection(conn)
        finally:
            pool_instance.putconn(conn)


def is_postgres_url(database_url: str) -> bool:
    """Check if the database URL is PostgreSQL."""
    return database_url.startswith("postgresql")


def connect_postgres(database_url: str) -> PostgresConnection:
    """
    Create a PostgreSQL connection.

    Args:
        database_url: PostgreSQL connection URL (postgresql:// or postgresql+psycopg2://)

    Returns:
        PostgresConnection: Wrapped PostgreSQL connection
    """
    # Normalize URL format (remove driver prefix if present)
    url = database_url.replace("postgresql+psycopg2://", "postgresql://").replace(
        "postgresql+asyncpg://", "postgresql://"
    )
    conn = psycopg2.connect(url)
    return PostgresConnection(conn)


def convert_sqlite_to_postgres_query(query: str) -> str:
    """Convert SQLite query syntax to PostgreSQL syntax."""
    # Replace ? with %s for parameter placeholders
    query = query.replace("?", "%s")
    # Replace INSERT OR REPLACE with PostgreSQL UPSERT
    if "INSERT OR REPLACE" in query.upper():
        # This is complex - would need to parse the query properly
        # For now, we'll handle this case-by-case in the calling code
        pass
    return query
