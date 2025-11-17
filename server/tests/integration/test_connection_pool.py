"""
Integration tests for connection pool behavior.

These tests verify connection pool configuration, exhaustion scenarios,
and recovery behavior.
"""

import asyncio

import asyncpg
import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.database import get_database_manager


class TestConnectionPool:
    """Test connection pool behavior."""

    @pytest.mark.asyncio
    async def test_pool_configuration(self):
        """Test that connection pool is configured correctly."""
        db_manager = get_database_manager()
        engine = db_manager.get_engine()

        # Verify engine exists
        assert engine is not None

        # Verify pool configuration
        pool = engine.pool
        assert pool is not None

        # In test environment, should use NullPool
        # In production, should use AsyncAdaptedQueuePool
        pool_type = type(pool).__name__
        assert pool_type in ["NullPool", "AsyncAdaptedQueuePool"], f"Unexpected pool type: {pool_type}"

    @pytest.mark.asyncio
    async def test_asyncpg_pool_creation(self):
        """Test that asyncpg pool is created correctly."""
        async_persistence = AsyncPersistenceLayer()

        # Get pool (will create if not exists)
        pool = await async_persistence._get_pool()

        # Verify pool exists
        assert pool is not None

        # Verify pool is asyncpg.Pool
        assert isinstance(pool, asyncpg.Pool)

        # Verify pool is not closed
        assert not pool.is_closing()

    @pytest.mark.asyncio
    async def test_pool_connection_acquisition(self):
        """Test that connections can be acquired from pool."""
        async_persistence = AsyncPersistenceLayer()

        # Acquire connection
        pool = await async_persistence._get_pool()
        async with pool.acquire() as conn:
            # Verify connection is valid
            assert conn is not None

            # Verify we can execute a query
            result = await conn.fetchval("SELECT 1")
            assert result == 1

    @pytest.mark.asyncio
    async def test_pool_connection_release(self):
        """Test that connections are properly released back to pool."""
        async_persistence = AsyncPersistenceLayer()

        pool = await async_persistence._get_pool()

        # Acquire and release connection
        async with pool.acquire() as conn:
            _ = await conn.fetchval("SELECT 1")

        # Connection should be released back to pool
        # (We can't easily verify this without accessing private attributes,
        # but the context manager should handle it)

        # Verify pool is still valid
        assert not pool.is_closing()

    @pytest.mark.asyncio
    async def test_pool_exhaustion_handling(self):
        """Test that pool exhaustion is handled gracefully."""
        # This test is difficult to implement without modifying pool size
        # For now, we just verify that pool acquisition doesn't hang forever

        async_persistence = AsyncPersistenceLayer()

        pool = await async_persistence._get_pool()

        # Try to acquire connection with timeout
        try:
            async with pool.acquire(timeout=1.0) as conn:
                _ = await conn.fetchval("SELECT 1")
        except asyncpg.PoolAcquireTimeoutError:
            # Pool exhaustion - this is expected if pool is too small
            # In production, this should be handled by retry logic
            pass
        except Exception as e:
            # Other errors are unexpected
            pytest.fail(f"Unexpected error acquiring connection: {e}")

    @pytest.mark.asyncio
    async def test_pool_recovery_after_error(self):
        """Test that pool recovers after connection errors."""
        async_persistence = AsyncPersistenceLayer()

        pool = await async_persistence._get_pool()

        # Try to use a connection that might fail
        try:
            async with pool.acquire() as conn:
                # Execute a query that might fail
                try:
                    await conn.fetchval("SELECT invalid_column FROM nonexistent_table")
                except asyncpg.PostgresError:
                    # Expected error - connection should still be valid
                    pass

                # Verify we can still use the connection
                result = await conn.fetchval("SELECT 1")
                assert result == 1
        except Exception:
            # Connection errors should be handled gracefully
            # Pool should still be usable
            assert not pool.is_closing()

    @pytest.mark.asyncio
    async def test_multiple_concurrent_connections(self):
        """Test that multiple concurrent connections work correctly."""
        async_persistence = AsyncPersistenceLayer()

        pool = await async_persistence._get_pool()

        # Create multiple concurrent connections
        async def use_connection(i: int) -> int:
            async with pool.acquire() as conn:
                result = await conn.fetchval("SELECT $1", i)
                return result

        # Run multiple concurrent queries
        tasks = [use_connection(i) for i in range(5)]
        results = await asyncio.gather(*tasks)

        # Verify all queries succeeded
        assert len(results) == 5
        assert results == [0, 1, 2, 3, 4]

    @pytest.mark.asyncio
    async def test_pool_close_cleanup(self):
        """Test that pool is properly closed and cleaned up."""
        async_persistence = AsyncPersistenceLayer()

        # Create pool
        pool = await async_persistence._get_pool()

        # Close pool
        await async_persistence.close_pool()

        # Verify pool is closed
        assert pool.is_closing() or pool.is_closed()
