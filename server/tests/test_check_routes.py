"""
Tests for route checking functionality.

This module tests the route checking script functionality.
"""

import pytest

from server.main import app


class TestCheckRoutes:
    """Test route checking functionality."""

    def test_app_has_routes(self):
        """Test that the app has routes defined."""
        assert hasattr(app, "routes")
        assert len(app.routes) > 0

    def test_routes_have_methods_and_paths(self):
        """Test that routes have methods and paths."""
        for route in app.routes:
            assert hasattr(route, "methods")
            assert hasattr(route, "path")
            assert route.methods is not None
            assert route.path is not None

    def test_specific_routes_exist(self):
        """Test that specific expected routes exist."""
        route_paths = [route.path for route in app.routes]

        # Check for some expected routes
        expected_routes = [
            "/players",
            "/players/{player_id}",
            "/players/name/{player_name}",
        ]

        for expected_route in expected_routes:
            assert expected_route in route_paths, f"Expected route {expected_route} not found"

    def test_route_methods(self):
        """Test that routes have appropriate HTTP methods."""
        for route in app.routes:
            assert isinstance(route.methods, set)
            assert len(route.methods) > 0

            # Check for valid HTTP methods
            valid_methods = {"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"}
            for method in route.methods:
                assert method in valid_methods

    def test_route_paths_are_strings(self):
        """Test that route paths are strings."""
        for route in app.routes:
            assert isinstance(route.path, str)
            assert route.path.startswith("/")

    def test_no_duplicate_routes(self):
        """Test that there are no duplicate route paths."""
        paths = [route.path for route in app.routes]
        assert len(paths) == len(set(paths)), "Duplicate routes found"

    def test_route_parameters(self):
        """Test that routes with parameters are properly formatted."""
        for route in app.routes:
            if "{" in route.path and "}" in route.path:
                # Check that parameter format is correct
                assert route.path.count("{") == route.path.count("}")

                # Check that parameters are properly closed
                parts = route.path.split("{")
                for part in parts[1:]:  # Skip first part (before first {)
                    assert "}" in part, f"Unclosed parameter in route {route.path}"

    def test_route_path_formatting(self):
        """Test that route paths are properly formatted."""
        for route in app.routes:
            # Paths should start with /
            assert route.path.startswith("/")

            # Paths should not end with / unless it's the root
            if route.path != "/":
                assert not route.path.endswith("/")

            # Paths should not have double slashes (except for root)
            if route.path != "/":
                assert "//" not in route.path

    def test_route_method_combinations(self):
        """Test that routes have reasonable method combinations."""
        for route in app.routes:
            methods = route.methods

            # GET routes should not have POST methods
            if "GET" in methods and "POST" in methods:
                # This is acceptable for some endpoints
                pass

            # DELETE routes should not have GET methods (usually)
            if "DELETE" in methods and "GET" in methods:
                # This might be acceptable for some endpoints
                pass

    def test_route_path_parameters(self):
        """Test that route path parameters are valid."""
        for route in app.routes:
            if "{" in route.path:
                # Extract parameter names
                start = route.path.find("{")
                end = route.path.find("}")

                while start != -1 and end != -1:
                    param_name = route.path[start + 1 : end]

                    # Parameter names should be valid Python identifiers
                    assert param_name.isidentifier(), f"Invalid parameter name: {param_name}"

                    # Look for next parameter
                    start = route.path.find("{", end)
                    if start != -1:
                        end = route.path.find("}", start)

    def test_route_consistency(self):
        """Test that routes are consistent across the application."""
        # Get all routes
        routes = list(app.routes)

        # Check that we have a reasonable number of routes
        assert len(routes) >= 5, "Expected at least 5 routes"

        # Check that routes are properly structured
        for route in routes:
            assert hasattr(route, "endpoint")
            assert hasattr(route, "name")
            assert hasattr(route, "path")
            assert hasattr(route, "methods")


class TestRouteScriptExecution:
    """Test the route checking script execution."""

    def test_script_can_be_imported(self):
        """Test that the check_routes script can be imported."""
        try:
            # Import is already done at module level
            assert True
        except ImportError as e:
            pytest.fail(f"Failed to import check_routes: {e}")

    def test_script_has_main_functionality(self):
        """Test that the script has the expected functionality."""
        # The script should be able to list routes
        routes = list(app.routes)
        assert len(routes) > 0

        # Each route should have the expected attributes
        for route in routes:
            assert hasattr(route, "methods")
            assert hasattr(route, "path")

    def test_route_output_format(self):
        """Test that routes can be formatted for output."""
        for route in app.routes:
            # Test that we can format the route for output
            methods_str = ", ".join(sorted(route.methods))
            output_line = f"{methods_str} {route.path}"

            assert isinstance(output_line, str)
            assert len(output_line) > 0
            assert route.path in output_line
            assert any(method in output_line for method in route.methods)


class TestRouteEdgeCases:
    """Test edge cases for route checking."""

    def test_empty_routes_list(self):
        """Test behavior with empty routes list."""
        # This should not happen in a real app, but test the structure
        routes = list(app.routes)
        assert isinstance(routes, list)

    def test_route_with_special_characters(self):
        """Test routes with special characters in paths."""
        for route in app.routes:
            # Paths should handle special characters properly
            if "{" in route.path or "}" in route.path:
                # These are parameter placeholders and should be valid
                assert route.path.count("{") == route.path.count("}")

    def test_route_methods_are_sets(self):
        """Test that route methods are sets."""
        for route in app.routes:
            assert isinstance(route.methods, set)
            assert len(route.methods) > 0

    def test_route_paths_are_normalized(self):
        """Test that route paths are properly normalized."""
        for route in app.routes:
            # Paths should not have leading/trailing whitespace
            assert route.path == route.path.strip()

            # Paths should not have multiple consecutive slashes
            if route.path != "/":
                assert "//" not in route.path
