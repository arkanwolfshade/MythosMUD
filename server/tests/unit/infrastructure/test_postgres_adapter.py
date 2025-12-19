"""
Tests for PostgreSQL adapter.

This module tests the PostgreSQL connection adapter, connection pool,
and related utilities in postgres_adapter.py.
"""

from unittest.mock import MagicMock, patch

import pytest
from psycopg2.extras import RealDictCursor

from server.postgres_adapter import (
    PostgresConnection,
    PostgresConnectionPool,
    PostgresCursor,
    PostgresRow,
    connect_postgres,
    convert_sqlite_to_postgres_query,
    is_postgres_url,
)


class TestPostgresRow:
    """Test PostgresRow class."""

    def test_postgres_row_init(self) -> None:
        """Test PostgresRow initialization."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert row._row_dict == row_dict

    def test_postgres_row_getitem_string_key(self) -> None:
        """Test PostgresRow __getitem__ with string key."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert row["id"] == 1
        assert row["name"] == "test"

    def test_postgres_row_getitem_int_key(self) -> None:
        """Test PostgresRow __getitem__ with integer key."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert row[0] == 1
        assert row[1] == "test"

    def test_postgres_row_getitem_int_key_out_of_range(self) -> None:
        """Test PostgresRow __getitem__ with out-of-range integer key."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        with pytest.raises(IndexError, match="Column index 2 out of range"):
            _ = row[2]

    def test_postgres_row_getitem_int_key_negative(self) -> None:
        """Test PostgresRow __getitem__ with negative integer key."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        with pytest.raises(IndexError, match="Column index -1 out of range"):
            _ = row[-1]

    def test_postgres_row_iter(self) -> None:
        """Test PostgresRow iteration."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        values = list(row)
        assert values == [1, "test"]

    def test_postgres_row_keys(self) -> None:
        """Test PostgresRow keys method."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert list(row.keys()) == ["id", "name"]

    def test_postgres_row_contains(self) -> None:
        """Test PostgresRow __contains__ method."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert "id" in row
        assert "name" in row
        assert "missing" not in row

    def test_postgres_row_len(self) -> None:
        """Test PostgresRow __len__ method."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert len(row) == 2

    def test_postgres_row_repr(self) -> None:
        """Test PostgresRow __repr__ method."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        repr_str = repr(row)
        assert "PostgresRow" in repr_str
        assert "id" in repr_str or "1" in repr_str


class TestPostgresConnection:
    """Test PostgresConnection class."""

    def test_postgres_connection_init(self) -> None:
        """Test PostgresConnection initialization."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        conn = PostgresConnection(mock_conn)
        assert conn._conn == mock_conn
        assert mock_conn.autocommit is False

    def test_postgres_connection_execute(self) -> None:
        """Test PostgresConnection execute method."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        conn = PostgresConnection(mock_conn)
        result = conn.execute("SELECT * FROM test", ("param",))

        assert isinstance(result, PostgresCursor)
        mock_conn.cursor.assert_called_once_with(cursor_factory=RealDictCursor)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test", ("param",))

    def test_postgres_connection_execute_no_params(self) -> None:
        """Test PostgresConnection execute method without params."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        conn = PostgresConnection(mock_conn)
        result = conn.execute("SELECT * FROM test")

        assert isinstance(result, PostgresCursor)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test", None)

    def test_postgres_connection_cursor_default(self) -> None:
        """Test PostgresConnection cursor method with default factory."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        conn = PostgresConnection(mock_conn)
        result = conn.cursor()

        assert result == mock_cursor
        mock_conn.cursor.assert_called_once_with(cursor_factory=RealDictCursor)

    def test_postgres_connection_cursor_custom_factory(self) -> None:
        """Test PostgresConnection cursor method with custom factory."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        mock_cursor = MagicMock()
        custom_factory = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        conn = PostgresConnection(mock_conn)
        result = conn.cursor(cursor_factory=custom_factory)

        assert result == mock_cursor
        mock_conn.cursor.assert_called_once_with(cursor_factory=custom_factory)

    def test_postgres_connection_commit(self) -> None:
        """Test PostgresConnection commit method."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        conn = PostgresConnection(mock_conn)
        conn.commit()
        mock_conn.commit.assert_called_once()

    def test_postgres_connection_rollback(self) -> None:
        """Test PostgresConnection rollback method."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        conn = PostgresConnection(mock_conn)
        conn.rollback()
        mock_conn.rollback.assert_called_once()

    def test_postgres_connection_close(self) -> None:
        """Test PostgresConnection close method."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        conn = PostgresConnection(mock_conn)
        conn.close()
        mock_conn.close.assert_called_once()

    def test_postgres_connection_context_manager_success(self) -> None:
        """Test PostgresConnection context manager on success."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        conn = PostgresConnection(mock_conn)

        with conn:
            pass

        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
        mock_conn.rollback.assert_not_called()

    def test_postgres_connection_context_manager_exception(self) -> None:
        """Test PostgresConnection context manager on exception."""
        mock_conn = MagicMock()
        mock_conn.autocommit = True
        conn = PostgresConnection(mock_conn)

        with pytest.raises(ValueError):
            with conn:
                raise ValueError("test error")

        mock_conn.rollback.assert_called_once()
        mock_conn.close.assert_called_once()
        mock_conn.commit.assert_not_called()


class TestPostgresCursor:
    """Test PostgresCursor class."""

    def test_postgres_cursor_init(self) -> None:
        """Test PostgresCursor initialization."""
        mock_cursor = MagicMock()
        cursor = PostgresCursor(mock_cursor)
        assert cursor._cursor == mock_cursor

    def test_postgres_cursor_fetchone_with_row(self) -> None:
        """Test PostgresCursor fetchone with a row."""
        mock_cursor = MagicMock()
        mock_row = {"id": 1, "name": "test"}
        mock_cursor.fetchone.return_value = mock_row

        cursor = PostgresCursor(mock_cursor)
        result = cursor.fetchone()

        assert isinstance(result, PostgresRow)
        assert result["id"] == 1
        assert result["name"] == "test"
        mock_cursor.fetchone.assert_called_once()

    def test_postgres_cursor_fetchone_none(self) -> None:
        """Test PostgresCursor fetchone with no rows."""
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None

        cursor = PostgresCursor(mock_cursor)
        result = cursor.fetchone()

        assert result is None
        mock_cursor.fetchone.assert_called_once()

    def test_postgres_cursor_fetchall_with_rows(self) -> None:
        """Test PostgresCursor fetchall with rows."""
        mock_cursor = MagicMock()
        mock_rows = [{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]
        mock_cursor.fetchall.return_value = mock_rows

        cursor = PostgresCursor(mock_cursor)
        result = cursor.fetchall()

        assert len(result) == 2
        assert all(isinstance(row, PostgresRow) for row in result)
        assert result[0]["id"] == 1
        assert result[1]["id"] == 2
        mock_cursor.fetchall.assert_called_once()

    def test_postgres_cursor_fetchall_empty(self) -> None:
        """Test PostgresCursor fetchall with no rows."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []

        cursor = PostgresCursor(mock_cursor)
        result = cursor.fetchall()

        assert result == []
        mock_cursor.fetchall.assert_called_once()

    def test_postgres_cursor_rowcount(self) -> None:
        """Test PostgresCursor rowcount method."""
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 5

        cursor = PostgresCursor(mock_cursor)
        result = cursor.rowcount()

        assert result == 5


class TestPostgresConnectionPool:
    """Test PostgresConnectionPool class."""

    def test_get_pool_creates_new_pool(self) -> None:
        """Test get_pool creates a new pool for a new URL."""
        database_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.ThreadedConnectionPool") as mock_pool_class:
            mock_pool = MagicMock()
            mock_pool_class.return_value = mock_pool
            with patch("server.postgres_adapter.logger") as mock_logger:
                # Clear any existing pools
                PostgresConnectionPool._pools.clear()
                pool = PostgresConnectionPool.get_pool(database_url)

                assert pool == mock_pool
                mock_pool_class.assert_called_once_with(1, 10, dsn=database_url)
                mock_logger.info.assert_called_once()

    def test_get_pool_returns_existing_pool(self) -> None:
        """Test get_pool returns existing pool for same URL."""
        database_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.ThreadedConnectionPool") as mock_pool_class:
            mock_pool = MagicMock()
            mock_pool_class.return_value = mock_pool
            # Clear any existing pools
            PostgresConnectionPool._pools.clear()
            pool1 = PostgresConnectionPool.get_pool(database_url)
            pool2 = PostgresConnectionPool.get_pool(database_url)

            assert pool1 == pool2
            assert pool1 == mock_pool
            # Should only be called once
            assert mock_pool_class.call_count == 1

    def test_get_pool_normalizes_psycopg2_url(self) -> None:
        """Test get_pool normalizes postgresql+psycopg2:// URLs."""
        database_url = "postgresql+psycopg2://user:pass@localhost/db"
        normalized_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.ThreadedConnectionPool") as mock_pool_class:
            mock_pool = MagicMock()
            mock_pool_class.return_value = mock_pool
            PostgresConnectionPool._pools.clear()
            PostgresConnectionPool.get_pool(database_url)

            mock_pool_class.assert_called_once_with(1, 10, dsn=normalized_url)

    def test_get_pool_normalizes_asyncpg_url(self) -> None:
        """Test get_pool normalizes postgresql+asyncpg:// URLs."""
        database_url = "postgresql+asyncpg://user:pass@localhost/db"
        normalized_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.ThreadedConnectionPool") as mock_pool_class:
            mock_pool = MagicMock()
            mock_pool_class.return_value = mock_pool
            PostgresConnectionPool._pools.clear()
            PostgresConnectionPool.get_pool(database_url)

            mock_pool_class.assert_called_once_with(1, 10, dsn=normalized_url)

    def test_get_connection_context_manager(self) -> None:
        """Test get_connection context manager."""
        database_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.ThreadedConnectionPool") as mock_pool_class:
            mock_pool = MagicMock()
            mock_conn = MagicMock()
            mock_pool.getconn.return_value = mock_conn
            mock_pool_class.return_value = mock_pool
            PostgresConnectionPool._pools.clear()

            with PostgresConnectionPool.get_connection(database_url) as conn:
                assert isinstance(conn, PostgresConnection)
                assert conn._conn == mock_conn

            mock_pool.getconn.assert_called_once()
            mock_pool.putconn.assert_called_once_with(mock_conn)

    def test_get_connection_context_manager_exception(self) -> None:
        """Test get_connection context manager handles exceptions."""
        database_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.ThreadedConnectionPool") as mock_pool_class:
            mock_pool = MagicMock()
            mock_conn = MagicMock()
            mock_pool.getconn.return_value = mock_conn
            mock_pool_class.return_value = mock_pool
            PostgresConnectionPool._pools.clear()

            with pytest.raises(ValueError):
                with PostgresConnectionPool.get_connection(database_url) as _conn:
                    raise ValueError("test error")

            mock_pool.getconn.assert_called_once()
            mock_pool.putconn.assert_called_once_with(mock_conn)


class TestUtilityFunctions:
    """Test utility functions."""

    def test_is_postgres_url_postgresql(self) -> None:
        """Test is_postgres_url with postgresql:// URL."""
        assert is_postgres_url("postgresql://user:pass@localhost/db") is True

    def test_is_postgres_url_postgresql_psycopg2(self) -> None:
        """Test is_postgres_url with postgresql+psycopg2:// URL."""
        assert is_postgres_url("postgresql+psycopg2://user:pass@localhost/db") is True

    def test_is_postgres_url_postgresql_asyncpg(self) -> None:
        """Test is_postgres_url with postgresql+asyncpg:// URL."""
        assert is_postgres_url("postgresql+asyncpg://user:pass@localhost/db") is True

    def test_is_postgres_url_sqlite(self) -> None:
        """Test is_postgres_url with SQLite URL."""
        assert is_postgres_url("sqlite:///path/to/db") is False

    def test_is_postgres_url_mysql(self) -> None:
        """Test is_postgres_url with MySQL URL."""
        assert is_postgres_url("mysql://user:pass@localhost/db") is False

    def test_connect_postgres(self) -> None:
        """Test connect_postgres function."""
        database_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.psycopg2.connect") as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            result = connect_postgres(database_url)

            assert isinstance(result, PostgresConnection)
            assert result._conn == mock_conn
            mock_connect.assert_called_once_with(database_url)

    def test_connect_postgres_normalizes_psycopg2_url(self) -> None:
        """Test connect_postgres normalizes postgresql+psycopg2:// URL."""
        database_url = "postgresql+psycopg2://user:pass@localhost/db"
        normalized_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.psycopg2.connect") as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            connect_postgres(database_url)

            mock_connect.assert_called_once_with(normalized_url)

    def test_connect_postgres_normalizes_asyncpg_url(self) -> None:
        """Test connect_postgres normalizes postgresql+asyncpg:// URL."""
        database_url = "postgresql+asyncpg://user:pass@localhost/db"
        normalized_url = "postgresql://user:pass@localhost/db"
        with patch("server.postgres_adapter.psycopg2.connect") as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            connect_postgres(database_url)

            mock_connect.assert_called_once_with(normalized_url)

    def test_convert_sqlite_to_postgres_query_placeholders(self) -> None:
        """Test convert_sqlite_to_postgres_query converts ? to %s."""
        sqlite_query = "SELECT * FROM test WHERE id = ? AND name = ?"
        postgres_query = convert_sqlite_to_postgres_query(sqlite_query)
        assert postgres_query == "SELECT * FROM test WHERE id = %s AND name = %s"

    def test_convert_sqlite_to_postgres_query_no_placeholders(self) -> None:
        """Test convert_sqlite_to_postgres_query with no placeholders."""
        query = "SELECT * FROM test"
        result = convert_sqlite_to_postgres_query(query)
        assert result == "SELECT * FROM test"

    def test_convert_sqlite_to_postgres_query_insert_replace(self) -> None:
        """Test convert_sqlite_to_postgres_query with INSERT OR REPLACE."""
        query = "INSERT OR REPLACE INTO test (id, name) VALUES (?, ?)"
        result = convert_sqlite_to_postgres_query(query)
        # Should convert ? to %s but leave INSERT OR REPLACE as-is
        # (handled case-by-case in calling code)
        assert "%s" in result
        assert "INSERT OR REPLACE" in result.upper()
