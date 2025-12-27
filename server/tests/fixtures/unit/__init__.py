"""
Unit-tier fixtures with strict mocking and in-memory fakes.
"""

from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

# Import strict_mocker from mock_helpers for compatibility
from .mock_helpers import strict_mocker


@pytest.fixture
def dummy_request() -> SimpleNamespace:
    """Provide a minimal request object for testing."""
    state = SimpleNamespace(
        persistence=MagicMock(),
        event_bus=MagicMock(),
        catatonia_registry=MagicMock(),
    )
    app = SimpleNamespace(state=state)
    return SimpleNamespace(app=app)


@pytest.fixture
def fakerandom() -> Any:
    """Provide deterministic random seed for unit tests."""
    import random

    random.seed(42)
    yield
    random.seed()

