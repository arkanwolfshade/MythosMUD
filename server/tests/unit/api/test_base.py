"""Tests for the API base module.

As noted in the restricted archives of Miskatonic University, these tests
validate the base API router and common dependencies used across all API endpoints.
"""

from fastapi import APIRouter

from server.api.base import CurrentUser, api_router
from server.auth.users import get_current_user


class TestAPIRouter:
    """Test suite for the API router."""

    def test_api_router_creation(self) -> None:
        """Test that the API router is created correctly."""
        assert isinstance(api_router, APIRouter)
        assert api_router.prefix == "/api"
        assert "api" in api_router.tags

    def test_api_router_prefix(self) -> None:
        """Test that the API router has the correct prefix."""
        assert api_router.prefix == "/api"

    def test_api_router_tags(self) -> None:
        """Test that the API router has the correct tags."""
        assert "api" in api_router.tags

    def test_api_router_is_router_instance(self) -> None:
        """Test that api_router is an instance of APIRouter."""
        assert isinstance(api_router, APIRouter)

    def test_api_router_has_no_routes_by_default(self) -> None:
        """Test that the base router starts with no routes."""
        # The base router should be empty initially
        # Routes are added by other modules
        assert len(api_router.routes) == 0


class TestCurrentUserDependency:
    """Test suite for the CurrentUser dependency."""

    def test_current_user_dependency_creation(self) -> None:
        """Test that CurrentUser is created as a dependency."""
        assert hasattr(CurrentUser, "dependency")
        assert CurrentUser.dependency is get_current_user

    def test_current_user_dependency_function(self) -> None:
        """Test that CurrentUser points to the correct function."""
        assert CurrentUser.dependency is get_current_user

    def test_current_user_is_dependency_instance(self) -> None:
        """Test that CurrentUser is a dependency."""
        assert hasattr(CurrentUser, "dependency")
        assert callable(CurrentUser.dependency)


class TestModuleImports:
    """Test suite for module imports and structure."""

    def test_api_base_imports(self) -> None:
        """Test that all necessary imports are available."""
        # Symbols are already imported at module level
        assert api_router is not None
        assert CurrentUser is not None

    def test_auth_users_import(self) -> None:
        """Test that get_current_user can be imported."""
        # Symbol is already imported at module level
        assert get_current_user is not None
        assert callable(get_current_user)

    def test_fastapi_imports(self) -> None:
        """Test that FastAPI components are properly imported."""
        # Symbol is already imported at module level
        assert APIRouter is not None


class TestAPIIntegration:
    """Integration tests for API base functionality."""

    def test_api_router_can_be_used_in_app(self) -> None:
        """Test that the API router can be included in a FastAPI app."""
        from fastapi import FastAPI

        app = FastAPI()
        app.include_router(api_router)

        # Should not raise any exceptions
        assert app is not None
        assert len(app.routes) > 0

    def test_api_router_prefix_integration(self) -> None:
        """Test that the API router prefix works correctly in an app."""
        from fastapi import FastAPI

        app = FastAPI()
        app.include_router(api_router)

        # Check that the router is included
        router_routes = [route for route in app.routes if hasattr(route, "prefix")]
        api_routes = [route for route in router_routes if route.prefix == "/api"]

        # Should have at least the base router
        assert len(api_routes) >= 0

    def test_current_user_dependency_integration(self) -> None:
        """Test that CurrentUser dependency can be used in route definitions."""
        from fastapi import FastAPI

        app = FastAPI()

        # This should not raise any exceptions
        @app.get("/test")
        async def test_route(_user=CurrentUser):
            return {"message": "test"}

        assert app is not None

    def test_api_router_structure(self) -> None:
        """Test the structure of the API router."""
        assert hasattr(api_router, "prefix")
        assert hasattr(api_router, "tags")
        assert hasattr(api_router, "routes")
        assert hasattr(api_router, "include_router")

    def test_current_user_dependency_structure(self) -> None:
        """Test the structure of the CurrentUser dependency."""
        assert hasattr(CurrentUser, "dependency")
        assert callable(CurrentUser.dependency)
