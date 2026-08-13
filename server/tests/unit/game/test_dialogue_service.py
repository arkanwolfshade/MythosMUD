"""Unit tests for DialogueService and talk formatting (#583)."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from pydantic import ValidationError

from server.game.dialogue.dialogue_service import (
    DialogueService,
    format_dialogue_prompt,
    reset_dialogue_service_for_tests,
)
from server.schemas.dialogue import DialogueTree

SAMPLE_TREE = {
    "start": "greeting",
    "nodes": {
        "greeting": {
            "text": "Welcome to the stacks.",
            "options": [
                {"label": "Ask about the library", "next": "library"},
                {"label": "Farewell", "next": None},
            ],
        },
        "library": {
            "text": "Knowledge has a price.",
            "options": [{"label": "Leave", "next": None}],
        },
    },
}


def test_dialogue_tree_rejects_unknown_next():
    """Pydantic tree validation rejects unknown next targets."""
    bad = {
        "start": "greeting",
        "nodes": {
            "greeting": {
                "text": "Hi",
                "options": [{"label": "Go", "next": "missing"}],
            }
        },
    }
    with pytest.raises(ValidationError):
        _ = DialogueTree.model_validate(bad)


def test_dialogue_tree_rejects_empty_string_next():
    """Empty-string next is invalid; use null to end a branch."""
    bad = {
        "start": "greeting",
        "nodes": {
            "greeting": {
                "text": "Hi",
                "options": [{"label": "Bye", "next": ""}],
            }
        },
    }
    with pytest.raises(ValidationError):
        _ = DialogueTree.model_validate(bad)


def test_dialogue_tree_rejects_missing_start():
    """Missing start node fails validation."""
    with pytest.raises(ValidationError):
        _ = DialogueTree.model_validate({"start": "nope", "nodes": {"greeting": {"text": "Hi", "options": []}}})


def test_format_dialogue_prompt_numbers_options():
    """Prompt includes NPC line and numbered options."""
    text = format_dialogue_prompt("Armitage", "Hello.", ["Ask", "Bye"])
    assert 'Armitage says: "Hello."' in text
    assert "1. Ask" in text
    assert "2. Bye" in text
    assert "talk <number>" in text


@pytest.mark.asyncio
async def test_dialogue_service_start_and_choose():
    """Start at greeting; option 1 advances; farewell clears cursor."""
    reset_dialogue_service_for_tests(None)
    repo = MagicMock()
    row = MagicMock()
    row.id = "armitage_greeting"
    row.definition = SAMPLE_TREE
    row.npc_definition_id = 53
    repo.get_by_npc_definition_id = AsyncMock(return_value=row)
    repo.get_by_id = AsyncMock(return_value=row)
    service = DialogueService(repository=repo)
    player_id = uuid.uuid4()

    prompt = await service.start_with_npc(player_id, npc_id="npc-1", npc_name="Armitage", npc_definition_id=53)
    assert not isinstance(prompt, str)
    assert prompt.text == "Welcome to the stacks."
    assert len(prompt.options) == 2
    assert service.get_cursor(player_id) is not None

    next_prompt = await service.choose_option(player_id, 1)
    assert not isinstance(next_prompt, str)
    assert next_prompt.text == "Knowledge has a price."

    end_prompt = await service.choose_option(player_id, 1)
    assert not isinstance(end_prompt, str)
    assert end_prompt.ended is True
    assert service.get_cursor(player_id) is None


@pytest.mark.asyncio
async def test_dialogue_service_choose_without_cursor():
    """talk <n> without prior talk returns guidance."""
    service = DialogueService(repository=MagicMock())
    result = await service.choose_option(uuid.uuid4(), 1)
    assert isinstance(result, str)
    assert "talk <npc>" in result
