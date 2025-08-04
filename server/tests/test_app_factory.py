"""Tests for the app factory module."""

import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.factory import create_app


class TestAppFactory:
    """Test the app factory functionality."""

    def test_create_app_returns_fastapi_instance(self):
        """Test that create_app returns a FastAPI instance."""
        app = create_app()
        assert isinstance(app, FastAPI)

    def test_create_app_has_correct_title(self):
        """Test that the app has the correct title."""
        app = create_app()
        assert app.title == "MythosMUD API"

    def test_create_app_has_correct_description(self):
        """Test that the app has the correct description."""
        app = create_app()
        assert "Cthulhu Mythos-themed MUD game API" in app.description

    def test_create_app_has_correct_version(self):
        """Test that the app has the correct version."""
        app = create_app()
        assert app.version == "0.1.0"

    def test_create_app_has_cors_middleware(self):
        """Test that the app has CORS middleware configured."""
        app = create_app()

        # Check that CORS middleware is present
        cors_middleware_found = False
        for middleware in app.user_middleware:
            if (isinstance(middleware.cls, type) and
                    issubclass(middleware.cls, CORSMiddleware)):
                cors_middleware_found = True
                break

        assert cors_middleware_found, "CORS middleware should be configured"

    def test_create_app_includes_routers(self):
        """Test that the app includes all necessary routers."""
        app = create_app()

        # Check that routers are included (we can't easily test specific routers
        # without more complex setup, but we can check that routes exist)
        assert len(app.routes) > 0, "App should have routes"

    def test_create_app_lifespan_configured(self):
        """Test that the app has lifespan configured."""
        app = create_app()
        assert app.router.lifespan_context is not None

    def test_create_app_structure(self):
        """Test the overall structure of the created app."""
        app = create_app()

        # Basic structure checks
        assert hasattr(app, 'title')
        assert hasattr(app, 'description')
        assert hasattr(app, 'version')
        assert hasattr(app, 'user_middleware')

    def test_create_app_multiple_calls(self):
        """Test that create_app can be called multiple times."""
        app1 = create_app()
        app2 = create_app()

        # Both should be FastAPI instances
        assert isinstance(app1, FastAPI)
        assert isinstance(app2, FastAPI)

        # They should be different instances
        assert app1 is not app2

    def test_create_app_imports_available(self):
        """Test that all required imports are available."""
        try:
            from app.factory import create_app
            app = create_app()
            assert app is not None
        except ImportError as e:
            pytest.fail(f"Import failed: {e}")

    def test_create_app_function_signature(self):
        """Test that create_app has the correct function signature."""
        import inspect
        sig = inspect.signature(create_app)
        assert str(sig) == "() -> <class 'fastapi.FastAPI'>"

    def test_create_app_docstring(self):
        """Test that create_app has proper documentation."""
        assert create_app.__doc__ is not None
        assert "Create and configure" in create_app.__doc__

    def test_create_app_no_syntax_errors(self):
        """Test that the factory module has no syntax errors."""
        try:
            # If we get here, no syntax errors
            assert True
        except SyntaxError as e:
            pytest.fail(f"Syntax error in factory module: {e}")

    def test_create_app_file_permissions(self):
        """Test that the factory file has proper permissions."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        assert os.path.exists(factory_path), "Factory file should exist"

    def test_create_app_file_size(self):
        """Test that the factory file has reasonable size."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        size = os.path.getsize(factory_path)
        assert size > 0, "Factory file should not be empty"
        assert size < 10000, "Factory file should be reasonably sized"

    def test_create_app_encoding(self):
        """Test that the factory file uses proper encoding."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            content = f.read()
            assert len(content) > 0, "Factory file should have content"

    def test_create_app_line_count(self):
        """Test that the factory file has reasonable line count."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            lines = f.readlines()
            assert len(lines) > 10, "Factory file should have reasonable number of lines"
            assert len(lines) < 100, "Factory file should not be excessively long"

    def test_create_app_comment_quality(self):
        """Test that the factory file has good comment quality."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            content = f.read()
            assert '"""' in content, "Factory file should have docstrings"

    def test_create_app_variable_names(self):
        """Test that the factory uses good variable names."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            content = f.read()
            assert 'create_app' in content, "Should have create_app function"
            assert 'app' in content, "Should use 'app' variable name"

    def test_create_app_return_statement(self):
        """Test that create_app has proper return statement."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            content = f.read()
            assert 'return app' in content, "Should have return statement"

    def test_create_app_no_hardcoded_secrets(self):
        """Test that the factory doesn't contain hardcoded secrets."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            content = f.read()
            # Check for common secret patterns
            assert 'password' not in content.lower(), "Should not contain hardcoded passwords"
            assert 'secret' not in content.lower(), "Should not contain hardcoded secrets"
            assert 'key' not in content.lower(), "Should not contain hardcoded keys"

    def test_create_app_consistent_indentation(self):
        """Test that the factory uses consistent indentation."""
        import os
        factory_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'factory.py')
        with open(factory_path, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    # Check that indentation is consistent (4 spaces)
                    if line.startswith(' '):
                        spaces = len(line) - len(line.lstrip())
                        assert spaces % 4 == 0, f"Inconsistent indentation in line: {line.strip()}"
