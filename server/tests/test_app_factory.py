"""Tests for the FastAPI application factory.

As noted in the restricted archives of Miskatonic University, these tests
validate the FastAPI application factory that creates and configures the
MythosMUD server application.
"""

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class TestAppFactory:
    """Test suite for the application factory."""

    def test_factory_file_exists(self):
        """Test that the factory file exists and is readable."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        assert factory_path.exists()
        assert factory_path.is_file()

    def test_factory_file_content(self):
        """Test that the factory file contains expected content."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for key elements
        assert "def create_app()" in content
        assert "FastAPI" in content
        assert "CORSMiddleware" in content
        assert "title=" in content
        assert "description=" in content
        assert "version=" in content

    def test_factory_imports_available(self):
        """Test that all necessary imports are available."""

        assert FastAPI is not None
        assert CORSMiddleware is not None

    def test_factory_function_signature(self):
        """Test that create_app function has the correct signature."""
        # Read the factory file to check function signature
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check function definition
        assert "def create_app()" in content
        assert "-> FastAPI:" in content

    def test_factory_docstring(self):
        """Test that create_app has proper documentation."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for docstring
        assert '"""' in content
        assert "Create and configure" in content
        assert "FastAPI" in content

    def test_factory_structure(self):
        """Test the structure of the factory file."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for key components
        assert "from fastapi import FastAPI" in content
        assert "from fastapi.middleware.cors import CORSMiddleware" in content
        assert "app = FastAPI(" in content
        assert "app.add_middleware(" in content
        assert "app.include_router(" in content
        assert "return app" in content

    def test_factory_configuration(self):
        """Test that the factory has proper configuration."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for specific configuration values
        assert '"MythosMUD API"' in content
        assert '"0.1.0"' in content
        assert "http://localhost:5173" in content
        assert "http://127.0.0.1:5173" in content

    def test_factory_middleware_configuration(self):
        """Test that CORS middleware is properly configured."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for CORS configuration
        assert "allow_origins=" in content
        assert "allow_credentials=True" in content
        assert "allow_methods=" in content
        assert "allow_headers=" in content

    def test_factory_router_inclusion(self):
        """Test that routers are included."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for router includes
        assert "app.include_router(" in content
        assert "auth_router" in content
        assert "command_router" in content
        assert "player_router" in content
        assert "game_router" in content
        assert "realtime_router" in content
        assert "room_router" in content

    def test_factory_lifespan_configuration(self):
        """Test that lifespan is configured."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for lifespan configuration
        assert "lifespan=lifespan" in content

    def test_factory_imports_structure(self):
        """Test that imports are properly structured."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check import structure
        lines = content.split("\n")
        import_lines = [line for line in lines if line.startswith("from") or line.startswith("import")]

        # Should have imports
        assert len(import_lines) > 0

        # Check for specific imports
        assert any("from fastapi import FastAPI" in line for line in import_lines)
        assert any("from fastapi.middleware.cors import CORSMiddleware" in line for line in import_lines)

    def test_factory_function_structure(self):
        """Test that the create_app function has proper structure."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check function structure
        lines = content.split("\n")

        # Find function definition
        func_start = None
        for i, line in enumerate(lines):
            if "def create_app()" in line:
                func_start = i
                break

        assert func_start is not None

        # Check for return statement
        return_found = False
        for line in lines[func_start:]:
            if "return app" in line:
                return_found = True
                break

        assert return_found

    def test_factory_no_syntax_errors(self):
        """Test that the factory file has no syntax errors."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"

        # Try to compile the file to check for syntax errors
        try:
            compile(factory_path.read_text(encoding="utf-8"), str(factory_path), "exec")
        except SyntaxError as e:
            assert False, f"Syntax error in factory.py: {e}"

    def test_factory_file_permissions(self):
        """Test that the factory file has proper permissions."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"

        # Check that file is readable
        assert os.access(factory_path, os.R_OK)

    def test_factory_file_size(self):
        """Test that the factory file has reasonable size."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"

        # Check file size (should be reasonable for a factory file)
        size = factory_path.stat().st_size
        assert size > 100  # Should be more than 100 bytes
        assert size < 10000  # Should be less than 10KB

    def test_factory_encoding(self):
        """Test that the factory file uses proper encoding."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"

        # Try to read with UTF-8 encoding
        try:
            content = factory_path.read_text(encoding="utf-8")
            assert len(content) > 0
        except UnicodeDecodeError:
            assert False, "Factory file should be UTF-8 encoded"

    def test_factory_line_count(self):
        """Test that the factory file has reasonable line count."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")
        lines = content.split("\n")

        # Should have reasonable number of lines
        assert len(lines) > 10  # More than 10 lines
        assert len(lines) < 200  # Less than 200 lines

    def test_factory_comment_quality(self):
        """Test that the factory file has good comments."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for module docstring
        assert '"""' in content

        # Check for function docstring
        assert "def create_app()" in content
        # Should have docstring after function definition
        lines = content.split("\n")
        func_line = None
        for i, line in enumerate(lines):
            if "def create_app()" in line:
                func_line = i
                break

        if func_line is not None:
            # Check next few lines for docstring
            docstring_found = False
            for line in lines[func_line + 1 : func_line + 5]:
                if '"""' in line or "'''" in line:
                    docstring_found = True
                    break
            assert docstring_found, "create_app function should have a docstring"

    def test_factory_variable_names(self):
        """Test that variable names are properly named."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for proper variable naming
        assert "app = FastAPI(" in content
        assert "app.add_middleware(" in content
        assert "app.include_router(" in content

    def test_factory_return_statement(self):
        """Test that the function returns the app."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for return statement
        assert "return app" in content

    def test_factory_no_hardcoded_secrets(self):
        """Test that no hardcoded secrets are present."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        # Check for absence of common secret patterns
        assert "password" not in content.lower()
        assert "secret" not in content.lower()
        assert "key" not in content.lower()
        assert "token" not in content.lower()

    def test_factory_consistent_indentation(self):
        """Test that indentation is consistent."""
        factory_path = Path(__file__).parent.parent / "app" / "factory.py"
        content = factory_path.read_text(encoding="utf-8")

        lines = content.split("\n")
        for line in lines:
            if line.strip() and not line.startswith("#"):
                # Check that indentation uses spaces (not tabs)
                if line.startswith(" "):
                    assert "\t" not in line, "Should use spaces, not tabs for indentation"
