"""
Unit tests for PostgreSQL adapter.

Tests PostgresRow, PostgresConnection, PostgresCursor, PostgresConnectionPool,
and utility functions.
"""

from unittest.mock import MagicMock, Mock, patch

import pytest

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

    def test_postgres_row_initialization(self):
        """Test PostgresRow initialization."""
        row_dict = {"id": 1, "name": "test", "value": 42}
        row = PostgresRow(row_dict)
        # Verify initialization using public API instead of accessing protected member
        assert list(row.keys()) == list(row_dict.keys())
        assert row["id"] == row_dict["id"]
        assert row["name"] == row_dict["name"]
        assert row["value"] == row_dict["value"]
        assert len(row) == len(row_dict)

    def test_postgres_row_getitem_string_key(self):
        """Test PostgresRow.__getitem__ with string key."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert row["id"] == 1
        assert row["name"] == "test"

    def test_postgres_row_getitem_int_key(self):
        """Test PostgresRow.__getitem__ with integer index."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        # First column
        assert row[0] == 1
        # Second column
        assert row[1] == "test"

    def test_postgres_row_getitem_int_key_out_of_range(self):
        """Test PostgresRow.__getitem__ with out-of-range integer index."""
        row_dict = {"id": 1}
        row = PostgresRow(row_dict)
        with pytest.raises(IndexError, match="Column index 5 out of range"):
            _ = row[5]

    def test_postgres_row_iter(self):
        """Test PostgresRow.__iter__."""
        row_dict = {"id": 1, "name": "test", "value": 42}
        row = PostgresRow(row_dict)
        values = list(row)
        assert values == [1, "test", 42]

    def test_postgres_row_keys(self):
        """Test PostgresRow.keys()."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        keys = list(row.keys())
        assert keys == ["id", "name"]

    def test_postgres_row_contains(self):
        """Test PostgresRow.__contains__."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        assert "id" in row
        assert "name" in row
        assert "missing" not in row

    def test_postgres_row_len(self):
        """Test PostgresRow.__len__."""
        row_dict = {"id": 1, "name": "test", "value": 42}
        row = PostgresRow(row_dict)
        assert len(row) == 3

    def test_postgres_row_repr(self):
        """Test PostgresRow.__repr__."""
        row_dict = {"id": 1, "name": "test"}
        row = PostgresRow(row_dict)
        repr_str = repr(row)
        assert "PostgresRow" in repr_str
        assert "id" in repr_str or "1" in repr_str


class TestPostgresConnection:
    """Test PostgresConnection class."""

    @pytest.fixture
    def mock_connection(self):
        """Create a mock psycopg2 connection."""
        conn = MagicMock()
        conn.autocommit = False
        return conn

    @pytest.fixture
    def mock_cursor(self):
        """Create a mock psycopg2 cursor."""
        cursor = MagicMock()
        cursor.execute = Mock()
        cursor.fetchone = Mock(return_value=None)
        cursor.fetchall = Mock(return_value=[])
        cursor.rowcount = 0
        return cursor

    def test_postgres_connection_initialization(self, mock_connection):
        """Test PostgresConnection initialization."""
        mock_cursor = MagicMock()
        mock_connection.cursor = Mock(return_value=mock_cursor)
        conn = PostgresConnection(mock_connection)
        # Verify initialization using public API instead of accessing protected member
        # Test that the connection works by calling cursor() and verifying it uses the mock
        result = conn.cursor()
        assert result == mock_cursor
        mock_connection.cursor.assert_called_once()
        assert mock_connection.autocommit is False

    def test_postgres_connection_execute(self, mock_connection, mock_cursor):
        """Test PostgresConnection.execute()."""
        from psycopg2.extras import RealDictCursor

        mock_connection.cursor = Mock(return_value=mock_cursor)
        conn = PostgresConnection(mock_connection)

        result = conn.execute("SELECT * FROM test WHERE id = %s", (1,))
        assert isinstance(result, PostgresCursor)
        mock_connection.cursor.assert_called_once_with(cursor_factory=RealDictCursor)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test WHERE id = %s", (1,))

    def test_postgres_connection_execute_no_params(self, mock_connection, mock_cursor):
        """Test PostgresConnection.execute() without parameters."""

        mock_connection.cursor = Mock(return_value=mock_cursor)
        conn = PostgresConnection(mock_connection)

        result = conn.execute("SELECT * FROM test")
        assert isinstance(result, PostgresCursor)
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test", None)

    def test_postgres_connection_cursor(self, mock_connection, mock_cursor):
        """Test PostgresConnection.cursor()."""
        from psycopg2.extras import RealDictCursor

        mock_connection.cursor = Mock(return_value=mock_cursor)
        conn = PostgresConnection(mock_connection)

        result = conn.cursor()
        assert result == mock_cursor
        mock_connection.cursor.assert_called_once_with(cursor_factory=RealDictCursor)

    def test_postgres_connection_cursor_with_factory(self, mock_connection, mock_cursor):
        """Test PostgresConnection.cursor() with custom factory."""
        custom_factory = Mock()
        mock_connection.cursor = Mock(return_value=mock_cursor)
        conn = PostgresConnection(mock_connection)

        result = conn.cursor(cursor_factory=custom_factory)
        assert result == mock_cursor
        mock_connection.cursor.assert_called_once_with(cursor_factory=custom_factory)

    def test_postgres_connection_commit(self, mock_connection):
        """Test PostgresConnection.commit()."""
        conn = PostgresConnection(mock_connection)
        conn.commit()
        mock_connection.commit.assert_called_once()

    def test_postgres_connection_rollback(self, mock_connection):
        """Test PostgresConnection.rollback()."""
        conn = PostgresConnection(mock_connection)
        conn.rollback()
        mock_connection.rollback.assert_called_once()

    def test_postgres_connection_close(self, mock_connection):
        """Test PostgresConnection.close()."""
        conn = PostgresConnection(mock_connection)
        conn.close()
        mock_connection.close.assert_called_once()

    def test_postgres_connection_context_manager_success(self, mock_connection):
        """Test PostgresConnection as context manager (success)."""
        with PostgresConnection(mock_connection) as conn:
            assert isinstance(conn, PostgresConnection)
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()
        mock_connection.rollback.assert_not_called()

    def test_postgres_connection_context_manager_exception(self, mock_connection):
        """Test PostgresConnection as context manager (exception)."""
        with pytest.raises(ValueError):
            with PostgresConnection(mock_connection):
                raise ValueError("Test error")
        mock_connection.rollback.assert_called_once()
        mock_connection.close.assert_called_once()
        mock_connection.commit.assert_not_called()


class TestPostgresCursor:
    """Test PostgresCursor class."""

    @pytest.fixture
    def mock_cursor(self):
        """Create a mock psycopg2 cursor."""
        cursor = MagicMock()
        return cursor

    def test_postgres_cursor_initialization(self, mock_cursor):
        """Test PostgresCursor initialization."""
        mock_cursor.rowcount = 5
        pg_cursor = PostgresCursor(mock_cursor)
        # Verify initialization using public API instead of accessing protected member
        # Test that the cursor works by calling rowcount() and verifying it uses the mock
        assert pg_cursor.rowcount() == 5

    def test_postgres_cursor_fetchone_with_row(self, mock_cursor):
        """Test PostgresCursor.fetchone() with row."""
        row_data = {"id": 1, "name": "test"}
        # Use the actual dict - dict() constructor works with dict objects
        mock_cursor.fetchone = Mock(return_value=row_data)

        pg_cursor = PostgresCursor(mock_cursor)
        result = pg_cursor.fetchone()
        assert isinstance(result, PostgresRow)
        assert result["id"] == 1
        assert result["name"] == "test"

    def test_postgres_cursor_fetchone_none(self, mock_cursor):
        """Test PostgresCursor.fetchone() with None."""
        mock_cursor.fetchone = Mock(return_value=None)
        pg_cursor = PostgresCursor(mock_cursor)
        result = pg_cursor.fetchone()
        assert result is None

    def test_postgres_cursor_fetchall_with_rows(self, mock_cursor):
        """Test PostgresCursor.fetchall() with rows."""
        row1_data = {"id": 1, "name": "test1"}
        row2_data = {"id": 2, "name": "test2"}
        # Use actual dicts - dict() constructor works with dict objects
        mock_cursor.fetchall = Mock(return_value=[row1_data, row2_data])

        pg_cursor = PostgresCursor(mock_cursor)
        result = pg_cursor.fetchall()
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], PostgresRow)
        assert isinstance(result[1], PostgresRow)
        assert result[0]["id"] == 1
        assert result[1]["id"] == 2

    def test_postgres_cursor_fetchall_empty(self, mock_cursor):
        """Test PostgresCursor.fetchall() with empty result."""
        mock_cursor.fetchall = Mock(return_value=[])
        pg_cursor = PostgresCursor(mock_cursor)
        result = pg_cursor.fetchall()
        assert isinstance(result, list)
        assert len(result) == 0

    def test_postgres_cursor_rowcount(self, mock_cursor):
        """Test PostgresCursor.rowcount()."""
        mock_cursor.rowcount = 42
        pg_cursor = PostgresCursor(mock_cursor)
        result = pg_cursor.rowcount()
        assert result == 42


class TestPostgresConnectionPool:
    """Test PostgresConnectionPool class."""

    def test_is_postgres_url_true(self):
        """Test is_postgres_url() with PostgreSQL URL."""
        assert is_postgres_url("postgresql://user:pass@host/db") is True
        assert is_postgres_url("postgresql+psycopg2://user:pass@host/db") is True
        assert is_postgres_url("postgresql+asyncpg://user:pass@host/db") is True

    def test_is_postgres_url_false(self):
        """Test is_postgres_url() with non-PostgreSQL URL."""
        assert is_postgres_url("sqlite:///test.db") is False
        assert is_postgres_url("mysql://user:pass@host/db") is False

    @patch("server.postgres_adapter.ThreadedConnectionPool")
    def test_get_pool_creates_new_pool(self, mock_pool_class):
        """Test get_pool() creates new pool."""
        mock_pool = MagicMock()
        mock_pool_class.return_value = mock_pool
        # Use unique database URL to avoid conflicts with other tests
        # instead of accessing protected _pools.clear()
        database_url = f"postgresql://user:pass@host/db_{id(self)}"

        result = PostgresConnectionPool.get_pool(database_url)
        assert result == mock_pool
        mock_pool_class.assert_called_once()
        # Verify pool was stored by calling get_pool() again and verifying reuse
        # instead of accessing protected _pools directly
        result2 = PostgresConnectionPool.get_pool(database_url)
        assert result2 == mock_pool
        mock_pool_class.assert_called_once()  # Should not create a new pool

    @patch("server.postgres_adapter.ThreadedConnectionPool")
    def test_get_pool_reuses_existing_pool(self, mock_pool_class):
        """Test get_pool() reuses existing pool."""
        mock_pool = MagicMock()
        mock_pool_class.return_value = mock_pool
        # Use unique database URL to avoid conflicts with other tests
        # instead of accessing protected _pools.clear()
        database_url = f"postgresql://user:pass@host/db_{id(self)}"

        # Call get_pool() once to create and store the pool
        result1 = PostgresConnectionPool.get_pool(database_url)
        assert result1 == mock_pool
        mock_pool_class.assert_called_once()

        # Call get_pool() again and verify it reuses the existing pool
        # instead of accessing protected _pools directly
        result2 = PostgresConnectionPool.get_pool(database_url)
        assert result2 == mock_pool
        assert result2 is result1  # Verify it's the same instance
        mock_pool_class.assert_called_once()  # Should not create a new pool

    @patch("server.postgres_adapter.ThreadedConnectionPool")
    def test_get_pool_normalizes_url(self, mock_pool_class):
        """Test get_pool() normalizes database URL."""
        mock_pool = MagicMock()
        mock_pool_class.return_value = mock_pool
        # Use unique database URL to avoid conflicts with other tests
        # instead of accessing protected _pools.clear()
        database_url = f"postgresql+psycopg2://user:pass@host/db_{id(self)}"
        PostgresConnectionPool.get_pool(database_url)

        # Should normalize to postgresql://
        call_args = mock_pool_class.call_args
        dsn_arg = call_args[1]["dsn"]
        assert dsn_arg.startswith("postgresql://")
        assert not dsn_arg.startswith("postgresql+psycopg2://")

    @patch("server.postgres_adapter.ThreadedConnectionPool")
    def test_get_connection_context_manager(self, mock_pool_class):
        """Test get_connection() context manager."""
        mock_pool = MagicMock()
        mock_conn = MagicMock()
        mock_pool.getconn = Mock(return_value=mock_conn)
        mock_pool_class.return_value = mock_pool
        # Use unique database URL to avoid conflicts with other tests
        # instead of accessing protected _pools.clear()
        database_url = f"postgresql://user:pass@host/db_{id(self)}"

        with PostgresConnectionPool.get_connection(database_url) as conn:
            assert isinstance(conn, PostgresConnection)
            mock_pool.getconn.assert_called_once()

        mock_pool.putconn.assert_called_once_with(mock_conn)

    @patch("server.postgres_adapter.ThreadedConnectionPool")
    def test_get_connection_context_manager_exception(self, mock_pool_class):
        """Test get_connection() context manager with exception."""
        mock_pool = MagicMock()
        mock_conn = MagicMock()
        mock_pool.getconn = Mock(return_value=mock_conn)
        mock_pool_class.return_value = mock_pool
        # Use unique database URL to avoid conflicts with other tests
        # instead of accessing protected _pools.clear()
        database_url = f"postgresql://user:pass@host/db_{id(self)}"

        with pytest.raises(ValueError):
            with PostgresConnectionPool.get_connection(database_url):
                raise ValueError("Test error")

        mock_pool.putconn.assert_called_once_with(mock_conn)


class TestUtilityFunctions:
    """Test utility functions."""

    @patch("server.postgres_adapter.psycopg2.connect")
    def test_connect_postgres(self, mock_connect):
        """Test connect_postgres()."""
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        database_url = "postgresql://user:pass@host/db"

        result = connect_postgres(database_url)
        assert isinstance(result, PostgresConnection)
        mock_connect.assert_called_once_with("postgresql://user:pass@host/db")

    @patch("server.postgres_adapter.psycopg2.connect")
    def test_connect_postgres_with_driver_prefix(self, mock_connect):
        """Test connect_postgres() with driver prefix."""
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        database_url = "postgresql+psycopg2://user:pass@host/db"

        result = connect_postgres(database_url)
        assert isinstance(result, PostgresConnection)
        # Should normalize URL
        call_args = mock_connect.call_args[0][0]
        assert call_args.startswith("postgresql://")
        assert not call_args.startswith("postgresql+psycopg2://")

    def test_convert_sqlite_to_postgres_query_basic(self):
        """Test convert_sqlite_to_postgres_query() basic conversion."""
        sqlite_query = "SELECT * FROM test WHERE id = ? AND name = ?"
        result = convert_sqlite_to_postgres_query(sqlite_query)
        assert result == "SELECT * FROM test WHERE id = %s AND name = %s"

    def test_convert_sqlite_to_postgres_query_no_params(self):
        """Test convert_sqlite_to_postgres_query() with no parameters."""
        sqlite_query = "SELECT * FROM test"
        result = convert_sqlite_to_postgres_query(sqlite_query)
        assert result == "SELECT * FROM test"

    def test_convert_sqlite_to_postgres_query_insert_replace(self):
        """Test convert_sqlite_to_postgres_query() with INSERT OR REPLACE."""
        sqlite_query = "INSERT OR REPLACE INTO test (id, name) VALUES (?, ?)"
        result = convert_sqlite_to_postgres_query(sqlite_query)
        # Should replace ? with %s but not handle INSERT OR REPLACE
        assert "%s" in result
        assert "?" not in result
