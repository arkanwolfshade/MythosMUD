"""
Unit tests for container_models schemas.

#755: these request models now inherit SecureBaseModel.
"""

from uuid import uuid4

import pytest
from pydantic import ValidationError

from server.api.container_models import (
    CloseContainerRequest,
    LootAllRequest,
    OpenContainerRequest,
    TransferContainerRequest,
)
from server.schemas.shared.base import SecureBaseModel


@pytest.mark.parametrize(
    "model_cls,payload",
    [
        (OpenContainerRequest, {"container_id": str(uuid4())}),
        (CloseContainerRequest, {"container_id": str(uuid4()), "mutation_token": "tok"}),
        (LootAllRequest, {"container_id": str(uuid4()), "mutation_token": "tok"}),
        (
            TransferContainerRequest,
            {
                "container_id": str(uuid4()),
                "mutation_token": "tok",
                "direction": "to_player",
                "stack": {},
                "quantity": 1,
            },
        ),
    ],
)
def test_container_request_schemas_reject_unknown_field(
    model_cls: type[SecureBaseModel], payload: dict[str, object]
) -> None:
    """An extra field in the request body must be rejected, not silently discarded."""
    with pytest.raises(ValidationError):
        _ = model_cls.model_validate({**payload, "unexpected_field": "nope"})


def test_transfer_container_request_still_validates_direction() -> None:
    """Regression guard: the field_validator on `direction` still runs after the migration."""
    with pytest.raises(ValidationError):
        _ = TransferContainerRequest.model_validate(
            {
                "container_id": str(uuid4()),
                "mutation_token": "tok",
                "direction": "sideways",
                "stack": {},
                "quantity": 1,
            }
        )
