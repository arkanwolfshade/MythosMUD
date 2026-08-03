"""Unit tests for admin dialogue schemas and API helpers (#583)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic import ValidationError

from server.api.admin.dialogue_definitions_api import create_dialogue_definition, to_response
from server.api.admin.dialogue_schemas import DialogueDefinitionCreate
from server.schemas.dialogue import DialogueTree

VALID_TREE = {
    "start": "greeting",
    "nodes": {
        "greeting": {
            "text": "Hello.",
            "options": [{"label": "Bye", "next": None}],
        }
    },
}


def test_dialogue_tree_schema_accepts_nav_only():
    """Happy-path tree validates."""
    tree = DialogueTree.model_validate(VALID_TREE)
    assert tree.start == "greeting"
    assert tree.nodes["greeting"].options[0].next is None


def test_dialogue_tree_schema_rejects_bad_start():
    """Invalid start fails before persistence."""
    with pytest.raises(ValidationError):
        _ = DialogueTree.model_validate({"start": "missing", "nodes": {"greeting": {"text": "Hi", "options": []}}})


def test_to_response_maps_row():
    """Repository row maps into API response shape."""
    row = MagicMock()
    row.id = "t1"
    row.definition = VALID_TREE
    row.npc_definition_id = 53
    row.created_at = None
    row.updated_at = None
    response = to_response(row)
    assert response.id == "t1"
    assert response.npc_definition_id == 53


@pytest.mark.asyncio
async def test_create_dialogue_definition_upserts():
    """Create endpoint validates admin permission and upserts via repository."""
    body = DialogueDefinitionCreate(
        id="t1",
        definition=DialogueTree.model_validate(VALID_TREE),
        npc_definition_id=53,
    )
    request = MagicMock()
    user = MagicMock()
    row = MagicMock()
    row.id = "t1"
    row.definition = VALID_TREE
    row.npc_definition_id = 53
    row.created_at = None
    row.updated_at = None

    auth_service: MagicMock = MagicMock()
    auth_service.get_username = MagicMock(return_value="admin")
    repo: MagicMock = MagicMock()
    upsert: AsyncMock = AsyncMock(return_value=row)
    repo.upsert = upsert

    with (
        patch("server.api.admin.dialogue_definitions_api.validate_admin_permission") as validate,
        patch("server.api.admin.dialogue_definitions_api.DialogueDefinitionRepository") as repo_cls,
        patch("server.api.admin.dialogue_definitions_api.get_admin_auth_service") as auth_svc,
    ):
        auth_svc.return_value = auth_service
        repo_cls.return_value = repo
        result = await create_dialogue_definition(body, request, user)

    validate.assert_called_once()
    assert result.id == "t1"
    upsert.assert_awaited_once()
