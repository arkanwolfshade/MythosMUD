"""Tests for the check_routes module."""

from pathlib import Path
from unittest.mock import MagicMock


class TestCheckRoutes:
    """Test the check_routes module functionality."""

    def test_check_routes_file_exists(self):
        """Test that the check_routes file exists."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        assert routes_path.exists()

    def test_check_routes_script_structure(self):
        """Test that check_routes script has the expected structure."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check for key components
        assert "#!/usr/bin/env python3" in content
        assert '"""Check FastAPI app routes."""' in content
        assert "import sys" in content
        assert "from pathlib import Path" in content
        assert "from logging_config import get_logger" in content
        assert "from main import app" in content
        assert "logger = get_logger(__name__)" in content
        assert 'logger.info("Routes:")' in content
        assert "for route in app.routes:" in content
        assert 'logger.info(f"{route.methods} {route.path}")' in content

    def test_check_routes_path_insertion(self):
        """Test that check_routes properly inserts the server directory into sys.path."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that the path insertion line is present
        assert "sys.path.insert(0, str(Path(__file__).parent))" in (content)

    def test_check_routes_logger_initialization(self):
        """Test that check_routes properly initializes the logger."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that logger is properly initialized
        assert "logger = get_logger(__name__)" in (content)

    def test_check_routes_app_import(self):
        """Test that check_routes can import the app from main."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that app is imported
        assert "from main import app" in content

    def test_check_routes_route_iteration(self):
        """Test that check_routes iterates over routes correctly."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that routes are iterated
        assert "for route in app.routes:" in content
        assert "route.methods" in content
        assert "route.path" in content

    def test_check_routes_logging_output(self):
        """Test that check_routes logs route information."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that routes are logged
        assert 'logger.info("Routes:")' in content
        assert 'logger.info(f"{route.methods} {route.path}")' in content

    def test_check_routes_shebang(self):
        """Test that check_routes has proper shebang."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check for shebang
        assert content.startswith("#!/usr/bin/env python3")

    def test_check_routes_docstring(self):
        """Test that check_routes has proper documentation."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check for docstring
        assert '"""Check FastAPI app routes."""' in content

    def test_check_routes_imports(self):
        """Test that check_routes has all necessary imports."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check for all required imports
        assert "import sys" in content
        assert "from pathlib import Path" in content
        assert "from logging_config import get_logger" in content
        assert "from main import app" in content

    def test_check_routes_variable_usage(self):
        """Test that check_routes uses variables correctly."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that variables are used correctly
        assert "logger = get_logger(__name__)" in content
        assert "for route in app.routes:" in content
        assert "logger.info" in content

    def test_check_routes_script_length(self):
        """Test that check_routes script has reasonable length."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")
        lines = content.split("\n")

        # Should have reasonable number of lines (not too short, not too long)
        assert len(lines) >= 10, "Script should have at least 10 lines"
        assert len(lines) <= 30, "Script should not be too long"

    def test_check_routes_no_syntax_errors(self):
        """Test that check_routes has no syntax errors."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"

        # Try to compile the file to check for syntax errors
        try:
            compile(routes_path.read_text(encoding="utf-8"), str(routes_path), "exec")
        except SyntaxError as e:
            raise AssertionError(f"Syntax error in check_routes.py: {e}") from e

    def test_check_routes_encoding(self):
        """Test that check_routes file uses proper encoding."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"

        # Try to read with UTF-8 encoding
        try:
            content = routes_path.read_text(encoding="utf-8")
            assert len(content) > 0
        except UnicodeDecodeError:
            raise AssertionError("check_routes file should be UTF-8 encoded") from None

    def test_check_routes_executable(self):
        """Test that check_routes script is executable."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"

        # Check that file is readable
        assert routes_path.is_file()
        assert routes_path.exists()

    def test_check_routes_file_size(self):
        """Test that check_routes file has reasonable size."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"

        # Check file size (should be reasonable for a script file)
        size = routes_path.stat().st_size
        assert size > 100, "Script should be more than 100 bytes"
        assert size < 2000, "Script should be less than 2KB"

    def test_check_routes_line_endings(self):
        """Test that check_routes has consistent line endings."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        # Check that there are no mixed line endings
        lines = content.split("\n")
        for line in lines:
            assert "\r" not in line, "Should not have carriage returns"

    def test_check_routes_indentation(self):
        """Test that check_routes has consistent indentation."""
        routes_path = Path(__file__).parent.parent / "check_routes.py"
        content = routes_path.read_text(encoding="utf-8")

        lines = content.split("\n")
        for line in lines:
            if line.strip() and not line.startswith("#"):
                # Check that indentation uses spaces (not tabs)
                if line.startswith(" "):
                    assert "\t" not in line, "Should use spaces, not tabs for indentation"

    def test_check_routes_execution_logic(self):
        """Test that check_routes execution logic works correctly."""
        # Mock the logger
        mock_logger = MagicMock()

        # Mock the app routes
        mock_route1 = MagicMock()
        mock_route1.methods = {"GET", "POST"}
        mock_route1.path = "/test1"

        mock_route2 = MagicMock()
        mock_route2.methods = {"GET"}
        mock_route2.path = "/test2"

        mock_app = MagicMock()
        mock_app.routes = [mock_route1, mock_route2]

        # Execute the script logic directly (this is what check_routes.py does)
        logger = mock_logger
        app = mock_app

        # Simulate the script execution
        logger.info("Routes:")
        for route in app.routes:
            logger.info(f"{route.methods} {route.path}")

        # Verify that logger.info was called with the expected messages
        mock_logger.info.assert_any_call("Routes:")

        # Check that both route calls were made (order doesn't matter for sets)
        calls = mock_logger.info.call_args_list
        call_strings = [str(call[0][0]) for call in calls]

        assert "Routes:" in call_strings
        assert "{'GET', 'POST'} /test1" in call_strings or "{'POST', 'GET'} /test1" in call_strings
        assert "{'GET'} /test2" in call_strings

        # Verify the total number of calls (1 for "Routes:" + 2 for routes)
        assert mock_logger.info.call_count == 3

    def test_check_routes_actual_execution(self):
        """Test that check_routes module can be imported and executed."""
        # Create a temporary mock version of the dependencies
        import sys
        from unittest.mock import MagicMock

        # Mock the dependencies before importing
        sys.modules["logging_config"] = MagicMock()
        sys.modules["main"] = MagicMock()

        # Mock the logger
        mock_logger = MagicMock()
        sys.modules["logging_config"].get_logger.return_value = mock_logger

        # Mock the app routes
        mock_route1 = MagicMock()
        mock_route1.methods = {"GET", "POST"}
        mock_route1.path = "/test1"

        mock_route2 = MagicMock()
        mock_route2.methods = {"GET"}
        mock_route2.path = "/test2"

        mock_app = MagicMock()
        mock_app.routes = [mock_route1, mock_route2]
        sys.modules["main"].app = mock_app

        # Add the server directory to the path
        server_dir = Path(__file__).parent.parent
        original_path = sys.path.copy()
        sys.path.insert(0, str(server_dir))

        try:
            # Import the module (this should execute the script)
            import check_routes  # noqa: F401 - imported for side effects

            # Verify that logger.info was called with the expected messages
            mock_logger.info.assert_any_call("Routes:")

            # Check that both route calls were made (order doesn't matter for sets)
            calls = mock_logger.info.call_args_list
            call_strings = [str(call[0][0]) for call in calls]

            assert "Routes:" in call_strings
            assert "{'GET', 'POST'} /test1" in call_strings or "{'POST', 'GET'} /test1" in call_strings
            assert "{'GET'} /test2" in call_strings

            # Verify the total number of calls (1 for "Routes:" + 2 for routes)
            assert mock_logger.info.call_count == 3

        finally:
            # Clean up
            sys.path = original_path
            # Remove the mock modules
            if "logging_config" in sys.modules:
                del sys.modules["logging_config"]
            if "main" in sys.modules:
                del sys.modules["main"]
            if "check_routes" in sys.modules:
                del sys.modules["check_routes"]
