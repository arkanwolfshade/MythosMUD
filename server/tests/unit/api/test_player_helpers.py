"""Unit tests for server.api.player_helpers (error context helper)."""

import uuid
from unittest.mock import MagicMock

from fastapi import Request

from server.api.player_helpers import create_error_context


def test_create_error_context_without_user_sets_metadata() -> None:
    """When current_user is None, context gets metadata only."""
    req = MagicMock(spec=Request)
    ctx = create_error_context(req, None, op="test")
    assert ctx.metadata.get("op") == "test"


def test_create_error_context_with_user_sets_user_id_and_metadata() -> None:
    """When current_user is set, user_id is populated and metadata merged."""
    req = MagicMock(spec=Request)
    uid = uuid.uuid4()
    user = MagicMock()
    user.id = uid
    ctx = create_error_context(req, user, reason="x")
    assert ctx.user_id == str(uid)
    assert ctx.metadata.get("reason") == "x"
