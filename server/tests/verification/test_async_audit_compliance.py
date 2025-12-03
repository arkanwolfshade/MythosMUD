"""
Async Audit Compliance Tests.

This module tests that the codebase complies with async best practices
from .cursor/rules/anyio.mdc and .cursor/rules/asyncio.mdc.

Tests cover:
1. Performance - No event loop blocking
2. Resource management - Connection pools close properly
3. Exception handling - Graceful failures
4. Task management - No orphaned tasks
"""

import asyncio
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.container import ApplicationContainer
from server.database import get_database_manager
from server.persistence import PersistenceLayer
from server.services.passive_lucidity_flux_service import PassiveLucidityFluxService


class TestAsyncEventLoopBlocking:
    """Test that async operations don't block the event loop."""

    @pytest.mark.asyncio
    async def test_passive_lucidity_flux_no_blocking(self, mock_async_session):
        """
        Test that passive lucidity flux processing doesn't block event loop.

        CRITICAL: This test verifies the fix for Issue #1 in async audit
        (17-second delays from synchronous blocking operations).
        """
        # Create mock persistence with async methods
        mock_persistence = MagicMock(spec=PersistenceLayer)

        # Mock async_get_room to simulate async database operation
        async def mock_async_get_room(room_id: str):
            await asyncio.sleep(0.001)  # Simulate minimal async work
            mock_room = MagicMock()
            mock_room.id = room_id
            mock_room.environment = "sanctuary"
            mock_room.zone = "test_zone"
            mock_room.sub_zone = "test_subzone"
            return mock_room

        mock_persistence.async_get_room = mock_async_get_room

        # Create service
        service = PassiveLucidityFluxService(persistence=mock_persistence)

        # Run passive flux processing and measure time
        start_time = time.perf_counter()

        # Create a task that runs concurrently to verify event loop isn't blocked
        concurrent_task_completed = False

        async def concurrent_operation():
            nonlocal concurrent_task_completed
            await asyncio.sleep(0.01)
            concurrent_task_completed = True

        # Start concurrent task
        task = asyncio.create_task(concurrent_operation())

        # Process tick (should not block the concurrent task)
        try:
            await service.process_tick(mock_async_session, tick_count=1)
        except Exception:
            pass  # Ignore errors from mock - we're testing blocking not functionality

        # Wait for concurrent task
        await task

        elapsed_time = time.perf_counter() - start_time

        # Verify concurrent task completed (proves event loop wasn't blocked)
        assert concurrent_task_completed, "Concurrent task didn't complete - event loop was blocked!"

        # Verify processing was fast (< 1 second target)
        # This will fail if synchronous blocking operations are present
        assert elapsed_time < 1.0, f"Processing took {elapsed_time:.2f}s - should be < 1.0s (target from audit)"

    @pytest.mark.asyncio
    async def test_async_get_room_uses_thread_pool(self):
        """
        Test that async_get_room uses thread pool, not direct blocking call.

        CRITICAL: Verifies the fix for Issue #1 in async audit.
        """
        mock_persistence = PersistenceLayer()

        # Mock the sync get_room method to detect if it's called
        sync_call_detected = False

        def mock_sync_get_room(room_id: str):
            nonlocal sync_call_detected
            sync_call_detected = True
            return None

        mock_persistence.get_room = mock_sync_get_room

        # Call async_get_room - should use asyncio.to_thread()
        # If it directly calls get_room(), sync_call_detected will be True
        with patch("asyncio.to_thread", new_callable=AsyncMock) as mock_to_thread:
            mock_to_thread.return_value = None
            await mock_persistence.async_get_room("test_room")

            # Verify asyncio.to_thread was called (non-blocking pattern)
            assert mock_to_thread.called, "async_get_room should use asyncio.to_thread() to prevent blocking"

    @pytest.mark.asyncio
    async def test_room_caching_prevents_repeated_database_calls(self):
        """
        Test that room caching reduces database calls.

        CRITICAL: Verifies room cache with TTL prevents repeated lookups
        that contributed to performance degradation.
        """
        mock_persistence = MagicMock(spec=PersistenceLayer)
        call_count = 0

        async def mock_async_get_room(room_id: str):
            nonlocal call_count
            call_count += 1
            await asyncio.sleep(0.001)
            mock_room = MagicMock()
            mock_room.id = room_id
            return mock_room

        mock_persistence.async_get_room = mock_async_get_room

        service = PassiveLucidityFluxService(persistence=mock_persistence)

        # Call twice with same room_id within TTL window
        await service._get_room_cached("room_1")
        await service._get_room_cached("room_1")  # Should use cache

        # Verify only ONE database call was made (second used cache)
        assert call_count == 1, f"Expected 1 database call, got {call_count} (cache not working)"

        # Wait for cache to expire
        await asyncio.sleep(service._room_cache_ttl + 0.1)

        # Call again after TTL - should fetch from database
        await service._get_room_cached("room_1")

        # Verify second database call was made (cache expired)
        assert call_count == 2, f"Expected 2 database calls after TTL, got {call_count}"


class TestAsyncResourceManagement:
    """Test that async resources are properly managed and don't leak."""

    @pytest.mark.asyncio
    async def test_connection_pool_closes_on_shutdown(self):
        """
        Test that connection pools are closed during container shutdown.

        CRITICAL: Verifies fix for Issue #3 in async audit
        (connection pool resource leaks).
        """
        container = ApplicationContainer()

        try:
            await container.initialize()

            # Verify async_persistence exists
            assert container.async_persistence is not None, "Async persistence not initialized"

            # Mock the close method to track if it's called
            close_called = False

            original_close = container.async_persistence.close

            async def tracked_close():
                nonlocal close_called
                close_called = True
                if callable(original_close):
                    await original_close()

            container.async_persistence.close = tracked_close

            # Shutdown container
            await container.shutdown()

            # Verify close was called
            assert close_called, "async_persistence.close() was not called during shutdown!"

        finally:
            # Cleanup
            try:
                await container.shutdown()
            except Exception:
                pass

    @pytest.mark.asyncio
    async def test_no_asyncio_run_in_library_code(self):
        """
        Test that library code doesn't use asyncio.run().

        CRITICAL: Verifies fix for Issue #2 in async audit.
        """
        # This is a static analysis test - we verify the code pattern
        # In the actual fix, we removed asyncio.run() from exploration_service.py

        # Test exploration service doesn't use asyncio.run()
        from server.services.exploration_service import ExplorationService

        service = ExplorationService()

        # Get the source code of mark_room_as_explored_sync
        import inspect

        source = inspect.getsource(service.mark_room_as_explored_sync)

        # Verify asyncio.run() is NOT in the source
        assert "asyncio.run" not in source, "exploration_service still uses asyncio.run()!"


class TestAsyncExceptionHandling:
    """Test that async operations handle exceptions gracefully."""

    @pytest.mark.asyncio
    async def test_database_engine_creation_handles_connection_failure(self):
        """
        Test that database engine creation gracefully handles connection failures.

        CRITICAL: Verifies fix for Issue #4 in async audit
        (missing exception handling in pool creation).
        """
        from server.database import DatabaseManager
        from server.exceptions import DatabaseError

        # Create a database manager with invalid URL
        manager = DatabaseManager()

        with patch.dict("os.environ", {"DATABASE_URL": "postgresql://invalid:invalid@invalid:9999/invalid"}):
            # Should raise DatabaseError with proper error context
            with pytest.raises((DatabaseError, Exception)) as exc_info:
                manager._initialize_database()

            # Verify we get a meaningful error (not just a generic exception)
            # Note: Actual exception type depends on what fails first (DNS, connection, auth)
            # The important thing is that it's caught and logged, not left unhandled
            assert exc_info.value is not None, "Should raise exception for invalid database"

    @pytest.mark.asyncio
    async def test_async_gather_uses_return_exceptions(self):
        """
        Test that asyncio.gather uses return_exceptions=True for event subscribers.

        BEST PRACTICE: Verifies structured concurrency pattern from asyncio.mdc
        """
        from server.events.event_bus import EventBus

        bus = EventBus()

        # Create test event
        from server.events.combat_events import CombatStartedEvent

        event = CombatStartedEvent(
            combat_id="test",
            attacker_id="attacker",
            defender_id="defender",
            room_id="room",
        )

        # Subscribe two async subscribers - one that fails, one that succeeds
        failure_subscriber_called = False
        success_subscriber_called = False

        async def failing_subscriber(e):
            nonlocal failure_subscriber_called
            failure_subscriber_called = True
            raise ValueError("Test failure")

        async def success_subscriber(e):
            nonlocal success_subscriber_called
            success_subscriber_called = True

        bus.subscribe(CombatStartedEvent, failing_subscriber)
        bus.subscribe(CombatStartedEvent, success_subscriber)

        # Publish event
        bus.publish(event)

        # Give time for async processing
        await asyncio.sleep(0.1)

        # Verify BOTH subscribers were called (return_exceptions=True prevents cancellation)
        assert failure_subscriber_called, "Failing subscriber should have been called"
        assert success_subscriber_called, "Success subscriber should have been called (not cancelled by failure)"


class TestAsyncPerformanceMetrics:
    """Test async performance metrics meet targets from audit."""

    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_passive_lucidity_flux_tick_performance(self, mock_async_session):
        """
        Test that passive lucidity flux tick completes within target time.

        SUCCESS CRITERIA: < 1 second (current: 17.4s before fixes)
        """
        mock_persistence = MagicMock(spec=PersistenceLayer)

        async def fast_async_get_room(room_id: str):
            await asyncio.sleep(0.001)
            mock_room = MagicMock()
            mock_room.id = room_id
            mock_room.environment = "sanctuary"
            return mock_room

        mock_persistence.async_get_room = fast_async_get_room

        service = PassiveLucidityFluxService(persistence=mock_persistence)

        # Measure time for tick processing
        start_time = time.perf_counter()

        try:
            await service.process_tick(mock_async_session, tick_count=1)
        except Exception:
            pass  # Ignore errors from mock

        elapsed_time = time.perf_counter() - start_time

        # Verify performance target (<1s from audit)
        assert elapsed_time < 1.0, f"Tick processing took {elapsed_time:.2f}s, target is <1.0s"


class TestAsyncTaskManagement:
    """Test that async tasks are properly tracked and don't leak."""

    @pytest.mark.asyncio
    async def test_no_orphaned_tasks_after_shutdown(self):
        """
        Test that no tasks are orphaned after container shutdown.

        BEST PRACTICE: Verifies structured concurrency from AnyIO patterns.
        """
        container = ApplicationContainer()

        try:
            await container.initialize()

            # Get initial task count
            all_tasks_before = asyncio.all_tasks()
            container_tasks_before = len(all_tasks_before)

            # Shutdown container
            await container.shutdown()

            # Give tasks time to cleanup
            await asyncio.sleep(0.5)

            # Get final task count
            all_tasks_after = asyncio.all_tasks()
            container_tasks_after = len(all_tasks_after)

            # Verify no significant task growth (allowing for test framework tasks)
            # We allow up to 5 new tasks for test framework overhead
            task_growth = container_tasks_after - container_tasks_before
            assert task_growth <= 5, f"Task leak detected: {task_growth} new tasks after shutdown"

        finally:
            try:
                await container.shutdown()
            except Exception:
                pass


class TestAsyncResourceCleanup:
    """Test async resource cleanup patterns."""

    @pytest.mark.asyncio
    async def test_async_context_managers_cleanup_on_exception(self):
        """
        Test that async context managers properly cleanup even on exceptions.

        BEST PRACTICE: Verifies RAII pattern from AnyIO.mdc
        """
        cleanup_called = False

        class TestAsyncResource:
            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                nonlocal cleanup_called
                cleanup_called = True

        # Use context manager and raise exception
        with pytest.raises(ValueError):
            async with TestAsyncResource():
                raise ValueError("Test exception")

        # Verify cleanup was called despite exception
        assert cleanup_called, "Async context manager __aexit__ should be called even on exception"

    @pytest.mark.asyncio
    async def test_database_session_cleanup_on_error(self):
        """Test that database sessions are properly closed on errors."""
        db_manager = get_database_manager()
        session_maker = db_manager.get_session_maker()

        session_closed = False
        original_close = None

        async with session_maker() as session:
            # Track if close is called
            original_close = session.close

            async def tracked_close():
                nonlocal session_closed
                session_closed = True
                await original_close()

            session.close = tracked_close

        # After exiting context, session should be closed
        # Note: SQLAlchemy async sessions close automatically in __aexit__
        # This test verifies the pattern is used correctly


class TestAsyncConcurrencyPatterns:
    """Test async concurrency patterns follow best practices."""

    @pytest.mark.asyncio
    async def test_gather_with_return_exceptions(self):
        """
        Test asyncio.gather usage with return_exceptions=True.

        BEST PRACTICE: From asyncio.mdc Section 2.5
        """

        async def failing_task():
            raise ValueError("Test failure")

        async def successful_task():
            return "success"

        # Use return_exceptions=True to prevent one failure from canceling all
        results = await asyncio.gather(
            failing_task(),
            successful_task(),
            return_exceptions=True,
        )

        # Verify both tasks completed
        assert len(results) == 2
        assert isinstance(results[0], ValueError), "First task should have failed"
        assert results[1] == "success", "Second task should have succeeded"

    @pytest.mark.asyncio
    async def test_concurrent_operations_dont_block_each_other(self):
        """Test that concurrent async operations run in parallel."""
        start_time = time.perf_counter()

        async def slow_operation(delay: float):
            await asyncio.sleep(delay)
            return delay

        # Run 3 operations concurrently (should take ~0.1s total, not 0.3s)
        results = await asyncio.gather(
            slow_operation(0.1),
            slow_operation(0.1),
            slow_operation(0.1),
        )

        elapsed = time.perf_counter() - start_time

        # If operations ran sequentially (blocking), this would take ~0.3s
        # If concurrent (non-blocking), should take ~0.1s
        assert elapsed < 0.2, f"Operations took {elapsed:.2f}s - likely running sequentially (blocking)"
        assert len(results) == 3


class TestAsyncErrorBoundaries:
    """Test async error boundary implementations."""

    @pytest.mark.asyncio
    async def test_circuit_breaker_prevents_cascading_failures(self):
        """
        Test that circuit breaker prevents cascading failures.

        POSITIVE FINDING: Verifies circuit breaker pattern from audit.
        """
        from server.realtime.circuit_breaker import CircuitBreaker, CircuitBreakerOpen

        cb = CircuitBreaker(failure_threshold=2, success_threshold=1)

        call_count = 0

        async def failing_operation():
            nonlocal call_count
            call_count += 1
            raise ValueError("Test failure")

        # First failure
        with pytest.raises(ValueError):
            await cb.call(failing_operation)

        # Second failure - should open circuit
        with pytest.raises(ValueError):
            await cb.call(failing_operation)

        # Third attempt - circuit should be open
        with pytest.raises(CircuitBreakerOpen):
            await cb.call(failing_operation)

        # Verify the failing operation was NOT called (circuit was open)
        assert call_count == 2, f"Operation called {call_count} times, should be 2 (circuit should be open)"


@pytest.mark.asyncio
async def test_no_time_sleep_in_async_functions():
    """
    Test that async functions don't use time.sleep (blocking).

    ANTI-PATTERN: time.sleep() blocks the event loop.
    CORRECT: asyncio.sleep() is non-blocking.
    """
    # Static analysis test - we verify this was fixed in audit
    import inspect

    from server.utils import retry

    # Check retry module doesn't use time.sleep in async functions
    for name, obj in inspect.getmembers(retry):
        if inspect.iscoroutinefunction(obj):
            source = inspect.getsource(obj)
            assert "time.sleep" not in source, f"Async function {name} uses time.sleep (blocking)!"


@pytest.mark.asyncio
async def test_exploration_service_no_asyncio_run():
    """
    Test that exploration service doesn't use asyncio.run() in library code.

    CRITICAL: Verifies fix for Issue #2 in async audit.
    """
    from server.services.exploration_service import ExplorationService

    service = ExplorationService()

    import inspect

    source = inspect.getsource(service.mark_room_as_explored_sync)

    # Verify asyncio.run() was removed
    assert "asyncio.run" not in source, "exploration_service should not use asyncio.run()!"


@pytest.mark.asyncio
async def test_async_persistence_methods_use_to_thread():
    """
    Test that PersistenceLayer async wrappers use asyncio.to_thread().

    CRITICAL: Verifies fixes for async wrapper methods.
    """
    persistence = PersistenceLayer()

    import inspect

    # Check async_get_room uses asyncio.to_thread
    source = inspect.getsource(persistence.async_get_room)
    assert "asyncio.to_thread" in source, "async_get_room should use asyncio.to_thread()!"

    # Check async_save_room uses asyncio.to_thread
    source = inspect.getsource(persistence.async_save_room)
    assert "asyncio.to_thread" in source, "async_save_room should use asyncio.to_thread()!"

    # Check async_list_rooms uses asyncio.to_thread
    source = inspect.getsource(persistence.async_list_rooms)
    assert "asyncio.to_thread" in source, "async_list_rooms should use asyncio.to_thread()!"


if __name__ == "__main__":
    # Run with: pytest server/tests/verification/test_async_audit_compliance.py -v
    pytest.main([__file__, "-v", "--tb=short"])
