"""
Unit tests for admin dialogue_schemas.

#755: these request models now inherit SecureBaseModel.
"""

import pytest
from pydantic import ValidationError

from server.api.admin.dialogue_schemas import DialogueDefinitionCreate, DialogueDefinitionUpdate
from server.schemas.shared.base import SecureBaseModel

_TREE_PAYLOAD = {"start": "root", "nodes": {"root": {"text": "Hello."}}}


@pytest.mark.parametrize(
    "model_cls,payload",
    [
        (DialogueDefinitionCreate, {"id": "greeting", "definition": _TREE_PAYLOAD}),
        (DialogueDefinitionUpdate, {"definition": _TREE_PAYLOAD}),
    ],
)
def test_dialogue_definition_request_schemas_reject_unknown_field(
    model_cls: type[SecureBaseModel], payload: dict[str, object]
) -> None:
    """An extra field must be rejected, not silently discarded."""
    with pytest.raises(ValidationError):
        _ = model_cls.model_validate({**payload, "unexpected_field": "nope"})
