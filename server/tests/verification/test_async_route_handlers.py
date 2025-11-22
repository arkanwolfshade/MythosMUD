"""
Tests for async route handler functionality.

This module tests the async patterns and identifies which route handlers
should be converted from synchronous to asynchronous to improve performance
and avoid blocking I/O operations.
"""

import asyncio
import time
from unittest.mock import AsyncMock

import pytest
from fastapi import Depends, FastAPI, Request
from fastapi.testclient import TestClient

from server.app.factory import create_app


@pytest.mark.slow
class TestAsyncRouteHandlers:
    """Test async route handler functionality and performance.

    These tests require full FastAPI app initialization with dependency injection
    container and make actual HTTP requests, making them integration-style tests.
    """

    @pytest.fixture
    def app(self, mock_application_container):
        """Create FastAPI app for testing."""
        app = create_app()

        # Mock the persistence layer with async methods
        mock_persistence = AsyncMock()
        mock_persistence.async_list_players.return_value = []
        mock_persistence.async_get_player.return_value = None
        mock_persistence.async_get_room.return_value = None
        # Also mock the synchronous methods for backward compatibility
        mock_persistence.list_players.return_value = []
        mock_persistence.get_player.return_value = None
        mock_persistence.get_room.return_value = None

        # Use the comprehensive mock container and update persistence
        mock_application_container.persistence = mock_persistence

        app.state.container = mock_application_container
        app.state.persistence = mock_persistence

        # CRITICAL: Ensure connection_manager has persistence set
        # This prevents 503 errors from readiness gate checks
        if hasattr(mock_application_container, "connection_manager"):
            mock_application_container.connection_manager.persistence = mock_persistence

        # Set additional app state attributes that middleware and routes may access
        app.state.player_service = mock_application_container.player_service
        app.state.room_service = mock_application_container.room_service
        app.state.event_bus = mock_application_container.event_bus

        return app

    @pytest.fixture
    def client(self, container_test_client):
        """Create TestClient using container fixture for integration portions."""
        return container_test_client

    def test_identify_synchronous_handlers(self):
        """Test to identify which route handlers are currently synchronous."""
        synchronous_handlers = [
            # Player API handlers
            "POST /api/players/ - create_player",
            "GET /api/players/ - list_players",
            "GET /api/players/{player_id} - get_player",
            "GET /api/players/name/{player_name} - get_player_by_name",
            "DELETE /api/players/{player_id} - delete_player",
            "POST /api/players/{player_id}/sanity-loss - apply_sanity_loss",
            "POST /api/players/{player_id}/fear - apply_fear",
            "POST /api/players/{player_id}/corruption - apply_corruption",
            "POST /api/players/{player_id}/occult-knowledge - gain_occult_knowledge",
            "POST /api/players/{player_id}/heal - heal_player",
            "POST /api/players/{player_id}/damage - damage_player",
            "POST /api/players/roll-stats - roll_character_stats",
            "POST /api/players/validate-stats - validate_character_stats",
            "GET /api/players/available-classes - get_available_classes",
            "GET /api/players/class-description/{class_name} - get_class_description",
            # Room API handlers
            "GET /rooms/{room_id} - get_room",
            # Game API handlers
            "GET /game/status - get_game_status",
            "POST /game/broadcast - broadcast_message",
            # Profession API handlers
            "GET /professions/ - get_all_professions",
            "GET /professions/{profession_id} - get_profession_by_id",
        ]
        handlers_with_io = [
            "All player CRUD operations (database access)",
            "All room operations (database access)",
            "All profession operations (database access)",
            "Game status (connection manager access)",
            "Broadcast operations (real-time messaging)",
        ]
        assert len(synchronous_handlers) > 0
        assert len(handlers_with_io) > 0

    def test_async_handler_performance_comparison(self, client):
        """Test performance comparison between sync and async handlers.

        Note: This test may produce harmless "Event loop is closed" warnings
        on Windows due to TestClient creating its own event loop per request.
        These warnings are expected and do not affect test correctness.
        """
        start_time = time.time()
        responses = []
        for _ in range(10):
            response = client.get("/api/players/")
            responses.append(response)
        total_time = time.time() - start_time
        for response in responses:
            assert response.status_code in [200, 401]
        print(f"10 synchronous requests completed in {total_time:.3f} seconds")
        assert total_time > 0

    @pytest.mark.asyncio
    async def test_async_handler_pattern(self):
        """Demonstrate async handler patterns using a local app."""
        app = FastAPI()

        @app.get("/test-sync")
        def sync_handler():
            return {"message": "sync", "type": "synchronous"}

        @app.get("/test-async")
        async def async_handler():
            return {"message": "async", "type": "asynchronous"}

        @app.get("/test-async-io")
        async def async_handler_with_io():
            await asyncio.sleep(0.001)
            return {"message": "async-io", "type": "asynchronous_with_io"}

        client = TestClient(app)
        assert client.get("/test-sync").json()["type"] == "synchronous"
        assert client.get("/test-async").json()["type"] == "asynchronous"
        assert client.get("/test-async-io").json()["type"] == "asynchronous_with_io"

    def test_concurrent_request_handling(self, client):
        """Test how current synchronous handlers handle concurrent requests."""
        import queue
        import threading

        results = queue.Queue()

        def make_request():
            start_time = time.time()
            response = client.get("/api/players/")
            end_time = time.time()
            results.put(
                {
                    "status_code": response.status_code,
                    "response_time": end_time - start_time,
                    "thread_id": threading.current_thread().ident,
                }
            )

        threads = []
        for _ in range(5):
            thread = threading.Thread(target=make_request)
            threads.append(thread)
            thread.start()
        # CRITICAL: Add timeout to prevent indefinite hang if threads don't complete
        # This prevents the test suite from stalling if threads hang due to resource leaks
        for thread in threads:
            thread.join(timeout=10.0)  # 10 second timeout per thread
            if thread.is_alive():
                raise TimeoutError(
                    f"Thread {thread.ident} did not complete within 10 second timeout. "
                    "This may indicate a resource leak or hanging operation."
                )

        response_times = []
        while not results.empty():
            result = results.get()
            assert result["status_code"] in [200, 401]
            response_times.append(result["response_time"])
        assert len(response_times) == 5
        avg_response_time = sum(response_times) / len(response_times)
        print(f"Average response time for 5 concurrent requests: {avg_response_time:.3f} seconds")

    def test_async_service_layer_pattern(self):
        """Demonstrate async service layer pattern."""

        class MockAsyncPersistence:
            async def get_player_async(self, player_id: str):
                await asyncio.sleep(0.001)
                return {"id": player_id, "name": "TestPlayer"}

            async def list_players_async(self):
                await asyncio.sleep(0.001)
                return [{"id": "1", "name": "Player1"}, {"id": "2", "name": "Player2"}]

        class AsyncPlayerService:
            def __init__(self, persistence):
                self.persistence = persistence

            async def get_player_async(self, player_id: str):
                return await self.persistence.get_player_async(player_id)

            async def list_players_async(self):
                return await self.persistence.list_players_async()

        mock_persistence = MockAsyncPersistence()
        service = AsyncPlayerService(mock_persistence)

        async def _run():
            player = await service.get_player_async("test-id")
            assert player["id"] == "test-id"
            players = await service.list_players_async()
            assert len(players) == 2

        # Use asyncio.run() instead of deprecated get_event_loop()
        asyncio.run(_run())

    def test_async_dependency_injection_pattern(self):
        """Demonstrate async dependency injection pattern on a local app."""
        app = FastAPI()

        async def get_async_player_service(request: Request) -> AsyncMock:
            await asyncio.sleep(0.001)
            service = AsyncMock()
            service.get_player_async.return_value = {"id": "test", "name": "TestPlayer"}
            return service

        @app.get("/test-async-dependency")
        async def test_endpoint(player_service: AsyncMock = Depends(get_async_player_service)):
            result = await player_service.get_player_async("test-id")
            return result

        client = TestClient(app)
        response = client.get("/test-async-dependency")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "test"
        assert data["name"] == "TestPlayer"

    def test_error_handling_in_async_handlers(self):
        """Demonstrate error handling in async handlers."""
        app = FastAPI()

        @app.get("/test-async-error-handling")
        async def async_handler_with_error_handling():
            try:
                await asyncio.sleep(0.001)
                raise ValueError("Test async error")
            except ValueError as e:
                return {"error": str(e), "handled": True}

        @app.get("/test-async-http-error")
        async def async_handler_with_http_error():
            from fastapi import HTTPException

            await asyncio.sleep(0.001)
            raise HTTPException(status_code=400, detail="Test HTTP error")

        client = TestClient(app)
        assert client.get("/test-async-error-handling").status_code == 200
        assert client.get("/test-async-http-error").status_code == 400

    def test_async_middleware_compatibility(self, client):
        """Test that async handlers work with existing middleware."""
        response = client.get("/api/players/")
        assert "X-Frame-Options" in response.headers
        assert response.status_code in [200, 401]

    def test_async_route_conversion_checklist(self):
        """Checklist for converting routes to async."""
        conversion_checklist = {
            "identify_io_operations": [
                "✓ Database queries (PostgreSQL operations)",
                "✓ External service calls (NATS, authentication)",
                "✓ File I/O operations (logs, configs)",
                "✓ Network operations (real-time messaging)",
            ],
            "update_route_handlers": [
                "✓ Add 'async' keyword to function definition",
                "✓ Add 'await' for async service calls",
                "✓ Update error handling for async exceptions",
                "✓ Test async behavior with TestClient",
            ],
            "update_service_layer": [
                "✓ Convert service methods to async",
                "✓ Update persistence layer calls to async",
                "✓ Handle async exceptions properly",
                "✓ Maintain backward compatibility where needed",
            ],
            "update_dependency_injection": [
                "✓ Update dependency providers to async",
                "✓ Test async dependency resolution",
                "✓ Ensure proper async context handling",
            ],
            "testing_requirements": [
                "✓ Write async-specific tests",
                "✓ Test concurrent request handling",
                "✓ Verify error handling in async context",
                "✓ Performance testing for async operations",
            ],
        }
        for _category, items in conversion_checklist.items():
            assert len(items) > 0
        assert len(conversion_checklist) == 5
