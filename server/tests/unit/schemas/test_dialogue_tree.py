"""
Unit tests for dialogue_tree schemas.

#755: these models now inherit SecureBaseModel.
"""

import pytest
from pydantic import ValidationError

from server.schemas.dialogue.dialogue_tree import DialogueNode, DialogueOption, DialogueTree
from server.schemas.shared.base import SecureBaseModel


@pytest.mark.parametrize(
    "model_cls,payload",
    [
        (DialogueOption, {"label": "Leave"}),
        (DialogueNode, {"text": "Hello."}),
        (DialogueTree, {"start": "root", "nodes": {"root": {"text": "Hello."}}}),
    ],
)
def test_dialogue_schemas_reject_unknown_field(model_cls: type[SecureBaseModel], payload: dict[str, object]) -> None:
    """An extra field must be rejected, not silently discarded."""
    with pytest.raises(ValidationError):
        _ = model_cls.model_validate({**payload, "unexpected_field": "nope"})


def test_dialogue_tree_graph_validation_still_runs() -> None:
    """Regression guard: the @model_validator("after") graph check still runs post-migration."""
    with pytest.raises(ValidationError, match="is not in nodes"):
        _ = DialogueTree.model_validate({"start": "missing", "nodes": {"root": {"text": "Hello."}}})
